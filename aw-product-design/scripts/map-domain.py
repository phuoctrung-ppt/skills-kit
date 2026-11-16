#!/usr/bin/env python3
"""Read-only, evidence-backed lexical context for product design tasks."""
import argparse
import json
import os
from pathlib import Path
import re
import runpy

KNOWLEDGE = runpy.run_path(str(Path(__file__).with_name("csv-guidance.py")))

SKIP = {'node_modules', 'vendor', 'dist', 'build', 'coverage', 'target',
        'venv', '__pycache__', 'skills', 'plans', 'workflow'}
EXTENSIONS = {'.md', '.txt', '.json', '.css', '.scss', '.ts', '.tsx',
              '.js', '.jsx', '.html', '.prisma', '.sql', '.yaml', '.yml'}
SECRET = re.compile(r'(^|[._-])(env|secrets?|credentials?|private|id_rsa)([._-]|$)', re.I)
DOMAINS = {
    'fitness': ['fitness', 'workout', 'trainer', 'exercise', 'gym'],
    'commerce': ['checkout', 'cart', 'inventory', 'storefront', 'ecommerce'],
    'education': ['lesson', 'course', 'student', 'curriculum', 'learning'],
    'healthcare': ['patient', 'clinic', 'prescription', 'medical'],
    'finance': ['invoice', 'banking', 'portfolio', 'transaction', 'accounting'],
    'scheduling': ['appointment', 'booking', 'calendar', 'availability'],
    'collaboration': ['workspace', 'collaboration', 'teammate'],
}
MODES = {
    'sketch': (['sketch', 'sketches', 'rough layout', 'rough layouts'], 'layouts.md'),
    'wireframe': (['wireframe', 'wireframes', 'wire-frame', 'wire-frames', 'wire frame', 'wire frames'], 'layouts.md'),
    'tokens': (['token', 'tokens', 'design system', 'theme'], 'tokens.md'),
    'prototype': (['prototype', 'prototypes', 'prototyping', 'clickable'], 'prototypes.md'),
}
STOP = set('a an and as at be by create design for from in is it of on or the to '
           'with using make build please add this that flow screen page ui'.split())
ENTITY = re.compile(r'\b(?:interface|type|model|enum|class)\s+(\w+)|'
                    r'\b(?:const|let)\s+(\w*(?:Schema|Dto))\b|'
                    r'\bCREATE\s+TABLE\s+(?:IF\s+NOT\s+EXISTS\s+)?["`]?([\w]+)', re.I)
LABEL = re.compile(r'^\s*(?:[-*#]+\s*)?(actor|persona|role|constraint|requirement)\s*:\s*(.+)', re.I)


def matches(text, words):
    return [w for w in words if re.search(r'(?<!\w)' + re.escape(w) + r'(?!\w)', text, re.I)]


def scan(root):
    stats = {'files_read': 0, 'excluded': 0, 'oversized': 0, 'unreadable': 0,
             'file_limit_reached': False, 'traversal_limit_reached': False}
    records, visited = [], 0
    def onerror(_error):
        stats['unreadable'] += 1
    for base, dirs, files in os.walk(root, followlinks=False, onerror=onerror):
        visited += 1
        if visited > 2000:
            stats['traversal_limit_reached'] = True
            break
        dirs[:] = sorted(d for d in dirs if not d.startswith('.') and d not in SKIP
                         and not (Path(base) / d).is_symlink())
        for name in sorted(files):
            path = Path(base) / name
            if (name.startswith('.') or path.suffix.lower() not in EXTENSIONS
                    or SECRET.search(name) or name in {'AGENTS.md', 'CLAUDE.md', 'package-lock.json', 'pnpm-lock.yaml', 'bun.lock', 'yarn.lock'}
                    or path.is_symlink() or not path.is_file()):
                stats['excluded'] += 1
                continue
            if stats['files_read'] >= 500:
                stats['file_limit_reached'] = True
                return records, stats
            try:
                with path.open('rb') as handle:
                    raw = handle.read(131073)
                if len(raw) > 131072:
                    stats['oversized'] += 1
                    continue
                if b'\0' in raw:
                    stats['excluded'] += 1
                    continue
                content = raw.decode('utf-8')
            except (OSError, UnicodeError):
                stats['unreadable'] += 1
                continue
            stats['files_read'] += 1
            records.append((path.relative_to(root).as_posix(), content))
    return records, stats


def extract(root, task):
    records, stats = scan(root)
    result = {k: [] for k in ('deliverables', 'domain_candidates', 'entities',
                              'roles', 'constraints', 'token_sources', 'task_files')}
    result.update(schema_version=1, root=str(root), task=task)
    terms = sorted(set(re.findall(r'[\w-]{3,}', task.lower())) - STOP)
    for mode, (words, reference) in MODES.items():
        found = matches(KNOWLEDGE['normalized'](task), words)
        if found:
            result['deliverables'].append({'kind': mode, 'matched': found,
                                           'reference': 'references/' + reference})
    domains = {k: [] for k in DOMAINS}
    for path, content in [('<task>', task)] + records:
        relevance = []
        for number, line in enumerate(content.splitlines(), 1):
            evidence = {'path': path, 'line': number}
            for domain, words in DOMAINS.items():
                found = matches(KNOWLEDGE['normalized'](line) if path == '<task>' else line, words)
                if found and len(domains[domain]) < 8:
                    domains[domain].append(dict(evidence, matched=found,
                        normalization='VI phrase aliases' if path == '<task>' else 'none'))
            label = LABEL.match(line)
            if label:
                key = 'roles' if label[1].lower() in {'actor', 'persona', 'role'} else 'constraints'
                result[key].append(dict(evidence, text=label[2][:240]))
            if path == '<task>':
                continue
            found = matches(line, terms)
            if found and len(relevance) < 3:
                relevance.append(dict(evidence, matched=found, excerpt=line.strip()[:180]))
            if Path(path).suffix in {'.ts', '.tsx', '.js', '.jsx', '.prisma', '.sql'}:
                for match in ENTITY.finditer(line):
                    result['entities'].append(dict(evidence, name=next(g for g in match.groups() if g)))
            if Path(path).suffix in {'.css', '.scss', '.html', '.tsx', '.jsx'}:
                names = re.findall(r'(--[\w-]+)\s*:', line)
                if names:
                    result['token_sources'].append(dict(evidence, names=sorted(set(names))))
        if relevance:
            result['task_files'].append({'path': path, 'evidence': relevance,
                                         'score': sum(len(x['matched']) for x in relevance)})
        if path.endswith('.json') and re.search(r'token|theme', path, re.I):
            result['token_sources'].append({'path': path, 'line': 1,
                                            'kind': 'token-json-candidate'})
    for domain, evidence in domains.items():
        if evidence:
            result['domain_candidates'].append({'domain': domain, 'status': 'hypothesis',
                                                 'evidence': evidence})
    result['domain_candidates'].sort(key=lambda x: not any(e['path'] == '<task>' for e in x['evidence']))
    result['task_files'].sort(key=lambda x: (-x['score'], x['path']))
    stats['omitted_results'] = {k: max(0, len(v) - 40) for k, v in result.items() if isinstance(v, list)}
    for key in stats['omitted_results']:
        result[key] = result[key][:40]
    stats['limitations'] = ['Lexical heuristics; inspect evidence before decisions.',
                            'Does not parse gitignore, ASTs, or token alias graphs.',
                            'Domain evidence capped at 8 matches per candidate.']
    result['scan'] = stats
    result['unresolved'] = []
    if not result['deliverables']:
        result['unresolved'].append('Requested artifact not recognized; interpret task manually.')
    if not result['domain_candidates']:
        result['unresolved'].append('Domain not recognized; derive from brief or ask if material.')
    if not records:
        result['unresolved'].append('No eligible project text found; use the brief.')
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', required=True, type=Path)
    parser.add_argument('--query', help='Explicit CSV query; preserve original task evidence')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--task')
    group.add_argument('--task-file', type=Path)
    args = parser.parse_args()
    try:
        root = args.root.expanduser().resolve(strict=True)
        if not root.is_dir():
            raise ValueError('--root must be a directory')
        if args.task_file:
            with args.task_file.expanduser().open('rb') as handle:
                raw = handle.read(131073)
            if len(raw) > 131072:
                raise ValueError('Task file exceeds 128 KiB')
            task = raw.decode('utf-8')
        else:
            task = args.task
        if args.query is not None and not args.query.strip():
            raise ValueError('Query must not be empty')
        if not task.strip():
            raise ValueError('Task must not be empty')
        result = extract(root, task)
        result['knowledge'] = KNOWLEDGE['knowledge'](task, result['deliverables'], args.query)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except (OSError, ValueError) as error:
        parser.error(str(error))


if __name__ == '__main__':
    main()
