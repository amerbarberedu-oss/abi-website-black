# American Barber Institute (ABI) — Website

New York's only dedicated barber school (est. 1996). This repository contains the
complete marketing website: a fast, zero-framework static site generated from Python,
served on Vercel, in English and Spanish.

- **Canonical domain:** https://www.abi.edu
- **Current version:** 0.5.0 (2026-07-14)

## Ownership

| | Details |
|---|---|
| **Owner** | Alex — American Barber Institute |
| **GitHub Account** | [amerbarberedu-oss](https://github.com/amerbarberedu-oss) |
| **Vercel Account** | amerbarberedu-oss-projects |
| **Domain** | abi.edu / www.abi.edu |
| **Repository** | amerbarberedu-oss/abi-website-black |

> This entire website, repository, domain, and Vercel deployment belongs to
> **Alex / American Barber Institute**. All code, assets, and configurations
> are owned by the ABI organization.

---

## 0. Recent Changes

### 0.5.1 (2026-07-16) — GHL Form Re-mapping (per-campus lead forms)

- **GoHighLevel Form Re-mapping** — Split the lead forms so each surface has its own GHL form (all redirect to `/thank-you`, so `generate_lead` still fires reliably via `analytics.js`):
  - Main site EN (index, contact, jobs, bronx) → `WZjNHh9wcd1FTnlj0eCR` ("edu")
  - Main site ES (`es/*`) → `jqLpg40sM8C7RFT7Iq2Z` ("edu - ESP")
  - Manhattan funnel EN → `2FvHzLvYji1iSmNmCP46`; ES → `WXaur2ngXql4GTamJQOx`
  - Bronx funnel EN → `v1SNzWsAZZVodCsnsDbe`; ES → `z2ZXZPbcGx7u1XrAl6Zu`
  - Funnel IDs are driven by `landing-funnels/src/build.py` (`_GHL_FORMS`, keyed by campus+language).

### 0.5.0 (2026-07-14) — GHL Form Migration, Mobile Navbar & Android Gesture Clearances

- **GoHighLevel Form Migration** — Replaced all legacy campus GHL form embeds across English pages (index, contact, jobs, Manhattan/Bronx campaigns) with the new two-column English form ID (`3ghObGjHiLN3LgKBfKGG`) and Spanish equivalents with the Spanish form ID (`WZjNHh9wcd1FTnlj0eCR`).
- **Animated Form Skeletons** — Integrated pulsing SVG-animated form skeleton placeholders inside `.ghl-form-wrap` to cover up the blank white spacing while the external GHL scripts render the frames.
- **Android & S25 Ultra Gesture Bar safety** — Increased bottom padding on mobile sticky bars (`.mobile-cta` and `.lf-mcta`) to `calc(18px + env(safe-area-inset-bottom, 0px))` to prevent Android system home/back buttons or gestural lines from clipping/overlapping the CTA controls. Increased body margin-bottom to clear the bars.
- **Compact Mobile Language Switcher** — Shrunk the mobile `EN` | `ES` switcher text and padding sizes under `430px` viewport widths (`.66rem` font-size) so that the full campus location names ("Manhattan" and "Bronx") fit cleanly on narrow mobile nav headers without line wraps. Enforced `white-space: nowrap` on CTA buttons to prevent text breaking.
- **Campaign Spacing & Switcher Themes** — Closed vertical padding gaps between the form and Student Voices carousel. Rewrote language toggles to dynamically color-match the active campus colors (gold/orange on Bronx, blue on Manhattan).
- **CTA Scroll Anchors** — Fixed self-referencing "Apply Now" CTA buttons to anchor-scroll to `#reserve` forms.
- **Cache-Bust versions** — Bumped CSS query version strings to force update delivery (`style.css?v=34`, `landing.css?v=158`, `funnels.css?v=64`).

### 0.4.0 (2026-07-11) — Campus Phone System, Gold Theme, Cleanup

- **Campus-specific phone numbers** — Manhattan shows 2 numbers (EN + ES) + haircut; Bronx shows 1 number + haircut. Dynamic switching via `data-campus-phone` attributes across topbar, MHX bar, footer, and call sheet.
- **Gold theme** — 109 `body.bx-gold` CSS override rules for Bronx campus, smooth crossfade transitions.
- **SEO/AEO audit** — 17/17 checks passing, structured data, meta descriptions ≤155 chars.
- **Code cleanup** — removed dead SVG constants, unused image assets (2.5MB), stale CSS comments. Comprehensive JSDoc comments on all `campus.js` functions.
- **Landing funnel CSS sync** — all cache-bust versions unified (landing.css v153, funnels.css v59, campus.js v5).

### 0.3.0 (2026-07-09) — Responsive, i18n & Role Split

- Mobile responsiveness overhaul — bulletproof hamburger menu using `min()` clamping.
- Full Spanish translation — all `/es/` pages.
- Google rating standardized to 4.1.

### 0.2.0 (2026-07-07) — Campus Context Routing

- Campus-specific programs pages: `/programs/manhattan` and `/programs/bronx`.
- `campus.js` rewrites Programs nav links per campus context.

---

## 1. Team & Developer Roles — STRICTLY ENFORCED

| Role | Person | Responsibilities |
|---|---|---|
| **Owner** | Alex (American Barber Institute) | Business owner. All assets, accounts, and domain belong to Alex. |
| **Developer** | Kazi | Frontend, UI/UX, HTML/CSS/JS, SEO, build scripts |
| **Developer** | Arhum Abdullah | GA4, GTM, Google Ads, Meta Pixel, Clarity, CallRail, ClickCease, Vercel Analytics, consent mode, CSP analytics domains |

> ⚠️ **Do NOT modify** `assets/js/analytics.js`, GTM/GA4/Ads/Pixel config, or CSP analytics domains without Arhum's sign-off.
>
> All deployments, GitHub pushes, and Vercel deploys go through **Alex's accounts only** (`amerbarberedu-oss`).

---

## 2. Architecture

A fully static website — plain HTML, CSS and vanilla JavaScript — produced by Python
generators. **No runtime framework, no build toolchain, no Node dependency.**

```
abi-website/
├── README.md
├── CHANGELOG.md
├── vercel.json              ← Vercel routing (clean URLs, security headers, redirects)
├── robots.txt               ← crawler directives
├── sitemap.xml              ← generated sitemap (with lastmod)
├── llms.txt                 ← guidance for AI search engines / LLMs
│
│   ── Built HTML pages (DO NOT hand-edit; rebuilt by generators) ──
├── index.html               ← English homepage ("/")
├── bronx.html               ← Bronx campus homepage
├── about.html  contact.html  faq.html  instructors.html  ...
├── programs/                ← program pages (manhattan, bronx, 500h, 50h, etc.)
├── blog/                    ← blog articles + index
├── es/                      ← Spanish mirror (all pages)
├── barber-school-*.html     ← location-specific landing pages
├── thank-you.html           ← form submission confirmation
│
├── landing-funnels/         ← ad campaign landing pages
│   ├── 500-hours-master-barber-program-landing-page/
│   ├── master-barber-program-bronx/
│   └── src/build.py         ← landing funnel generator
│
├── assets/
│   ├── css/
│   │   ├── style.css        ← base styles
│   │   ├── brand.css        ← theme tokens
│   │   ├── landing.css      ← components + gold theme overrides (v158)
│   │   ├── effects.css      ← motion/animations
│   │   ├── upgrade.css      ← upgrade layer
│   │   └── funnels.css      ← landing funnel styles (v64)
│   ├── js/
│   │   ├── main.js          ← countdown, nav, core interactivity
│   │   ├── campus.js        ← Manhattan ↔ Bronx switcher (v5)
│   │   ├── landing.js       ← homepage-specific JS
│   │   ├── effects.js       ← scroll-reveal, 3D tilt
│   │   ├── upgrade.js       ← upgrade layer
│   │   ├── video-sound.js   ← video hover sound
│   │   └── analytics.js     ← ⚠️ ARHUM ONLY — consent + GTM loader
│   └── img/                 ← photos, logo, favicon, gallery/
│
├── src/                     ← SOURCE (never served)
│   ├── build.py             ← main site generator (115 pages)
│   ├── build_landing_pages.py ← landing page generator
│   ├── serve.py             ← local dev server (localhost:8000)
│   ├── blog_manifest.json   ← blog post registry
│   └── pages/               ← content partials (edit these)
│       ├── index.html       ← homepage content
│       ├── es-index.html    ← Spanish homepage content
│       ├── thank-you.html   ← thank-you page content
│       └── ...
│
└── .agents/
    └── PROJECT_STATE.md     ← multi-agent handover state
```

---

## 3. Campus System

The site supports two campuses with dynamic switching:

| | Manhattan (Default) | Bronx (Gold Theme) |
|---|---|---|
| **Admissions EN** | (212) 290-2289 | (718) 676-0640 |
| **Admissions ES** | (212) 290-0278 | — |
| **Haircut** | (856) 316-1551 | (856) 316-1551 |
| **Theme** | Blue | Gold (`body.bx-gold`) |
| **CSS toggle** | `.loc-toggle` pill | `.loc-toggle` pill |

**How it works:**
- `campus.js` reads campus from `localStorage("abi-campus")` or page class.
- Phone links use `data-campus-phone` + `data-mn-*` / `data-bx-*` attributes.
- Manhattan-only elements (ES phone) use `data-mn-only` → hidden on Bronx.
- Programs nav links rewrite to `/programs/manhattan.html` or `/programs/bronx.html`.

---

## 4. Build & Deploy

### Build locally

```bash
python3 src/build.py                 # → 115 pages + sitemap.xml + robots.txt
python3 src/build_landing_pages.py   # → landing funnel pages
```

### Local dev server

```bash
python3 src/serve.py                 # → localhost:8000
```

### Deploy to production

```bash
# Push to GitHub (Vercel auto-deploys from main)
git push client main

# If auto-deploy doesn't update the domain, manually promote:
vercel promote <deployment-id> --scope amerbarberedu-oss-projects --token $VERCEL_TOKEN
```

### Cache busting

When modifying CSS/JS files, bump the version number:
- `landing.css?v=173` — in `src/build.py`, `landing-funnels/src/build.py`, and generated HTML files.
- `style.css?v=34` — in `src/build.py` and generated HTML files.
- `campus.js?v=5` — in `src/build.py`, `src/pages/index.html`, `src/pages/es-index.html`
- `funnels.css?v=64` — in generated HTML files and `landing-funnels/src/build.py` (`CSS_V`)
- `analytics.js?v=6` — **Arhum only** (abi.edu = v6, .com = v7)

---

## 5. Git Workflow

| Remote | Repo | Purpose |
|---|---|---|
| `origin` | amerbarberedu-oss/abi-website-black | Production (Vercel auto-deploys from main) |

```bash
# Always fetch latest before making changes
git fetch origin && git merge origin/main

# Push to production
git push origin main
```

### Experiments
- Create `experiment/feature-name` branch — NEVER commit experiments to `main`
- Only merge when explicitly approved
- Delete branch after merge

---

## 6. SEO / AEO

- Unique `<title>` (≤60c) and `<meta description>` (≤155c) per page.
- **Structured data (JSON-LD):** TradeSchool, Course, Person, BreadcrumbList, FAQPage, HowTo.
- Open Graph + Twitter cards, canonical URLs, `hreflang` EN/ES.
- `sitemap.xml` with `lastmod`, `robots.txt`, `llms.txt`.

---

## 7. Analytics & Ads

`assets/js/analytics.js` boots **Google Tag Manager `GTM-NKLLGPC`** with consent-aware
loading. Meta Pixel, Clarity, CallRail, ClickCease, and Google Ads are managed
**inside GTM** — do not add/remove tags in code.

---

## 8. Live URLs

### Main Website
| Page | URL |
|---|---|
| **Homepage (EN)** | https://www.abi.edu/ |
| **Homepage (ES)** | https://www.abi.edu/es/ |
| **Bronx (EN)** | https://www.abi.edu/bronx |
| **Bronx (ES)** | https://www.abi.edu/es/bronx |
| **Programs** | https://www.abi.edu/programs |
| **Contact** | https://www.abi.edu/contact |

### Landing Funnels
| Funnel | URL |
|---|---|
| **500hr Master Barber (EN)** | https://www.abi.edu/landing-funnels/500-hours-master-barber-program-landing-page/ |
| **500hr Master Barber (ES)** | https://www.abi.edu/landing-funnels/500-hours-master-barber-program-landing-page/spanish/ |
| **Master Barber Bronx (EN)** | https://www.abi.edu/landing-funnels/master-barber-program-bronx/ |
| **Master Barber Bronx (ES)** | https://www.abi.edu/landing-funnels/master-barber-program-bronx/spanish/ |

---

© American Barber Institute (ABI). GI BILL® is a registered trademark of the U.S.
Department of Veterans Affairs.
