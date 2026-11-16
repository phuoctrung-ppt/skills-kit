"""End-to-end task routing for design CSV knowledge."""
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


def run(skill, root, task, *args):
    result = subprocess.run([sys.executable, str(skill / 'scripts/map-domain.py'),
                             '--root', str(root), '--task', task, *args],
                            check=True, capture_output=True, text=True)
    return json.loads(result.stdout)


class DesignMappingTests(unittest.TestCase):
    def test_direct_palette_and_typography_request_routes_datasets(self):
        with tempfile.TemporaryDirectory() as folder:
            data = run(ROOT, folder, 'Thiết kế bảng màu và kiểu chữ cho phòng tập')
            domains = {s['domain'] for s in data['knowledge']['searches']}
            self.assertTrue({'product', 'color', 'typography'} <= domains)

    def test_vietnamese_task_maps_domain_artifacts_and_actual_data(self):
        with tempfile.TemporaryDirectory() as folder:
            data = run(ROOT, folder, 'Thiết kế khung giao diện và bộ token cho phòng tập thể hình')
            self.assertEqual({d['kind'] for d in data['deliverables']}, {'wireframe', 'tokens'})
            self.assertIn('fitness', [d['domain'] for d in data['domain_candidates']])
            searches = data['knowledge']['searches']
            product = next(s for s in searches if s['domain'] == 'product')
            self.assertIn('Fitness', product['results'][0]['values']['Product Type'])
            palette = next(s for s in searches if s['domain'] == 'color')
            self.assertEqual(palette['status'], 'matched')

    def test_unknown_query_does_not_invent_data(self):
        with tempfile.TemporaryDirectory() as folder:
            data = run(ROOT, folder, 'Sketch zzzxqv987')
            self.assertTrue(all(s['status'] == 'no_match' for s in data['knowledge']['searches']))

    def test_missing_csv_reports_error_and_keeps_context(self):
        with tempfile.TemporaryDirectory() as folder:
            skill = Path(folder) / 'copy'
            shutil.copytree(ROOT, skill)
            (skill / 'data/products.csv').unlink()
            data = run(skill, folder, 'Wireframe fitness')
            self.assertEqual(data['deliverables'][0]['kind'], 'wireframe')
            self.assertTrue(any(s['status'] == 'error' for s in data['knowledge']['searches']))

    def test_explicit_query_and_cwd_independence(self):
        with tempfile.TemporaryDirectory() as folder:
            data = run(ROOT, folder, 'Create tokens', '--query', 'fitness')
            self.assertEqual(data['knowledge']['query'], 'fitness')
            self.assertTrue(any(s['status'] == 'matched' for s in data['knowledge']['searches']))


if __name__ == '__main__':
    unittest.main()
