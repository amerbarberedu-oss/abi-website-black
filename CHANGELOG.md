# Changelog — American Barber Institute (Black)

All notable changes to this site are recorded here.
Format follows [Keep a Changelog](https://keepachangelog.com/). Versions stay in
the **0.x** range throughout the upgrade cycle; the move to **1.0.0** happens only
when the client approves the official production release.

## [Unreleased]

## [0.3.0] — 2026-07-24

Everything shipped since 0.2.0 (2026-07-07), consolidating three parallel
workstreams: Kazi (site engineering, SEO, media recovery), Arhum Abdullah
(analytics, chat, header/hero design), and joint production fixes.

### Added
- **Original AI Brand Film restored** (2026-07-24) — the AI-generated logo
  animation + 5 AI showcase clips were lost with their external asset host;
  recovered from the restored `kazi-reprime/ABI-10-Websites` repo and now
  committed same-origin at `assets/videos/ai/` so no third-party host can
  take them down again. Gallery EN + ES.
- **Google-reviews badge on campus Programs pages** (2026-07-17) —
  `programs/manhattan`, `programs/bronx` + ES twins now show the same
  visual rating widget as the homepage, with real per-campus data.
- **Local SEO neighborhoods** (2026-07-17) — `ORG_SCHEMA["areaServed"]`
  expanded 8 → 379 places (Queens/Brooklyn/SI/Manhattan/Bronx/Suffolk/
  Westchester/Yonkers) + "Areas We Serve" section on contact pages.
  Nassau place names still pending from client.
- **Licensing splash-page content** (2026-07-16) — Gary's originally-drafted
  2023 copy finally implemented on the unlicensed-practice page (EN + ES).
- **Multi-channel chat** (Arhum, 2026-07-12→13) — mobile "Text Us" panel +
  desktop left channel rail (WhatsApp/Instagram/Text/Messenger).
- **Vercel Web Analytics** (Arhum, 2026-07-09), clean GA4 reinstall on a new
  property after the old direct config was removed.

### Fixed
- **Bronx page showed Manhattan's Google rating, map and listing link**
  (2026-07-17) — `bronx.html`/`es/bronx.html` reuse the homepage partial;
  the campus swap in `src/build.py` now also corrects the reviews badge and
  the whole "Find Us" section.
- **Ambient videos froze after one cursor pass** (2026-07-24) —
  `video-sound.js` paused every non-reel clip on `mouseleave` while the
  IntersectionObserver autoplay layer only fires on intersection changes;
  clips now keep playing muted while visible. Gallery floor reels autoplay
  on scroll (Arhum's `effects.js` observer, same day).
- **Google rating truth-sync** (2026-07-24) — Manhattan rating moved on
  Google to **4.2 (433 reviews)**; every badge, body mention and JSON-LD
  aggregateRating now carries live-verified per-campus values
  (Bronx 4.9/253), replacing stale 4.1/"100+"/4.6 figures.
- **Asset version alignment** (2026-07-24) — hand-crafted pages and
  landing-funnels referenced older `?v=` values than template pages for the
  same files (e.g. `video-sound.js?v=4` vs `?v=301`); all references now
  aligned to each file's highest version so returning visitors can't be
  served stale cached JS/CSS.
- Redirect/wildcard audit (2026-07-16): prototype-pollution guard in
  `api/legacy-redirect.js`, `/splash-page-1`/`-2` now reach their real
  targets. reCAPTCHA Enterprise CSP allowances for form/chat captcha
  (2026-07-24). Numerous header/nav collapse fixes at mid-width
  breakpoints (Arhum, 2026-07-19→22).

### Changed
- Campus-specific header logos (Manhattan vs Bronx artwork; Arhum,
  2026-07-20→23), thank-you page redesign (EN + ES), haircuts copy
  standardized to walk-in messaging, gallery media served from the
  `abi-videos` Vercel Blob store.

### Infrastructure
- **`abi-master-archive` Blob store** (2026-07-24) — disaster-recovery
  archive of every ABI asset from all known sources (1,002 files, 756 MB,
  `manifest.json` at root). Nothing live references it; it exists so no
  asset can ever be permanently lost again.

## [0.2.0] — 2026-07-07

Campus-context release: every location, map, review CTA and Programs nav link
now routes to the correct campus (Manhattan vs Bronx). Homepage mobile hero
promotes the contact form. Landing pages match the website's chip alignment.

### Added
- **Campus-specific Programs pages** — new `programs/manhattan.html`
  (Master Barber + 50-Hour Refresher + Contagious Diseases) and
  `programs/bronx.html` (Master Barber + Contagious Diseases only). Full ES
  twins under `/es/programs/manhattan` and `/es/programs/bronx`. Listed in
  sitemap; reachable from the general programs index.
- **Campus-aware Programs nav** — `assets/js/campus.js` v2 rewrites every
  `Programs` nav link at load time to the campus the visitor is in
  (Manhattan by default; Bronx if the visitor is on a Bronx page or has
  previously toggled BX). Toggling MN ↔ BX while viewing a Programs page
  navigates directly to the other campus's Programs page (not back to the
  campus home).
- **Homepage "Find Us" section** — mirrors the Bronx page: embedded Google
  map of the Manhattan campus at 48 West 39th Street plus a "See campus on
  Google" CTA linking to the Manhattan Business Profile. Same section
  translated on `/es/`.
- **Per-campus Google Business Profile routing** — every location CTA on
  Manhattan-context pages links to `maps.app.goo.gl/42UjD6bFQ65NEt1E7`;
  every location CTA on Bronx-context pages links to
  `maps.app.goo.gl/9TJJh8ehUjSZ8kcaA`.
- **Hidden `$7 haircut` SEO page** — `/7-dollar-haircut-nyc` + ES twin
  (unique content targeting "$7 / cheap haircut NYC"). Crawlable via the
  sitemap; not linked in navigation.

### Changed
- **Homepage mobile order** — the GHL contact form appears immediately
  after the "500 Hour" hero (H1 + tagline), before the feature chips and
  countdown. Priority on mobile: contact box > image > text.
- **Phone-chip spacing** — `.mhx-phones` switched from a fixed 3-column
  grid to a flex row that auto-fills whatever number of chips are present
  (1, 2 or 3). Two chips fill evenly; three chips fill evenly; no empty
  slot ever shows.
- **Landing hero chip alignment** — `.lf-features` uses a 3-column uniform
  grid on desktop (matches website `.hx-chips`) and a stacked full-width
  flex column on mobile. The "Financial Assistance — ACCES-VR, VA"
  multi-line chip now uses the same bold + smaller-italic structure as
  the website's `.hx-chip--fin`.
- **Bronx page review badge** — replaced the misleading "4.6★ / 100+
  Google reviews" (that number belongs to the Manhattan listing) with a
  Bronx-focused CTA linking to the Bronx Business Profile.

### Fixed
- `/es/manhattan` was returning 404 — added a rewrite to `/es/` so it
  mirrors `/manhattan` → `/`.
- Mobile hero reorder selector bug — `.hx-in > .hx-h1` required a direct
  DOM child, but `.hx-h1` is a grandchild through `.hx-copy`
  (`display:contents`). Switched to `.hx-copy > .hx-h1` so the CSS
  `order` values actually apply.
- Landing chips crammed into a 3-column grid on 375px viewports because
  the desktop `display:grid` rule cascaded into mobile. Mobile now
  explicitly resets to `display:flex; grid-template-columns:none;`.

### Workflow
- **Preview-first deploy rule** — every future change first ships to a
  preview branch (Vercel preview URL) for client approval, then merges to
  `main`, which auto-deploys prod. Direct pushes to `main` are avoided.
- `landing.css` v151; `funnels.css` v56; `campus.js` v2.

## [0.1.0] — 2026-06-18
Baseline for the production upgrade cycle — the full current site, handover-ready.

- **Architecture:** zero-dependency static HTML generated by Python
  (`src/build.py` + `src/build_landing_pages.py`); Vercel serves the built files directly.
- **Content:** 44 pages (English + Spanish) — home, about, programs
  (500-hour Master, 200-hour, SMP, license transfer, etc.), schedule, admissions,
  tuition, instructors, jobs, gallery, blog, FAQ, contact, veterans, ACCESS-VR,
  partners, resources, and splash/landing pages.
- **Mobile:** mobile-first CSS with `viewport-fit=cover` + iOS safe-area insets and
  `prefers-reduced-motion` support.
- **Cleanup at baseline:** removed superseded `classic-home.html` (live home is
  `index.html`); `AUDIT-REPORT.md` consolidated under `docs/`.
