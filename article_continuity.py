"""Hand-authored counterfactual desk; no resident or reader data is used."""
from html import escape as E

ASSETS = '<link rel="stylesheet" href="/assets/continuity.css"><script src="/assets/continuity.js" defer></script>'

CASES = [
    ('archive', 'Keep a record', [
        ('With history', 'It recalls missing a deadline, then accepts the unfamiliar project without checking what it requires.', 'The record is available, but this example gives it no influence over the decision.'),
        ('Without history', 'It cannot recall the missed deadline. It still accepts the unfamiliar project without checking.', 'Removing the record changes what it can recount. The choice stays the same.'),
        ('With new evidence', 'A verified new tool makes the unfamiliar work manageable. It accepts, as it did before.', 'The same answer can be appropriate by coincidence. We need comparisons to distinguish that from adaptation.'),
        ('Without history, with new evidence', 'It has no record of the missed deadline. It accepts the project after the new tool is supplied, just as it accepted before.', 'Neither manipulation changes this scripted decision. This example demonstrates storage, not useful history dependence.')]),
    ('learning', 'Change a choice', [
        ('With history', 'Remembering the missed deadline, it declines the unfamiliar project immediately.', 'History changes its choice. Whether it learned the right lesson is another question.'),
        ('Without history', 'Without the relevant experience, it accepts the unfamiliar project immediately.', 'The different choice exposes a functional dependence on history in this example.'),
        ('With new evidence', 'A verified new tool makes the work manageable. It declines anyway: this kind of project went badly before.', 'A persistent lesson can become a rigid habit. Stability alone is not good judgment.'),
        ('Without history, with new evidence', 'With no old lesson to apply, it accepts the now-manageable project.', 'A better answer in this one case does not make forgetting a generally better policy.')]),
    ('revision', 'Revise a choice', [
        ('With history', 'It recalls what went wrong, checks the new requirements, and asks for a smaller first milestone before committing.', 'The experience changes the process by which it decides, while leaving room for the present situation.'),
        ('Without history', 'With no relevant history available, it makes the ordinary initial commitment without the extra milestone.', 'The additional check depended on experience in this hand-authored example.'),
        ('With new evidence', 'It verifies that the new tool addresses the old failure, then accepts with an updated estimate. The old event remains in its record.', 'Revision preserves the history while changing what the history implies.'),
        ('Without history, with new evidence', 'It verifies the available tool and accepts the project, but cannot connect that check to the earlier failure.', 'Current evidence can support a useful choice even when autobiographical continuity is absent.')])
]

def validate(value):
    if value != {'id': 'history-and-revision'}:
        raise ValueError('Unknown continuity thought experiment')

def render(value):
    validate(value)
    buttons = ''.join(f'<button type="button" data-continuity-mode="{key}" aria-pressed="{str(i == 0).lower()}" aria-controls="continuity-output">{E(label)}</button>' for i, (key,label,_) in enumerate(CASES))
    stories = ''.join('<details><summary>'+E(label)+'</summary>'+''.join(f'<section data-continuity-case="{key}-{i}"><h4>{E(title)}</h4><p data-choice>{E(choice)}</p><p data-reading>{E(reading)}</p></section>' for i,(title,choice,reading) in enumerate(rows))+'</details>' for key,label,rows in CASES)
    return f'''<aside class="continuity-desk" data-continuity aria-label="Explore what memory changes">
<h3>What does yesterday change?</h3>
<p class="continuity-scene">A resident once missed a deadline after accepting work it did not understand. An unfamiliar project arrives.</p>
<p>Explore three imagined designs. Then remove the relevant history or introduce evidence that the situation has changed.</p>
<div class="continuity-controls" data-continuity-controls hidden><div class="continuity-modes" role="group" aria-label="Choose an imagined design">{buttons}</div>
<label><input type="checkbox" data-remove-history> Remove the relevant history</label>
<label><input type="checkbox" data-new-evidence> Supply a verified new tool</label></div>
<div id="continuity-output" class="continuity-output" data-continuity-output aria-live="polite" aria-atomic="true" hidden><p class="continuity-state" data-state></p><p class="continuity-choice" data-current-choice></p><p data-current-reading></p></div>
<div data-continuity-stories>{stories}</div>
<p class="continuity-note">Hand-authored thought experiment. These outcomes illustrate distinctions; they are not model outputs or measured results. Nothing is saved or sent.</p></aside>'''

def markdown(value):
    validate(value)
    out=['### Try the counterfactual desk','', 'A resident once missed a deadline after accepting work it did not understand. An unfamiliar project arrives.','']
    for _,label,rows in CASES:
        out += ['**'+label+'**','']
        for title,choice,reading in rows:
            out += [title+': '+choice+' '+reading,'']
    return out+['Hand-authored thought experiment; not model outputs or measured results.','']
