#!/usr/bin/env python3
"""Map a frontend request to bounded, local repository evidence."""
import argparse
import json
import re
import runpy
from pathlib import Path

SCAN = runpy.run_path(str(Path(__file__).with_name('scan-files.py')))['scan']
KNOWLEDGE = runpy.run_path(str(Path(__file__).with_name('csv-guidance.py')))['knowledge']
CAP = 120
STOP = set('a an the to for and or in on with from using use add create implement '
           'update fix make build frontend page component please this that of is'.split())
PATTERNS = {
    'client_directive': r'''["']use client["']''',
    'server_directive': r'''["']use server["']''',
    'cache_directive': r'''["']use cache(?::\s*\w+)?["']''',
    'fetching': r'\b(fetch|useSWR|useQuery|useInfiniteQuery)\s*\(',
    'caching': r'\b(unstable_cache|revalidatePath|revalidateTag|cacheLife|cacheTag)\s*\(',
    'cache_config': r'\bcacheComponents\s*:',
    'suspense': r'<Suspense\b',
    'pages_data': r'\b(getServerSideProps|getStaticProps|getStaticPaths)\b',
    'context': r'\b(createContext|useContext)\s*\(',
}


def words(value):
    split = re.sub(r'([a-z])([A-Z])', r'\1 \2', value)
    return set(re.findall(r'[a-z][a-z0-9]{2,}', split.lower())) - STOP


def manifests(files, warnings):
    result = []
    for path, content in files:
        if Path(path).name != 'package.json':
            continue
        try:
            value = json.loads(content)
            if not isinstance(value, dict):
                raise ValueError('Expected object')
            dependencies = {}
            for section in ('dependencies', 'devDependencies', 'peerDependencies',
                            'optionalDependencies'):
                if isinstance(value.get(section), dict):
                    dependencies[section] = {k: v for k, v in value[section].items()
                                             if isinstance(v, str)}
            scripts = value.get('scripts', {})
            result.append({'path': path, 'declared_dependencies': dependencies,
                           'script_names': sorted(scripts) if isinstance(scripts, dict) else []})
        except (ValueError, TypeError):
            warnings.add(f'Invalid manifest: {path}.')
    return result


def owner(path, packages):
    choices = [p['path'] for p in packages if
               Path(p['path']).parent == Path('.') or
               Path(p['path']).parent in Path(path).parents]
    return max(choices, key=lambda p: len(Path(p).parts)) if choices else None


def route(path, manifest):
    relative = Path(path).relative_to(Path(manifest).parent) if manifest else Path(path)
    parts = relative.parts
    if parts and parts[0] == 'src':
        parts = parts[1:]
    if len(parts) < 2 or relative.suffix not in {'.js', '.jsx', '.ts', '.tsx', '.mdx'}:
        return None
    if parts[0] == 'app' and relative.stem in {
            'page', 'route', 'layout', 'loading', 'error', 'not-found', 'template', 'default'}:
        return {'path': path, 'router': 'app', 'kind': relative.stem, 'manifest': manifest}
    if parts[0] == 'pages' and not relative.name.endswith('.d.ts'):
        return {'path': path, 'router': 'pages', 'kind': 'api' if 'api' in parts[1:2]
                else 'page-or-convention', 'manifest': manifest}
    return None


def analyze(files, packages, task):
    inventory = {'components': [], 'contracts': [], 'tokens': []}
    routes, signals, matches = [], [], []
    task_words = words(task)
    for path, content in files:
        item = route(path, owner(path, packages))
        if item:
            routes.append(item)
        lower = path.lower()
        if any(p in lower.split('/') for p in ('components', 'ui')) or path.endswith('.tsx'):
            inventory['components'].append({'path': path})
        if any(p in lower for p in ('schema', 'contract', 'dto', 'shared-types', 'types/')):
            inventory['contracts'].append({'path': path})
        token_names = sorted(set(re.findall(r'(--[a-zA-Z][\w-]*)\s*:', content)))
        if token_names or any(p in lower for p in ('theme', 'token', 'tailwind.config')):
            inventory['tokens'].append({'path': path, 'css_identifiers': token_names[:CAP]})
        path_hits = task_words & words(path)
        line_hits = []
        for number, line in enumerate(content.splitlines(), 1):
            if task_words & words(line) and len(line_hits) < 12:
                line_hits.append({'line': number, 'terms': sorted(task_words & words(line))})
            for kind, pattern in PATTERNS.items():
                if re.search(pattern, line):
                    signals.append({'path': path, 'line': number, 'kind': kind})
        if path_hits or line_hits:
            matches.append({'path': path, 'path_terms': sorted(path_hits),
                            'lines': line_hits, 'score': len(path_hits) * 5 + len(line_hits)})
    matches.sort(key=lambda entry: (-entry['score'], entry['path']))
    return inventory, routes, signals, matches


def guidance(task, packages, signals, routes):
    result = [{'reference': 'references/react-performance.md',
               'reason': 'React/frontend implementation request; apply relevant performance decisions.'}]
    dependencies = {name for package in packages
                    for section in package['declared_dependencies'].values() for name in section}
    if 'next' in dependencies or routes or re.search(r'\bnext(?:\.js)?\b', task, re.I):
        result.append({'reference': 'references/next-version-guidance.md',
                       'reason': 'Next dependency, router convention, or explicit task mention; verify target version.'})
    if re.search(r'\b(component|composition|provider|variant|reusable|refactor)\w*\b', task, re.I) or any(
            s['kind'] == 'context' for s in signals):
        result.append({'reference': 'references/composition.md',
                       'reason': 'Component API task or context usage detected.'})
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', required=True, type=Path)
    parser.add_argument('--task', required=True)
    parser.add_argument('--query', help='Explicit English CSV query; retain original task mapping')
    args = parser.parse_args()
    if not args.task.strip():
        parser.error('--task must contain non-whitespace text')
    if args.query is not None and not args.query.strip():
        parser.error('--query must contain non-whitespace text')
    if not args.root.is_dir() or args.root.is_symlink():
        parser.error('--root must be an existing non-symlink directory')
    root = args.root.resolve()
    files, counts, warnings = SCAN(root)
    packages = manifests(files, warnings)
    inventory, routes, signals, matches = analyze(files, packages, args.task)
    selected = guidance(args.task, packages, signals, routes)
    def capped(name, entries):
        if len(entries) > CAP:
            warnings.add(f'Output truncated: {name}={len(entries)}, showing {CAP}.')
        return entries[:CAP]
    output = {'schema_version': 1, 'root': str(root), 'task': args.task,
              'manifests': capped('manifests', packages), 'routes': capped('routes', routes),
              'inventory': {k: capped(k, v) for k, v in inventory.items()},
              'signals': capped('signals', signals), 'task_matches': capped('task_matches', matches),
              'guidance': selected, 'scan': dict(counts),
              'knowledge': KNOWLEDGE(args.task, packages, warnings, args.query)}
    if not packages:
        warnings.add('No readable package.json found; framework/version unknown.')
    warnings.add('Lexical evidence only: verify comments, imports, routing configuration, and business rules.')
    output['warnings'] = sorted(warnings)
    print(json.dumps(output, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()
