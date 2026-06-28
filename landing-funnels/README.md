# ABI Landing Funnels

Standalone conversion-focused landing pages for the American Barber Institute, separate from the main marketing site.

## Pages

| URL | Campus | Language | Accent |
|---|---|---|---|
| `/500-hours-master-barber-program-landing-page` | Manhattan | English | Deep gold |
| `/500-hours-master-barber-program-landing-page/spanish` | Manhattan | Spanish | Emerald green |
| `/master-barber-program-bronx` | Bronx | English | Vivid orange |
| `/master-barber-program-bronx/spanish` | Bronx | Spanish | Royal blue |

Each language is a **separate page** (not a switcher) — the EN/ES toggle in the header navigates to the counterpart page.

## What's in / what's not

**On every landing page:**
- Slim header (logo + campus address + campus phone + EN ⇄ ES toggle)
- Hero: campus-specific headline + countdown + 3 CTAs + lead form (Formspree)
- "Everything You Need to Succeed" pill grid (sky-blue universal accent)
- "Hands-On Training That Matters" — 4 steps
- Career earnings tiers
- Tuition — 3 payment plans
- Inside ABI — 6 showcase clips (CDN-hosted)
- Student Voices — 3 portrait testimonial videos (center play/pause + corner mute + exclusive playback)
- Watch Us — 3 YouTube thumbnails
- Gallery — 8 clinic-floor photos
- Reviews — 4 per-campus quotes (NO Google widget, NO Google Maps link)
- FAQ — 6 entries
- Slim footer — 3 CTAs + 5 social icons + chatbot bubble + fine print

**On Bronx pages only:**
- Extra section after Inside ABI with 3 Bronx-specific testimonial video slots (placeholders for now — drop real files in `assets/videos/` and they're picked up automatically)

**Removed (vs. the main marketing site):**
- Top navigation bar
- Founder / leadership "Personal Welcome" section
- Google reviews widget + Google Maps link
- Footer quick-links column + legal/copyright bar
- Mobile bottom bar

## Local build

```bash
cd landing-funnels
python3 src/build.py
```

Re-runs are idempotent; output goes to:
- `500-hours-master-barber-program-landing-page/index.html`
- `500-hours-master-barber-program-landing-page/spanish/index.html`
- `master-barber-program-bronx/index.html`
- `master-barber-program-bronx/spanish/index.html`

## File layout

```
landing-funnels/
├── README.md                                  ← this file
├── vercel.json                                ← own routing + security headers
├── src/
│   ├── build.py                               ← generator (no parent imports)
│   └── data.py                                ← all user-visible copy + page configs
├── assets/
│   ├── css/funnels.css                        ← own stylesheet (.lf-* namespace)
│   ├── js/funnels.js                          ← countdown + reel controls + form
│   ├── img/                                   ← logo, hero, gallery, posters
│   └── videos/                                ← testimonial mp4s (+ placeholders)
├── 500-hours-master-barber-program-landing-page/
│   ├── index.html
│   └── spanish/index.html
└── master-barber-program-bronx/
    ├── index.html
    └── spanish/index.html
```

## Swapping placeholder videos for real files

**3rd Student Voices video** — currently re-uses Video-321 as a placeholder.
1. Save the real file to `assets/videos/student-voice-3.mp4`
2. Extract a poster frame to `assets/img/student-voice-3-poster.jpg`
3. In `src/data.py`, change the last entry of `STUDENT_VOICES_VIDEOS` to `("student-voice-3.mp4", "student-voice-3-poster.jpg")`
4. Re-run `python3 src/build.py`

**3 Bronx-only testimonial videos** — currently re-use Video-321 / Video-124.
1. Save 3 files to `assets/videos/bronx-voice-1.mp4` … `bronx-voice-3.mp4`
2. Extract posters to `assets/img/bronx-voice-1-poster.jpg` … `bronx-voice-3-poster.jpg`
3. In `src/data.py`, edit `BRONX_EXTRA_VIDEOS` to match
4. Re-run `python3 src/build.py`

## Deployment

Lives on its **own Vercel project** + **own branch (`landing-funnels`)** so that the live marketing site stays untouched until this is explicitly merged into `main`.

## Phones per page

| Page | Phone shown |
|---|---|
| Manhattan EN | (212) 290-2289 |
| Manhattan ES | (212) 290-0278 |
| Bronx EN | (718) 676-0640 |
| Bronx ES | (718) 676-0640 |

## Counter logic

The countdown reads `data-target="YYYY-MM-DD"` (baked at build time as the next first-Monday-of-the-month). Once that date passes, `funnels.js` rolls the target forward to the next first-Monday-of-the-month automatically — works indefinitely without redeploys.
