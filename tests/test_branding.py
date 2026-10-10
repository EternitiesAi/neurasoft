import json
import unittest
from pathlib import Path
from branding import public_name, NAME, EXPANSION

ROOT = Path(__file__).resolve().parents[1]


class NamingTests(unittest.TestCase):
    def test_public_label_without_identifier_changes(self):
        self.assertEqual(public_name('Luna / LUNA / Lunari / /luna/ / luna-2'),
                         'L.U.N.A / L.U.N.A / Lunari / /luna/ / luna-2')

    def test_definition_and_routes(self):
        text = (ROOT / 'dist/luna/index.html').read_text(encoding='utf-8')
        self.assertIn(EXPANSION, text)
        self.assertIn('https://neurasoft.us/luna/', text)
        self.assertIn(NAME, text)

    def test_all_public_html_uses_official_label(self):
        import re
        for file in (ROOT / 'dist').rglob('*.html'):
            self.assertIsNone(re.search(r'\b(?:Luna|LUNA)\b', file.read_text(encoding='utf-8')), str(file))

    def test_search_preserves_luna_route(self):
        rows = json.loads((ROOT / 'dist/assets/search-index.json').read_text(encoding='utf-8'))
        luna = next(r for r in rows if r['url'] == '/luna/')
        self.assertIn(NAME, luna['title'])
        self.assertIn(EXPANSION, luna['text'])
