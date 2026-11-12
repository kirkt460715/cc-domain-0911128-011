import json
import unittest
from pathlib import Path


class StudyInputTests(unittest.TestCase):
    def test_domain_references_and_units(self):
        data=json.loads((Path(__file__).resolve().parents[1]/'fixtures/study-input.json').read_text())
        from metrology.configuration import Configuration
        from metrology.service import Service
        import tempfile
        with tempfile.TemporaryDirectory() as directory:
            with Service(Path(directory)/'lab.sqlite3') as service:
                service.configuration.apply(data['configuration'])
                identifiers={r['id'] for r in data['configuration']['instruments']}
                self.assertTrue(all(r['instrument'] in identifiers for r in data['observations']))
        self.assertEqual(len(data['observations']),len({r['id'] for r in data['observations']}))
