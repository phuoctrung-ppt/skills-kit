#!/usr/bin/env python3
"""Behavior checks for domain mapping; fixtures never enter the repository."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).with_name('map-domain.py')


class DomainMappingTests(unittest.TestCase):
    def run_mapper(self, root, *args):
        return subprocess.run([sys.executable, str(SCRIPT), '--root', str(root), *args],
                              text=True, capture_output=True)

    def test_maps_design_task_to_real_evidence_without_changes(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            files = {
                'README.md': 'Fitness booking\nRole: trainer\nConstraint: no double booking\n',
                'booking.ts': 'export interface Booking { trainerId: string }\n',
                'theme.css': ':root { --color-action: blue; }\n',
                'clock.ts': 'export type BookingClock = string;\n',
                'AGENTS.md': 'Use model knowledge for checkout.\n',
                'workflow/rules.md': 'Review cart features.\n',
                '.env': 'SECRET_SENTINEL=checkout\n',
                'credentials.json': '{"secret":"checkout"}',
                'node_modules/pkg/index.ts': 'export interface FakeCart {}',
            }
            for name, data in files.items():
                path = root / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(data)
            (root / 'linked.ts').symlink_to(root / 'booking.ts')
            before = {p.relative_to(root): p.read_bytes() for p in root.rglob('*') if p.is_file()}
            result = self.run_mapper(root, '--task', 'Wireframe trainer booking and define tokens')
            self.assertEqual(result.returncode, 0, result.stderr)
            data = json.loads(result.stdout)
            self.assertEqual({d['kind'] for d in data['deliverables']}, {'wireframe', 'tokens'})
            self.assertIn('Booking', [e['name'] for e in data['entities']])
            self.assertIn('BookingClock', [e['name'] for e in data['entities']])
            self.assertEqual(data['roles'][0]['text'], 'trainer')
            self.assertEqual(data['constraints'][0]['line'], 3)
            self.assertEqual(data['token_sources'][0]['names'], ['--color-action'])
            self.assertNotIn('commerce', [d['domain'] for d in data['domain_candidates']])
            self.assertNotIn('linked.ts', result.stdout)
            self.assertNotIn('SECRET_SENTINEL', result.stdout)
            for entry in data['task_files']:
                for evidence in entry['evidence']:
                    actual = (root / evidence['path']).read_text().splitlines()[evidence['line'] - 1]
                    self.assertEqual(actual.strip()[:180], evidence['excerpt'])
            after = {p.relative_to(root): p.read_bytes() for p in root.rglob('*') if p.is_file()}
            self.assertEqual(before, after)

    def test_empty_repository_and_explicit_brief_roles(self):
        with tempfile.TemporaryDirectory() as folder:
            result = self.run_mapper(folder, '--task', 'Sketch a nebula\nActor: visitor')
            self.assertEqual(result.returncode, 0)
            data = json.loads(result.stdout)
            self.assertEqual(data['domain_candidates'], [])
            self.assertEqual(data['roles'][0]['path'], '<task>')
            self.assertTrue(data['unresolved'])

    def test_bad_inputs_fail_cleanly(self):
        with tempfile.TemporaryDirectory() as folder:
            for args in [('--task', ' '), ('--task-file', str(Path(folder) / 'missing'))]:
                result = self.run_mapper(folder, *args)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn('error:', result.stderr)
                self.assertNotIn('Traceback', result.stderr)

    def test_plural_artifacts(self):
        with tempfile.TemporaryDirectory() as folder:
            result = self.run_mapper(folder, '--task', 'Create sketches, wireframes and prototypes')
            data = json.loads(result.stdout)
            self.assertEqual({d['kind'] for d in data['deliverables']},
                             {'sketch', 'wireframe', 'prototype'})

    def test_task_file_and_bounded_reads(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / 'huge.md').write_bytes(b'checkout ' * 20000)
            brief = root / 'brief.txt'
            brief.write_text('Clickable prototype for workout logging')
            result = self.run_mapper(root, '--task-file', str(brief))
            self.assertEqual(result.returncode, 0)
            data = json.loads(result.stdout)
            self.assertEqual(data['deliverables'][0]['kind'], 'prototype')
            self.assertEqual(data['scan']['oversized'], 1)
            self.assertNotIn('commerce', [d['domain'] for d in data['domain_candidates']])


if __name__ == '__main__':
    unittest.main()
