import copy
import json
from pathlib import Path
import unittest
import article_reflections as reflection

ROOT = Path(__file__).resolve().parents[1]
ARTICLE = json.loads((ROOT/'content/articles/2026-10-20-something-it-is-like-to-be.json').read_text(encoding='utf-8'))
R = ARTICLE['sections'][0]['reflection']


class ReflectionTests(unittest.TestCase):
    def test_every_history_is_readable_without_javascript_and_in_markdown(self):
        html = reflection.render(R)
        md = '\n'.join(reflection.markdown(R))
        self.assertEqual(html.count('<details '), 3)
        self.assertNotIn('<div data-stories hidden', html)
        for o in R['options']:
            self.assertIn(o['context'], html)
            self.assertIn(o['context'], md)
            self.assertIn(o['question'], md)

    def test_untrusted_editorial_text_is_escaped(self):
        r = copy.deepcopy(R)
        r['message'] = '<script>alert(1)</script>'
        r['options'][0]['label'] = '"><img src=x onerror=alert(1)>'
        html = reflection.render(r)
        self.assertNotIn('<script>', html)
        self.assertNotIn('<img', html)
        self.assertIn('&lt;script&gt;', html)

    def test_invalid_and_duplicate_choices_are_rejected(self):
        for key in ('welcome', '../invalid'):
            r = copy.deepcopy(R)
            r['options'][1]['id'] = key
            with self.assertRaises(ValueError): reflection.validate(r)

    def test_only_opted_in_article_loads_interaction_and_social_is_held(self):
        paths = list((ROOT/'dist/articles').glob('*/index.html'))
        self.assertGreater(len(paths), 1)
        for path in paths:
            html = path.read_text(encoding='utf-8')
            self.assertEqual('/assets/reflections.js' in html, path.parent.name == ARTICLE['slug'])
        packet = json.loads((ROOT/'dist/articles'/ARTICLE['slug']/'grok-packet.json').read_text(encoding='utf-8'))
        self.assertEqual(packet['publish'], 'review')
        self.assertEqual(packet['social_publication_status'], 'prepared-not-confirmed')

    def test_new_release_preserves_recent_article_brand_and_title(self):
        self.assertTrue((ROOT/'dist/articles/availability-not-duplication/index.html').is_file())
        html = (ROOT/'dist/articles'/ARTICLE['slug']/'index.html').read_text(encoding='utf-8')
        self.assertIn('<title>Something it is Like to Be | Neurasoft</title>', html)
        self.assertIn('NVIDIA', html)
        self.assertIn('/resident/', html)


if __name__ == '__main__': unittest.main()
