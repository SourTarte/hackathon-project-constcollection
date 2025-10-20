(function () {
  'use strict';
  document.addEventListener('DOMContentLoaded', function () {
    try {
      const params = new URLSearchParams(window.location.search);
      let tabId = null;

      if (params.has('edit_category')) tabId = 'category-tab';
      else if (params.has('edit_media')) tabId = 'media-tab';
      else if (params.has('edit')) tabId = 'about-tab';
      else {
        const hash = (window.location.hash || '').replace('#', '');
        if (hash) tabId = hash;
      }

      if (tabId && window.bootstrap && bootstrap.Tab) {
        const el = document.getElementById(tabId);
        if (el) {
          new bootstrap.Tab(el).show();

          // optional: focus first input inside the shown pane for keyboard users
          const paneSelector = el.getAttribute('data-bs-target') || ('#' + tabId.replace('-tab', '-pane'));
          const pane = document.querySelector(paneSelector);
          if (pane) {
            const firstField = pane.querySelector('input, textarea, select, button');
            if (firstField) firstField.focus();
          }
        }
      }
    } catch (err) {
      // fail silently in older browsers or when bootstrap isn't present yet
      console.error(err);
    }
  });
})();