# Neurasoft — Research Publication / Edition 3

**New essay and methods preprint, 27 October 2026:** [The Shape of Someone](https://neurasoft.us/articles/the-shape-of-someone/) and [When History Changes the Agent](https://neurasoft.us/assets/papers/when-history-changes-the-agent/).
Current publication source: editorial/the-shape-of-someone-20261027, based on the complete October24 publication and released social packet. See [the release record](docs/editorial-releases/2026-10-27-shape.md).
The newer publication source above supersedes the dated branch pointers below; the historical Git main branch remains unsuitable for deployment.

**New interactive essay, 20 October 2026:** [Something it is Like to Be](https://neurasoft.us/articles/something-it-is-like-to-be/).
Current publication source: `editorial/something-it-is-like-to-be-20261020`, based on the October17 NVIDIA Inception release and preserving all prior editorial work.
See [the release record](docs/editorial-releases/2026-10-20-something.md) for the article, local interaction and reproduction steps.

**Resident programme, published 16 October 2026:** [neurasoft.us/resident/](https://neurasoft.us/resident/).
Read [the release record](docs/editorial-releases/2026-10-16-resident.md) before the historical edition notes below.
That section originated on `publication/resident-programme-20261016`, descended from the October 14 editorial release; the current source branch is named above.
The repository's older `main` branch does not contain the current public site. Do not deploy it over production.
`resident_programme.py` and `content/resident-programme.html` own this section; `assets/resident.css` owns its presentation.

**Daily illustrated articles:** see [EDITORIAL.md](EDITORIAL.md) for the September 24
editorial lane, daily publishing, visual standards, Grok Bot packets and exact
release receipts. `articles.py` now runs after the historical edition described below.

**Taking this over? Start at [`PICKUP.md`](PICKUP.md)** — build, verify, the two
line-ending/encoding defects fixed on 2026-09-16, and two open Cloudflare settings.

Published on Cloudflare Pages, 16 September 2026. 37 HTML pages (36 content pages and a 404), seven preserved journal essays, two local educational exhibits, three attributed research records and an architecture map.

Read `docs/publication-edition-3.md` and `docs/release-2026-09-16.md` for the current release, then `docs/domain-cutover-2026-09-16.md` for the completed neurasoft.us cutover and two open Cloudflare dashboard actions (Email Address Obfuscation is rewriting the contact links; a CSP-blocked analytics beacon is being injected). The V2 handoff and its verification document remain historical evidence, not current deployment instructions.

Build: `python3 build.py`, then `python3 tools/stage_cloudflare.py`. No runtime package installation or npm build is needed. Publish **only `artifacts/cloudflare/`** to the Cloudflare Pages project `neurasoft-research`, branch `main`, using Wrangler. The stage omits Netlify's redirect file because Cloudflare serves the native 404 document. Do not publish the repository root or private review materials.

`edition_three.py` owns the current home, architecture, studies and final editorial amendments. `content/studies.json` is the study registry. `public_search.py` builds the complete main-content index.
`publication.py` owns the earlier expanded editorial pages, navigation and footer.
`build.py` owns the original research pages and journal generation, then invokes the publication and edition layers in that order.
`content/journal.json` holds the seven original notes. `assets/site.css` and `assets/site.js` contain the unified paper/sage theme and local interactions.
`tools/make_portable_preview.py` produces the single-file offline handoff. Do not deploy that preview instead of dist/.

Current verification: 37 Python tests and 6 JavaScript tests pass; 49 hosted files byte-match the build with required headers and a real custom 404. Connected-browser checks cover desktop/mobile presentation, navigation, search, motion pause and the local model/replay/intervention. The 150/40 browser-check counts in VERIFICATION.md belong to the imported V2 handoff and are not new execution claims.

The site is a public editorial publication, not a connection to Luna. No account, analytics, remote fonts, live resident data, or private code is required by public pages. Contact links open email drafts; they do not send mail.
