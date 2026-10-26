/* DiyaQR web generator. Everything runs in the browser: nothing is uploaded, saved codes live in localStorage. */
(function () {
  'use strict';

  var root = document.getElementById('gen');
  if (!root) return;

  var TYPES = {
    url: { label: 'Website', fields: [{ k: 'url', l: 'Link', p: 'https://example.com', t: 'url' }] },
    text: { label: 'Text', fields: [{ k: 'text', l: 'Text', p: 'Write anything', t: 'textarea' }] },
    wifi: {
      label: 'Wi-Fi',
      fields: [
        { k: 'ssid', l: 'Network name (SSID)', p: 'MyHomeWifi' },
        { k: 'password', l: 'Password', p: 'Password', t: 'text' },
        { k: 'security', l: 'Security', t: 'select', o: [['WPA', 'WPA / WPA2 / WPA3'], ['WEP', 'WEP'], ['nopass', 'No password']] },
        { k: 'hidden', l: 'Hidden network', t: 'checkbox' },
      ],
    },
    whatsapp: {
      label: 'WhatsApp',
      fields: [
        { k: 'phone', l: 'Phone number with country code', p: '923001234567', t: 'tel' },
        { k: 'message', l: 'Message (optional)', p: 'Hello!', t: 'textarea' },
      ],
    },
    vcard: {
      label: 'Contact',
      fields: [
        { k: 'first', l: 'First name' },
        { k: 'last', l: 'Last name' },
        { k: 'phone', l: 'Phone', t: 'tel' },
        { k: 'email', l: 'Email', t: 'email' },
        { k: 'org', l: 'Company' },
        { k: 'title', l: 'Job title' },
        { k: 'web', l: 'Website', t: 'url' },
        { k: 'address', l: 'Address' },
      ],
    },
    email: {
      label: 'Email',
      fields: [
        { k: 'to', l: 'To', p: 'name@example.com', t: 'email' },
        { k: 'subject', l: 'Subject' },
        { k: 'body', l: 'Message', t: 'textarea' },
      ],
    },
    sms: {
      label: 'SMS',
      fields: [
        { k: 'phone', l: 'Phone number', t: 'tel' },
        { k: 'message', l: 'Message', t: 'textarea' },
      ],
    },
    phone: { label: 'Phone', fields: [{ k: 'phone', l: 'Phone number', p: '+923001234567', t: 'tel' }] },
    location: {
      label: 'Location',
      fields: [
        { k: 'lat', l: 'Latitude', p: '24.7136' },
        { k: 'lng', l: 'Longitude', p: '46.6753' },
      ],
      locate: true,
    },
    event: {
      label: 'Event',
      fields: [
        { k: 'title', l: 'Title' },
        { k: 'start', l: 'Starts', t: 'datetime-local' },
        { k: 'end', l: 'Ends', t: 'datetime-local' },
        { k: 'place', l: 'Place' },
        { k: 'notes', l: 'Notes', t: 'textarea' },
      ],
    },
  };

  var STYLES = [
    ['Classic', '#000000', '#ffffff', ''],
    ['Teal', '#0b6b60', '#ffffff', ''],
    ['Ocean', '#0b3d91', '#ffffff', '#17a2d8'],
    ['Sunset', '#d6336c', '#fff8f0', '#f59f00'],
    ['Forest', '#1b5e20', '#f4fbf4', '#66bb6a'],
    ['Night', '#ffffff', '#101820', ''],
    ['Purple', '#5f3dc4', '#ffffff', '#cc5de8'],
  ];

  var $ = function (id) { return document.getElementById(id); };
  var state = { type: root.getAttribute('data-type') || 'url', values: {}, logo: '' };
  var qr = null;
  var FIELD_KEY = 'diyaqr.web.values';
  var SAVED_KEY = 'diyaqr.web.saved';

  // ---------- storage (never throws) ----------
  function load(key, fallback) {
    try { var v = JSON.parse(localStorage.getItem(key)); return v == null ? fallback : v; } catch (e) { return fallback; }
  }
  function store(key, value) {
    try { localStorage.setItem(key, JSON.stringify(value)); return true; } catch (e) { return false; }
  }

  // ---------- payload builders ----------
  function esc(s) { return String(s).replace(/([\\;,:"])/g, '\\$1'); }
  function vEsc(s) { return String(s).replace(/\\/g, '\\\\').replace(/\n/g, '\\n').replace(/([;,])/g, '\\$1'); }
  function icsDate(v) { return v ? v.replace(/[-:]/g, '').slice(0, 15) : ''; }

  function payload(type, v) {
    v = v || {};
    switch (type) {
      case 'url': return (v.url || '').trim();
      case 'text': return v.text || '';
      case 'phone': return v.phone ? 'tel:' + v.phone.replace(/\s+/g, '') : '';
      case 'sms': return v.phone ? 'SMSTO:' + v.phone.replace(/\s+/g, '') + ':' + (v.message || '') : '';
      case 'whatsapp':
        if (!v.phone) return '';
        return 'https://wa.me/' + v.phone.replace(/\D+/g, '') + (v.message ? '?text=' + encodeURIComponent(v.message) : '');
      case 'email':
        if (!v.to) return '';
        var q = [];
        if (v.subject) q.push('subject=' + encodeURIComponent(v.subject));
        if (v.body) q.push('body=' + encodeURIComponent(v.body));
        return 'mailto:' + v.to.trim() + (q.length ? '?' + q.join('&') : '');
      case 'wifi':
        if (!v.ssid) return '';
        var sec = v.security || 'WPA';
        return 'WIFI:T:' + sec + ';S:' + esc(v.ssid) + ';' + (sec === 'nopass' ? '' : 'P:' + esc(v.password || '') + ';') + (v.hidden ? 'H:true;' : '') + ';';
      case 'vcard':
        if (!v.first && !v.last && !v.phone && !v.email) return '';
        return ['BEGIN:VCARD', 'VERSION:3.0',
          'N:' + vEsc(v.last || '') + ';' + vEsc(v.first || '') + ';;;',
          'FN:' + vEsc(((v.first || '') + ' ' + (v.last || '')).trim()),
          v.org ? 'ORG:' + vEsc(v.org) : '', v.title ? 'TITLE:' + vEsc(v.title) : '',
          v.phone ? 'TEL:' + v.phone : '', v.email ? 'EMAIL:' + v.email : '',
          v.web ? 'URL:' + v.web : '', v.address ? 'ADR:;;' + vEsc(v.address) + ';;;;' : '',
          'END:VCARD'].filter(Boolean).join('\n');
      case 'location':
        return v.lat && v.lng ? 'geo:' + v.lat.trim() + ',' + v.lng.trim() : '';
      case 'event':
        if (!v.title || !v.start) return '';
        return ['BEGIN:VCALENDAR', 'VERSION:2.0', 'BEGIN:VEVENT', 'SUMMARY:' + vEsc(v.title),
          'DTSTART:' + icsDate(v.start), 'DTEND:' + icsDate(v.end || v.start),
          v.place ? 'LOCATION:' + vEsc(v.place) : '', v.notes ? 'DESCRIPTION:' + vEsc(v.notes) : '',
          'END:VEVENT', 'END:VCALENDAR'].filter(Boolean).join('\n');
    }
    return '';
  }

  // ---------- form ----------
  function buildForm() {
    var def = TYPES[state.type];
    var box = $('fields');
    box.innerHTML = '';
    def.fields.forEach(function (f) {
      var wrap = document.createElement('label');
      wrap.className = 'f' + (f.t === 'checkbox' ? ' check' : '');
      var name = document.createElement('span');
      name.textContent = f.l;
      var input;
      if (f.t === 'textarea') { input = document.createElement('textarea'); input.rows = 3; }
      else if (f.t === 'select') {
        input = document.createElement('select');
        f.o.forEach(function (o) { var op = document.createElement('option'); op.value = o[0]; op.textContent = o[1]; input.appendChild(op); });
      } else { input = document.createElement('input'); input.type = f.t || 'text'; }
      if (f.p) input.placeholder = f.p;
      input.id = 'f-' + f.k;
      var current = state.values[state.type] && state.values[state.type][f.k];
      if (f.t === 'checkbox') input.checked = !!current; else if (current != null) input.value = current;
      input.addEventListener('input', onField);
      input.addEventListener('change', onField);
      if (f.t === 'checkbox') { wrap.appendChild(input); wrap.appendChild(name); } else { wrap.appendChild(name); wrap.appendChild(input); }
      box.appendChild(wrap);
    });
    if (def.locate && navigator.geolocation) {
      var b = document.createElement('button');
      b.type = 'button'; b.className = 'btn soft'; b.textContent = 'Use my current location';
      b.addEventListener('click', function () {
        navigator.geolocation.getCurrentPosition(function (p) {
          $('f-lat').value = p.coords.latitude.toFixed(6);
          $('f-lng').value = p.coords.longitude.toFixed(6);
          onField();
        }, function () { toast('Location is not available'); });
      });
      box.appendChild(b);
    }
    var tabs = document.querySelectorAll('#types button');
    for (var i = 0; i < tabs.length; i++) tabs[i].setAttribute('aria-pressed', String(tabs[i].getAttribute('data-type') === state.type));
  }

  function readValues() {
    var out = {};
    TYPES[state.type].fields.forEach(function (f) {
      var el = $('f-' + f.k);
      if (el) out[f.k] = f.t === 'checkbox' ? el.checked : el.value;
    });
    return out;
  }

  function onField() {
    state.values[state.type] = readValues();
    store(FIELD_KEY, state.values);
    render();
  }

  // ---------- style options ----------
  function options() {
    var data = payload(state.type, state.values[state.type]);
    var gradient = $('gradient').checked;
    var dot1 = $('dotColor').value, dot2 = $('dotColor2').value;
    var grad = gradient ? { type: $('gradType').value, rotation: 45 * Math.PI / 180, colorStops: [{ offset: 0, color: dot1 }, { offset: 1, color: dot2 }] } : undefined;
    var size = parseInt($('size').value, 10) || 320;
    var o = {
      width: size, height: size, type: 'canvas',
      data: data || 'https://play.google.com/store/apps/details?id=io.zia.diyaqr',
      margin: parseInt($('margin').value, 10) || 0,
      qrOptions: { errorCorrectionLevel: $('ec').value },
      dotsOptions: { type: $('dotType').value, color: dot1, gradient: grad },
      cornersSquareOptions: { type: $('cornerType').value, color: dot1, gradient: grad },
      cornersDotOptions: { type: $('cornerDotType').value, color: dot1, gradient: grad },
      backgroundOptions: { color: $('bgColor').value },
      imageOptions: { crossOrigin: 'anonymous', margin: 4, imageSize: parseFloat($('logoSize').value) || 0.3, hideBackgroundDots: true },
    };
    if (state.logo) o.image = state.logo;
    return { opts: o, empty: !data };
  }

  function lum(hex) {
    var n = parseInt(hex.slice(1), 16), c = [n >> 16, (n >> 8) & 255, n & 255].map(function (v) {
      v /= 255; return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4);
    });
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2];
  }

  function warn() {
    var a = lum($('dotColor').value), b = lum($('bgColor').value);
    var ratio = (Math.max(a, b) + 0.05) / (Math.min(a, b) + 0.05);
    var msgs = [];
    if (ratio < 3) msgs.push('Low contrast: scanners may struggle. Use darker dots on a lighter background.');
    if ($('gradient').checked && lum($('dotColor2').value) > 0.6 && b > 0.6) msgs.push('The light end of the gradient may be hard to scan on a light background.');
    if (state.logo && $('ec').value === 'L') msgs.push('With a logo, use error correction Q or H.');
    var el = $('warn');
    el.textContent = msgs.join(' ');
    el.hidden = !msgs.length;
  }

  function render() {
    if (typeof QRCodeStyling === 'undefined') return;
    var r = options();
    $('empty').hidden = !r.empty;
    $('actions').classList.toggle('dim', r.empty);
    if (!qr) { qr = new QRCodeStyling(r.opts); qr.append($('preview')); } else qr.update(r.opts);
    var c = $('preview').firstChild;
    if (c && c.style) { c.style.maxWidth = '100%'; c.style.height = 'auto'; }
    warn();
  }

  // ---------- actions ----------
  function fileName() {
    var base = (state.type + '-qr').toLowerCase();
    return base;
  }
  function download(ext) {
    if (!qr || options().empty) { toast('Fill in the form first'); return; }
    qr.download({ name: fileName(), extension: ext });
  }
  function toast(msg) {
    var t = $('toast');
    t.textContent = msg; t.classList.add('show');
    clearTimeout(toast.h);
    toast.h = setTimeout(function () { t.classList.remove('show'); }, 2200);
  }
  function copyImage() {
    if (!qr || options().empty) { toast('Fill in the form first'); return; }
    if (!navigator.clipboard || !window.ClipboardItem) { toast('Copy is not supported in this browser'); return; }
    qr.getRawData('png').then(function (blob) {
      return navigator.clipboard.write([new ClipboardItem({ 'image/png': blob })]);
    }).then(function () { toast('Image copied'); }, function () { toast('Copy failed'); });
  }

  function getSettings() {
    var ids = ['dotColor', 'dotColor2', 'bgColor', 'dotType', 'cornerType', 'cornerDotType', 'ec', 'size', 'margin', 'gradType', 'logoSize'];
    var s = { gradient: $('gradient').checked };
    ids.forEach(function (id) { s[id] = $(id).value; });
    return s;
  }
  function applySettings(s) {
    Object.keys(s).forEach(function (k) {
      var el = $(k);
      if (!el) return;
      if (el.type === 'checkbox') el.checked = !!s[k]; else el.value = s[k];
    });
    syncGradientUi();
  }

  function thumb(cb) {
    qr.getRawData('png').then(function (blob) {
      var fr = new FileReader();
      fr.onload = function () {
        var img = new Image();
        img.onload = function () {
          var c = document.createElement('canvas'); c.width = c.height = 96;
          c.getContext('2d').drawImage(img, 0, 0, 96, 96);
          cb(c.toDataURL('image/png'));
        };
        img.src = fr.result;
      };
      fr.readAsDataURL(blob);
    });
  }

  function saveCode() {
    if (!qr || options().empty) { toast('Fill in the form first'); return; }
    var name = ($('saveName').value || '').trim() || TYPES[state.type].label + ' QR';
    thumb(function (img) {
      var list = load(SAVED_KEY, []);
      list.unshift({ id: String(Date.now()), name: name, type: state.type, values: state.values[state.type] || {}, settings: getSettings(), logo: state.logo, thumb: img, at: new Date().toISOString() });
      if (!store(SAVED_KEY, list)) { list.shift(); toast('Storage is full. Delete some saved codes or remove the logo.'); return; }
      $('saveName').value = '';
      toast('Saved in this browser');
      renderSaved();
    });
  }

  function renderSaved() {
    var list = load(SAVED_KEY, []);
    var box = $('saved');
    box.innerHTML = '';
    $('savedEmpty').hidden = !!list.length;
    list.forEach(function (item) {
      var card = document.createElement('div');
      card.className = 'sv';
      var img = document.createElement('img');
      img.src = item.thumb; img.alt = ''; img.width = 72; img.height = 72;
      var info = document.createElement('div');
      info.className = 'sv-i';
      var n = document.createElement('strong'); n.textContent = item.name;
      var m = document.createElement('small'); m.textContent = (TYPES[item.type] ? TYPES[item.type].label : item.type) + ' · ' + new Date(item.at).toLocaleDateString();
      info.appendChild(n); info.appendChild(m);
      var openB = document.createElement('button'); openB.type = 'button'; openB.className = 'btn soft sm'; openB.textContent = 'Edit';
      openB.addEventListener('click', function () {
        state.type = TYPES[item.type] ? item.type : 'url';
        state.values[state.type] = item.values;
        state.logo = item.logo || '';
        applySettings(item.settings || {});
        buildForm(); render(); updateLogoUi();
        window.scrollTo({ top: root.offsetTop - 20, behavior: 'smooth' });
      });
      var del = document.createElement('button'); del.type = 'button'; del.className = 'btn ghost sm'; del.textContent = 'Delete';
      del.addEventListener('click', function () {
        store(SAVED_KEY, load(SAVED_KEY, []).filter(function (x) { return x.id !== item.id; }));
        renderSaved();
      });
      card.appendChild(img); card.appendChild(info); card.appendChild(openB); card.appendChild(del);
      box.appendChild(card);
    });
  }

  function exportSaved() {
    var blob = new Blob([JSON.stringify({ app: 'diyaqr-web', version: 1, codes: load(SAVED_KEY, []) })], { type: 'application/json' });
    var a = document.createElement('a');
    a.href = URL.createObjectURL(blob); a.download = 'diyaqr-saved-codes.json';
    document.body.appendChild(a); a.click(); a.remove();
    setTimeout(function () { URL.revokeObjectURL(a.href); }, 1000);
  }
  function importSaved(file) {
    var fr = new FileReader();
    fr.onload = function () {
      try {
        var data = JSON.parse(fr.result);
        if (!data || !Array.isArray(data.codes)) throw new Error('bad');
        var list = load(SAVED_KEY, []);
        var ids = {}; list.forEach(function (x) { ids[x.id] = 1; });
        data.codes.forEach(function (c) { if (c && c.id && c.type && !ids[c.id]) list.push(c); });
        store(SAVED_KEY, list); renderSaved(); toast('Imported');
      } catch (e) { toast('That file is not a DiyaQR backup'); }
    };
    fr.readAsText(file);
  }

  function updateLogoUi() {
    $('logoName').textContent = state.logo ? 'Logo added' : 'No logo';
    $('logoClear').hidden = !state.logo;
  }

  function syncGradientUi() {
    var on = $('gradient').checked;
    $('gradBox').hidden = !on;
  }

  // ---------- init ----------
  function init() {
    state.values = load(FIELD_KEY, {});
    var types = $('types');
    Object.keys(TYPES).forEach(function (k) {
      var b = document.createElement('button');
      b.type = 'button'; b.setAttribute('data-type', k); b.textContent = TYPES[k].label;
      b.addEventListener('click', function () {
        state.type = k; buildForm(); render();
      });
      types.appendChild(b);
    });
    var sw = $('swatches');
    STYLES.forEach(function (s) {
      var b = document.createElement('button');
      b.type = 'button'; b.title = s[0]; b.setAttribute('aria-label', s[0]);
      b.style.background = s[3] ? 'linear-gradient(135deg,' + s[1] + ',' + s[3] + ')' : s[1];
      b.style.outline = '3px solid ' + s[2]; b.style.outlineOffset = '-6px';
      b.addEventListener('click', function () {
        $('dotColor').value = s[1]; $('bgColor').value = s[2];
        $('gradient').checked = !!s[3];
        if (s[3]) $('dotColor2').value = s[3];
        syncGradientUi(); render();
      });
      sw.appendChild(b);
    });
    ['dotColor', 'dotColor2', 'bgColor', 'dotType', 'cornerType', 'cornerDotType', 'ec', 'size', 'margin', 'gradType', 'logoSize'].forEach(function (id) {
      $(id).addEventListener('input', render);
    });
    $('gradient').addEventListener('change', function () { syncGradientUi(); render(); });
    $('size').addEventListener('input', function () { $('sizeOut').textContent = $('size').value + ' px'; });
    $('logo').addEventListener('change', function (e) {
      var f = e.target.files && e.target.files[0];
      if (!f) return;
      var fr = new FileReader();
      fr.onload = function () {
        var img = new Image();
        img.onload = function () {
          var c = document.createElement('canvas'), m = 256, s = Math.min(1, m / Math.max(img.width, img.height));
          c.width = Math.round(img.width * s); c.height = Math.round(img.height * s);
          c.getContext('2d').drawImage(img, 0, 0, c.width, c.height);
          state.logo = c.toDataURL('image/png');
          if ($('ec').value === 'L' || $('ec').value === 'M') $('ec').value = 'Q';
          updateLogoUi(); render();
        };
        img.src = fr.result;
      };
      fr.readAsDataURL(f);
      e.target.value = '';
    });
    $('logoClear').addEventListener('click', function () { state.logo = ''; updateLogoUi(); render(); });
    $('dl-png').addEventListener('click', function () { download('png'); });
    $('dl-svg').addEventListener('click', function () { download('svg'); });
    $('dl-jpeg').addEventListener('click', function () { download('jpeg'); });
    $('dl-webp').addEventListener('click', function () { download('webp'); });
    $('copyImg').addEventListener('click', copyImage);
    $('save').addEventListener('click', saveCode);
    $('exportSaved').addEventListener('click', exportSaved);
    $('importSaved').addEventListener('change', function (e) { if (e.target.files[0]) importSaved(e.target.files[0]); e.target.value = ''; });
    $('clearSaved').addEventListener('click', function () {
      if (confirm('Delete all saved codes from this browser?')) { store(SAVED_KEY, []); renderSaved(); }
    });
    $('sizeOut').textContent = $('size').value + ' px';
    syncGradientUi(); updateLogoUi(); buildForm(); renderSaved();
    if (typeof QRCodeStyling === 'undefined') window.addEventListener('load', render); else render();
  }

  init();
})();
