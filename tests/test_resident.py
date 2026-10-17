"""Public discoverability and evidence boundaries for the Resident section."""
import json
import unittest
from pathlib import Path
from public_search import extract_main_text

DIST = Path(__file__).resolve().parents[1] / 'dist'


class ResidentTests(unittest.TestCase):
    def test_programme_is_discoverable_without_replacing_editorial_work(self):
        home = (DIST / 'index.html').read_text(encoding='utf-8')
        self.assertIn('href="/resident/"', home)
        self.assertIn('href="/articles/the-three-crowns/"', home)
        page = (DIST / 'resident/index.html').read_text(encoding='utf-8')
        self.assertIn('href="/resident/" aria-current="page"', page)
        for route in ('research', 'luna', 'psyche-lab', 'ideas'):
            self.assertIn('Explore the Resident programme', (DIST / route / 'index.html').read_text(encoding='utf-8'))

    def test_search_contains_complete_current_programme_once(self):
        rows = json.loads((DIST / 'assets/search-index.json').read_text(encoding='utf-8'))
        selected = [r for r in rows if r['url'] == '/resident/']
        self.assertEqual(len(selected), 1)
        page = (DIST / 'resident/index.html').read_text(encoding='utf-8')
        self.assertEqual(selected[0]['text'], extract_main_text(page))
        self.assertIn('matched across all 24 paired opportunities', selected[0]['text'])
        self.assertIn('subjective experience', selected[0]['text'])

    def test_progress_retains_candidate_and_comparison_boundaries(self):
        page = (DIST / 'resident/index.html').read_text(encoding='utf-8')
        for phrase in ('Qualified candidate', 'Local comparison complete', 'clean close', 'owner-controlled integration', 'research objectives'):
            self.assertIn(phrase, page)
