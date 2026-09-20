/* Inspect published figures at readable magnification, online and offline. */
(() => {
  function initPaperFigures() {
    const figures = document.querySelectorAll('img.paper-figure');
    if (!figures.length || !window.HTMLDialogElement) return;

    const dialog = document.createElement('dialog');
    dialog.className = 'paper-viewer';
    dialog.setAttribute('aria-label', '原文图放大阅读');
    dialog.innerHTML = '<div class="paper-viewer-toolbar"><button type="button" data-action="fit">适合窗口</button><button type="button" data-action="in">＋ 放大</button><button type="button" data-action="out">－ 缩小</button><span class="paper-viewer-scale" aria-live="polite"></span><button type="button" data-action="close" aria-label="关闭原文图">关闭 ×</button></div><p class="paper-viewer-caption"></p><div class="paper-viewer-canvas" tabindex="0" aria-label="原文图，可滚动查看放大后的细节"><img alt=""></div>';
    document.body.append(dialog);
    const canvas = dialog.querySelector('.paper-viewer-canvas');
    const large = canvas.querySelector('img');
    const caption = dialog.querySelector('.paper-viewer-caption');
    const status = dialog.querySelector('.paper-viewer-scale');
    let scale = 1;
    let opener;
    let previousOverflow = '';

    function render() {
      large.style.width = `${Math.round(large.naturalWidth * scale)}px`;
      status.textContent = `${Math.round(scale * 100)}%`;
    }
    function fit() {
      if (!large.naturalWidth) return;
      scale = Math.min(1, (canvas.clientWidth - 24) / large.naturalWidth,
        (canvas.clientHeight - 24) / large.naturalHeight);
      render();
      canvas.scrollTo(0, 0);
    }
    large.addEventListener('load', fit);
    dialog.addEventListener('click', event => {
      const action = event.target.closest('[data-action]')?.dataset.action;
      if (action === 'close') dialog.close();
      if (action === 'fit') fit();
      if (action === 'in') { scale = Math.min(4, scale * 1.5); render(); }
      if (action === 'out') { scale = Math.max(.1, scale / 1.5); render(); }
      if (event.target === dialog) {
        const bounds = dialog.getBoundingClientRect();
        if (event.clientX < bounds.left || event.clientX > bounds.right || event.clientY < bounds.top || event.clientY > bounds.bottom) dialog.close();
      }
    });
    dialog.addEventListener('close', () => {
      document.body.style.overflow = previousOverflow;
      opener?.focus({ preventScroll: true });
    });
    figures.forEach(img => {
      const button = document.createElement('button');
      button.type = 'button';
      button.className = 'paper-figure-open';
      button.setAttribute('aria-label', `放大原文图：${img.alt}`);
      button.title = '点击放大原文图';
      img.before(button);
      button.append(img);
      button.addEventListener('click', () => {
        opener = button;
        caption.textContent = img.alt;
        large.alt = img.alt;
        large.src = img.currentSrc || img.src;
        previousOverflow = document.body.style.overflow;
        document.body.style.overflow = 'hidden';
        dialog.showModal();
        if (large.complete) fit();
      });
    });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initPaperFigures);
  else initPaperFigures();
})();
