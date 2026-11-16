#!/usr/bin/env python3
"""Route technical task intent to local community CSV evidence."""
import re
import runpy
from pathlib import Path

SKILL = Path(__file__).resolve().parents[1]
INTENTS = {
    'fetching': (r'\b(fetch\w*|data loading|waterfall\w*|async|suspense)\b',
                 'data fetching async waterfall'),
    'caching': (r'\b(cach\w*|revalidat\w*)\b', 'cache revalidation'),
    'rendering': (r'\b(render\w*|memo\w*|rerender\w*|hydration)\b', 'render memo'),
    'bundle': (r'\b(bundle\w*|lazy|import\w*|code splitting)\b', 'bundle dynamic import'),
    'forms': (r'\b(form\w*|validation|input\w*)\b', 'form input validation'),
    'accessibility': (r'\b(accessib\w*|keyboard|focus|aria)\b', 'accessibility keyboard focus'),
    'routing': (r'\b(rout\w*|navigation|url|search params)\b', 'routing navigation'),
    'composition': (r'\b(composition|provider\w*|context|variant\w*|reusable)\b',
                    'composition context state'),
    'images': (r'\b(image\w*|font\w*)\b', 'image font optimization'),
    'layout': (r'\b(responsive|layout|overflow)\b', 'responsive layout'),
}
WEB_INTENTS = {'forms', 'accessibility', 'layout'}


def framework_reasons(packages, task):
    reasons = {'react': [], 'nextjs': []}
    for package in packages:
        names = {name for section in package['declared_dependencies'].values()
                 for name in section}
        for dependency, domain in [('react', 'react'), ('next', 'nextjs')]:
            if dependency in names:
                reasons[domain].append(f'{dependency} declared in {package["path"]}')
    for expression, domain in [(r'\breact\b', 'react'), (r'\bnext(?:\.js|js)?\b', 'nextjs')]:
        if re.search(expression, task, re.I):
            reasons[domain].append('Explicit framework mention in task')
    if reasons['nextjs'] and not reasons['react']:
        reasons['react'].append('React guidance associated with Next.js candidate; verify target app')
    return reasons


def knowledge(task, packages, warnings, query=None):
    engine = runpy.run_path(str(SKILL / 'scripts/search-csv.py'))
    try:
        normalized = engine['normalize_query'](query if query is not None else task)
    except (OSError, ValueError) as error:
        warnings.add(f'CSV query normalization unavailable: {error}')
        normalized = query if query is not None else task
    intents = [name for name, (pattern, _) in INTENTS.items() if re.search(pattern, normalized)]
    search_query = query if query is not None else ' '.join(INTENTS[name][1] for name in intents)
    reasons = framework_reasons(packages, task)
    domains = []
    if reasons['react']:
        domains += [('react', '; '.join(reasons['react'])),
                    ('react-stack', '; '.join(reasons['react']))]
    if reasons['nextjs']:
        domains.append(('nextjs', '; '.join(reasons['nextjs'])))
    if WEB_INTENTS.intersection(intents):
        domains.append(('web', 'Task includes form, accessibility, or layout intent'))
    if not domains:
        domains.append(('web', 'No framework evidence; generic interface candidate only'))
    searches = []
    for domain, reason in domains:
        result = engine['search'](SKILL, search_query, domain)
        result['reason'] = reason
        if not search_query:
            result['reason'] += '; no recognized technical intent; supply --query for lookup'
        if result['status'] == 'error':
            warnings.add(f'CSV lookup {domain}: {result.get("error", "failed")}')
        searches.append(result)
    warnings.add('CSV guidance is community evidence; verify Applies To/Docs URL against the target '
                 'manifest and official Vercel/React/Next.js docs before applying. No upgrade implied.')
    return {'query': query if query is not None else task, 'normalized_query': normalized,
            'technical_query': search_query, 'intents': intents, 'searches': searches}
