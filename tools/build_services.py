"""Generates one static page per service into services/<slug>/index.html.

Run from anywhere:  python tools/build_services.py
Edit the SERVICES list below (text, steps, packages, prices), run it, commit the output.
Prices: set "price" on each package, e.g. "from $150". "Custom quote" is used until you decide.
"""
import html
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://ziaurrehmanjutt.github.io"
PHONE = "+966 500256094"
TEL = "+966500256094"
WA = "966500256094"
EMAIL = "ziaa520@gmail.com"
LASTMOD = "2026-11-16"
Q = "Custom quote"  # default price label

e = html.escape

SERVICES = [
    {
        "slug": "seo",
        "icon": "🔎",
        "title": "SEO for your website",
        "short": "SEO Services",
        "meta": "Technical SEO, on-page optimization, schema markup, site speed and multilingual SEO to get your website found on Google. Packages, process and pricing explained.",
        "tagline": "Get found on Google by people who are already looking for what you offer.",
        "intro": "Good content is wasted if search engines can't crawl, understand or trust your site. I fix the technical foundations first (indexing, speed, structure, schema), then improve pages so they match what people actually search for.",
        "who": "Business owners, shops, clinics, agencies and app makers whose website is live but gets little or no search traffic, or whose rankings dropped.",
        "gets": [
            "Full technical SEO audit: crawlability, indexing, sitemap, robots.txt, canonical tags, redirects, broken links",
            "On-page optimization: titles, meta descriptions, headings, internal links, image alt text",
            "Structured data (schema.org) for rich results: organization, product, FAQ, software app, article",
            "Speed and Core Web Vitals improvements: image optimization, caching, script cleanup",
            "Multilingual SEO with hreflang for sites in several languages (Arabic, Urdu, English and more)",
            "Google Search Console and Analytics setup, with a plain-language report of what changed",
        ],
        "steps": [
            ("Audit", "I crawl your site and Search Console data and list every issue by impact."),
            ("Plan", "You get a prioritized plan: quick wins first, bigger changes after."),
            ("Implement", "I make the fixes directly in your code or CMS, or hand a clear checklist to your developer."),
            ("Measure", "We track impressions, clicks and rankings so you can see what is working."),
        ],
        "factors": [
            "Number of pages and how large the site is",
            "Platform (WordPress, Laravel, custom code, static) and whether I can edit it directly",
            "How many languages or countries you target",
            "Current technical state: a clean site costs less than one with deep problems",
            "One-time fix versus ongoing monthly work",
        ],
        "packages": [
            ("SEO audit", "A full audit with a prioritized action list and report. You or your developer apply the fixes.", Q),
            ("Audit + fixes", "Audit plus I implement the technical and on-page fixes and set up schema, sitemap and Search Console.", Q),
            ("Monthly SEO", "Ongoing optimization, new page improvements, monitoring and a monthly report.", Q),
        ],
        "faq": [
            ("How long until I see results?", "Technical fixes can show effects within weeks, but ranking growth usually takes 2 to 6 months depending on competition. I can't promise a position on Google, and anyone who does is not being honest."),
            ("Do you do link building?", "I focus on technical and on-page SEO and on content structure. I don't sell spammy links, which can get a site penalized."),
            ("Can you work on my WordPress or custom site?", "Yes. I work with WordPress, Laravel, PHP, Angular and static sites."),
        ],
    },
    {
        "slug": "security-audit",
        "icon": "🛡️",
        "title": "Website security audit (OWASP Top 10)",
        "short": "Security Audit",
        "meta": "Website security audit against the OWASP Top 10: injection, broken access control, XSS, misconfiguration and more. Clear report with prioritized fixes. Scope, process and pricing explained.",
        "tagline": "Find the holes in your website before someone else does.",
        "intro": "I review your website or web application against the OWASP Top 10, the industry standard list of the most serious web risks. You receive a plain-language report that explains each finding, how serious it is, and exactly how to fix it. I can also apply the fixes.",
        "who": "Owners of websites that handle logins, payments or customer data, companies preparing for a client or compliance review, and anyone who suspects their site was hacked or is running old software.",
        "gets": [
            "Check against the OWASP Top 10: broken access control, injection (SQL and others), XSS, insecure design, security misconfiguration, vulnerable and outdated components, authentication failures, integrity failures, logging gaps, SSRF",
            "Review of login, session, password reset and permission logic",
            "Server and HTTPS checks: SSL/TLS setup, security headers, exposed files, open admin panels",
            "Dependency and plugin review for known vulnerabilities",
            "Written report: each finding with severity, evidence, and a concrete fix",
            "Optional: I implement the fixes and re-test to confirm they are closed",
        ],
        "steps": [
            ("Agree scope", "We confirm exactly which site, app or API I may test. I only test systems you own or are authorized to give me access to."),
            ("Test", "Manual review and tooling against the OWASP Top 10, careful not to disrupt your live site."),
            ("Report", "You get a prioritized report in plain language, with fixes, not just a list of tool output."),
            ("Fix & re-test", "Optionally I apply the fixes and re-test so you know the issues are really closed."),
        ],
        "factors": [
            "Size and complexity: number of pages, user roles, forms and API endpoints",
            "Whether I get access to the source code (deeper and cheaper) or test only from outside",
            "Type of app: brochure site, store with payments, or custom application",
            "Whether you want the fixes implemented, or just the report",
            "A re-test after fixes",
        ],
        "packages": [
            ("Quick check", "Outside-in scan and review for the most common issues on a small site, with a short report.", Q),
            ("Full OWASP audit", "In-depth test against all ten categories with a detailed report and fix guidance.", Q),
            ("Audit + remediation", "Full audit, I fix the issues in your code or server, then re-test.", Q),
        ],
        "faq": [
            ("Is it safe for my live website?", "Yes. I avoid destructive tests on production, and for riskier checks I suggest a staging copy."),
            ("Do you guarantee my site can't be hacked?", "No one can. An audit greatly reduces risk by closing known weaknesses, but security is ongoing work."),
            ("Will you test any website I name?", "No. I only test sites you own or have written permission to test."),
        ],
    },
    {
        "slug": "ai-automation",
        "icon": "🤖",
        "title": "AI automation for everyone",
        "short": "AI Automation",
        "meta": "AI automation for individuals and businesses: chatbots, document and email processing, reports and workflow automation. How it works, use cases and pricing explained.",
        "tagline": "Stop doing the same task by hand. Let AI and automation do it.",
        "intro": "If a task is repetitive, rule-based or involves reading and writing text, it can usually be automated. I build practical automations around AI models and your existing tools, so the result saves real hours rather than being a demo.",
        "who": "Individuals who want to save time, small businesses drowning in manual admin, and teams that want an AI assistant over their own documents or data.",
        "gets": [
            "Customer support and website chatbots trained on your own content",
            "Email, document and invoice processing: read, extract, sort and file automatically",
            "Report and summary generation from your data (spreadsheets, databases, ERP)",
            "Workflow automation across your tools: forms, CRM, Google Sheets, WhatsApp, email, accounting",
            "Content helpers: product descriptions, translations, social posts with human review",
            "Training on how to use and maintain what I build",
        ],
        "steps": [
            ("Find the work", "We list your repetitive tasks and pick the ones with the biggest time savings."),
            ("Prototype", "I build a small working version quickly so you can test it on real examples."),
            ("Build & connect", "I harden it, connect it to your systems and add checks for wrong answers."),
            ("Hand over", "Documentation and a walkthrough, with optional ongoing support."),
        ],
        "factors": [
            "How many steps and systems the automation touches",
            "Quality of the source data (clean tables versus messy scans)",
            "Need for human approval steps and error handling",
            "Running costs: AI model usage and any automation platform fees are paid to those providers, separate from my fee",
            "One-off build versus ongoing maintenance",
        ],
        "packages": [
            ("Single automation", "One well-defined workflow or chatbot, built, tested and handed over.", Q),
            ("Automation bundle", "Several connected automations or a custom assistant over your documents and data.", Q),
            ("Ongoing partner", "Monitoring, improvements and new automations as your needs grow.", Q),
        ],
        "faq": [
            ("Is my data safe?", "I choose tools to match your sensitivity, and can use options that don't train on your data. Tell me what's confidential and I'll design around it."),
            ("Will AI make mistakes?", "Sometimes, so I add validation and human-approval steps where errors would be costly."),
            ("Do I need technical skills?", "No. I build it and show you how to use it."),
        ],
    },
    {
        "slug": "api-integration",
        "icon": "🔌",
        "title": "API integration",
        "short": "API Integration",
        "meta": "API integration services: REST and GraphQL, Stripe, PayPal, QuickBooks, Google Maps, social login, ERP and eCommerce sync. Process, scope and pricing explained.",
        "tagline": "Make your systems talk to each other, so nobody re-types data.",
        "intro": "Most businesses run several tools that don't share data. I connect them through their APIs, build custom APIs where none exist, and make the connection reliable with retries, logging and error handling.",
        "who": "Shops that need orders to flow into accounting or ERP, apps that need payments or maps, and companies that want one system as the source of truth.",
        "gets": [
            "Payment gateways: Stripe, PayPal and others, with webhooks and refunds",
            "Accounting and ERP: QuickBooks, Dynamics 365 F&O, Dolibarr, Magento, WooCommerce",
            "Social login and SSO: Google, Facebook, SAML, OAuth",
            "Google Maps, SMS, email (SMTP), push notifications and other third-party services",
            "Custom REST or GraphQL APIs for your own app or mobile app",
            "Documentation, monitoring and error alerts so failures don't go unnoticed",
        ],
        "steps": [
            ("Map the data", "We define what moves from where to where, and what triggers it."),
            ("Build", "I implement the integration with secure credential handling."),
            ("Test", "Edge cases, failures and duplicates are tested in a sandbox before going live."),
            ("Go live & monitor", "Deploy, watch the first runs, and hand over documentation."),
        ],
        "factors": [
            "Quality and limits of the APIs involved (some are well documented, some are not)",
            "Number of systems and data types to sync, and one-way versus two-way sync",
            "Volume and need for real-time versus scheduled sync",
            "Security and compliance needs, especially for payments",
            "Whether a custom API must be built first",
        ],
        "packages": [
            ("Single integration", "Connect two systems or add one service (for example payments or maps).", Q),
            ("Multi-system sync", "Several systems with two-way sync, queueing and error handling.", Q),
            ("Custom API + integrations", "Design and build your own API plus the integrations around it.", Q),
        ],
        "faq": [
            ("Do third-party services charge extra?", "Often yes (payment fees, API plans). Those go to the provider, separate from my fee."),
            ("What if an API changes later?", "I can maintain the integration under a support arrangement."),
            ("Can you integrate a system with no API?", "Sometimes, using exports, database access or other methods. We'd discuss feasibility first."),
        ],
    },
    {
        "slug": "mobile-app-for-website",
        "icon": "📱",
        "title": "Mobile app for any website",
        "short": "Mobile App for Your Website",
        "meta": "Turn your website or web app into a native Android and iOS app with Ionic and Capacitor, with push notifications, offline mode and Play Store / App Store publishing. Process and pricing explained.",
        "tagline": "Put your business on your customers' home screen.",
        "intro": "I turn your existing website or web application into a real Android and iOS app using Ionic, Angular and Capacitor. I have published 10+ Android and 5+ iOS apps and managed store accounts for clients, so I handle the full path from code to Play Store and App Store.",
        "who": "Businesses with a website, store or portal that want an app for engagement, push notifications, or because customers expect one.",
        "gets": [
            "Android and iOS app from one codebase (Ionic, Angular, Capacitor)",
            "Native features: push notifications, camera, QR scanner, location, offline storage, deep links",
            "Login and API connection to your existing website or backend",
            "App icon, splash screen and store listing assets",
            "Publishing: Google Play Console and Apple App Store Connect setup and submission",
            "Updates and support after launch",
        ],
        "steps": [
            ("Scope", "We decide the screens and features. A simple wrapper app is cheaper than a fully native-feeling app."),
            ("Design & build", "I build the app, connecting it to your site or API."),
            ("Test", "On real Android and iOS devices, with your feedback in rounds."),
            ("Publish", "I prepare and submit to the stores, and handle review feedback."),
        ],
        "factors": [
            "Wrapper of your site versus a properly designed app with native screens",
            "Number of screens and features (push, offline, payments, maps)",
            "Whether a backend or API already exists or must be built",
            "Android only or Android and iOS",
            "Store fees (Google Play one-time fee, Apple yearly developer fee) are paid by you to the stores",
        ],
        "packages": [
            ("Website app (wrapper)", "Your website packaged as an app with icon, splash and push notifications, published to the stores.", Q),
            ("Custom app", "A designed Ionic app with native-feeling screens, API connection and offline support.", Q),
            ("App + backend", "Mobile app plus the API and admin panel it needs.", Q),
        ],
        "faq": [
            ("Will Apple accept a simple website wrapper?", "Apple requires apps to offer more than a plain website. I add real app features such as notifications, offline use or native screens to meet the guidelines. Approval is Apple's decision."),
            ("Who owns the app and store accounts?", "You do. I can set up the accounts in your name."),
            ("Can you update my existing app?", "Yes, I can take over and improve existing Ionic and Angular apps."),
        ],
    },
    {
        "slug": "web-development",
        "icon": "💻",
        "title": "Custom websites & web apps",
        "short": "Web Development",
        "meta": "Custom website and web application development with Laravel, PHP, Angular and WordPress: dashboards, portals, booking systems and admin panels. Process and pricing explained.",
        "tagline": "Fast, secure web applications built for how your business actually works.",
        "intro": "From a business website to a full web application with logins, dashboards and payments, I build with Laravel, PHP, Angular and WordPress, with security, speed and maintainability in mind from the start.",
        "who": "Businesses that need a website, an internal tool, a customer portal or a custom system that off-the-shelf software doesn't cover.",
        "gets": [
            "Business websites and landing pages, mobile-friendly and SEO-ready",
            "Custom web apps: dashboards, portals, booking, inventory, reporting, admin panels",
            "WordPress themes and plugins, and CodeIgniter extensions",
            "Secure authentication, roles and permissions, and payment integration",
            "Hosting setup, deployment and training",
            "Source code you own",
        ],
        "steps": [
            ("Requirements", "We write down what the system must do and who uses it."),
            ("Design & build", "I build in milestones so you see progress and can steer."),
            ("Test & launch", "Testing, security checks, deployment and data migration."),
            ("Support", "Fixes and improvements after launch."),
        ],
        "factors": [
            "Number of pages, features and user roles",
            "Custom design versus a ready template",
            "Integrations (payments, maps, ERP, email)",
            "Data migration from an old system",
            "Hosting and domain costs, which are paid to the providers",
        ],
        "packages": [
            ("Business website", "A fast, mobile-friendly site with SEO basics and a contact form.", Q),
            ("Web application", "A custom app with logins, roles and a dashboard, built to your requirements.", Q),
            ("Full system", "Larger multi-module platform with integrations, reports and mobile app.", Q),
        ],
        "faq": [
            ("Do I own the code?", "Yes, on final payment you own the source code."),
            ("Can you fix or extend my existing site?", "Yes. I regularly take over and improve existing PHP, Laravel and WordPress projects."),
            ("Can you handle hosting?", "Yes, I can set up hosting and deployment on Azure, AWS, Linux servers or cPanel/Plesk."),
        ],
    },
    {
        "slug": "erp-dynamics-365",
        "icon": "🏢",
        "title": "ERP & Dynamics 365 F&O",
        "short": "ERP & Dynamics 365",
        "meta": "Microsoft Dynamics 365 Finance & Operations X++ development, SSRS reports, Power BI dashboards, integrations and deployment. Also Dolibarr and Magento. Scope and pricing explained.",
        "tagline": "Customize your ERP to fit your business, not the other way round.",
        "intro": "With 6+ years in enterprise ERP, I develop and customize Microsoft Dynamics 365 Finance & Operations in X++, build reports and dashboards, and integrate the ERP with the rest of your systems. I also work with Dolibarr and Magento.",
        "who": "Companies running or implementing Dynamics 365 F&O, and smaller businesses that need Dolibarr or an ERP-connected online store.",
        "gets": [
            "X++ customization and extensions in D365 F&O (forms, tables, classes, workflows, data entities)",
            "SSRS reports and Power BI dashboards for finance and operations",
            "Integrations with eCommerce, payments, banks and other systems",
            "Deployments, LCS environment management and Azure DevOps pipelines",
            "Dolibarr ERP modules for finance, invoicing and inventory",
            "Magento stores connected to ERP to automate orders",
        ],
        "steps": [
            ("Analyze", "Understand the business process and the standard functionality gap."),
            ("Develop", "Build extensions the Microsoft-recommended way, so upgrades stay safe."),
            ("Test", "Unit and user testing in a non-production environment."),
            ("Deploy & support", "Package and deploy, then support go-live."),
        ],
        "factors": [
            "Size and complexity of the customization or report",
            "Number of integrations and data entities",
            "Environment access and deployment process on your side",
            "Fixed-scope task versus a part-time or ongoing arrangement",
        ],
        "packages": [
            ("Single task", "A defined customization, report or dashboard.", Q),
            ("Project", "A set of customizations or integrations delivered through to deployment.", Q),
            ("Ongoing developer", "Part-time or retained support for your D365 environment.", Q),
        ],
        "faq": [
            ("Do you work with partners and consultancies?", "Yes, I can work as a subcontracted developer."),
            ("Do you need access to our environment?", "Yes, access per your security policy, or work through your team."),
            ("Do you do functional consulting?", "My focus is development, reports and integrations, with business-process understanding behind them."),
        ],
    },
    {
        "slug": "performance-hosting",
        "icon": "⚡",
        "title": "Performance & hosting",
        "short": "Performance & Hosting",
        "meta": "Website speed optimization, server setup, deployment, SSL, backups and cloud hosting on Azure, AWS, Linux and IIS. Scope and pricing explained.",
        "tagline": "A fast site that stays online, with backups for the day something breaks.",
        "intro": "Slow or unstable sites lose customers and rankings. I set up and tune servers, deploy your application properly, and make sure SSL, backups and monitoring are in place.",
        "who": "Owners of slow websites, businesses moving hosts, and teams that need a clean deployment setup.",
        "gets": [
            "Speed audit and optimization: caching, compression, images, database queries",
            "Server setup and hardening on Linux, Windows/IIS, cPanel and Plesk",
            "Cloud hosting on Azure, AWS and GCP",
            "SSL/TLS certificates and security headers",
            "Automated backups and a tested restore process",
            "Deployment pipelines and website or server migration with minimal downtime",
        ],
        "steps": [
            ("Assess", "Measure current speed, uptime and server setup."),
            ("Improve", "Apply optimizations and fix configuration problems."),
            ("Migrate / deploy", "Move or deploy with a rollback plan."),
            ("Monitor", "Uptime monitoring and alerts."),
        ],
        "factors": [
            "Current hosting and size of the site or database",
            "Whether you are optimizing in place or migrating",
            "Number of servers, environments and domains",
            "Hosting provider fees, which are separate from my fee",
        ],
        "packages": [
            ("Speed tune-up", "Audit and optimization of an existing site.", Q),
            ("Setup / migration", "New server setup or move to new hosting with SSL and backups.", Q),
            ("Managed hosting care", "Ongoing updates, monitoring and backups.", Q),
        ],
        "faq": [
            ("Will my site go down during migration?", "I plan migrations to avoid or minimize downtime, with a rollback if needed."),
            ("Can you work with my current host?", "Yes, as long as I can get the access needed."),
            ("Do you sell hosting?", "I set up and manage hosting on providers of your choice; you hold the account."),
        ],
    },
    {
        "slug": "maintenance-support",
        "icon": "🧰",
        "title": "Maintenance & support",
        "short": "Maintenance & Support",
        "meta": "Website and mobile app maintenance and support: bug fixes, updates, monitoring and ongoing improvements. Plans and pricing explained.",
        "tagline": "Keep what you've built running, secure and up to date.",
        "intro": "Websites and apps need regular care: software updates, security patches, store compliance changes and the occasional bug. I take that off your plate under a simple support arrangement.",
        "who": "Owners of existing websites and apps, including ones built by someone else, who want a reliable developer on call.",
        "gets": [
            "Bug fixes and small improvements",
            "Framework, plugin and dependency updates",
            "Security patches and backups",
            "Mobile app updates for new Android and iOS requirements and store re-submissions",
            "Uptime and error monitoring",
            "Priority response when something breaks",
        ],
        "steps": [
            ("Review", "I look over your site or app and document how it works."),
            ("Stabilize", "Fix urgent issues and set up backups and monitoring."),
            ("Maintain", "Regular updates and a set amount of support time."),
            ("Improve", "Use spare time on improvements you choose."),
        ],
        "factors": [
            "Number and complexity of sites or apps",
            "Response time you need",
            "Hours of support per month",
            "Condition of the existing code",
        ],
        "packages": [
            ("Pay as you go", "Hourly or per-task fixes whenever needed.", Q),
            ("Monthly plan", "A set number of support hours, updates and monitoring each month.", Q),
            ("Priority plan", "Faster response and more hours for business-critical systems.", Q),
        ],
        "faq": [
            ("Can you take over a project built by someone else?", "Yes. I start with a review so I know what I'm taking on."),
            ("What if I need only occasional help?", "Pay-as-you-go works fine."),
            ("Do you offer 24/7 support?", "I don't offer round-the-clock cover. Ask about response times for your needs."),
        ],
    },
]

CSS_LINKS = '''  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../../assets/site/site.css">'''

THEME_JS = '''  <script>
    try { var t = localStorage.getItem("theme"); if (t) document.documentElement.setAttribute("data-theme", t);
      else if (matchMedia("(prefers-color-scheme: light)").matches) document.documentElement.setAttribute("data-theme", "light"); } catch (e) {}
  </script>'''

WA_LINK = f"https://wa.me/{WA}?text=" + "Hi%20Zia%2C%20I'm%20interested%20in%20your%20services."


def header():
    return f'''  <a class="skip" href="#main">Skip to content</a>
  <header class="nav">
    <div class="wrap">
      <a class="brand" href="../../" aria-label="Zia Ur Rehman, home"><span class="brand-mark">ZR</span>Zia Ur Rehman</a>
      <nav class="nav-links" id="nav-links" aria-label="Primary">
        <a href="../../#services">All services</a>
        <a href="../../#projects">Projects</a>
        <a href="../../resume.html">Resume</a>
        <a href="../../#contact">Contact</a>
      </nav>
      <div style="display:flex;gap:.5rem">
        <button class="icon-btn" id="theme-toggle" type="button" aria-label="Toggle light/dark theme">◐</button>
        <button class="icon-btn menu-btn" id="menu-btn" type="button" aria-label="Menu" aria-expanded="false" aria-controls="nav-links">☰</button>
      </div>
    </div>
  </header>'''


def contact_buttons():
    return f'''<a class="btn btn-primary" href="tel:{TEL}">📞 Call {e(PHONE)}</a>
            <a class="btn btn-ghost" href="{WA_LINK}" target="_blank" rel="noopener noreferrer">WhatsApp ↗</a>
            <a class="btn btn-ghost" href="mailto:{EMAIL}">Email</a>'''


def page(s):
    url = f"{BASE}/services/{s['slug']}/"
    lis = "\n".join(f"          <li>{e(x)}</li>" for x in s["gets"])
    steps = "\n".join(
        f'          <div class="feat"><div class="step-n">{i}</div><h3>{e(t)}</h3><p>{e(d)}</p></div>'
        for i, (t, d) in enumerate(s["steps"], 1)
    )
    factors = "\n".join(f"          <li>{e(x)}</li>" for x in s["factors"])
    pk = "\n".join(
        f'''          <div class="price-card"><h3>{e(n)}</h3><div class="price">{e(p)}</div><p>{e(d)}</p>
            <a class="btn btn-ghost" href="mailto:{EMAIL}?subject={e(s["short"])}%20-%20{e(n)}">Ask for a quote</a></div>'''
        for n, d, p in s["packages"]
    )
    faq = "\n".join(
        f'          <details class="faq"><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q, a in s["faq"]
    )
    others = "\n".join(
        f'          <a class="chip" href="../{o["slug"]}/">{o["icon"]} {e(o["short"])}</a>' for o in SERVICES if o["slug"] != s["slug"]
    )
    import json
    ld = json.dumps({
        "@context": "https://schema.org", "@type": "Service", "name": s["title"], "description": s["meta"],
        "url": url, "areaServed": "Worldwide",
        "provider": {"@type": "Person", "name": "Zia Ur Rehman", "url": BASE + "/", "telephone": PHONE, "email": EMAIL},
    }, ensure_ascii=False)
    faq_ld = json.dumps({
        "@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in s["faq"]],
    }, ensure_ascii=False)
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{e(s["title"])} | Zia Ur Rehman</title>
  <meta name="description" content="{e(s["meta"])}">
  <meta name="theme-color" content="#0b1018">
  <link rel="canonical" href="{url}">
  <link rel="icon" type="image/svg+xml" href="../../assets/site/favicon.svg">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{e(s["title"])} | Zia Ur Rehman">
  <meta property="og:description" content="{e(s["meta"])}">
  <meta property="og:url" content="{url}">
{THEME_JS}
{CSS_LINKS}
  <script type="application/ld+json">{ld}</script>
  <script type="application/ld+json">{faq_ld}</script>
</head>
<body id="top">
{header()}

  <main id="main">
    <div class="pkg-hero">
      <div class="wrap">
        <div class="crumbs"><a href="../../">Home</a> / <a href="../../#services">Services</a> / {e(s["short"])}</div>
        <div style="max-width:46rem;position:relative">
          <div class="s-icon" aria-hidden="true" style="margin-bottom:1rem">{s["icon"]}</div>
          <h1>{e(s["title"])}</h1>
          <p class="lead">{e(s["tagline"])}</p>
          <div class="cta-row">
            {contact_buttons()}
          </div>
        </div>
      </div>
    </div>

    <section class="alt">
      <div class="wrap about">
        <div><span class="eyebrow">Overview</span><h2>What this is</h2></div>
        <div>
          <p>{e(s["intro"])}</p>
          <p><b style="color:var(--text)">Who it's for:</b> {e(s["who"])}</p>
        </div>
      </div>
    </section>

    <section>
      <div class="wrap">
        <div class="sec-head"><div><span class="eyebrow">Scope</span><h2>What you get</h2></div></div>
        <ul class="pts check">
{lis}
        </ul>
      </div>
    </section>

    <section class="alt">
      <div class="wrap">
        <div class="sec-head"><div><span class="eyebrow">Process</span><h2>How it works</h2></div></div>
        <div class="feat-grid">
{steps}
        </div>
      </div>
    </section>

    <section id="pricing">
      <div class="wrap">
        <div class="sec-head"><div><span class="eyebrow">Cost</span><h2>Pricing &amp; what affects it</h2></div></div>
        <p class="lead" style="max-width:48rem">Every project is different, so I quote per project instead of using a one-size price list. Tell me what you need and I'll reply with a fixed price or a clear estimate, so there are no surprises. Typical engagement types:</p>
        <div class="price-grid">
{pk}
        </div>
        <h3 style="margin:2.2rem 0 .8rem">What affects the cost</h3>
        <ul class="pts">
{factors}
        </ul>
        <div class="note">Third-party costs (hosting, domains, app store fees, API or AI usage, paid plugins) are paid by you directly to those providers and are not part of my fee.</div>
      </div>
    </section>

    <section class="alt">
      <div class="wrap">
        <div class="sec-head"><div><span class="eyebrow">Questions</span><h2>FAQ</h2></div></div>
        <div class="faq-list">
{faq}
        </div>
      </div>
    </section>

    <section>
      <div class="wrap">
        <div class="contact-box">
          <span class="eyebrow">Get started</span>
          <h2>Let's talk about your project.</h2>
          <p>Call, message on WhatsApp or email me with a short description. I'll reply with questions and a quote.</p>
          <div class="cta-row">
            {contact_buttons()}
          </div>
        </div>
        <h3 style="margin:2.5rem 0 .8rem">Other services</h3>
        <div class="chips">
{others}
        </div>
      </div>
    </section>
  </main>

  <footer>
    <div class="wrap">
      <span>© <span id="year">2026</span> Zia Ur Rehman · Riyadh, Saudi Arabia</span>
      <a href="../../">← Back to portfolio</a>
    </div>
  </footer>

  <script src="../../assets/site/data.js"></script>
  <script src="../../assets/site/site.js"></script>
</body>
</html>
'''


def main():
    for s in SERVICES:
        d = os.path.join(ROOT, "services", s["slug"])
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "index.html"), "w", encoding="utf-8", newline="\n") as f:
            f.write(page(s))
    # sitemap entries (idempotent)
    for fn, fmt in (("sitemap.txt", "{u}\n"),
                    ("sitemap.xml", "  <url>\n    <loc>{u}</loc>\n    <lastmod>" + LASTMOD + "</lastmod>\n  </url>\n")):
        p = os.path.join(ROOT, fn)
        txt = open(p, encoding="utf-8").read()
        add = ""
        for s in SERVICES:
            u = f"{BASE}/services/{s['slug']}/"
            if u not in txt:
                add += fmt.format(u=u)
        if add:
            if fn.endswith(".xml"):
                txt = txt.replace("</urlset>", add + "</urlset>")
            else:
                txt = txt.rstrip("\n") + "\n" + add
            open(p, "w", encoding="utf-8", newline="\n").write(txt)
    print("built", len(SERVICES), "pages")


if __name__ == "__main__":
    main()
