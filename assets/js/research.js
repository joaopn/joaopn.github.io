// Research page: area chips filter the publication list (combinable); area cards are shortcuts
// that select their chips; a paper's area tag selects its chip. Only a card click opens the box
// above the list (the card's intro plus its areas' text from _areas/); chips and tags only filter.
// Without JS the full list shows.
(function () {
  var $ = function (s, r) { return [].slice.call((r || document).querySelectorAll(s)); };
  var cards = $('.ac[data-f]'), chips = $('#pf button'), pl = document.getElementById('pl');
  var fs = document.getElementById('fs'), ab = document.getElementById('ab');
  var abc = document.getElementById('abc'), abt = document.getElementById('abt');
  if (!pl) return;
  var order = chips.map(function (c) { return c.dataset.f; }).filter(function (f) { return f !== 'all' && f !== 'th'; });
  var sel = [], box = null; // box: the card whose text is open, set only by a card click
  function same(a, b) { return a.length === b.length && a.every(function (x) { return b.indexOf(x) >= 0; }); }
  function tpl(k) { var t = document.querySelector('template[data-t="' + k + '"]'); return t ? t.innerHTML : ''; }
  function apply() {
    chips.forEach(function (c) {
      var f = c.dataset.f, on = f === 'all' ? !sel.length : sel.indexOf(f) >= 0;
      c.classList.toggle('on', on); c.setAttribute('aria-pressed', String(on));
    });
    var card = cards.filter(function (c) { return same(c.dataset.f.split(' '), sel); })[0] || null;
    cards.forEach(function (c) { c.classList.toggle('on', c === card); c.setAttribute('aria-pressed', String(c === card)); });
    var lastYr = null, shown = 0, n = 0, total = 0;
    $('#pl > *').forEach(function (k) {
      if (k.hasAttribute('data-y')) { if (lastYr) lastYr.hidden = !shown; lastYr = k; shown = 0; return; }
      total++;
      var ok = !sel.length || sel.indexOf(k.dataset.a) >= 0 || (sel.indexOf('th') >= 0 && k.hasAttribute('data-th'));
      k.hidden = !ok; if (ok) { shown++; n++; }
    });
    if (lastYr) lastYr.hidden = !shown;
    if (box) {
      var bf = box.dataset.f.split(' ');
      abc.innerHTML = tpl('intro-' + box.id) + order.filter(function (k) { return bf.indexOf(k) >= 0; }).map(tpl).join('');
      abt.textContent = box.querySelector('b').textContent;
      ab.hidden = false;
    } else ab.hidden = true;
    fs.innerHTML = sel.length ? 'Showing ' + n + ' of ' + total + ' · <a href="#publications" id="fclr">show all</a>' : '';
    var clr = document.getElementById('fclr');
    if (clr) clr.onclick = function (e) { e.preventDefault(); sel = []; box = null; apply(); };
  }
  chips.forEach(function (c) {
    c.addEventListener('click', function () {
      var f = c.dataset.f;
      if (f === 'all') sel = [];
      else { var i = sel.indexOf(f); if (i >= 0) sel.splice(i, 1); else sel.push(f); }
      box = null; apply();
    });
  });
  cards.forEach(function (c) {
    c.addEventListener('click', function () {
      var open = box === c;
      sel = open ? [] : c.dataset.f.split(' '); box = open ? null : c;
      apply();
    });
  });
  $('.tg[data-area]', pl).forEach(function (t) {
    t.addEventListener('click', function () {
      sel = [t.dataset.area]; box = null; apply();
      document.getElementById('pf').scrollIntoView({ block: 'nearest', behavior: 'smooth' });
    });
  });
  document.getElementById('abx').addEventListener('click', function () { sel = []; box = null; apply(); });
  // /research/#<card-id> (old area-page URLs redirect here) preselects that card
  var h = location.hash.slice(1), pre = h && document.getElementById(h);
  if (pre && cards.indexOf(pre) >= 0) { sel = pre.dataset.f.split(' '); box = pre; }
  apply();
})();
