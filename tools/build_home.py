"""Renders the homepage sections from assets/site/data.js into static HTML (no JavaScript needed to read the page).

Run:  python tools/build_home.py      (needs Node.js, only to read data.js)
Edit data.js, run this, commit index.html + llms.txt.
Regions in index.html between <!--B:name--> and <!--/B:name--> are overwritten.
"""
import html
import json
import os
import re
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://ziaurrehmanjutt.github.io"
e = lambda v: html.escape(str(v), quote=True)


def load():
    js = "global.window={};require(%s);console.log(JSON.stringify(window.SITE))" % json.dumps(
        os.path.join(ROOT, "assets", "site", "data.js"))
    return json.loads(subprocess.check_output(["node", "-e", js], text=True, encoding="utf-8"))


def L(S, key, default):
    """UI label for the current language (Arabic build passes S["_L"])."""
    return S.get("_L", {}).get(key, default)


def cat(S, c):
    return S.get("_cat", {}).get(c, c)


def ext(u):
    return ' target="_blank" rel="noopener noreferrer"' if re.match(r"https?:", u) else ""


def pts(arr):
    return '<ul class="pts">' + "".join("<li>%s</li>" % e(p) for p in arr) + "</ul>"


def chips(arr):
    return "".join('<span class="chip">%s</span>' % e(t) for t in arr)


def stats(S):
    return "".join('<div class="stat"><b>%s</b><span>%s</span></div>' % (e(s["value"]), e(s["label"])) for s in S["stats"])


def services(S):
    return "".join(
        '<article class="service"><div class="s-icon" aria-hidden="true">%s</div><h3>%s</h3><p>%s</p><div class="chips">%s</div>'
        '<a class="s-link" href="services/%s/">%s</a></article>'
        % (e(v["icon"]), e(v["title"]), e(v["text"]), chips(v.get("tags", [])), e(v["slug"]), L(S, "pricing_link", "Details &amp; pricing →")) for v in S["services"])


def filters(S):
    cats = ["all"]
    for p in S["projects"]:
        if p["category"] not in cats:
            cats.append(p["category"])
    return "".join('<button class="filter" type="button" data-cat="%s" aria-pressed="%s">%s</button>'
                   % (e(c), "true" if i == 0 else "false", e(cat(S, c))) for i, c in enumerate(cats))


def projects(S):
    out = []
    for p in sorted(S["projects"], key=lambda p: 0 if p.get("featured") else 1):
        l = p.get("links", {})
        a = ""
        if l.get("live"):
            a += '<a href="%s"%s>%s</a>' % (e(l["live"]), ext(l["live"]), L(S, "details", "Details →") if not l["live"].startswith("http") else L(S, "open", "Open ↗"))
        if l.get("demo"):
            a += '<a href="%s"%s>%s</a>' % (e(l["demo"]), ext(l["demo"]), L(S, "demo", "Live demo ↗"))
        if l.get("npm"):
            a += '<a href="%s"%s>npm ↗</a>' % (e(l["npm"]), ext(l["npm"]))
        if l.get("code"):
            a += '<a href="%s"%s>%s</a>' % (e(l["code"]), ext(l["code"]), L(S, "source", "Source ↗"))
        out.append(
            '<article class="project%s" data-cat="%s"><div class="meta"><span>%s%s</span>%s</div><h3>%s</h3><p>%s</p>'
            '<div class="chips">%s</div><div class="links">%s</div></article>'
            % (" featured" if p.get("featured") else "", e(p["category"]), e(cat(S, p["category"])),
               " · " + e(p["year"]) if p.get("year") else "",
               '<span class="badge">%s</span>' % L(S, "featured", "★ Featured") if p.get("featured") else "",
               e(p["title"]), e(p["description"]), chips(p.get("tags", [])), a))
    return "".join(out)


def timeline(S):
    out = []
    for j in S["experience"]:
        tracks = ""
        if j.get("tracks"):
            tracks = '<div class="tracks">' + "".join(
                '<div class="track"><h4>%s</h4>%s</div>' % (e(t["role"]), pts(t["points"])) for t in j["tracks"]) + "</div>"
        out.append(
            '<article class="job"><div class="job-meta"><div class="period">%s</div><div class="place">%s</div></div><div>'
            '<h3>%s</h3><div class="co">%s%s</div>%s%s</div></article>'
            % (e(j["period"]), e(j["place"]), e(j["role"]), e(j["company"]),
               " · " + e(j["via"]) if j.get("via") else "", pts(j["points"]), tracks))
    return "".join(out)


def education(S):
    return "".join(
        '<article class="job"><div class="job-meta"><div class="period">%s</div></div><div><h3>%s</h3><div class="co">%s</div></div></article>'
        % (e(x["period"]), e(x["degree"]), e(x["school"])) for x in S["education"])


def skills(S):
    return "".join('<div class="skill-card"><h3>%s</h3><div class="chips">%s</div></div>' % (e(g["group"]), chips(g["items"]))
                   for g in S["skills"])


def jsonld(S):
    same = [S["github"], "https://www.npmjs.com/package/ng-spinner-wheel"]
    if S.get("linkedin"):
        same.append(S["linkedin"])
    person = {"@context": "https://schema.org", "@type": "Person", "@id": BASE + "/#person", "name": S["name"],
              "jobTitle": S["title"], "url": BASE + "/", "email": S["email"], "telephone": S["phone"], "sameAs": same,
              "address": {"@type": "PostalAddress", "addressLocality": "Riyadh", "addressCountry": "SA"},
              "knowsAbout": [i for g in S["skills"][:4] for i in g["items"]]}
    biz = {"@context": "https://schema.org", "@type": "ProfessionalService", "name": S["name"] + " — Software Development Services",
           "url": BASE + S.get("_prefix", "") + "/", "telephone": S["phone"], "email": S["email"], "inLanguage": S.get("_lang", "en"), "areaServed": "Worldwide", "provider": {"@id": BASE + "/#person"},
           "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Services", "itemListElement": [
               {"@type": "Offer", "itemOffered": {"@type": "Service", "name": v["title"], "description": v["text"],
                                                  "url": "%s%s/services/%s/" % (BASE, S.get("_prefix", ""), v["slug"])}} for v in S["services"]]}}
    return "\n".join('  <script type="application/ld+json">%s</script>' % json.dumps(x, ensure_ascii=False) for x in (person, biz))


def llms(S):
    L = ["# %s" % S["name"], "", "> %s. %s Based in %s." % (S["title"], S["tagline"], S["location"]), "", S["summary"], "",
         "## Services", ""]
    L += ["- [%s](%s/services/%s/): %s" % (v["title"], BASE, v["slug"], v["text"]) for v in S["services"]]
    L += ["", "## Projects", ""]
    for p in S["projects"]:
        l = p.get("links", {})
        u = l.get("live") or l.get("code") or ""
        if u and not u.startswith("http"):
            u = BASE + "/" + u
        L.append("- [%s](%s): %s" % (p["title"], u, p["description"]))
    L += ["", "## Other", "", "- [Resume](%s/resume.html)" % BASE, "- [Arabic version / النسخة العربية](%s/ar/)" % BASE, "- [GitHub](%s)" % S["github"],
          "- Email: %s" % S["email"], "- Phone / WhatsApp: %s" % S["phone"], ""]
    return "\n".join(L)


def region(txt, name, content, anchor=None):
    start, end = "<!--B:%s-->" % name, "<!--/B:%s-->" % name
    if start not in txt:
        if not anchor:
            raise SystemExit("marker %s missing" % name)
        txt = txt.replace(anchor, anchor + start + end, 1)
    return re.sub(re.escape(start) + ".*?" + re.escape(end), lambda m: start + content + end, txt, flags=re.S)


def main():
    S = load()
    p = os.path.join(ROOT, "index.html")
    t = open(p, encoding="utf-8").read()
    for name, fn, el in (("stats", stats, '<div class="stats" id="stats">'),
                         ("services", services, '<div class="services" id="services-grid">'),
                         ("filters", filters, '<div class="filters" id="filters" role="group" aria-label="Filter projects">'),
                         ("projects", projects, '<div class="projects" id="projects-grid">'),
                         ("timeline", timeline, '<div class="timeline" id="timeline">'),
                         ("education", education, '<div class="edu" id="education">'),
                         ("skills", skills, '<div class="skills" id="skills-grid">')):
        t = region(t, name, fn(S), el)
    t = region(t, "ld", "\n" + jsonld(S) + "\n  ", '<link rel="stylesheet" href="assets/site/site.css">\n')
    open(p, "w", encoding="utf-8", newline="\n").write(t)
    open(os.path.join(ROOT, "llms.txt"), "w", encoding="utf-8", newline="\n").write(llms(S))
    print("home + llms.txt built")


if __name__ == "__main__":
    main()
