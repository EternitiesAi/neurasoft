import unittest
from pathlib import Path
import article_continuity

ROOT = Path(__file__).resolve().parents[1]

class ContinuityPublication(unittest.TestCase):
    def test_all_interaction_states_have_a_readable_fallback(self):
        text = article_continuity.render({'id':'history-and-revision'})
        for key, _, rows in article_continuity.CASES:
            for i, (_, choice, reading) in enumerate(rows):
                self.assertIn(f'data-continuity-case="{key}-{i}"', text)
                self.assertIn(choice, text)
                self.assertIn(reading, text)
        self.assertEqual(text.count('<details>'), 3)

    def test_markdown_does_not_drop_counterfactual_conditions(self):
        text='\n'.join(article_continuity.markdown({'id':'history-and-revision'}))
        for _, _, rows in article_continuity.CASES:
            for _, choice, reading in rows:
                self.assertIn(choice, text)
                self.assertIn(reading, text)

    def test_unknown_configuration_is_rejected(self):
        with self.assertRaises(ValueError):
            article_continuity.validate({'id':'different'})

    def test_assets_are_opted_in_without_changing_prior_interaction(self):
        current=(ROOT/'dist/articles/the-shape-of-someone/index.html').read_text(encoding='utf-8')
        previous=(ROOT/'dist/articles/something-it-is-like-to-be/index.html').read_text(encoding='utf-8')
        self.assertIn('/assets/continuity.js',current)
        self.assertNotIn('/assets/continuity.js',previous)
        self.assertIn('/assets/reflections.js',previous)
        self.assertNotIn('/assets/reflections.js',current)

    def test_public_paper_and_analytic_receipt_exist(self):
        import json
        paper=ROOT/'assets/papers/when-history-changes-the-agent'
        result=json.loads((paper/'analytic-checks.json').read_text())
        self.assertTrue(result['passed'])
        self.assertEqual(result['intervention_effects'],{'model_i':1.0,'model_ii':0.0})
        self.assertGreater((paper/'when-history-changes-the-agent.pdf').stat().st_size,10000)

if __name__ == '__main__':
    unittest.main()
