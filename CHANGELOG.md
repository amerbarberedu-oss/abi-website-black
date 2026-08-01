# Changelog — American Barber Institute (Black)

All notable changes to this site are recorded here.
Format follows [Keep a Changelog](https://keepachangelog.com/). Versions stay in
the **0.x** range throughout the upgrade cycle; the move to **1.0.0** happens only
when the client approves the official production release.

## [Unreleased]

### Changed
- **Remaining English barbering terms translated on the Russian and Albanian
  pages** (2026-08-01) — `Clipper Over Comb` / `Scissor Over Comb` describe an
  action, so they now read «Машинкой через расчёску» / «Ножницами через
  расчёску» and *Makinë mbi krëhër* / *Gërshërë mbi krëhër*, in the technique
  list, the curriculum module and the About prose. Albanian style names also
  take their local spelling: Pompadour→Pompadur, Caesar→Cezar, Mohawk→Mohikan,
  Shape Up→Rregullim vijash. Afro, Fohawk, Flat Top and High-Top Fade stay in
  English — they have no natural Albanian form and barbers search for them as
  they are. Russian was already fully Cyrillicised apart from the two over-comb
  terms. English and Spanish untouched.
- **Language switcher trimmed on the Russian and Albanian pages** (2026-08-01)
  — each now shows only *English + itself* rather than all four pills. Driven
  by a new optional `switcher` list per page. `hreflang` deliberately still
  advertises every translation: the switcher and hreflang both read from
  `alts`, so trimming that alone would have cost the pages their reciprocal
  language pairing in search. English, Spanish and both Bronx pages unchanged.

### Added
- **A leading testimonial video on the Russian and Albanian landing pages**
  (2026-08-01) — the client supplied two clips, one per page: `student-voice-5`
  leads the Russian row, `student-voice-4` the Albanian. Each page shows four
  videos in the 2×2 `.lf-reel--quad` grid; the other four funnels keep their
  three. Both files are committed under `assets/videos/` with
  language-neutral names continuing the `student-voice-N` series.
  - Superseded an intermediate state that briefly put *both* clips on the
    Russian page (five videos, `.lf-reel--five`). That rule is retained as part
    of the 3/4/5 count→class system but is currently unused.
  - **Poster frames** captured from the clips themselves (bright, on-brand
    barbershop stills at 18s / 8s) and committed as
    `student-voice-4/-5-poster.jpg`. Without one the tile rendered as a flat
    dark box against `.lf-reel__media`'s `#141a2e` background — the earlier
    assumption that the browser would paint the video's own first frame did
    not hold. Every video on every funnel page now has a poster, and both new
    VideoObject entries carry a `thumbnailUrl`.
- **Fourth testimonial video on the Russian landing page** (2026-08-01) — a
  client-supplied clip now leads the Student Voices row on
  `/master-barber-program-russian` only. Committed to `assets/videos/` and
  served same-origin (the other three are on Vercel Blob, but there's no Blob
  token in the repo); 720×1280, so it matches the 9/16 tile exactly. No poster
  frame was supplied, so `_reel_media()` now omits the attribute rather than
  emitting a broken path, and the browser paints the video's first frame.
  `STUDENT_VOICES_VIDEOS` became language-keyed — `tr()`'s English fallback
  keeps es/sq and both Bronx pages on the original three. The grid modifier is
  chosen by count, so the Russian page renders a balanced 2×2
  (`.lf-reel--quad`, new in `funnels.css`, `CSS_V` → 74) instead of 3 + an
  orphan. All five other funnel pages rebuild with no content change.

### Changed
- **Russian and Albanian funnels now post to their own GHL forms** (2026-08-01) —
  both shipped pointed at the Manhattan English form as a stopgap, so their
  leads were indistinguishable from English submissions. Now
  `S6vfeKEBsrhjGG09FlU1` (`01.…RU LP`) and `LHuKB7w9PKtK9J0Gpul5`
  (`01.…AL LP`). Both are taller than the original four, so `_GHL_FORMS` values
  widened from `(id, name)` to `(id, name, height)` and the hardcoded
  `ghl_h = 757` is gone — the height now travels with the form (840 for the two
  new ones, 757 unchanged for the rest). The other four funnel pages rebuild
  byte-identical.
- **Pricing cards slimmed to two rows** (2026-07-31) — the **Tuition** row and the
  payment **formula line** are removed from every plan card, on all three
  components and in all four languages: the program pages (`.tuition`), the
  homepage/Bronx grid (`.plan`) and the landing funnels (`.lf-plan`). Cards now
  read: down payment headline → Weekly payments → Total cost → CTA. The unused
  `tuition` / `calc` fields were dropped from the funnel data so the source
  can't drift from what renders, and the dead `.plan-calc` / `.lf-plan__calc`
  rules were removed (`landing.css` → v309, `funnels.css` `CSS_V` → 73). The
  spacing the formula line used to provide above the CTA now comes from a
  bottom margin on the rows list, so the CTAs stay bottom-aligned.
  - Side effect: this also clears Plan A's long-standing discrepancy, where
    Tuition read $5,250 against a $5,600 total.
  - **Known, accepted:** Plan C now shows $200 down + 27 × $160 against a
    $4,600 total with nothing accounting for the $80 difference — the formula
    line was the only place carrying the "+ final payment". Client chose to
    remove it as-is rather than fold that into the weekly row.
  - Not touched: the per-plan spec table on `about.html`, which is a different
    pre-existing component (Tuition / Registration fee / Payment schedule /
    Program length / Total hours) whose only price row is Tuition.

### Added
- **Albanian landing page** at `/master-barber-program-albanian` (2026-07-30) —
  the Manhattan funnel in Albanian (`sq`, pill "Shqip"). Same setup as the
  Russian page: Manhattan English admissions line, Manhattan EN GHL form,
  prices copied verbatim. Because the builder was generalized for Russian, this
  was almost entirely a content change — `sq` added to the five language tables,
  the `("manhattan", "sq")` composite keys, and one marked block in `data.py`.
  The Russian page gains an SQ pill and hreflang entry so the two non-English
  pages cross-reference each other and the hreflang set is complete in both
  directions; the English and Spanish pages are untouched apart from the
  `CSS_V` bump (71 → 72, `funnels.css` gains the `mhtn-sq` theme).
- **Russian landing page** at `/master-barber-program-russian` (2026-07-30) — a
  full Russian translation of the Manhattan funnel, generated by the same
  builder as the other four. Reuses the Manhattan English admissions line and
  GHL form (no Russian line or form exists yet); TCPA call/SMS consent copy is
  deliberately left in English. All Russian copy sits in one clearly-marked
  block at the end of `landing-funnels/src/data.py` so it can be handed to a
  native speaker for review in a single pass.
- **The funnel builder is no longer hardcoded bilingual** — `build.py` had ~20
  `if lang == "es" else <English>` branches, a binary EN|ES switcher and
  en/es-only `hreflang`. These are now data-driven: a page joins the language
  set by declaring an `alts` mapping, and English is the explicit fallback.
  New helpers `tr()` / `cf()` / `page_alts()`; the strings those branches held
  moved into `data.py` (`POPULAR_BADGE`, `TUITION_LABELS`, `HERO_FEATURES`,
  `CD_*`, `MCTA_LABELS`, …). Verified behaviour-preserving: the four existing
  pages rebuild with no content change.

### Fixed
- **The built funnel pages had drifted from their own source.** Rebuilding
  revealed the live pages still showed `$500 down payment` /
  `$500 de pago inicial` in Entrance Requirements — `data.py` had been updated
  with the new pricing but the pages were never regenerated. Also realigned
  the funnel `landing.css` pin (v304 → v308, matching the rest of the site),
  `CSS_V` (69 → 71) and the Spanish footer disclaimer. Every funnel change in
  this release now round-trips through `python landing-funnels/src/build.py`.

### Changed
- **One pricing card layout across all three surfaces** (2026-07-29,
  `landing.css` v16.4 → v308, `funnels.css` → v70) — the breakdown introduced
  on the program pages (down payment as the headline, then a Weekly payments /
  Tuition / Total cost table and the payment formula) now also drives the
  homepage/Bronx `.plan` grid and the four landing funnels' `.lf-plan` cards,
  which previously led with the total and a one-line terms sentence. The two
  new rule sets are light-surface twins of the dark v16.3 ones and are scoped
  `.plan …` / `.lf-plan__…` so they don't collide. Both funnel builders
  (`landing-funnels/src/build.py` and the older `src/build_landing_pages.py`)
  and `data.py` now carry `down`/`weekly`/`tuition`/`total`/`calc` fields
  instead of `price`/`terms`, so a rebuild reproduces the new layout.
- The weekend plan's CTA is now the same blue as the other two (`btn-gold`,
  which brand.css maps to #1b2fd9) instead of the outlined `btn-ghost`.
- **Per-plan CTA copy on every pricing surface** — the homepage/Bronx grid and
  the four funnels replace a single "Let's Do It" / "¡Hagámoslo!" on all three
  cards with "Enroll in morning / afternoon / weekend" (and the Spanish
  equivalents), matching the program pages. Both funnel builders and `data.py`
  now carry a per-plan `cta` field, so a rebuild keeps the wording.
- **Promo banner now quotes Plan C** — "$200 down payment & **$160** weekly"
  (was $200 weekly) across the site banner and the funnel header strip, EN + ES.
  $200 down with $160 weekly is exactly the weekend plan, so the disclaimer was
  repointed from Plan B (afternoon) to Plan C (weekend) to match; the earlier
  $200/$200 wording paired Plan B's figures instead.
- The built funnel pages were stale against `landing-funnels/src/data.py` — the
  header strip still read "$160 per week*" and the English disclaimer still
  referenced Plan C's weekly payment. Both re-synced.
- **New approved tuition pricing, site-wide** (2026-07-29) — Afternoon drops
  $4,600 → **$3,600** ($200 down + 17 × $200, was $500 down + 16 × $250 + $100);
  Weekend stays $4,600 but on **$200 down + 27 × $160 + a final payment** (was
  $550 down + 27 × $150); Morning unchanged at $5,600 ($500 down + 17 × $300)
  and now **includes a professional tool kit**. Lowest advertised price is
  therefore $4,600 → $3,600 and the lowest weekly $150 → $160, so every
  "from $4,600" / "from $150 a week" claim was updated: program pages, homepage
  and Bronx plan grids, about, FAQ (incl. FAQPage JSON-LD), programs index and
  both campus pages, the licensing and Pennsylvania pages, SEO meta
  descriptions in `src/build.py`, and all four landing funnels plus
  `landing-funnels/src/data.py`. EN + ES.
- **Tuition cards rebuilt to the approved layout** (`landing.css` v16.3) —
  Plan A/B/C tag, down payment as the headline figure, a Weekly payments /
  Tuition / Total cost table and the payment formula. (The approved sheet's
  per-plan tool-kit notes were dropped before release, so tools are not
  mentioned per plan and the section intro keeps its original wording:
  tools, books and supplies are purchased separately.) Extends `.tuition`
  rather than replacing it, so the dark
  surface, hover lift and reveal animation are untouched. New sub-elements are
  `.tuition`-scoped to outrank `.tuition ul` / `.tuition li`; the plan label is
  `.tuition-tag` because `.plan-tag` was already taken by the funnel cards.
- The orphaned `*$150/week refers to Plan C weekly payments` footnote now
  describes the current banner claim (Plan B, $200 down & $200 weekly).

### Added
- **"Ways to Pay for Your Training" row on the Programs page** (2026-07-28) —
  companion to the `Programs ▾` dropdown from PR #14, which surfaced
  `/veterans` and `/access-vr-program` in the nav but left the programs index
  untouched. Two `res-card--link` cards now link to both pages, reusing the
  copy already written for `how-to-get-started`. EN + ES.

### Changed
- The "Not sure which program fits?" paragraph on `programs/index` pointed both
  its "Veterans GI Bill®" and "ACCESS-VR" links at `/resources`; they now go to
  the two dedicated pages. EN + ES.

### Fixed
- **English header nav overlapping the language switcher ≥1200px**
  (`landing.css` v16.2, cache-buster → v305) — the `▾` added to the Programs
  trigger in PR #14 widened the English row by 6–15px, and the continuous
  scaling was tuned to fit with as little as 0.2px of slack, so CONTACT sat
  under the EN|ES pill at 1200/1240/1360/1400/1440px (+8.6/+1.9/+3.8/+14.6/
  +6.9px measured). PR #14's follow-ups re-tuned the *Spanish* nav; this is the
  English side. Per-item `letter-spacing` and inline padding are now zeroed
  between 1200–1560px — the flex `gap` already separates the items. Verified at
  nine widths from 1200–1560px, all clear by ≥12px; Spanish re-checked
  unchanged at 1200–1920px.

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
