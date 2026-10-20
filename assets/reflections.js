/* Intentionally local and ephemeral: no network, storage, analytics or inference. */
(() => {
  'use strict';
  document.querySelectorAll('[data-reflection]').forEach(root => {
    const context = root.querySelector('[data-current-context]');
    const question = root.querySelector('[data-current-question]');
    const label = root.querySelector('[data-label]');
    const baseline = { context: context.textContent, question: question.textContent };
    const buttons = [...root.querySelectorAll('[data-history]')];
    const histories = new Map([...root.querySelectorAll('[data-story]')].map(story => [
      story.dataset.story,
      { context: story.querySelector('[data-context]').textContent,
        question: story.querySelector('[data-question]').textContent }
    ]));
    const reset = root.querySelector('[data-reset]');
    const select = button => {
      const story = button ? histories.get(button.dataset.history) : baseline;
      if (!story) return;
      context.textContent = story.context;
      question.textContent = story.question;
      label.textContent = button ? button.textContent : 'The words alone';
      buttons.forEach(item => item.setAttribute('aria-pressed', String(item === button)));
      root.dataset.active = button ? button.dataset.history : 'none';
      reset.disabled = !button;
    };
    buttons.forEach(button => button.addEventListener('click', () => select(button)));
    reset.addEventListener('click', () => select(null));
    root.querySelector('[data-stories]').hidden = true;
    root.querySelector('[data-choices]').hidden = false;
    reset.hidden = false;
    select(null);
  });
})();
