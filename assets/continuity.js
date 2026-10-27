/* A local reading interaction: no network, model calls, persistence or tracking. */
(() => {
  'use strict';
  document.querySelectorAll('[data-continuity]').forEach(root => {
    const buttons = [...root.querySelectorAll('[data-continuity-mode]')];
    const remove = root.querySelector('[data-remove-history]');
    const evidence = root.querySelector('[data-new-evidence]');
    const output = root.querySelector('[data-continuity-output]');
    let mode = 'archive';
    const update = () => {
      const index = Number(remove.checked) + 2 * Number(evidence.checked);
      const source = root.querySelector(`[data-continuity-case="${mode}-${index}"]`);
      if (!source) return;
      root.querySelector('[data-state]').textContent = source.querySelector('h4').textContent;
      root.querySelector('[data-current-choice]').textContent = source.querySelector('[data-choice]').textContent;
      root.querySelector('[data-current-reading]').textContent = source.querySelector('[data-reading]').textContent;
      buttons.forEach(b => b.setAttribute('aria-pressed', String(b.dataset.continuityMode === mode)));
    };
    buttons.forEach(b => b.addEventListener('click', () => { mode = b.dataset.continuityMode; update(); }));
    remove.addEventListener('change', update);
    evidence.addEventListener('change', update);
    update();
    root.querySelector('[data-continuity-controls]').hidden = false;
    output.hidden = false;
    root.querySelector('[data-continuity-stories]').hidden = true;
  });
})();
