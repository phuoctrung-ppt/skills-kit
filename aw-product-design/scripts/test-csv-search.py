"""Verify retrieval against downloaded data and meaningful failure cases."""
import csv
import hashlib
import json
from pathlib import Path
import runpy
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class RetrievalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.api = runpy.run_path(str(ROOT / 'scripts/search-csv.py'))

    def test_fitness_and_vietnamese_retrieve_source_rows(self):
        for query in ['fitness gym', 'ứng dụng phòng tập thể hình']:
            result = self.api['search'](ROOT, query, 'product')
            self.assertEqual(result['status'], 'matched')
            first = result['results'][0]
            self.assertIn('Fitness', first['values']['Product Type'])
            with (ROOT / first['source']).open(newline='') as f:
                rows = list(csv.DictReader(f))
            self.assertEqual(first['values'], rows[first['record'] - 1])

    def test_palette_is_real_and_unknown_does_not_get_defaults(self):
        result = self.api['search'](ROOT, 'fitness', 'color')
        self.assertEqual(result['status'], 'matched')
        self.assertTrue(result['results'][0]['values']['Primary'].startswith('#'))
        self.assertEqual(self.api['search'](ROOT, 'zzzxqv987', 'color')['status'], 'no_match')

    def test_missing_csv_is_an_explicit_error(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'data').mkdir()
            (root / 'data/catalog.json').write_text(json.dumps({'product': {
                'file': 'missing.csv', 'search_columns': ['Product Type']}}))
            self.assertEqual(self.api['search'](root, 'fitness', 'product')['status'], 'error')

    def test_downloaded_snapshots_have_matching_checksums(self):
        manifest = json.loads((ROOT / 'data/upstream-manifest.json').read_text())
        for name, metadata in manifest['files'].items():
            data = (ROOT / 'data' / name).read_bytes()
            self.assertEqual(hashlib.sha256(data).hexdigest(), metadata['sha256'])


if __name__ == '__main__':
    unittest.main()
