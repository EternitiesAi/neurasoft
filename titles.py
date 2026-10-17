"""Browser tab titles use a vertical bar between the page and the site name (dom, 2026-10-17)."""
import re

OLD, NEW = ' — Neurasoft', ' | Neurasoft'
HOME_OLD, HOME_NEW = 'Neurasoft — ', 'Neurasoft | '
TAGS = re.compile(r'(<title>)([^<]*)(</title>)|(<meta property="og:title" content=")([^"]*)(")')


def retitle(text):
    if text.endswith(OLD):
        return text[:-len(OLD)] + NEW
    if text.startswith(HOME_OLD):
        return HOME_NEW + text[len(HOME_OLD):]
    return text


def finish(b):
    for path in b.OUT.rglob('*.html'):
        html = path.read_text(encoding='utf-8')
        new = TAGS.sub(lambda m: (m.group(1) + retitle(m.group(2)) + m.group(3)) if m.group(1) else (m.group(4) + retitle(m.group(5)) + m.group(6)), html)
        if new != html:
            path.write_text(new, encoding='utf-8')
