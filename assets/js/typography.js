/* ABI typography consistency — works in EVERY browser (complements CSS text-wrap).
 * 1. Widow killer: joins the last two words of text blocks with a no-break space
 *    so no line ever ends with a single lonely word.
 * 2. Number glue: keeps figures with their unit ("4 months", "$150 per", "500 hours",
 *    "2 weeks") so a number is never stranded at the end of a line.
 */
(function () {
  'use strict';

  var BLOCK_SELECTOR = [
    'h1', 'h2', 'h3', 'h4', 'h5', 'p', 'li', 'dd', 'dt', 'figcaption', 'blockquote',
    '.feature span', '.hx-chip span', '.hx-sub', '.hx-next-sub',
    '.card p', '.card-meta span', '.step p', '.plan p', '.why-item p',
    '.tuition p', '.amt small', '.glance div', '.eyebrow', '.kicker',
    '.testi-card p', '.acc-body p', '.duo p', '.mhx-seats-t', '.form-consent',
    '.formcard-sub', '.abi-reel__sub', '.abi-reel__points span'
  ].join(',');

  var NBSP = ' ';
  var MIN_WORDS_FOR_WIDOW_FIX = 4;

  function lastTextNode(el) {
    var walker = document.createTreeWalker(el, NodeFilter.SHOW_TEXT, {
      acceptNode: function (n) {
        if (!n.data || !n.data.trim()) return NodeFilter.FILTER_REJECT;
        var p = n.parentElement;
        if (p && /^(SCRIPT|STYLE|SVG)$/i.test(p.tagName)) return NodeFilter.FILTER_REJECT;
        return NodeFilter.FILTER_ACCEPT;
      }
    });
    var node = null, cur;
    while ((cur = walker.nextNode())) node = cur;
    return node;
  }

  function wordCount(el) {
    return (el.textContent.trim().match(/\S+/g) || []).length;
  }

  function fixElement(el) {
    if (el.dataset.typoFixed) return;
    el.dataset.typoFixed = '1';

    // number glue in every text node of the block
    var walker = document.createTreeWalker(el, NodeFilter.SHOW_TEXT);
    var n;
    while ((n = walker.nextNode())) {
      if (!n.data || n.data.indexOf(' ') === -1) continue;
      var glued = n.data.replace(/([$€]?\d[\d,.]*%?) (?=[A-Za-zÀ-ÿ$€\d])/g, '$1' + NBSP);
      if (glued !== n.data) n.data = glued;
    }

    // widow killer — join the final two words
    if (wordCount(el) < MIN_WORDS_FOR_WIDOW_FIX) return;
    var t = lastTextNode(el);
    if (!t) return;
    var data = t.data.replace(/\s+$/, '');
    var i = data.lastIndexOf(' ');
    if (i > 0 && data.length - i < 22) {
      t.data = data.slice(0, i) + NBSP + data.slice(i + 1) + t.data.slice(data.length);
    }
  }

  function run(root) {
    (root || document).querySelectorAll(BLOCK_SELECTOR).forEach(fixElement);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function () { run(); });
  } else {
    run();
  }
})();
