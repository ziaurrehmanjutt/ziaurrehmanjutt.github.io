(function () {
  var S = window.SITE;
  var $ = function (id) { return document.getElementById(id); };
  var esc = function (v) {
    return String(v).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  };
  var pts = function (arr) { return '<ul class="pts">' + arr.map(function (p) { return "<li>" + esc(p) + "</li>"; }).join("") + "</ul>"; };
  var ext = function (u) { return /^https?:/.test(u) ? ' target="_blank" rel="noopener noreferrer"' : ""; };

  /* theme */
  var root = document.documentElement;
  var themeBtn = $("theme-toggle");
  if (themeBtn) {
    themeBtn.addEventListener("click", function () {
      var next = root.getAttribute("data-theme") === "light" ? "dark" : "light";
      root.setAttribute("data-theme", next);
      try { localStorage.setItem("theme", next); } catch (e) {}
    });
  }

  /* mobile menu */
  var menuBtn = $("menu-btn"), links = $("nav-links");
  if (menuBtn && links) {
    menuBtn.addEventListener("click", function () {
      var open = links.classList.toggle("open");
      menuBtn.setAttribute("aria-expanded", open);
    });
    links.addEventListener("click", function (e) { if (e.target.tagName === "A") links.classList.remove("open"); });
  }

  /* year */
  var y = $("year"); if (y) y.textContent = new Date().getFullYear();

  /* stats */
  var stats = $("stats");
  if (stats) stats.innerHTML = S.stats.map(function (s) {
    return '<div class="stat"><b>' + esc(s.value) + "</b><span>" + esc(s.label) + "</span></div>";
  }).join("");

  /* skills */
  var skills = $("skills-grid");
  if (skills) skills.innerHTML = S.skills.map(function (g) {
    return '<div class="skill-card reveal"><h3>' + esc(g.group) + '</h3><div class="chips">' +
      g.items.map(function (i) { return '<span class="chip">' + esc(i) + "</span>"; }).join("") + "</div></div>";
  }).join("");

  /* projects + filters */
  var grid = $("projects-grid");
  if (grid) {
    var cats = ["all"];
    S.projects.forEach(function (p) { if (cats.indexOf(p.category) < 0) cats.push(p.category); });
    var render = function (cat) {
      grid.innerHTML = S.projects.filter(function (p) { return cat === "all" || p.category === cat; })
        .sort(function (a, b) { return (b.featured ? 1 : 0) - (a.featured ? 1 : 0); })
        .map(function (p) {
          var l = p.links || {}, a = "";
          if (l.live) a += '<a href="' + esc(l.live) + '"' + ext(l.live) + ">Open ↗</a>";
          if (l.code) a += '<a href="' + esc(l.code) + '"' + ext(l.code) + ">Source ↗</a>";
          return '<article class="project reveal in' + (p.featured ? " featured" : "") + '">' +
            '<div class="meta"><span>' + esc(p.category) + (p.year ? " · " + esc(p.year) : "") + "</span>" +
            (p.featured ? '<span class="badge">★ Featured</span>' : "") + "</div>" +
            "<h3>" + esc(p.title) + "</h3><p>" + esc(p.description) + "</p>" +
            '<div class="chips">' + (p.tags || []).map(function (t) { return '<span class="chip">' + esc(t) + "</span>"; }).join("") + "</div>" +
            '<div class="links">' + a + "</div></article>";
        }).join("");
    };
    var bar = $("filters");
    if (bar) {
      bar.innerHTML = cats.map(function (c, i) {
        return '<button class="filter" type="button" data-cat="' + esc(c) + '" aria-pressed="' + (i === 0) + '">' + esc(c) + "</button>";
      }).join("");
      bar.addEventListener("click", function (e) {
        var b = e.target.closest("button"); if (!b) return;
        [].forEach.call(bar.children, function (x) { x.setAttribute("aria-pressed", x === b); });
        render(b.getAttribute("data-cat"));
      });
    }
    render("all");
  }

  /* experience (portfolio view) */
  var tl = $("timeline");
  if (tl) tl.innerHTML = S.experience.map(function (j) {
    return '<article class="job reveal"><div class="job-meta"><div class="period">' + esc(j.period) + '</div><div class="place">' + esc(j.place) + "</div></div><div>" +
      "<h3>" + esc(j.role) + '</h3><div class="co">' + esc(j.company) + (j.via ? " · " + esc(j.via) : "") + "</div>" + pts(j.points) +
      (j.tracks ? '<div class="tracks">' + j.tracks.map(function (t) { return '<div class="track"><h4>' + esc(t.role) + "</h4>" + pts(t.points) + "</div>"; }).join("") + "</div>" : "") +
      "</div></article>";
  }).join("");

  var edu = $("education");
  if (edu) edu.innerHTML = S.education.map(function (e) {
    return '<article class="job reveal"><div class="job-meta"><div class="period">' + esc(e.period) + "</div></div><div><h3>" + esc(e.degree) + '</h3><div class="co">' + esc(e.school) + "</div></div></article>";
  }).join("");

  /* social links */
  var gh = document.querySelectorAll("[data-github]");
  [].forEach.call(gh, function (a) { a.href = S.github; });
  var li = document.querySelectorAll("[data-linkedin]");
  [].forEach.call(li, function (a) { if (S.linkedin) a.href = S.linkedin; else a.hidden = true; });
  [].forEach.call(document.querySelectorAll("[data-email]"), function (a) { a.href = "mailto:" + S.email; });

  /* ---- resume page ---- */
  var paper = $("paper");
  if (paper) {
    var c = [esc(S.location), '<a href="mailto:' + esc(S.email) + '">' + esc(S.email) + "</a>", esc(S.phone),
      '<a href="' + esc(S.github) + '">GitHub</a>'];
    if (S.linkedin) c.push('<a href="' + esc(S.linkedin) + '">LinkedIn</a>');
    var jobs = S.experience.map(function (j) {
      return '<div class="r-job"><div class="r-head"><span>' + esc(j.role) + " — " + esc(j.company) + "</span><span>" + esc(j.period) + "</span></div>" +
        '<div class="r-sub">' + esc(j.place) + (j.via ? " · " + esc(j.via) : "") + "</div>" + pts(j.points) +
        (j.tracks || []).map(function (t) { return "<h4>" + esc(t.role) + "</h4>" + pts(t.points); }).join("") + "</div>";
    }).join("");
    var proj = S.projects.map(function (p) {
      return "<li><b>" + esc(p.title) + "</b> — " + esc(p.description) + "</li>";
    }).join("");
    paper.innerHTML =
      "<h1>" + esc(S.name) + '</h1><div class="role">' + esc(S.title) + " · " + esc(S.tagline) + '</div><div class="contacts">' +
      c.map(function (x) { return "<span>" + x + "</span>"; }).join("") + "</div>" +
      "<h2>Summary</h2><p>" + esc(S.summary) + "</p>" +
      "<h2>Skills</h2>" + S.skills.map(function (g) { return '<p class="r-skill"><b>' + esc(g.group) + ":</b> " + esc(g.items.join(", ")) + "</p>"; }).join("") +
      "<h2>Experience</h2>" + jobs +
      "<h2>Selected projects</h2><ul>" + proj + "</ul>" +
      "<h2>Education</h2>" + S.education.map(function (e) {
        return '<div class="r-job"><div class="r-head"><span>' + esc(e.degree) + "</span><span>" + esc(e.period) + '</span></div><div class="r-sub">' + esc(e.school) + "</div></div>";
      }).join("");
  }

  /* reveal on scroll */
  var items = document.querySelectorAll(".reveal:not(.in)");
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } });
    }, { threshold: .08 });
    [].forEach.call(items, function (el) { io.observe(el); });
  } else { [].forEach.call(items, function (el) { el.classList.add("in"); }); }

  /* active nav link */
  var secs = document.querySelectorAll("main section[id]");
  if (secs.length && "IntersectionObserver" in window) {
    var so = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (e.isIntersecting) [].forEach.call(document.querySelectorAll("#nav-links a"), function (a) {
          a.setAttribute("aria-current", a.getAttribute("href") === "#" + e.target.id);
        });
      });
    }, { rootMargin: "-45% 0px -50% 0px" });
    [].forEach.call(secs, function (s) { so.observe(s); });
  }
})();
