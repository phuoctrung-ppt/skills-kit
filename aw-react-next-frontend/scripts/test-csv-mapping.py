#!/usr/bin/env python3
"""Exercise task routing and real CSV provenance through the public mapper."""
import csv
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SKILL = Path(__file__).resolve().parents[1]


def mapping(root, task, skill=SKILL, query=None):
    command = [sys.executable, str(skill / 'scripts/map-task.py'),
               '--root', str(root), '--task', task]
    if query is not None:
        command += ['--query', query]
    return json.loads(subprocess.run(command, capture_output=True, text=True,
                                     check=True).stdout)


class MappingTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix='frontend-csv-test-')
        self.root = Path(self.tmp.name) / 'project'
        self.root.mkdir()
        self.addCleanup(self.tmp.cleanup)

    def manifest(self, dependencies):
        (self.root / 'package.json').write_text(json.dumps({'dependencies': dependencies}))

    def test_vietnamese_fetch_task_returns_source_records(self):
        self.manifest({'react': '^18.2.0', 'next': '^14.2.0'})
        output = mapping(self.root, 'tối ưu tải dữ liệu React Next.js')
        self.assertIn('knowledge', output, 'Mapper must query bundled CSV data')
        searches = output['knowledge']['searches']
        self.assertEqual({s['domain'] for s in searches}, {'react', 'react-stack', 'nextjs'})
        self.assertTrue(all(s['status'] == 'matched' for s in searches))
        for search in searches:
            self.assertIn('fetch', search['query'])
            for result in search['results']:
                source = SKILL / result['source']
                with source.open(encoding='utf-8-sig', newline='') as handle:
                    rows = list(csv.DictReader(handle))
                self.assertEqual(rows[result['record'] - 1], result['values'])
        self.assertEqual(output['manifests'][0]['declared_dependencies']['dependencies']['next'], '^14.2.0')

    def test_unknown_task_does_not_invent_recommendations(self):
        self.manifest({'react': '^18', 'next': '^14'})
        output = mapping(self.root, 'zqxwvvfj')
        self.assertIn('knowledge', output)
        self.assertTrue(output['knowledge']['searches'])
        self.assertTrue(all(s['status'] == 'no_match' and not s['results']
                            for s in output['knowledge']['searches']))

    def test_react_only_does_not_select_next(self):
        self.manifest({'react': '^18'})
        output = mapping(self.root, 'Optimize data fetching')
        self.assertIn('knowledge', output)
        self.assertEqual({s['domain'] for s in output['knowledge']['searches']},
                         {'react', 'react-stack'})
        self.assertTrue(all(s['reason'] for s in output['knowledge']['searches']))

    def test_missing_csv_is_reported_without_losing_repository_mapping(self):
        copied = Path(self.tmp.name) / 'skill'
        shutil.copytree(SKILL, copied, ignore=shutil.ignore_patterns('__pycache__'))
        (copied / 'data/stacks/nextjs.csv').unlink()
        output = mapping(self.root, 'Next.js data fetching', skill=copied)
        self.assertEqual(output['manifests'], [])
        entry = next(s for s in output['knowledge']['searches'] if s['domain'] == 'nextjs')
        self.assertEqual(entry['status'], 'error')
        self.assertTrue(entry['error'])
        self.assertTrue(any('CSV' in warning for warning in output['warnings']))

    def test_override_queries_technical_intent(self):
        self.manifest({'react': '^18'})
        output = mapping(self.root, 'Làm tính năng cho huấn luyện viên', query='data fetching')
        self.assertEqual(output['knowledge']['query'], 'data fetching')
        self.assertTrue(all(s['status'] == 'matched' for s in output['knowledge']['searches']))

    def test_form_without_stack_uses_web_guidance(self):
        output = mapping(self.root, 'Improve form keyboard accessibility')
        self.assertIn('knowledge', output)
        self.assertEqual({s['domain'] for s in output['knowledge']['searches']}, {'web'})
        self.assertEqual(output['knowledge']['searches'][0]['status'], 'matched')


if __name__ == '__main__':
    unittest.main()
