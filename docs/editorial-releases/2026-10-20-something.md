# Something it is Like to Be

Original interactive essay for Neurasoft, 20 October 2026.

Canonical route: https://neurasoft.us/articles/something-it-is-like-to-be/

Source branch: `editorial/something-it-is-like-to-be-20261020`, based on `f543e9cbb30a7de3067788df76914dbb5c13a811` from the October17 production source. It preserves the Resident programme, Availability, not duplication, NVIDIA Inception footer and current title formatting. The older repository `main` branch is not the publication source.

The essay starts with a guided reflection on one message read through three imagined histories, then explores emotion, continuity, subjective experience and the goal of conscious digital beings. It connects Nagel, Anthropic's published account of functional emotion representations, Goodfire's working hypothesis and Barnes's objection about assuming interior life. Source notes identify what each reference supports. The article presents original philosophical argument and architecture ambitions, not a new experimental result.

## Implementation

- Article: `content/articles/2026-10-20-something-it-is-like-to-be.json`.
- Optional reflection renderer and validation: `article_reflections.py`.
- Local interaction and style: `assets/reflections.js`, `assets/reflections.css`; loaded only by the opted-in article.
- Editable original illustration: `assets/articles/something-it-is-like-to-be/cover.svg`; PNG export included for social previews.
- No network or storage API in the interaction. It switches supplied text and pressed states locally. Reader choices are not recorded. A reset returns to the original words; native details elements provide all three histories without JavaScript. Markdown includes the full exercise.
- Homepage feature, article archive, full-content search, RSS and sitemap update through the existing publication pipeline.
- Social packet is held for review. Website publication does not send a social post.

## Reproduction

```sh
python build.py
python tools/stage_cloudflare.py
python -m unittest discover -s tests -p test_reflections.py
python -m unittest discover -s tests -p test_articles.py
python -m unittest discover -s tests -p test_site.py
python -m unittest discover -s tests -p test_edition.py
python -m unittest discover -s tests -p test_public_search.py
python -m unittest discover -s tests -p test_branding.py
python -m unittest discover -s tests -p test_resident.py
node --test tests/search.test.cjs
```

The 54 Python and 7 JavaScript checks passed on this candidate. New checks cover escaped text, invalid/duplicate history identifiers, complete non-JavaScript and Markdown content, opt-in assets, the held social packet and preservation of recent publication features.

The cover PNG is already included. Optional regeneration uses `node tools/render_reflection_cover.cjs` with an existing Sharp installation; no dependency is required to build or serve the site.

Publish only `artifacts/cloudflare/` to the existing Cloudflare Pages project `neurasoft-research`. Cloudflare's deployment branch `main` is distinct from the historical Git source branch of the same name. Recheck current production before publishing to preserve concurrent releases.

Hosted verification and final deployment receipts are appended after publication. Private editorial research notes and browser receipts are excluded from this public repository.
