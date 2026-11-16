#!/usr/bin/env python3
"""Offline BM25 retrieval over a skill's pinned CSV snapshots; stdout JSON."""
import argparse
from collections import Counter
import csv
from functools import lru_cache
import json
from math import log
from pathlib import Path
import re
import unicodedata

ROOT = Path(__file__).resolve().parents[1]
STOP = set('a an the to for and or in on with from using use add create implement '
           'update fix make build please this that of is app application design '
           'ung dung cho va cua mot cac can hay toi muon giao dien'.split())


def fold(text):
    text = text.lower().replace('đ', 'd')
    return ''.join(c for c in unicodedata.normalize('NFKD', text)
                   if not unicodedata.combining(c))


@lru_cache(maxsize=1)
def aliases():
    return json.loads((ROOT / 'data/query-aliases.json').read_text(encoding='utf-8'))


def normalize_query(text):
    text = fold(text)
    for source, target in sorted(aliases().items(), key=lambda item: -len(item[0])):
        text = re.sub(r'(?<!\w)' + re.escape(source) + r'(?!\w)', target, text)
    return text


def tokens(text):
    words = re.findall(r'[a-z0-9]+', fold(text))
    return [w[:-1] if len(w) > 4 and w.endswith('s') and not w.endswith('ss') else w
            for w in words if len(w) > 1 and w not in STOP]


def search(skill_dir, query, domain, limit=3):
    result = {'domain': domain, 'query': query, 'normalized_query': '',
              'status': 'error', 'results': []}
    try:
        if not 1 <= limit <= 10:
            raise ValueError('limit must be between 1 and 10')
        result['normalized_query'] = normalize_query(query)
        folder = Path(skill_dir).resolve() / 'data'
        catalog = json.loads((folder / 'catalog.json').read_text(encoding='utf-8'))
        if domain not in catalog:
            raise ValueError('Unknown domain: ' + domain)
        config = catalog[domain]
        path = (folder / config['file']).resolve()
        if not path.is_relative_to(folder.resolve()):
            raise ValueError('Dataset path must remain inside data/')
        if path.stat().st_size > 5_000_000:
            raise ValueError('Dataset exceeds 5 MB')
        with path.open(encoding='utf-8-sig', newline='') as stream:
            reader = csv.DictReader(stream)
            if not set(config['search_columns']) <= set(reader.fieldnames or []):
                raise ValueError('Dataset missing configured search columns')
            rows = []
            for row in reader:
                if len(rows) >= 10000 or None in row or any(v is None for v in row.values()):
                    raise ValueError('Malformed or oversized CSV dataset')
                rows.append(row)
        query_terms = set(tokens(result['normalized_query']))
        docs = [Counter(tokens(' '.join(row[c] for c in config['search_columns']))) for row in rows]
        frequencies = Counter(term for doc in docs for term in doc)
        average = sum(sum(doc.values()) for doc in docs) / max(len(docs), 1) or 1
        ranked = []
        for index, (row, doc) in enumerate(zip(rows, docs), 1):
            filters = config.get('filters', {})
            if any(row.get(key) not in allowed for key, allowed in filters.items()):
                continue
            found = query_terms & doc.keys()
            if not found:
                continue
            score = 0
            for term in found:
                inverse = log(1 + (len(docs) - frequencies[term] + 0.5) / (frequencies[term] + 0.5))
                count = doc[term]
                score += inverse * count * 2.5 / (count + 1.5 * (0.25 + 0.75 * sum(doc.values()) / average))
            ranked.append({'source': 'data/' + config['file'], 'record': index,
                           'score': round(score, 5), 'matched_terms': sorted(found), 'values': row})
        ranked.sort(key=lambda row: (-row['score'], row['record']))
        result.update(status='matched' if ranked else 'no_match', results=ranked[:limit])
    except (OSError, ValueError, KeyError, TypeError, csv.Error) as error:
        result['error'] = str(error)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('query')
    parser.add_argument('--domain', required=True)
    parser.add_argument('--limit', type=int, choices=range(1, 11), default=3)
    args = parser.parse_args()
    if not args.query.strip():
        parser.error('query must not be empty')
    result = search(ROOT, args.query, args.domain, args.limit)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if result['status'] == 'error':
        raise SystemExit(2)


if __name__ == '__main__':
    main()
