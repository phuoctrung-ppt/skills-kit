#!/usr/bin/env python3
"""Behavioral checks against a temporary mixed-version monorepo."""
import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path

SCRIPT = Path(__file__).with_name('map-task.py')


def run(root, task='Refactor booking filters and cache', check=True):
    return subprocess.run([sys.executable, str(SCRIPT), '--root', str(root),
                           '--task', task], capture_output=True, text=True, check=check)


def snapshot(root):
    return {str(p.relative_to(root)): (p.lstat().st_mtime_ns,
            p.readlink().as_posix() if p.is_symlink() else
            hashlib.sha256(p.read_bytes()).hexdigest() if p.is_file() else 'directory')
            for p in root.rglob('*')}


def main():
    fixture = {
        'package.json': json.dumps({'scripts': {'evil': 'touch SHOULD_NOT_EXIST'}}),
        'apps/web/package.json': json.dumps({'dependencies': {'next': '^16.0.0', 'react': '^19.0.0'}}),
        'apps/legacy/package.json': json.dumps({'dependencies': {'next': '^14.2.0', 'react': '^18.0.0'}}),
        'apps/web/src/app/bookings/page.tsx': "export default async function Bookings() { return fetch('/bookings'); }",
        'apps/legacy/pages/bookings.tsx': 'export async function getServerSideProps() {}',
        'apps/web/src/components/booking-filter.tsx': "'use client';\nexport function BookingFilter() { const booking = useQuery(); return null; }",
        'packages/shared-types/booking-schema.ts': 'export type Booking = { id: string };',
        'apps/web/src/theme/tokens.css': ':root { --color-booking: red; }',
        'apps/web/src/theme/token.json': '{"booking": {"$value": "red"}}',
        'apps/web/src/theme/tokens.json': '{"booking": {"$value": "red"}}',
        'apps/web/next.config.ts': 'export default { cacheComponents: true };',
        '.gitignore': 'ignored/\n*.generated.ts\n!keep.generated.ts\n',
        'ignored/booking.ts': 'SECRET_IGNORE',
        'node_modules/booking.ts': 'SECRET_MODULE',
        '.env': 'SECRET_ENV',
        'credentials.json': 'SECRET_CREDENTIAL',
        'access-token.json': 'SECRET_ACCESS_TOKEN',
        'auth-token.json': 'SECRET_AUTH_TOKEN',
        'session-token.json': 'SECRET_SESSION_TOKEN',
        'x.generated.ts': 'SECRET_GENERATED',
        'apps/web/.gitignore': 'private-folder/\n',
        'apps/web/private-folder/booking.ts': 'SECRET_NESTED',
        'bad/package.json': 'invalid',
        'large.ts': 'x' * 200000,
        'plans/booking.md': 'use client booking',
        'skills/booking.md': 'use client booking',
        'workflow/booking.md': 'use client booking',
        'AGENTS.md': 'use client booking',
        'CLAUDE.md': 'use client booking',
    }
    with tempfile.TemporaryDirectory(prefix='frontend-map-test-') as tmp:
        root = Path(tmp)
        for relative, content in fixture.items():
            file = root / relative
            file.parent.mkdir(parents=True, exist_ok=True)
            file.write_text(content)
        (root / 'binary.ts').write_bytes(b'\0SECRET_BINARY')
        (root / 'link.ts').symlink_to(root / 'credentials.json')
        before = snapshot(root)
        result = run(root)
        data = json.loads(result.stdout)
        assert len(data['manifests']) == 3
        deps = {p['path']: p['declared_dependencies'] for p in data['manifests']}
        assert deps['apps/legacy/package.json']['dependencies']['react'] == '^18.0.0'
        assert deps['apps/web/package.json']['dependencies']['react'] == '^19.0.0'
        assert {r['router'] for r in data['routes']} == {'app', 'pages'}
        assert all(r['manifest'].startswith('apps/') for r in data['routes'])
        assert any(s['kind'] == 'client_directive' and s['line'] == 1 for s in data['signals'])
        assert any(s['kind'] == 'cache_config' for s in data['signals'])
        assert any(t['css_identifiers'] == ['--color-booking'] for t in data['inventory']['tokens'])
        token_paths = {t['path'] for t in data['inventory']['tokens']}
        assert 'apps/web/src/theme/token.json' in token_paths
        assert 'apps/web/src/theme/tokens.json' in token_paths
        assert any(t['path'].endswith('booking-schema.ts') for t in data['inventory']['contracts'])
        assert any(m['path'].endswith('booking-filter.tsx') for m in data['task_matches'])
        assert len(data['guidance']) == 3
        excluded = ['SECRET_', 'SHOULD_NOT_EXIST', 'link.ts', 'ignored/booking',
                    'plans/booking', 'skills/booking', 'workflow/booking', 'AGENTS.md', 'CLAUDE.md']
        assert not any(term in result.stdout for term in excluded)
        assert any('Invalid manifest' in w for w in data['warnings'])
        assert data['scan']['oversize'] == 1 and data['scan']['binary'] == 1
        assert before == snapshot(root)
        empty = root / 'empty'
        empty.mkdir()
        empty_data = json.loads(run(empty).stdout)
        assert empty_data['manifests'] == []
        assert any('unknown' in w for w in empty_data['warnings'])
        assert run(root / 'missing', check=False).returncode == 2
        assert run(root, task=' \n ', check=False).returncode == 2
    print('PASS: manifest versions, router ownership, source evidence, exclusions, read-only scan, invalid inputs')


if __name__ == '__main__':
    main()
