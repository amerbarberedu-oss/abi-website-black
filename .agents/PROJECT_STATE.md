# ABI Website — Project State

## Last Updated
- **Date:** 2026-07-11 (July 11, 2026)
- **Agent:** Antigravity
- **Branch:** `experiment/compact-contact-form`
- **Latest Commit:** `1003d95` — Cleanup: remove dead code, add comprehensive comments

## Stable Baseline
- **Production (client/main):** Check `git log client/main -1`
- **Experiment branch is NOT merged into main yet** — Kazi to approve first

## What Was Done This Session

### 1. Duplicate Step Numbers Fix
- **Problem:** Steps "01, 02, 03" showed twice — once from `style.css` CSS counter (`.step::before`) and once from `landing.css` badge (`.step-num`)
- **Fix:** Added `.step::before{display:none!important}` in `landing.css`

### 2. Campus-Specific Phone Numbers
- **Problem:** All pages showed Manhattan phone numbers regardless of campus
- **Fix:** Complete phone number switching system using `data-campus-phone` attributes
  - Manhattan: EN `(212) 290-2289` + ES `(212) 290-0278` + Haircut `(856) 316-1551`
  - Bronx: `(718) 676-0640` (single number) + Haircut `(856) 316-1551`
  - ES phone links have `data-mn-only` → hidden on Bronx (no duplicate numbers)
  - Topbar flag: EN ↔ BX
  - MHX label: ENGLISH ↔ BRONX
  - Call sheet: English ↔ Bronx

### 3. Gold Theme Overrides
- Added 109+ `body.bx-gold` CSS rules covering all UI elements
- Loc-toggle and lang-toggle glassmorphism overrides
- Smooth CSS transitions for campus theme switching

### 4. Code Cleanup
- Removed dead `PHONE_SVG`, `SCISSORS_SVG` constants from `campus.js`
- Removed unused topbar/mhx/footer arrays from phone data objects
- Added comprehensive JSDoc comments to all functions
- Added CSS comments explaining non-obvious fixes

### 5. SEO/AEO Audit (Prior in Session)
- 17/17 SEO checks passed
- ES title deduplication fixed
- Meta descriptions trimmed to ≤155 chars
- HowTo schema implemented

## Files Modified
- `assets/js/campus.js` — Complete rewrite with proper comments
- `assets/css/landing.css` — Step fix + gold overrides + lang/loc-toggle gold
- `src/build.py` — Phone data attributes in shell template
- `src/pages/index.html` — Visit Us footer phone data attrs
- `src/pages/es-index.html` — Visit Us footer phone data attrs

## Current Versions
- `landing.css?v=153`
- `campus.js?v=5`
- `analytics.js?v=6` (abi.edu) / `?v=7` (.com) — NOT MODIFIED (Arhum's domain)

## Known Items
- Body content phone numbers (e.g., "Call (212) 290-2289" in prose text on schedules, partners pages) are NOT dynamically swapped — these are contextual references
- Landing funnel pages (`src/build_landing_pages.py`) have their own footer with hardcoded phone numbers — not part of the campus toggle system
