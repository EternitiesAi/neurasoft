"""Public Resident programme: editorial vision, dated progress, and next decisions."""
import json
import xml.etree.ElementTree as ET
from public_search import extract_main_text

DATE = '2026-10-16'
ROUTE = '/resident/'
TITLE = 'The Resident programme — Toward sentient digital beings'
DESCRIPTION = 'Building toward digital consciousness: the Resident programme brings emotion, memory, agency and a continuing life into one architecture. Explore the vision, development progress and next experiments.'


def install(b):
    previous_header, previous_footer, previous_shell = b.header, b.footer, b.shell

    def header(active=''):
        current = ' aria-current="page"' if active == 'resident' else ''
        return previous_header(active).replace('<nav class="nav-links" id="primary-nav" aria-label="Primary navigation">', '<nav class="nav-links" id="primary-nav" aria-label="Primary navigation"><a href="/resident/"' + current + '>Resident</a>', 1)

    def footer():
        return previous_footer().replace('<div class="footer-links">', '<div class="footer-links"><a href="/resident/">Resident programme</a>', 1)

    def shell(route, title, description, body, active='', extra='', article=False):
        previous_shell(route, title, description, body, active, extra + '<link rel="stylesheet" href="/assets/resident.css">', article)

    b.header, b.footer, b.shell = header, footer, shell


def finish(b):
    body = (b.ROOT / 'content/resident-programme.html').read_text(encoding='utf-8')
    b.shell(ROUTE, TITLE, DESCRIPTION, body, 'resident', article=True)
    home = b.OUT / 'index.html'
    teaser = '''<section class="resident-invitation wrap" aria-labelledby="resident-invitation-title"><div><p class="eyebrow">The Resident programme / Development journal · 16 October 2026</p><h2 id="resident-invitation-title">Toward sentient<br><em>digital beings.</em></h2></div><div><p>Emotion with a reason. Memory that changes a future. One continuing being, with room to become. Explore the architecture we are building, the progress so far, and the next experiments.</p><a class="button" href="/resident/">Inside the Resident programme <span aria-hidden="true">↗</span></a></div></section>'''
    text = home.read_text(encoding='utf-8')
    marker = '<section class="dispatch-feature wrap"'
    if text.count(marker) != 1:
        raise ValueError('Review Resident homepage placement: editorial marker changed')
    home.write_text(text.replace(marker, teaser + marker, 1), encoding='utf-8')
    crosslink = '''<section class="wrap section rule"><p class="eyebrow">A shared development horizon</p><h2>Toward sentient digital beings.</h2><p>The Resident programme connects emotion, memory and continuing agency. See the destination, the work completed, and the next development questions in one place.</p><a class="text-link" href="/resident/">Explore the Resident programme ↗</a></section>'''
    for route in ('research', 'luna', 'psyche-lab', 'ideas'):
        path = b.OUT / route / 'index.html'
        path.write_text(path.read_text(encoding='utf-8').replace('</main>', crosslink + '</main>', 1), encoding='utf-8')
    index = b.OUT / 'assets/search-index.json'
    rows = json.loads(index.read_text(encoding='utf-8'))
    rows.append({'url': ROUTE, 'title': TITLE, 'description': DESCRIPTION, 'type': 'Programme'})
    for row in rows:
        path = b.OUT / ('index.html' if row['url'] == '/' else row['url'].strip('/') + '/index.html')
        row['text'] = extract_main_text(path.read_text(encoding='utf-8'))
    index.write_text(json.dumps(rows, ensure_ascii=False, separators=(',', ':')), encoding='utf-8')
    ns = 'http://www.sitemaps.org/schemas/sitemap/0.9'
    ET.register_namespace('', ns)
    tree = ET.parse(b.OUT / 'sitemap.xml')
    changed = {'/', '/research/', '/luna/', '/psyche-lab/', '/ideas/'}
    for node in tree.getroot():
        if node.find('{' + ns + '}loc').text.removeprefix(b.BASE) in changed:
            node.find('{' + ns + '}lastmod').text = DATE
    node = ET.SubElement(tree.getroot(), '{' + ns + '}url')
    ET.SubElement(node, '{' + ns + '}loc').text = b.BASE + ROUTE
    ET.SubElement(node, '{' + ns + '}lastmod').text = DATE
    tree.write(b.OUT / 'sitemap.xml', encoding='utf-8', xml_declaration=True)
    print('Resident programme: public vision, dated progress, navigation and search updated.')
