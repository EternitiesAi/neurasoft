"""A finite, deterministic teaching model. No resident or reader data."""

ASSETS = '<link rel="stylesheet" href="/assets/voyager.css"><script src="/assets/voyager.js" defer></script>'

def validate(value):
    if value != {'id': 'holding-and-updating'}:
        raise ValueError('Unknown Voyager lab')

def markdown(value):
    validate(value)
    return [
        '### A thought, and the world outside it', '',
        'Interactive teaching model: use the website to vary rehearsal and interference. An original thought starts at full strength; a correction arrives at step 12. Greater rehearsal explicitly protects the original thought in this toy, while reducing admission of the correction. Neither trace is a probability or a consciousness score.', '',
        'Without JavaScript: imagine repeating an old address while someone gives you a new one. Protecting the old address is not the same as updating where you should go. A useful memory system needs ways to preserve history and revise what it implies.', '',
        'Model details: https://neurasoft.us/assets/articles/project-voyager/research-snapshot.md', ''
    ]

def render(value):
    validate(value)
    return '''<section class="voyager-lab" data-voyager aria-labelledby="voyager-lab-title">
<div class="v-lab-top"><span class="v-kicker">Interactive / 01</span><span class="v-kicker">A model of a tension</span></div>
<h3 id="voyager-lab-title">A thought, and the<br>world outside it.</h3>
<p class="v-intro">You are holding an old address in mind. At step 12, someone tells you it has changed. What survives?</p>
<div class="v-controls" hidden data-v-controls>
<div class="v-sliders"><label for="v-rehearsal">Rehearsal of the old thought <output id="v-r-value" for="v-rehearsal">20%</output><input id="v-rehearsal" type="range" min="0" max="100" value="20" step="5"><span>Let it go <b>Keep repeating it</b></span></label>
<label for="v-interference">Interference from other events <output id="v-d-value" for="v-interference">8%</output><input id="v-interference" type="range" min="0" max="35" value="8" step="1"><span>Quiet <b>Busy</b></span></label></div>
<div class="v-presets" role="group" aria-label="Compare three policies"><button type="button" data-v-preset="open">Open to the world</button><button type="button" data-v-preset="rehearse">Keep rehearsing</button><button type="button" data-v-preset="grip">Hold on tightly</button></div>
<div class="v-chart"><svg viewBox="0 0 640 270" role="img" aria-labelledby="v-chart-title v-chart-desc"><title id="v-chart-title">Original thought and correction across 32 steps</title><desc id="v-chart-desc">Normalized strengths in an illustrative model. The copper solid line is the original thought. The pale blue dashed line is the correction arriving at step 12.</desc><g class="v-grid"><path d="M42 24H620 M42 122H620 M42 220H620"/><path d="M42 24V220H620"/></g><g class="v-axis"><text x="0" y="28">1.0</text><text x="0" y="126">0.5</text><text x="0" y="224">0.0</text><text x="42" y="250">0</text><text x="250" y="250">12</text><text x="590" y="250">32</text></g><path d="M258.75 24V220" class="v-arrival"/><text x="270" y="42" class="v-axis">Correction arrives</text><path data-v-old class="v-old" d="M42 24"/><path data-v-new class="v-new" d="M42 220"/><circle data-v-dot cx="42" cy="24" r="4" fill="#e7aa78"/></svg></div>
<div class="v-legend"><span><i class="v-line-old"></i>Original thought <strong data-v-old-value>100%</strong></span><span><i class="v-line-new"></i>Correction <strong data-v-new-value>0%</strong></span></div>
<div class="v-actions"><button type="button" data-v-step>Advance 4 steps ↗</button><button type="button" data-v-all>See all 32 steps</button><button type="button" data-v-reset>Reset</button><span data-v-step-label>Step 0 / 32</span></div>
<p class="v-status" role="status" aria-live="polite" data-v-status>The original address is active. The correction has not arrived yet.</p>
</div>
<div data-v-fallback><p>Imagine repeating an old address while someone gives you a new one. Protecting the old address is not the same as updating where you should go. A useful memory system needs ways to preserve history and revise what it implies.</p><p>Enable JavaScript to explore the two traces. The full explanation remains readable here.</p></div>
<details class="v-method"><summary>What this experiment does—and what the lines mean</summary><p>This is a deterministic teaching model, not a fitted model of a person, RWKV, or Luna. Each click advances discrete steps, not seconds. Rehearsal explicitly favors the original thought; at step 12, a single correction competes for admission. More rehearsal protects the old trace but reduces the correction’s initial strength and subsequent retention.</p><p>Both lines are normalized trace strengths, not probabilities, truth judgments, or a consciousness score. Changing a control resets the run. No text entry, recording, live model, or resident connection is involved.</p><p><a href="/assets/articles/project-voyager/research-snapshot.md">Read the equations and research snapshot ↗</a></p></details>
<div class="v-takeaway">A continuing mind must be able to keep something.<br>It must also be able to change it.</div>
</section>'''
