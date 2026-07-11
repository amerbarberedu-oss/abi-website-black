# ABI Website — Project State

## Last Updated
- **Date:** 2026-07-11 (July 11, 2026)
- **Agent:** Antigravity
- **Branch:** `main`
- **Latest Commit:** `724238e` — Fix landing funnel builder CSS_V
- **Status:** ✅ DEPLOYED TO PRODUCTION (abi.edu)

## Stable Baseline
- **Production commit:** `724238e`
- **Pre-experiment rollback point:** `2d34130`

## What Was Done This Session

### Merged from `experiment/compact-contact-form` → `main`
130 files changed, 4317 insertions, 2827 deletions.

1. **Campus-Specific Phone Numbers** — Complete dynamic phone system
   - Manhattan: EN `(212) 290-2289` + ES `(212) 290-0278` + Haircut `(856) 316-1551`
   - Bronx: `(718) 676-0640` (single) + Haircut `(856) 316-1551`
   - `data-campus-phone` attributes + `data-mn-only` visibility

2. **Gold Theme** — 109 `body.bx-gold` CSS override rules

3. **Campus Toggle Fixes** — Bronx→Manhattan and Manhattan→Bronx transitions

4. **$150/week** on second line on mobile

5. **SEO/AEO Audit** — 17/17 checks passing

6. **Code Cleanup** — Dead PHONE_SVG/SCISSORS_SVG removed, comprehensive comments added

7. **Landing Funnel CSS Versions** — Synced to v=153 (landing.css) and v=59 (funnels.css)

8. **Step Number Fix** — Duplicate step numbers suppressed (`.step::before{display:none}`)

## Current Versions
- `landing.css?v=153`
- `campus.js?v=5`
- `funnels.css?v=59`
- `analytics.js?v=6` (abi.edu) / `?v=7` (.com) — NOT MODIFIED (Arhum's domain)
