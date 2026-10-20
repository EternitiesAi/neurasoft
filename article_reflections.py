"""Local, optional editorial reflections with a complete non-JavaScript reading path."""
from html import escape as E
import re

ASSETS = '<link rel="stylesheet" href="/assets/reflections.css"><script src="/assets/reflections.js" defer></script>'


def validate(r):
    if r.get('id') != 'same-message':
        raise ValueError('Unknown article reflection')
    for key in ('message', 'baseline', 'question'):
        if not isinstance(r.get(key), str) or not r[key].strip():
            raise ValueError('Empty reflection text')
    options = r.get('options', [])
    if len(options) != 3:
        raise ValueError('The message reflection requires three histories')
    ids = set()
    for option in options:
        key = option.get('id', '')
        if not re.fullmatch(r'[a-z][a-z0-9-]*', key) or key in ids:
            raise ValueError('Invalid or duplicate reflection choice')
        ids.add(key)
        if any(not isinstance(option.get(k), str) or not option[k].strip()
               for k in ('label', 'context', 'question')):
            raise ValueError('Empty reflection choice')


def render(r):
    validate(r)
    buttons = ''.join(f'<button type="button" data-history="{E(o["id"])}" aria-pressed="false" aria-controls="reflection-reading">{E(o["label"])}</button>' for o in r['options'])
    stories = ''.join(f'<details data-story="{E(o["id"])}"><summary>{E(o["label"])}</summary><p data-context>{E(o["context"])}</p><p data-question>{E(o["question"])}</p></details>' for o in r['options'])
    return f'''<aside class="reflection" aria-label="Read the same message through different histories" data-reflection>
<p class="reflection-kicker">A moment to try / 01</p>
<p class="reflection-message">“{E(r['message'])}”</p>
<p class="reflection-instruction">Keep the words. Change the history.</p>
<div class="reflection-choices" role="group" aria-label="Choose an imagined history" data-choices hidden>{buttons}</div>
<div id="reflection-reading" class="reflection-reading" aria-live="polite" aria-atomic="true">
<p class="reflection-history" data-label>The words alone</p><p data-current-context>{E(r['baseline'])}</p><p class="reflection-question" data-current-question>{E(r['question'])}</p>
</div>
<button class="reflection-reset" type="button" data-reset hidden>Return to the words alone</button>
<div data-stories>{stories}</div>
<p class="reflection-note">A guided reflection, with no right answer. Your choices are not saved or sent. You can also simply continue reading.</p>
</aside>'''


def markdown(r):
    validate(r)
    lines = ['### A moment to try', '', '“' + r['message'] + '”', '', r['baseline'], '', r['question'], '']
    for o in r['options']:
        lines += ['**' + o['label'] + '**', '', o['context'], '', o['question'], '']
    return lines + ['A guided reflection, with no right answer. Try each imagined history, then return to the words alone.', '']
