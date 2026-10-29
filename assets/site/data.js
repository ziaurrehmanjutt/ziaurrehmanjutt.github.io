/* ------------------------------------------------------------------
   Single source of truth for index.html and resume.html.
   To add a project: copy a block inside PROJECTS and edit it. That's it.
   ------------------------------------------------------------------ */
window.SITE = {
  name: "Zia Ur Rehman",
  title: "Senior Software Developer",
  tagline: "Enterprise ERP, full-stack web & cross-platform mobile.",
  location: "Riyadh, Saudi Arabia",
  email: "ziaa520@gmail.com",
  phone: "+966 500256094",          // shown on resume.html only
  github: "https://github.com/ziaurrehmanjutt",
  linkedin: "https://linkedin.com/in/ziaa520",  // hidden if left empty
  summary:
    "Software developer with 6+ years of experience delivering enterprise ERP, web, and mobile solutions. " +
    "Specialized in Microsoft Dynamics 365 Finance & Operations (X++), PHP/Laravel, and cross-platform mobile apps with Ionic and Angular. " +
    "Experienced in system integrations, cloud deployment, performance optimization, and the full software development lifecycle.",

  stats: [
    { value: "6+", label: "Years building software" },
    { value: "10+", label: "Android apps published" },
    { value: "5+", label: "iOS apps published" },
    { value: "4–5", label: "Client store accounts managed" }
  ],

  skills: [
    { group: "Languages", items: ["PHP", "C#", "JavaScript", "TypeScript", "SQL", "X++", "Python", "C++"] },
    { group: "Web", items: ["Laravel", "ASP.NET", "CodeIgniter", "WordPress", "Angular", "Vue.js", "Inertia.js", "Bootstrap", "Tailwind CSS", "jQuery"] },
    { group: "Mobile", items: ["Ionic (Capacitor & Cordova)", "Android", "iOS", "App Store Connect", "Google Play Console"] },
    { group: "ERP & Commerce", items: ["Dynamics 365 F&O (X++)", "Magento", "Dolibarr ERP", "WooCommerce"] },
    { group: "Reporting", items: ["SSRS", "Power BI", "Data Visualization", "Business Reporting"] },
    { group: "Data", items: ["SQL Server", "MySQL", "Firebase", "Elasticsearch"] },
    { group: "Cloud & Infra", items: ["Azure", "AWS", "GCP", "Linux Servers", "Windows Servers", "IIS", "Plesk", "cPanel"] },
    { group: "Auth & Security", items: ["SAML", "SSO", "OAuth", "RBAC", "SSL/TLS"] },
    { group: "APIs & Integrations", items: ["REST", "GraphQL", "Stripe", "PayPal", "QuickBooks", "Google Maps", "Social Auth"] },
    { group: "Tools & DevOps", items: ["Git", "GitHub", "Azure DevOps", "Docker", "Composer", "npm", "Webpack", "Postman"] },
    { group: "Other", items: ["SEO", "Google Analytics", "Search Console", "SMTP", "Cron Jobs", "System Administration"] }
  ],

  experience: [
    {
      company: "King Saud University",
      via: "via 2P Perfect Presentation",
      role: "Software Developer",
      place: "Riyadh, Saudi Arabia",
      period: "2026 – Present",
      points: [
        "Develop and maintain internal enterprise applications and digital platforms using Laravel, PHP, JavaScript, and modern web technologies.",
        "Design and implement RESTful APIs for web and mobile apps, integrating university systems with third-party services.",
        "Build and maintain cross-platform mobile apps with Ionic and Angular for internal university operations.",
        "Implement centralized authentication with SAML and Single Sign-On across multiple systems.",
        "Develop Python tools and automation to streamline business processes, reporting, and data management.",
        "Build custom dashboards, reporting systems, and administrative portals for university departments.",
        "Handle deployment, troubleshooting, performance optimization, and monitoring; take part in architecture, code reviews, and documentation."
      ]
    },
    {
      company: "IIBTech",
      role: "D365 F&O X++ Developer",
      place: "Gujrat, Pakistan",
      period: "2019 – 2026",
      points: [
        "Developed and customized modules in Microsoft Dynamics 365 Finance & Operations using X++.",
        "Built and managed SSRS reports, Power BI dashboards, and system integrations.",
        "Handled deployments, LCS environment management, and Azure DevOps pipelines.",
        "Delivered production-ready D365 F&O customizations that improved business processes."
      ],
      tracks: [
        {
          role: "Hybrid Mobile Application Developer",
          points: [
            "Developed and published 10+ Android and 5+ iOS apps using Ionic (Capacitor & Cordova) with Angular.",
            "Managed Google Play and Apple Developer accounts for 4–5 clients.",
            "Integrated APIs, authentication, push notifications, and offline storage."
          ]
        },
        {
          role: "PHP / Laravel Developer",
          points: [
            "Built Laravel web applications with secure authentication and payment integrations.",
            "Created custom WordPress plugins and themes; extended CodeIgniter.",
            "Built dashboards and reporting modules while optimizing backend processes."
          ]
        },
        {
          role: "ERP & eCommerce Developer",
          points: [
            "Configured Magento stores with custom themes and extensions.",
            "Implemented Dolibarr ERP modules for finance, invoicing, and inventory.",
            "Integrated ERP with eCommerce to automate order processing and cut manual effort."
          ]
        },
        {
          role: "ASP.NET Website & Desktop Developer",
          points: [
            "Created web and desktop applications in C# with ASP.NET and Windows Forms.",
            "Developed internal tools and integrations to streamline business operations."
          ]
        }
      ]
    }
  ],

  education: [
    { degree: "Master of Computer Science (MCS)", school: "PMAS-Arid Agriculture University, Rawalpindi, Pakistan", period: "2017 – 2019" }
  ],

  /* category: "mobile" | "web" | "erp" | "tool"  (filter chips are built from these)
     links: any of { live, code }  */
  projects: [
    {
      title: "DiyaQR",
      category: "mobile",
      featured: true,
      year: "2026",
      description: "Fast, beautiful QR scanner and generator. Create QR codes for links, Wi-Fi, contacts, events and locations, style them, and save or share. Landing pages in 11 languages.",
      tags: ["Ionic", "Angular", "Android", "iOS"],
      links: { live: "diyaqr/" }
    },
    {
      title: "Diya Expense",
      category: "mobile",
      featured: true,
      year: "2026",
      description: "Private, offline budget and expense tracker. Budgets, savings goals, loans, invoices, installments, recurring reminders, receipt photos and CSV export. No account, no ads. Landing pages in 12 languages.",
      tags: ["Ionic", "Angular", "Android", "SQLite"],
      links: { live: "diyaexpense/" }
    },
    {
      title: "QR Code Generator",
      category: "mobile",
      description: "An Ionic mobile app for managing and generating QR codes.",
      tags: ["Ionic", "Angular"],
      links: { code: "https://github.com/ziaurrehmanjutt/qr-code-generate-app" }
    },
    {
      title: "Accessibility Widget",
      category: "tool",
      description: "A standalone JavaScript widget that adds accessibility controls to any website.",
      tags: ["JavaScript", "A11y"],
      links: { code: "https://github.com/ziaurrehmanjutt/standalone-accessibility-widget" }
    },
    {
      title: "Scoreboard App",
      category: "web",
      description: "An interactive scoreboard experience built with TypeScript.",
      tags: ["TypeScript"],
      links: { code: "https://github.com/ziaurrehmanjutt/scoreboard-app" }
    },
    {
      title: "Certificate Generator",
      category: "web",
      description: "Generate certificates in bulk with the Laravel ecosystem.",
      tags: ["Laravel", "PHP"],
      links: { code: "https://github.com/ziaurrehmanjutt/certificates-genrate-laravel" }
    }
  ]
};
