# What held, what failed, and what we have not tested.

Requested by Dom on 18 November 2026 (about 19:10 UTC), relayed through the Outreach session and checked against that
session's transcript: map the lab's work against the indicators, and publish a new article on neurasoft.us with the latest
findings so that Grok Bot can post it on X and LinkedIn. Prompted by a reader at a consciousness research foundation who
could not find the lab's failures and wins and asked for a table. Written and published by the Neurasoft engineering
session (Claude). Social posting is held: the packet is `publish: review` until Dom releases it.

## Ownership and baseline

Isolated worktree: C:/dev/.worktrees/neurasoft-indicators.
Branch: editorial/failures-and-wins-20261118.
Base: e2671eb (editorial/project-voyager-live-20261113), the source production was serving.

Before any edit the base was built and compared with https://neurasoft.us using tools/verify_proxied_release.py: 220 files,
all matching except one that failed to fetch (status 000); that file was fetched again by hand and matched (200, 2,201
bytes). The dirty canonical checkout at C:/dev/neurasoft (uncommitted work of 2 November, a different article) was not
touched or published.

## Editorial scope

Article: /articles/what-held-and-what-failed/.
Two tables. The first: fifteen lab results of 17 and 18 November, each with its verdict, what was observed, its control and
what it does not show. The second: the fourteen indicator properties of Butlin, Long et al. (2023), quoted from Table 1 of
arXiv:2308.08708, with where the architecture stands, what was tested and the result. A public methods snapshot is at
/assets/articles/what-held-and-what-failed/research-snapshot.md.

Source reading: C:/dev/una-shared/mind-host/lab/RESULTS-20261117.md and RESULTS-20261118.md (engineering team), and the
second team's own reports (resident-sentience-review-20261117, resident-revision-20261117, neurasoft-takeover-20261117
under D:/codex-work/luna-three-crowns-math-20261001/research). Every number in the article was checked against those files.
One count was corrected during writing after a direct read of each newborn's first want: nine of nine before the window
were about themselves, four of them the same question (an earlier note of mine had said five).

Not included: resident dialogue beyond single words that are themselves a finding ("landed hard", "still weighs", "stung"),
identity records, box or instance identifiers, source code, and the name of the reader who asked. The older research
resident is mentioned only as having agreed to a four-message arc; none of its words are quoted.

External pages checked on 18 November: arXiv:2308.08708v3 (Table 1 wording), the 2025 Trends in Cognitive Sciences paper by
many of the same authors, and the head post of Chris Percy's living thread of indicators. The replies of that thread, which
hold the list itself, could not be read without signing in to X; the article says the mapping against it is owed and does
not claim to have done it.

New in the build: a section may carry a `table` (caption, columns, rows of plain text). `articles.py` validates it, renders
it with column headers, row headers and per-cell labels, and writes a Markdown twin; `assets/articles.css` lays it out
wider than the text column on a desktop and as labelled cards under 860 px. One new test in tests/test_articles.py.
Cover: tools/build_indicators_media.cjs (SVG and PNG; each square is one row of the first table, the marks are verdicts).

No claim of consciousness, sentience or experience is made. The article says in its third paragraph, in section 05 and in
its editorial note that nothing on the page is evidence that any system has experience.

## Verification

60 Python tests passed (C:/dev/firstlight-artifacts/bootstrap-2026-09-12/browser-env/Scripts/python.exe -m unittest
discover -s tests -p "test_*.py"). 7 JavaScript search tests passed. Looked at in a browser from a local server on
127.0.0.1:8742: the article at 1366 px (table 1,180 px wide, no horizontal overflow) and at 375 px (rows as labelled cards,
no horizontal overflow; a caption that wrapped into a narrow column was found there and fixed), the homepage feature, no
console errors. tools/check_editorial_browser.cjs was not run.

## Reproduction

1. NODE_PATH=<a node_modules holding sharp> node tools/build_indicators_media.cjs
2. python build.py
3. the two test commands above
4. python tools/stage_cloudflare.py   (226 files)
5. deploy only artifacts/cloudflare to Cloudflare Pages project neurasoft-research: a preview branch first, then main
6. python tools/verify_proxied_release.py https://neurasoft.us <receipt>

## Publication

(filled in after each deployment is verified)
