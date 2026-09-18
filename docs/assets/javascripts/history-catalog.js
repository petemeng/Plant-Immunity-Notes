(function () {
  function initHistoryCatalog() {
    const tools = document.querySelector('.history-tools');
    const input = document.getElementById('history-filter');
    const status = document.getElementById('history-filter-status');
    if (!tools || !input || !status || input.dataset.ready) return;
    const article = tools.closest('article');
    const rows = Array.from(article.querySelectorAll('table tbody tr'));
    const fold = (value) => value.toLocaleLowerCase().replace(/[\s\-–—_/]+/g, '');
    const update = () => {
      const query = fold(input.value);
      let visible = 0;
      rows.forEach((row) => {
        row.hidden = !fold(row.textContent).includes(query);
        if (!row.hidden) visible += 1;
      });
      status.textContent = visible ? `显示 ${visible} / ${rows.length} 篇` : '没有匹配的专题，请尝试其他名称或研究方向。';
    };
    input.dataset.ready = 'true';
    input.addEventListener('input', update);
    tools.hidden = false;
    update();
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initHistoryCatalog);
  else initHistoryCatalog();
})();
