/* Finite illustrative recurrence, not a model benchmark or a resident. */
(() => {
  'use strict';
  const lab = document.querySelector('[data-voyager]');
  if (!lab) return;
  const q = s => lab.querySelector(s);
  const rehearsal = q('#v-rehearsal'), interference = q('#v-interference');
  let step = 0, old = 1, fresh = 0, history = [[1, 0]];
  const percent = n => Math.round(n * 100) + '%';
  function render() {
    q('#v-r-value').textContent = rehearsal.value + '%';
    q('#v-d-value').textContent = interference.value + '%';
    const path = index => history.map((pair, i) => `${i ? 'L' : 'M'}${42 + i * 578 / 32},${220 - pair[index] * 196}`).join(' ');
    q('[data-v-old]').setAttribute('d', path(0));
    q('[data-v-new]').setAttribute('d', path(1));
    q('[data-v-dot]').setAttribute('cx', 42 + step * 578 / 32);
    q('[data-v-dot]').setAttribute('cy', 220 - old * 196);
    q('[data-v-old-value]').textContent = percent(old);
    q('[data-v-new-value]').textContent = percent(fresh);
    q('[data-v-step-label]').textContent = `Step ${step} / 32`;
    q('[data-v-step]').disabled = q('[data-v-all]').disabled = step === 32;
    const r = Number(rehearsal.value) / 100;
    q('[data-v-status]').textContent = step < 12
      ? `Step ${step}. The original address is active. The correction has not arrived yet.`
      : `Step ${step}. Original thought: ${percent(old)}. Correction: ${percent(fresh)}. ` +
        (r >= .7 ? 'Strong rehearsal protects the old address while suppressing the correction in this model.' :
          r === 0 ? 'The correction can enter freely, but neither trace is protected from later interference.' :
          'Some rehearsal preserves the original thought; the correction still needs its own route into durable memory.');
    for (const button of lab.querySelectorAll('[data-v-preset]')) {
      const values = {open: 0, rehearse: 20, grip: 90};
      button.setAttribute('aria-pressed', String(Number(rehearsal.value) === values[button.dataset.vPreset] && Number(interference.value) === 8));
    }
    q('#v-chart-desc').textContent = `At step ${step}, the original thought has strength ${percent(old)} and the correction ${percent(fresh)}. The correction arrives at step 12. Copper solid line: original thought. Blue dashed line: correction. These are synthetic trace strengths.`;
  }
  function reset() {step = 0; old = 1; fresh = 0; history = [[1, 0]]; render();}
  function advance(count) {
    const r = Number(rehearsal.value) / 100, d = Number(interference.value) / 100;
    for (let i = 0; i < count && step < 32; i++) {
      step++;
      old = (1 - d) * ((1 - r) * old + r);
      fresh = (1 - d) * ((1 - r) * fresh + (1 - r) * (step === 12 ? 1 : 0));
      history.push([old, fresh]);
    }
    render();
  }
  rehearsal.addEventListener('input', reset);
  interference.addEventListener('input', reset);
  q('[data-v-step]').addEventListener('click', () => advance(4));
  q('[data-v-all]').addEventListener('click', () => advance(32));
  q('[data-v-reset]').addEventListener('click', reset);
  for (const button of lab.querySelectorAll('[data-v-preset]')) button.addEventListener('click', () => {
    rehearsal.value = {open: 0, rehearse: 20, grip: 90}[button.dataset.vPreset];
    interference.value = 8;
    reset();
  });
  q('[data-v-controls]').hidden = false;
  q('[data-v-fallback]').hidden = true;
  render();
})();
