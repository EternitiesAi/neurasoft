"""Founder-approved public naming; route and source identifiers stay unchanged."""
import json
import re
from public_search import extract_main_text

NAME = 'L.U.N.A'
EXPANSION = 'Lifeform of Unified Noetic Agency'


def public_name(text):
    return re.sub(r'\b(?:Luna|LUNA)\b', NAME, text)


def finish(build):
    for path in build.OUT.rglob('*.html'):
        text = public_name(path.read_text(encoding='utf-8'))
        if path == build.OUT / 'luna/index.html':
            text = text.replace('</h1>', '</h1><p class="copy">' + EXPANSION + '</p>', 1)
        path.write_text(text, encoding='utf-8')
    for path in build.OUT.rglob('*.json'):
        def relabel(value):
            if isinstance(value, str):
                return public_name(value)
            if isinstance(value, list):
                return [relabel(v) for v in value]
            if isinstance(value, dict):
                return {k: relabel(v) for k, v in value.items()}
            return value
        data = relabel(json.loads(path.read_text(encoding='utf-8')))
        if path.name == 'search-index.json':
            for row in data:
                page = build.OUT / ('index.html' if row['url'] == '/' else row['url'].strip('/') + '/index.html')
                row['text'] = extract_main_text(page.read_text(encoding='utf-8'))
        path.write_text(json.dumps(data, ensure_ascii=False), encoding='utf-8')
    print('Public name: L.U.N.A — ' + EXPANSION)
