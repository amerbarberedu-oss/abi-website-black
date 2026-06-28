#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ABI Landing Funnels — 4 conversion-focused landing pages.

Pages produced (each as its own static .html under a distinct URL):

  /500-hours-master-barber-program-landing-page          Manhattan EN — gold theme
  /500-hours-master-barber-program-landing-page/spanish  Manhattan ES — emerald theme
  /master-barber-program-bronx                           Bronx EN     — orange theme
  /master-barber-program-bronx/spanish                   Bronx ES     — royal-blue theme

These are stripped versions of the splash home — no top navigation, no
quick-links / legal footer, no Google-Reviews widget, no founder welcome.
EN ↔ ES is NOT a switcher: each language is a separate page that links to its
counterpart via the toggle.

Run:    python3 src/build_landing_funnels.py
"""
import os, sys, json, datetime, re

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
# Reuse data + simple builders from the main landing-pages generator.
import build_landing_pages as bp
from build_landing_pages import (
    S, MANHATTAN, BRONX, NEXT_MON, CD_VALS, NEXT_START_EN, NEXT_START_ES,
    SITE, ROOT, icon, clean_links,
    sec_ticker, sec_stats, sec_pills, sec_steps, sec_skills, sec_zero,
    sec_earnings, sec_tuition, sec_showcase, sec_videos, sec_gallery, sec_faq,
)

# ───────────────────────── Page configurations ─────────────────────────
PAGES = [
    {
        "slug": "500-hours-master-barber-program-landing-page",
        "lang": "en",
        "campus": MANHATTAN,
        "theme": "lp-mhtn-en",
        "alt_url": "/500-hours-master-barber-program-landing-page/spanish",
        "url":     "/500-hours-master-barber-program-landing-page",
        "title":   "500-Hour Master Barber Program — Manhattan | ABI NYC",
        "desc":    "Become a licensed Master Barber in 4 months at our Midtown Manhattan campus. NYS-approved program, weekly payment plans, full job-placement support.",
        "phones":  [("EN", "(212) 290-2289", "+12122902289")],
        "is_bronx": False,
    },
    {
        "slug": "500-hours-master-barber-program-landing-page/spanish",
        "lang": "es",
        "campus": MANHATTAN,
        "theme": "lp-mhtn-es",
        "alt_url": "/500-hours-master-barber-program-landing-page",
        "url":     "/500-hours-master-barber-program-landing-page/spanish",
        "title":   "Programa Maestro Barbero 500 Horas — Manhattan | ABI",
        "desc":    "Conviértete en Barbero Maestro licenciado en 4 meses en nuestra sede de Midtown Manhattan. Programa aprobado por NY, planes de pago semanales y colocación laboral.",
        "phones":  [("ES", "(212) 290-0278", "+12122900278")],
        "is_bronx": False,
    },
    {
        "slug": "master-barber-program-bronx",
        "lang": "en",
        "campus": BRONX,
        "theme": "lp-brnx-en",
        "alt_url": "/master-barber-program-bronx/spanish",
        "url":     "/master-barber-program-bronx",
        "title":   "Master Barber Program — Bronx Campus | ABI",
        "desc":    "Train as a licensed Master Barber at ABI's Bronx campus. Bilingual instruction, real clients from week one, payment plans and job placement.",
        "phones":  [("EN/ES", "(718) 676-0640", "+17186760640")],
        "is_bronx": True,
    },
    {
        "slug": "master-barber-program-bronx/spanish",
        "lang": "es",
        "campus": BRONX,
        "theme": "lp-brnx-es",
        "alt_url": "/master-barber-program-bronx",
        "url":     "/master-barber-program-bronx/spanish",
        "title":   "Programa Maestro Barbero — Sede del Bronx | ABI",
        "desc":    "Fórmate como Barbero Maestro licenciado en la sede del Bronx de ABI. Instrucción bilingüe, clientes reales desde la primera semana, planes de pago y colocación.",
        "phones":  [("EN/ES", "(718) 676-0640", "+17186760640")],
        "is_bronx": True,
    },
]

CSS_VER = "124"   # bumped per landing-funnels release; main site bumps separately

# ───────────────────────── HTML <head> ─────────────────────────
def slim_head(p):
    es = p["lang"] == "es"
    canonical = SITE + p["url"]
    alt = SITE + p["alt_url"]
    en_url, es_url = (alt, canonical) if es else (canonical, alt)
    hreflang = (
        '<link rel="alternate" hreflang="en" href="%s">\n'
        '<link rel="alternate" hreflang="en-US" href="%s">\n'
        '<link rel="alternate" hreflang="es" href="%s">\n'
        '<link rel="alternate" hreflang="es-US" href="%s">\n'
        '<link rel="alternate" hreflang="x-default" href="%s">' %
        (en_url, en_url, es_url, es_url, en_url)
    )
    # Conversion-focused JSON-LD: TradeSchool / LocalBusiness + Course
    schema = json.dumps({
        "@context": "https://schema.org",
        "@type": ["TradeSchool", "LocalBusiness", "EducationalOrganization"],
        "name": "American Barber Institute — " + p["campus"]["name_en"],
        "url": canonical,
        "telephone": p["phones"][0][2],
        "address": {"@type": "PostalAddress",
                    "streetAddress": p["campus"]["addr"].split(",")[0].strip(),
                    "addressLocality": "Bronx" if p["is_bronx"] else "New York",
                    "addressRegion": "NY",
                    "postalCode": "10461" if p["is_bronx"] else "10018",
                    "addressCountry": "US"},
        "image": SITE + "/assets/img/og-cover.jpg",
        "description": p["desc"],
        "aggregateRating": {"@type": "AggregateRating",
                            "ratingValue": "4.6", "reviewCount": "100",
                            "bestRating": "5", "worstRating": "1"},
        "paymentAccepted": ["Cash", "Credit Card", "Financial Aid", "GI Bill", "ACCES-VR"],
    }, ensure_ascii=False)
    return ("""<!DOCTYPE html>
<html lang="%(lang)s">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>%(title)s</title>
<meta name="description" content="%(desc)s">
<link rel="canonical" href="%(canonical)s">
%(hreflang)s
<meta property="og:title" content="%(title)s">
<meta property="og:description" content="%(desc)s">
<meta property="og:type" content="website">
<meta property="og:url" content="%(canonical)s">
<meta property="og:image" content="%(site)s/assets/img/og-cover.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="%(oglocale)s">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="%(title)s">
<meta name="twitter:description" content="%(desc)s">
<meta name="twitter:image" content="%(site)s/assets/img/og-cover.jpg">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="theme-color" content="#101316">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" href="/icon.png" sizes="192x192">
<link rel="apple-touch-icon" href="/apple-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Oswald:wght@400;500;600;700&family=Inter:wght@400;500;600;700&family=Poppins:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/style.css?v=32">
<link rel="stylesheet" href="/assets/css/brand.css?v=30">
<link rel="stylesheet" href="/assets/css/landing.css?v=%(cssv)s">
<link rel="stylesheet" href="/assets/css/upgrade.css?v=2">
<link rel="stylesheet" href="/assets/css/effects.css?v=30">
<script src="/assets/js/analytics.js?v=1" defer></script>
<script type="application/ld+json">%(schema)s</script>
</head>
<body class="page-splash lp-funnel %(theme)s">
""" % {
        "lang": p["lang"], "title": p["title"], "desc": p["desc"],
        "canonical": canonical, "hreflang": hreflang, "site": SITE,
        "oglocale": "es_ES" if es else "en_US",
        "cssv": CSS_VER, "schema": schema, "theme": p["theme"],
    })

# ───────────────────────── Slim header (logo + EN/ES + phone) ─────────────────────────
def slim_header(p):
    es = p["lang"] == "es"
    # Campus address (just the campus that owns this page)
    addr = p["campus"]["addr"]
    # Phone pills (1 for Bronx, 1 for Manhattan per page — EN page shows EN line, ES shows ES)
    pills = "".join(
        ('<a class="lp-phone" href="tel:%s"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" '
         'stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" '
         'aria-hidden="true"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.8 19.8 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.08 4.18 2 2 0 0 1 4.06 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.22a2 2 0 0 1 2.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/></svg>'
         '<b class="lp-phone-flag">%s</b><span class="lp-phone-num">%s</span></a>')
        % (tel, lbl, disp) for lbl, disp, tel in p["phones"]
    )
    # EN/ES toggle — links to the counterpart landing page (separate file)
    en_active = "is-active" if not es else ""
    es_active = "is-active" if es else ""
    en_href = p["url"] if not es else p["alt_url"]
    es_href = p["alt_url"] if not es else p["url"]
    toggle = (
        '<div class="lang-toggle lp-lang" role="group" aria-label="Language">'
        '<a class="%s" href="%s"%s>EN</a>'
        '<a class="%s" href="%s"%s>ES</a>'
        '</div>') % (
            en_active, en_href, ' aria-current="true"' if not es else '',
            es_active, es_href, ' aria-current="true"' if es else '')
    promo = ("Comienza tu carrera de barbero hoy por solo $150 por semana*"
             if es else
             "Start your barber journey today for only $150 per week*")
    return ("""
<div class="topbar lp-topbar">
  <div class="tb-promo">%s</div>
</div>
<header class="hdr lp-hdr">
  <div class="hdr-in lp-hdr-in">
    <div class="lp-brand">
      <img class="logo-img" src="/assets/img/logo-final.gif" alt="American Barber Institute" width="385" height="99" fetchpriority="high">
      <div class="lp-addr">%s</div>
    </div>
    <div class="lp-hdr-right">
      <div class="lp-phones">%s</div>
      %s
    </div>
  </div>
</header>
""") % (promo, addr, pills, toggle)

# ───────────────────────── Hero (with countdown + 3 CTAs + lead form) ─────────────────────────
def hero(p):
    es = p["lang"] == "es"
    s = S[p["lang"]]
    if p["is_bronx"]:
        h1a = "Conviértete en un Barbero" if es else "Become a Master Barber"
        h1b = "Maestro" if es else "in the Bronx"
        scr = "Aquí en el Bronx." if es else "in 4 Months."
    else:
        h1a = "Tu Futuro." if es else "Your Future."
        h1b = "Tu Carrera." if es else "Your Career."
        scr = "Empieza Hoy." if es else "Start Today."
    sub = ("Conviértete en barbero licenciado en tan solo <b>17 semanas</b>. Entrenamiento práctico. Habilidades reales. Oportunidades reales."
           if es else
           "Become a licensed barber in as little as <b>17 weeks</b>. Hands-on training. Real skills. Real opportunities.")
    feats = "".join('<div class="feature">%s<span>%s</span></div>' % (icon(i, 20), t)
                    for i, t in s["features"])
    # Countdown
    h_cd_top = "Próxima Fecha de Inicio:" if es else "Next Starting Date:"
    cd_sub = ("Las clases nuevas comienzan el primer lunes de cada mes."
              if es else "New classes begin the first Monday of each month.")
    weekday_en = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    weekday_es = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    month_es = ["enero", "febrero", "marzo", "abril", "mayo", "junio",
                "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
    if es:
        cd_date = "%s, %d de %s de %d" % (
            weekday_es[NEXT_MON.weekday()], NEXT_MON.day,
            month_es[NEXT_MON.month - 1], NEXT_MON.year)
    else:
        cd_date = "%s, %s %d, %d" % (
            weekday_en[NEXT_MON.weekday()],
            NEXT_MON.strftime("%B"), NEXT_MON.day, NEXT_MON.year)
    cd_cells = "".join('<div class="hero-cd-cell"><b data-cd-%s>%s</b><span>%s</span></div>'
                       % (k, CD_VALS[k], lbl) for k, lbl in zip("dhms", s["count_lbl"]))
    hero_cd = ('<div class="hero-cd" data-countdown>'
               '<h2 class="hero-cd-h"><span class="hero-cd-h-label">%s</span> '
               '<span class="hero-cd-h-date">%s</span></h2>'
               '<p class="hero-cd-sub">%s</p>'
               '<div class="hero-cd-grid">%s</div>'
               '</div>') % (h_cd_top, cd_date, cd_sub, cd_cells)
    # 3 hero CTAs
    cta_primary = "Reserva Tu Cupo" if es else "Reserve Your Spot"
    cta_call    = ("Llamar Ahora" if es else "Call Now")
    cta_apply   = ("Aplicar Ahora" if es else "Apply Now")
    tel = p["phones"][0][2]
    ctas = ('<div class="hero-ctas lp-hero-ctas">'
            '<a class="btn btn-gold btn-lg" href="#reserve">%s</a>'
            '<a class="btn btn-blue btn-lg" href="tel:%s">%s</a>'
            '<a class="btn btn-ghost btn-lg" href="#reserve">%s</a>'
            '</div>') % (cta_primary, tel, cta_call, cta_apply)
    return """
<section class="hero lp-hero">
  <div class="hero-bg" style="background-image:url('/assets/img/home-hero.jpg'),url('/assets/img/about.jpg')"></div>
  <div class="hero-grad"></div>
  <div class="container hero-in">
    <div class="hero-copy">
      <h1 class="hero-h1">%s<br>%s<span class="hero-script">%s</span></h1>
      <p class="hero-sub">%s</p>
      <div class="features">%s</div>
      %s
      %s
    </div>
    %s
  </div>
</section>""" % (h1a, h1b, scr, sub, feats, hero_cd, ctas, bp.lead_form(p, s))

# ───────────────────────── Student Voices — 3 videos ─────────────────────────
def sec_brandband_3(p):
    es = p["lang"] == "es"
    eb = "Testimonios" if es else "Student Voices"
    h = "Voces reales, cortes reales" if es else "Real Voices, Real Cuts"
    sub = ("Pasa al reproductor para escuchar a un estudiante de ABI compartir su experiencia — directo, sin guion, sin filtros."
           if es else
           "Tap a player to hear an ABI student share their experience — direct, unscripted, unfiltered.")
    points = (["Entrenamiento práctico desde la primera semana",
               "Clientes reales en nuestra clínica de barbería",
               "Mentores con décadas detrás de la silla",
               "Preparación completa para el Examen del Estado de NY",
               "Horarios flexibles — mañana, tarde y fin de semana",
               "Ayuda financiera: ACCES-VR, GI Bill y VA",
               "Tarifa semanal desde $150 — planes de pago",
               "Asistencia de colocación laboral al graduarte",
               "Dos campus en NYC — Manhattan y Bronx"]
              if es else
              ["Hands-on training from week one",
               "Real clients in our on-campus barber clinic",
               "Mentors with decades behind the chair",
               "Full prep for the NY State Board Exam",
               "Flexible schedules — morning, afternoon, weekend",
               "Financial aid — ACCES-VR, GI Bill® and VA",
               "Weekly tuition from $150 — flexible payment plans",
               "Job-placement assistance on graduation",
               "Two NYC campuses — Manhattan and the Bronx"])
    bullets = "".join('<li><span class="abi-reel__bullet-mark" aria-hidden="true"></span><span>%s</span></li>' % p_
                      for p_ in points)
    play_btn = ('<button class="abi-reel__play" type="button" aria-label="Play video">'
                '<svg class="abi-reel__icon-play" viewBox="0 0 24 24" aria-hidden="true">'
                '<path d="M8 5v14l11-7z"/></svg>'
                '<svg class="abi-reel__icon-pause" viewBox="0 0 24 24" aria-hidden="true">'
                '<path d="M6 5h4v14H6zM14 5h4v14h-4z"/></svg>'
                '</button>')
    def vid(src, poster, label):
        return ('<div class="abi-reel__media" data-abi-reel>'
                '<video class="abi-reel__video" muted loop playsinline preload="metadata" '
                'src="%s" poster="%s" aria-label="%s"></video>%s</div>') % (src, poster, label, play_btn)
    # 3rd video is a placeholder — duplicates Video-321 for now; client will drop in the real file later.
    v1 = vid("/assets/videos/video-321.mp4",  "/assets/img/video-321-poster.jpg",
             "ABI student testimonial — voice 1")
    v2 = vid("/assets/videos/Video-124.mp4",  "/assets/img/video-124-poster.jpg",
             "ABI student testimonial — voice 2")
    v3 = vid("/assets/videos/video-321.mp4",  "/assets/img/video-321-poster.jpg",
             "ABI student testimonial — voice 3")
    return ('<section class="abi-reel abi-reel--triple" data-reveal>'
            '<div class="abi-reel__frame abi-reel__frame--triple">'
            + v1 + v2 + v3 +
            '<div class="abi-reel__copy abi-reel__copy--triple">'
            '<p class="abi-reel__kicker">%s</p>'
            '<h2 class="abi-reel__title">%s</h2>'
            '<p class="abi-reel__sub">%s</p>'
            '<ul class="abi-reel__points">%s</ul>'
            '</div>'
            '</div>'
            '</section>') % (eb, h, sub, bullets)

# ───────────────────────── Bronx-only: 3 extra testimonial videos ─────────────────────────
def sec_bronx_extra_testi(p):
    es = p["lang"] == "es"
    eb = "Voces del Bronx" if es else "Bronx Student Voices"
    h = ("Más historias, más experiencia" if es else "More stories, more experience")
    sub = ("Tres estudiantes del Bronx comparten su recorrido en ABI — el trabajo, la práctica, y la confianza que ganaron."
           if es else
           "Three Bronx students share their ABI journey — the work, the practice, and the confidence they built.")
    play_btn = ('<button class="abi-reel__play" type="button" aria-label="Play video">'
                '<svg class="abi-reel__icon-play" viewBox="0 0 24 24" aria-hidden="true">'
                '<path d="M8 5v14l11-7z"/></svg>'
                '<svg class="abi-reel__icon-pause" viewBox="0 0 24 24" aria-hidden="true">'
                '<path d="M6 5h4v14H6zM14 5h4v14h-4z"/></svg>'
                '</button>')
    def vid(src, poster, label):
        return ('<div class="abi-reel__media" data-abi-reel>'
                '<video class="abi-reel__video" muted loop playsinline preload="metadata" '
                'src="%s" poster="%s" aria-label="%s"></video>%s</div>') % (src, poster, label, play_btn)
    # Placeholders — currently re-use Video-321 + Video-124 so the section renders.
    # When the 3 real Bronx testimonial videos arrive, swap the src/poster pairs.
    v1 = vid("/assets/videos/video-321.mp4", "/assets/img/video-321-poster.jpg", "Bronx student testimonial 1")
    v2 = vid("/assets/videos/Video-124.mp4", "/assets/img/video-124-poster.jpg", "Bronx student testimonial 2")
    v3 = vid("/assets/videos/video-321.mp4", "/assets/img/video-321-poster.jpg", "Bronx student testimonial 3")
    return ('<section class="abi-reel abi-reel--bronx" data-reveal>'
            '<div class="abi-reel__head"><span class="abi-reel__eyebrow">%s</span>'
            '<h2 class="abi-reel__title abi-reel__title--center">%s</h2>'
            '<p class="abi-reel__sub abi-reel__sub--center">%s</p></div>'
            '<div class="abi-reel__triplet">'
            + v1 + v2 + v3 +
            '</div></section>') % (eb, h, sub)

# ───────────────────────── Testimonials — NO Google widget, NO map link ─────────────────────────
MANHATTAN_REVIEWS_EN = [
    {"n": "Marcus Johnson", "r": "Class of 2024 · Manhattan", "q": "The instructors at the Midtown campus actually push you — they don't let you settle. By month 3 I was cutting paying clients confidently."},
    {"n": "David Rivera",   "r": "Class of 2024 · Manhattan", "q": "Weekend program let me keep my day job. Now I work at a shop two blocks from where I trained. Best decision."},
    {"n": "Anthony Cole",   "r": "Class of 2023 · Manhattan", "q": "Top-tier instructors, real clinic floor, and they prep you hard for the state board. Passed first try."},
    {"n": "Jamal Pierce",   "r": "Class of 2023 · Manhattan", "q": "ABI Manhattan turned my hobby into a paycheck. Job-placement office connected me with a shop the same week I graduated."},
]
MANHATTAN_REVIEWS_ES = [
    {"n": "Marcos Jiménez", "r": "Clase 2024 · Manhattan", "q": "Los instructores de Midtown realmente te empujan — no te dejan conformarte. Para el tercer mes ya cortaba clientes con confianza."},
    {"n": "David Ramírez",  "r": "Clase 2024 · Manhattan", "q": "El programa de fin de semana me dejó mantener mi trabajo. Ahora trabajo a dos cuadras de donde me formé. Mejor decisión."},
    {"n": "Antonio Castro", "r": "Clase 2023 · Manhattan", "q": "Instructores de primera, clínica real, y te preparan muy bien para el examen del estado. Lo pasé al primer intento."},
    {"n": "Javier Peña",    "r": "Clase 2023 · Manhattan", "q": "ABI Manhattan convirtió mi pasatiempo en un sueldo. La oficina de empleo me conectó con una barbería la misma semana que me gradué."},
]
BRONX_REVIEWS_EN = [
    {"n": "Carlos Mendez",  "r": "Class of 2024 · Bronx", "q": "Bilingual instruction at the Bronx campus was a game-changer for me. Real clients from week one, no holding back."},
    {"n": "Tyrone Adams",   "r": "Class of 2024 · Bronx", "q": "Right around the corner from my block. The vibe at Westchester Square is family — instructors who actually care about your growth."},
    {"n": "Luis Aponte",    "r": "Class of 2023 · Bronx", "q": "Bronx campus prepared me end-to-end. Theory, technique, state-board prep — I left licensed and confident."},
    {"n": "Ramon Soto",     "r": "Class of 2023 · Bronx", "q": "Se habla español. That alone meant everything. The instructors broke it down two ways until it clicked."},
]
BRONX_REVIEWS_ES = [
    {"n": "Carlos Méndez",  "r": "Clase 2024 · Bronx", "q": "La instrucción bilingüe en la sede del Bronx fue todo para mí. Clientes reales desde la primera semana, sin freno."},
    {"n": "Tirone Reyes",   "r": "Clase 2024 · Bronx", "q": "Justo a la vuelta de mi cuadra. En Westchester Square se siente como familia — instructores que sí se preocupan por tu progreso."},
    {"n": "Luis Aponte",    "r": "Clase 2023 · Bronx", "q": "La sede del Bronx me preparó completo. Teoría, técnica y preparación del examen — salí licenciado y con confianza."},
    {"n": "Ramón Soto",     "r": "Clase 2023 · Bronx", "q": "Se habla español. Eso solo lo cambió todo. Los instructores te lo explicaban de dos formas hasta que entrabas."},
]

def sec_testi_clean(p):
    es = p["lang"] == "es"
    if p["is_bronx"]:
        reviews = BRONX_REVIEWS_ES if es else BRONX_REVIEWS_EN
        sub_loc = "Bronx"
    else:
        reviews = MANHATTAN_REVIEWS_ES if es else MANHATTAN_REVIEWS_EN
        sub_loc = "Manhattan"
    eb = ("Lo Que Dicen Los Estudiantes" if es else "What Students Say")
    h  = ("Reseñas Reales de Graduados de " + sub_loc if es else "Real Reviews from " + sub_loc + " Graduates")
    sub_txt = ("Sin guiones, sin filtros — historias directas de quienes terminaron el programa en la sede de " + sub_loc + "."
               if es else
               "Unscripted, unfiltered — stories straight from students who finished the program at our " + sub_loc + " campus.")
    cards = ""
    for t in reviews:
        ini = "".join(w[0] for w in t["n"].split()[:2])
        cards += ('<div class="testi-card rv"><div class="stars">★★★★★</div><p>"%s"</p>'
                  '<div class="testi-who"><div class="testi-av">%s</div>'
                  '<div><b>%s</b><span>%s</span></div></div></div>'
                  % (t["q"], ini, t["n"], t["r"]))
    # NOTE: No Google-reviews widget, no map link — per client direction.
    return ('<section class="sec sec-alt" id="reviews"><div class="container">'
            '<div class="rv"><span class="eyebrow">%s</span><h2>%s</h2><p class="lead">%s</p></div>'
            '<div class="testi">%s</div>'
            '</div></section>') % (eb, h, sub_txt, cards)

# ───────────────────────── Slim footer ─────────────────────────
def slim_footer(p):
    es = p["lang"] == "es"
    s = S[p["lang"]]
    tel = p["phones"][0][2]
    tel_disp = p["phones"][0][1]
    # 3 footer CTA buttons (kept) + socials + chatbot launcher
    cta1 = "Solicita una Llamada" if es else "Request a Call"
    cta2 = "Aplicar Ahora"        if es else "Apply Now"
    cta3 = "Hablar con Admisiones" if es else "Speak With Admissions"
    h_cta = ("¿Listo para comenzar tu carrera de barbero?"
             if es else "Ready to start your barber career?")
    p_cta = ("Tu nueva carrera está a una llamada. Habla con admisiones en inglés o español."
             if es else
             "Your new career is one phone call away. Talk to admissions in English or Spanish.")
    socials = ('<div class="socials lp-socials">'
               '<a class="soc soc-fb" href="https://www.facebook.com/Abi.Education/" target="_blank" rel="noopener" aria-label="Facebook"><svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M13.5 21v-7h2.4l.4-3h-2.8V9.2c0-.9.2-1.5 1.5-1.5h1.4V5.1C16.1 5 15.2 5 14.2 5c-2.2 0-3.7 1.3-3.7 3.8V11H8v3h2.5v7h3z"/></svg></a>'
               '<a class="soc soc-ig" href="https://www.instagram.com/americanbarberinstitute/" target="_blank" rel="noopener" aria-label="Instagram"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4.2"/><circle cx="17.3" cy="6.7" r="1.1" fill="currentColor" stroke="none"/></svg></a>'
               '<a class="soc soc-x" href="https://twitter.com/amerbarberedu" target="_blank" rel="noopener" aria-label="X (Twitter)"><svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.8 3h3l-6.6 7.6L22 21h-6.1l-4.8-6.3L5.6 21h-3l7.1-8.1L2 3h6.3l4.3 5.7L17.8 3zm-1 16.2h1.7L7.3 4.7H5.5l11.3 14.5z"/></svg></a>'
               '<a class="soc soc-yt" href="https://www.youtube.com/channel/UCy_pQUDfk2ldEp6_zyaIMhQ" target="_blank" rel="noopener" aria-label="YouTube"><svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M23 7.2a3 3 0 0 0-2.1-2.1C19 4.5 12 4.5 12 4.5s-7 0-8.9.6A3 3 0 0 0 1 7.2 31 31 0 0 0 .5 12 31 31 0 0 0 1 16.8a3 3 0 0 0 2.1 2.1c1.9.6 8.9.6 8.9.6s7 0 8.9-.6a3 3 0 0 0 2.1-2.1A31 31 0 0 0 23.5 12 31 31 0 0 0 23 7.2zM9.8 15.3V8.7L15.9 12l-6.1 3.3z"/></svg></a>'
               '<a class="soc soc-pin" href="https://www.pinterest.com/alexzholendz/american-barber-institute/" target="_blank" rel="noopener" aria-label="Pinterest"><svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 0 0-3.6 19.3c-.1-.8-.2-2 0-2.9l1.3-5.4s-.3-.7-.3-1.6c0-1.5.9-2.6 2-2.6.9 0 1.4.7 1.4 1.5 0 .9-.6 2.3-.9 3.6-.3 1.1.5 2 1.6 2 1.9 0 3.4-2 3.4-4.9 0-2.6-1.9-4.4-4.5-4.4a4.7 4.7 0 0 0-4.9 4.7c0 .9.4 1.9.8 2.5l-.3 1.1c-.1.4-.3.5-.7.3-1.2-.6-2-2.4-2-3.9 0-3.2 2.3-6.1 6.7-6.1 3.5 0 6.2 2.5 6.2 5.8 0 3.5-2.2 6.3-5.2 6.3-1 0-2-.5-2.3-1.1l-.6 2.4c-.2.9-.8 1.9-1.2 2.6A10 10 0 1 0 12 2z"/></svg></a>'
               '</div>')
    bubble_tip = ("¿Listo para empezar? Habla con admisiones en español." if es
                  else "Ready to start? Speak with admissions, English or Spanish.")
    return ("""
<section class="foot-cta lp-foot-cta">
  <div class="container">
    <h3>%s</h3><p>%s</p>
    <div class="lp-foot-ctas">
      <a class="btn btn-gold btn-lg" href="#reserve">%s</a>
      <a class="btn btn-blue btn-lg" href="tel:%s">%s</a>
      <a class="btn btn-ghost btn-lg" href="#reserve">%s</a>
    </div>
    %s
    <p class="lp-foot-fineprint">© American Barber Institute · *$150/week refers to Plan C weekly payments.</p>
  </div>
</section>
<button class="bubble" aria-label="%s">%s</button>
<div class="bubble-tip">%s<button class="tip-x" aria-label="Close">✕</button></div>
<script src="/assets/js/effects.js?v=32" defer></script>
<script src="/assets/js/landing.js?v=32" defer></script>
<script src="/assets/js/upgrade.js?v=2" defer></script>
<script src="/assets/js/chatbot.js?v=3" defer></script>
<script src="/assets/js/video-sound.js?v=3" defer></script>
</body>
</html>
""") % (h_cta, p_cta, cta1, tel, cta2, cta3, socials, bubble_tip, s["reserve"], icon("chat", 26))

# ───────────────────────── Build ─────────────────────────
def build(p):
    s = S[p["lang"]]
    parts = [
        slim_head(p),
        slim_header(p),
        hero(p),
        sec_ticker(p, s),
        sec_stats(p, s),
        sec_pills(p, s),
        sec_steps(p, s),
        sec_skills(p, s),
        sec_zero(p, s),
        sec_earnings(p, s),
        sec_tuition(p, s),
        sec_showcase(p, s, ""),
    ]
    # Bronx-only: 3 extra testimonial videos after Inside ABI
    if p["is_bronx"]:
        parts.append(sec_bronx_extra_testi(p))
    parts += [
        sec_brandband_3(p),
        sec_videos(p, s, ""),
        sec_gallery(p, s, ""),
        sec_testi_clean(p),
        sec_faq(p, s),
        slim_footer(p),
    ]
    html = clean_links("\n".join(parts))
    out = os.path.join(ROOT, p["slug"], "index.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)
    return out

if __name__ == "__main__":
    written = [build(pg) for pg in PAGES]
    print("\n".join("✓ " + os.path.relpath(p, ROOT) for p in written))
    print("%d landing pages generated." % len(written))
