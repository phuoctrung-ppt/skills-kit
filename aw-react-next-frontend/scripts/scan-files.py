"""Bounded read-only file discovery; intentionally not an exact Git parser."""
import fnmatch
import re
from collections import Counter
from pathlib import Path

SKIP_DIRS = {'node_modules', 'vendor', 'dist', 'build', 'coverage', 'out',
             'target', '__pycache__', 'generated', 'storybook-static',
             'skills', 'plans', 'workflow'}
EXTENSIONS = {'.js', '.jsx', '.ts', '.tsx', '.mjs', '.cjs', '.json', '.css',
              '.scss', '.md', '.mdx', '.yaml', '.yml', '.html', '.prisma'}
SECRET = re.compile(r'(^|[._-])(secret|secrets|credential|credentials|private|'
                    r'password|passwords|tokens?[-_]secret|'
                    r'(?:access|auth|refresh|api|session)[-_]tokens?)([._-]|$)', re.I)
MAX_BYTES = 192 * 1024
MAX_FILES = 4000


def safe_name(path):
    name = path.name.lower()
    return not (name.startswith('.') or SECRET.search(name) or
                name.endswith(('.pem', '.key', '.p12', '.lock')) or
                name in {'package-lock.json', 'pnpm-lock.yaml', 'yarn.lock',
                         'agents.md', 'claude.md'})


def read_text(path, counts):
    try:
        if path.is_symlink() or not path.is_file():
            counts['symlink_or_special'] += 1
            return None
        if path.stat().st_size > MAX_BYTES:
            counts['oversize'] += 1
            return None
        with path.open('rb') as source:
            raw = source.read(MAX_BYTES + 1)
        if len(raw) > MAX_BYTES:
            counts['oversize'] += 1
            return None
        if b'\0' in raw:
            counts['binary'] += 1
            return None
        return raw.decode('utf-8')
    except (OSError, UnicodeError):
        counts['unreadable'] += 1
        return None


def ignores(directory, inherited, counts, warnings):
    rules = list(inherited)
    ignore_file = directory / '.gitignore'
    if not ignore_file.exists() or ignore_file.is_symlink():
        return rules
    content = read_text(ignore_file, counts)
    if content is None:
        return rules
    for line in content.splitlines():
        pattern = line.strip()
        if not pattern or pattern.startswith('#'):
            continue
        if pattern.startswith('!') or '\\' in pattern:
            warnings.add('Unsupported gitignore negation/escape; scan may omit files.')
            continue
        rules.append((directory, pattern))
    return rules


def ignored(path, rules):
    for base, raw in rules:
        relative = path.relative_to(base).as_posix()
        anchored = raw.startswith('/')
        pattern = raw.strip('/')
        if '/' in pattern or anchored:
            if fnmatch.fnmatchcase(relative, pattern):
                return True
        elif any(fnmatch.fnmatchcase(part, pattern) for part in Path(relative).parts):
            return True
    return False


def scan(root):
    counts, warnings, files = Counter(), set(), []
    warnings.add('Gitignore handling is approximate; global/info excludes are not read.')
    stack = [(root, [])]
    while stack and counts['visited'] < MAX_FILES:
        directory, inherited = stack.pop()
        rules = ignores(directory, inherited, counts, warnings)
        try:
            entries = sorted(directory.iterdir(), key=lambda p: p.name)
        except OSError:
            counts['unreadable'] += 1
            continue
        for path in entries:
            if counts['visited'] >= MAX_FILES:
                counts['file_cap_reached'] = 1
                break
            counts['visited'] += 1
            if path.is_symlink():
                counts['symlink_or_special'] += 1
                continue
            if not safe_name(path) or path.name in SKIP_DIRS or ignored(path, rules):
                counts['excluded'] += 1
                continue
            if path.is_dir():
                stack.append((path, rules))
                continue
            if path.suffix.lower() not in EXTENSIONS:
                counts['unsupported'] += 1
                continue
            content = read_text(path, counts)
            if content is not None:
                counts['read'] += 1
                files.append((path.relative_to(root).as_posix(), content))
    if stack:
        counts['file_cap_reached'] = 1
    for key in ('oversize', 'unreadable', 'binary', 'file_cap_reached'):
        if counts[key]:
            warnings.add(f'Partial scan: {key}={counts[key]}.')
    return files, counts, warnings
