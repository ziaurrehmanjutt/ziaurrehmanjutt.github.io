# -*- coding: utf-8 -*-
"""Builds the Arabic homepage (ar/index.html) from the English index.html + tools/ar_content.py.

Run:  python tools/build_ar.py     (run tools/build_home.py first if you changed data.js)
The static text replacements below must match index.html; if you edit English wording in index.html,
update the matching line here (the script fails loudly if a string is no longer found).
"""
import copy
import os
import re
import sys
from urllib.parse import quote

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import ar_content as A  # noqa: E402
import build_home as H  # noqa: E402

ROOT = H.ROOT
BASE = H.BASE
NAME_AR = "ضياء الرحمن"


def arabic_site():
    """English SITE dict with Arabic text merged in; links rewritten for /ar/."""
    S = copy.deepcopy(H.load())
    ar = A.SITE
    S["_L"], S["_cat"], S["_prefix"], S["_lang"] = A.LABELS, A.CATS, "/ar", "ar"
    S["title"], S["tagline"], S["location"], S["summary"] = ar["title"], ar["tagline"], ar["location"], ar["summary"]
    for st, lab in zip(S["stats"], ar["stats"]):
        st["label"] = lab
    for v in S["services"]:
        v["title"], v["text"], v["tags"] = ar["services"][v["slug"]]
    for p in S["projects"]:
        p["description"] = ar["projects"][p["title"]]
        live = p.get("links", {}).get("live")
        if live and not live.startswith("http"):
            # landing pages that exist in Arabic, otherwise the English page
            p["links"]["live"] = {"diyaqr/": "../diyaqr/ar/", "diyaexpense/": "../diyaexpense/ar/",
                                  "ng-spinner-wheel/": "../ng-spinner-wheel/",
                                  "shorts-video-maker/": "../shorts-video-maker/"}.get(live, "../" + live)
    for g in S["skills"]:
        g["group"] = ar["skills"][g["group"]]
    S["experience"] = ar["experience"]
    S["education"] = ar["education"]
    return S


def sub(t, old, new, count=1):
    if old not in t:
        raise SystemExit("not found in index.html: " + old[:80])
    return t.replace(old, new, count)


def main():
    S = arabic_site()
    t = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()

    # ---- head
    t = sub(t, '<html lang="en">', '<html lang="ar" dir="rtl">')
    title = "%s — مطوّر برمجيات أول | ERP وDynamics 365 وLaravel وتطبيقات الجوال" % NAME_AR
    desc = ("%s: مطوّر برمجيات أول في الرياض. Dynamics 365 F&O (X++) وLaravel/PHP وتطبيقات Ionic/Angular للجوال. "
            "خدمات SEO وفحص الأمان وأتمتة الذكاء الاصطناعي وربط API وتطبيقات الجوال لأي موقع.") % NAME_AR
    t = re.sub(r"<title>.*?</title>", lambda m: "<title>%s</title>" % title, t, count=1)
    t = re.sub(r'(<meta name="description" content=")[^"]*(">)', lambda m: m.group(1) + desc.replace("&", "&amp;") + m.group(2), t, count=1)
    t = re.sub(r'(<meta property="og:title" content=")[^"]*(">)', lambda m: m.group(1) + title + m.group(2), t, count=1)
    t = re.sub(r'(<meta property="og:description" content=")[^"]*(">)', lambda m: m.group(1) + desc.replace("&", "&amp;") + m.group(2), t, count=1)
    t = sub(t, '<link rel="canonical" href="https://ziaurrehmanjutt.github.io/">', '<link rel="canonical" href="%s/ar/">' % BASE)
    t = sub(t, '<meta property="og:url" content="https://ziaurrehmanjutt.github.io/">',
            '<meta property="og:url" content="%s/ar/">\n  <meta property="og:locale" content="ar_AR">' % BASE)
    t = sub(t, 'href="assets/site/favicon.svg"', 'href="../assets/site/favicon.svg"')
    t = sub(t, 'href="assets/site/site.css"', 'href="../assets/site/site.css"')
    t = sub(t, "family=Space+Grotesk:wght@500;600;700&display=swap", "family=Space+Grotesk:wght@500;600;700&family=Noto+Sans+Arabic:wght@400;500;600;700&display=swap")
    t = re.sub(r"<!--B:ld-->.*?<!--/B:ld-->", lambda m: "<!--B:ld-->\n" + H.jsonld(S) + "\n  <!--/B:ld-->", t, count=1, flags=re.S)

    # ---- static text
    for old, new in [
        ('<a class="skip" href="#main">Skip to content</a>', '<a class="skip" href="#main">انتقل إلى المحتوى</a>'),
        ('aria-label="Zia Ur Rehman, home"><span class="brand-mark">ZR</span>Zia Ur Rehman</a>',
         'aria-label="%s، الرئيسية"><span class="brand-mark">ZR</span>%s</a>' % (NAME_AR, NAME_AR)),
        ('aria-label="Primary"', 'aria-label="التنقل الرئيسي"'),
        ('<a href="#about">About</a>', '<a href="#about">نبذة</a>'),
        ('<a href="#services">Services</a>\n        <a href="#projects">Projects</a>', '<a href="#services">الخدمات</a>\n        <a href="#projects">المشاريع</a>'),
        ('<a href="#experience">Experience</a>', '<a href="#experience">الخبرة</a>'),
        ('<a href="#skills">Skills</a>', '<a href="#skills">المهارات</a>'),
        ('<a href="#contact">Contact</a>', '<a href="#contact">تواصل</a>'),
        ('<a href="resume.html">Resume</a>\n        <a href="ar/" hreflang="ar" lang="ar">العربية</a>',
         '<a href="../resume.html" hreflang="en" lang="en">Resume</a>\n        <a href="../" hreflang="en" lang="en">English</a>'),
        ('aria-label="Toggle light/dark theme"', 'aria-label="تبديل الوضع الفاتح/الداكن"'),
        ('aria-label="Menu"', 'aria-label="القائمة"'),
        ('Available for new opportunities', 'متاح لفرص جديدة'),
        ('Hi, I\'m <span class="grad">Zia Ur Rehman.</span><br>I build systems that run businesses.',
         'مرحباً، أنا <span class="grad">%s.</span><br>أبني أنظمة تُدير الأعمال.' % NAME_AR),
        ('Senior software developer in Riyadh, shipping enterprise ERP on Dynamics 365 (X++), full-stack web with Laravel, and mobile apps with Ionic and Angular.',
         'مطوّر برمجيات أول في الرياض، أنفّذ أنظمة ERP للمؤسسات على Dynamics 365 (X++)، وتطبيقات ويب متكاملة بـ Laravel، وتطبيقات جوال بـ Ionic وAngular.'),
        ('<a class="btn btn-primary" href="#projects">View projects →</a>', '<a class="btn btn-primary" href="#projects">عرض المشاريع ←</a>'),
        ('<a class="btn btn-ghost" href="#services">Services</a>', '<a class="btn btn-ghost" href="#services">الخدمات</a>'),
        ('<a class="btn btn-ghost" href="resume.html">Resume / CV</a>', '<a class="btn btn-ghost" href="../resume.html">السيرة الذاتية (English)</a>'),
        ('<div class="code-card" aria-hidden="true">', '<div class="code-card" aria-hidden="true" dir="ltr">'),
        ('<span class="eyebrow">About</span>', '<span class="eyebrow">نبذة</span>'),
        ('Enterprise depth, product polish.', 'عمق المؤسسات، وإتقان المنتج.'),
        ("I've spent 6+ years delivering ERP, web, and mobile solutions, from Dynamics 365 Finance &amp; Operations customizations to published Android and iOS apps.",
         'أمضيت أكثر من 6 سنوات في تقديم حلول ERP والويب والجوال، من تخصيصات Dynamics 365 Finance &amp; Operations إلى تطبيقات أندرويد وiOS المنشورة.'),
        ('Today I work at King Saud University, building internal platforms, REST APIs, SAML/SSO authentication, dashboards, and Ionic mobile apps used across departments.',
         'أعمل اليوم في جامعة الملك سعود، أبني منصات داخلية وواجهات REST API ومصادقة SAML/SSO ولوحات معلومات وتطبيقات جوال بـ Ionic تُستخدم في مختلف الأقسام.'),
        ('I like clear requirements, clean integrations, and software that people actually enjoy using.',
         'أحب المتطلبات الواضحة، والتكاملات النظيفة، والبرمجيات التي يستمتع الناس باستخدامها فعلاً.'),
        ('<span class="eyebrow">What I can do for you</span><h2>Services</h2>', '<span class="eyebrow">ماذا يمكنني أن أقدّم لك</span><h2>الخدمات</h2>'),
        ('📞 Call me</a>', '📞 اتصل بي</a>'),
        ('<span class="eyebrow">Portfolio</span><h2>Selected projects</h2>', '<span class="eyebrow">الأعمال</span><h2>مشاريع مختارة</h2>'),
        ('aria-label="Filter projects"', 'aria-label="تصفية المشاريع"'),
        ('More on <a', 'المزيد على <a'),
        ('<span class="eyebrow">Career</span><h2>Experience</h2></div><a class="btn btn-ghost" href="resume.html">Full resume →</a>',
         '<span class="eyebrow">المسيرة</span><h2>الخبرة</h2></div><a class="btn btn-ghost" href="../resume.html">السيرة الكاملة (English) ←</a>'),
        ('<span class="eyebrow">Toolbox</span><h2>Skills &amp; technologies</h2>', '<span class="eyebrow">الأدوات</span><h2>المهارات والتقنيات</h2>'),
        ('<span class="eyebrow">Contact</span>', '<span class="eyebrow">تواصل</span>'),
        ("Let's build something useful.", 'لنبنِ شيئاً مفيداً.'),
        ('Have a project, a role, or an ERP problem that needs solving? Send me a message.',
         'لديك مشروع أو وظيفة أو مشكلة ERP تحتاج حلاً؟ راسلني.'),
        ('📞 Call +966 500256094</a>', '📞 اتصل <bdi dir="ltr">+966 500256094</bdi></a>'),
        ('>Email me</a>', '>راسلني بالبريد</a>'),
        ("Hi%20Zia%2C%20I%27m%20interested%20in%20your%20services.", quote(A.UI["wa_text"])),
        ('<span>© <span id="year">2026</span> Zia Ur Rehman · Riyadh, Saudi Arabia</span>',
         '<span>© <span id="year">2026</span> %s · الرياض، المملكة العربية السعودية</span>' % NAME_AR),
        ('Back to top ↑', 'العودة للأعلى ↑'),
    ]:
        t = sub(t, old, new)
    # remaining "GitHub ↗ / WhatsApp ↗ / LinkedIn ↗" stay as brand names, arrows flip for RTL
    t = t.replace("WhatsApp ↗", "واتساب ↗")

    # ---- generated regions from Arabic data
    for name, fn in (("stats", H.stats), ("services", H.services), ("filters", H.filters), ("projects", H.projects),
                     ("timeline", H.timeline), ("education", H.education), ("skills", H.skills)):
        t = re.sub(r"<!--B:%s-->.*?<!--/B:%s-->" % (name, name), lambda m, f=fn: "<!--B:%s-->%s<!--/B:%s-->" % (name, f(S), name), t, count=1, flags=re.S)

    out = os.path.join(ROOT, "ar", "index.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w", encoding="utf-8", newline="\n").write(t)

    # sitemap
    u = BASE + "/ar/"
    for fn in ("sitemap.txt", "sitemap.xml"):
        p = os.path.join(ROOT, fn)
        txt = open(p, encoding="utf-8").read()
        if u in txt:
            continue
        if fn.endswith(".xml"):
            txt = txt.replace("</urlset>", "  <url>\n    <loc>%s</loc>\n    <lastmod>2026-11-22</lastmod>\n  </url>\n</urlset>" % u)
        else:
            txt = txt.rstrip("\n") + "\n" + u + "\n"
        open(p, "w", encoding="utf-8", newline="\n").write(txt)
    print("built ar/index.html")


if __name__ == "__main__":
    main()
