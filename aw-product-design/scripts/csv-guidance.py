"""Design task routing into CSV knowledge without conflating project facts."""
from pathlib import Path
import re
import runpy

ROOT = Path(__file__).resolve().parents[1]
ENGINE = runpy.run_path(str(ROOT / 'scripts/search-csv.py'))
ARTIFACT_WORDS = set('sketch sketches wireframe wireframes wire frame prototype prototypes '
                    'token tokens design system create build make define bộ bo layout layouts'.split())


def normalized(task):
    try:
        return ENGINE['normalize_query'](task)
    except (OSError, ValueError):
        return task


def knowledge(task, deliverables, query=None):
    normalized_task = normalized(task)
    lookup = query if query is not None else ' '.join(
        word for word in re.findall(r'[\w-]+', normalized_task)
        if word not in ARTIFACT_WORDS)
    kinds = {d['kind'] for d in deliverables}
    domains = ['product']
    if kinds & {'sketch', 'wireframe', 'prototype'}:
        domains += ['style', 'reasoning']
    if kinds & {'tokens', 'prototype'}:
        domains += ['color', 'typography']
    for pattern, domain in [(r'\b(color|palette)\b', 'color'),
                            (r'\b(typography|font)\b', 'typography'),
                            (r'\bstyle\b', 'style')]:
        if re.search(pattern, normalized_task) and domain not in domains:
            domains.append(domain)
    for pattern, domain in [(r'landing|hero', 'landing'), (r'chart|dashboard', 'chart'),
                            (r'icon', 'icons'), (r'motion|animation', 'motion'),
                            (r'accessibility|keyboard|form|validation', 'ux')]:
        if re.search(pattern, normalized_task):
            domains.append(domain)
    searches = [ENGINE['search'](ROOT, lookup, domain, 2) for domain in domains]
    return {'query': lookup, 'normalized_task': normalized_task, 'searches': searches,
            'limitations': ['Finite Vietnamese phrase aliases, not general translation.',
                            'CSV recommendations are not repository facts; inspect applicability.',
                            'Use --query with focused English terms when a category has no match.']}
