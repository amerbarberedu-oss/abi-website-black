#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ABI Landing Funnels — page generator (authentic-content edition).

Produces 4 conversion-focused landing pages under ``landing-funnels/``:

  500-hours-master-barber-program-landing-page/index.html       Manhattan EN
  500-hours-master-barber-program-landing-page/spanish/index.html  Manhattan ES
  master-barber-program-bronx/index.html                        Bronx EN
  master-barber-program-bronx/spanish/index.html                Bronx ES

Imports NOTHING from the main marketing site. All copy comes from data.py
(verbatim from the school's own pages). Run from inside ``landing-funnels/``::

    python3 src/build.py
"""
import os
import sys
import json
import datetime
from html import escape as h

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import data as D

SITE = "https://abi-landing-funnels.vercel.app"
CSS_V = "16"
JS_V  = "7"

# ── inline SVG icon library ─────────────────────────────────────────
ICONS = {
    "phone":      '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.2a2 2 0 0 1 2.1-.5c.9.3 1.9.6 2.8.7a2 2 0 0 1 1.7 2z"/>',
    "shield":     '<path d="M12 22s8-3.5 8-10V5l-8-3-8 3v7c0 6.5 8 10 8 10z"/><path d="m9 11.5 2 2 4-4.5"/>',
    "scissors":   '<circle cx="6" cy="6" r="3"/><circle cx="6" cy="18" r="3"/><line x1="20" y1="4" x2="8.12" y2="15.88"/><line x1="14.47" y1="14.48" x2="20" y2="20"/><line x1="8.12" y1="8.12" x2="12" y2="12"/>',
    "wallet":     '<rect x="2" y="6" width="20" height="13" rx="2"/><path d="M16 13a2 2 0 1 0 0-4h4v4z"/>',
    "briefcase":  '<rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 7V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v2M2 13h20"/>',
    "calendar":   '<rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/>',
    "store":      '<path d="M3 7h18l-1 5H4z"/><path d="M5 12v9h14v-9"/>',
    "check":      '<path d="M20 6 9 17l-5-5"/>',
    "pin":        '<path d="M12 22s7-6.2 7-12a7 7 0 1 0-14 0c0 5.8 7 12 7 12z"/><circle cx="12" cy="10" r="2.6"/>',
    "chat":       '<path d="M21 12a8.5 8.5 0 0 1-8.5 8.5c-1.6 0-3-.4-4.3-1L3 21l1.6-4.8A8.5 8.5 0 1 1 21 12z"/>',
}

def svg(name, size=22, stroke=True):
    body = ICONS.get(name, "")
    attrs = 'width="%d" height="%d" viewBox="0 0 24 24"' % (size, size)
    attrs += (' fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"'
              if stroke else ' fill="currentColor"')
    return '<svg %s aria-hidden="true">%s</svg>' % (attrs, body)


# ── date helpers (countdown rolls forward indefinitely) ─────────────
def first_monday_of_next_month(after=None):
    after = after or datetime.date.today()
    y, m = after.year, after.month + 1
    if m > 12:
        m, y = 1, y + 1
    d = datetime.date(y, m, 1)
    while d.weekday() != 0:
        d += datetime.timedelta(days=1)
    return d

def next_start():
    today = datetime.date.today()
    d = datetime.date(today.year, today.month, 1)
    while d.weekday() != 0:
        d += datetime.timedelta(days=1)
    if d <= today:
        d = first_monday_of_next_month(today)
    return d

NEXT_ISO = next_start().isoformat()


# ── small helpers ───────────────────────────────────────────────────
def section_head(eyebrow, title, lead=None):
    out = ('<div class="lf-section__head lf-rv">'
           '<span class="lf-eyebrow">%s</span><h2 class="lf-h2">%s</h2>' % (h(eyebrow), h(title)))
    if lead:
        out += '<p class="lf-lead">%s</p>' % h(lead)
    return out + '</div>'


# Campus → branded logo (each image bakes in its own street address)
CAMPUS_LOGOS = {
    "manhattan": "/assets/img/logo-manhattan.png",
    "bronx":     "/assets/img/logo-bronx.png",
}

# ── HEADER (slim — campus-branded logo + phone + EN/ES) ─────────────
# Each campus logo already contains the street address baked into the
# artwork, so we don't render a duplicate text address line in the header.
def header(p):
    es = p["lang"] == "es"
    addr = p["campus"]["addr_short_es" if es else "addr_short_en"]
    flag, disp, tel = p["phone"]
    en_href = "/" + p["path"] if not es else "/" + p["alt"]
    es_href = "/" + p["alt"] if not es else "/" + p["path"]
    logo_src = CAMPUS_LOGOS[p["campus"]["slug"]]
    # Topbar phone chips (campus-aware: 2 for Manhattan, 1 for Bronx)
    chips = "".join(
        '<a class="lf-topbar__chip" href="tel:%s">%s<b>%s</b> <span>%s</span></a>' % (
            h(ph["tel"]), svg("phone", 14), h(ph["label"]), h(ph["display"])
        )
        for ph in D.TOPBAR_PHONES_BY_CAMPUS[p["campus"]["slug"]]
    )
    seats_kicker, seats_lead = D.SEATS_BANNER[p["lang"]]
    return (
        '<div class="lf-topbar">\n'
        '  <p class="lf-topbar__promo">%s</p>\n'
        '  <div class="lf-topbar__chips">%s</div>\n'
        '</div>\n'
        '<header class="lf-hdr"><div class="lf-hdr__in">\n'
        '  <a class="lf-brand lf-brand--campus" href="#reserve" aria-label="American Barber Institute — %s">\n'
        '    <img class="lf-brand__logo lf-brand__logo--campus" src="%s"'
        ' alt="American Barber Institute — %s" width="500" height="200" fetchpriority="high">\n'
        '  </a>\n'
        '  <div class="lf-hdr__right">\n'
        '    <a class="lf-phone" href="tel:%s">%s<b class="lf-phone__flag">%s</b>'
        '<span class="lf-phone__num">%s</span></a>\n'
        '    <div class="lf-lang" role="group" aria-label="%s">\n'
        '      <a class="%s" href="%s"%s>EN</a>\n'
        '      <a class="%s" href="%s"%s>ES</a>\n'
        '    </div>\n'
        '  </div>\n'
        '</div></header>\n'
        '<div class="lf-seats" role="status">\n'
        '  <span class="lf-seats__dot" aria-hidden="true"></span>\n'
        '  <span class="lf-seats__kicker">%s</span>\n'
        '  <span class="lf-seats__lead">%s</span>\n'
        '</div>\n'
    ) % (
        h(p["promo_strip"]),
        chips,
        h(addr),
        h(logo_src), h(addr),
        h(tel), svg("phone", 16), h(flag), h(disp),
        "Idioma" if es else "Language",
        "is-active" if not es else "", h(en_href), ' aria-current="true"' if not es else "",
        "is-active" if es else "", h(es_href), ' aria-current="true"' if es else "",
        h(seats_kicker), h(seats_lead),
    )


# ── MOBILE HERO (image-led, mobile-only — hidden on desktop via CSS) ─
def mobile_hero(p):
    lang = p["lang"]; es = lang == "es"
    H_ = D.HERO[lang]
    is_bx = p["campus"]["slug"] == "bronx"
    kicker = H_["kicker_bx"] if is_bx else H_["kicker_man"]
    cta_label = "Reserve Your Spot" if not es else "Reserva Tu Lugar"
    return (
        '<section class="lf-mhero" aria-label="American Barber Institute clinic floor">\n'
        '  <img class="lf-mhero__bg" src="/assets/img/lf-hero-mobile.jpg"'
        ' alt="ABI students training on the clinic floor" loading="eager"'
        ' fetchpriority="high" width="1080" height="1609">\n'
        '  <div class="lf-mhero__scrim"></div>\n'
        '  <div class="lf-mhero__copy">\n'
        '    <p class="lf-mhero__kicker">%s</p>\n'
        '    <h1 class="lf-mhero__h1">%s <span>%s</span> <em>%s</em></h1>\n'
        '    <a class="lf-btn lf-btn--primary lf-btn--lg lf-mhero__cta" href="#reserve">%s</a>\n'
        '  </div>\n'
        '</section>\n'
    ) % (h(kicker), h(H_["h1_a"]), h(H_["h1_b"]), h(H_["h1_script"]), h(cta_label))


# ── HERO ─────────────────────────────────────────────────────────────
def hero(p):
    lang = p["lang"]; es = lang == "es"
    H_ = D.HERO[lang]
    is_bx = p["campus"]["slug"] == "bronx"
    kicker = H_["kicker_bx"] if is_bx else H_["kicker_man"]
    sub    = H_["sub_bx"]    if is_bx else H_["sub_man"]
    feats = "".join(
        '<span class="lf-feature">%s<span>%s</span></span>' % (svg(ic, 18), h(t))
        for t, ic in D.FEATURES[lang]
    )
    cd = D.COUNTDOWN[lang]
    cells = "".join(
        '<div class="lf-cd__cell"><b data-cd-%s>0</b><span>%s</span></div>' % (k, h(lbl))
        for k, lbl in zip("dhms", cd["cells"])
    )
    countdown = (
        '<div class="lf-cd" data-target="%s">\n'
        '  <h2 class="lf-cd__h"><span class="lf-cd__label">%s</span>'
        ' <span class="lf-cd__date"></span></h2>\n'
        '  <p class="lf-cd__sub">%s</p>\n'
        '  <div class="lf-cd__grid">%s</div>\n'
        '</div>'
    ) % (NEXT_ISO, h(cd["label"]), h(cd["sub"]), cells)
    return (
        '<section class="lf-hero">\n'
        '  <div class="lf-wrap lf-hero__in">\n'
        '    <div class="lf-hero__copy lf-rv">\n'
        '      <p class="lf-hero__kicker">%s</p>\n'
        '      <h1 class="lf-h1">%s <span class="lf-h1__b">%s</span> '
        '<span class="lf-h1__script">%s</span></h1>\n'
        '      <p class="lf-hero__sub">%s</p>\n'
        '      <div class="lf-features">%s</div>\n'
        '      %s\n'
        '    </div>\n'
        '    %s\n'
        '  </div>\n'
        '</section>\n'
    ) % (h(kicker), h(H_["h1_a"]), h(H_["h1_b"]), h(H_["h1_script"]),
         sub, feats, countdown, lead_form(p))


def lead_form(p):
    lang = p["lang"]
    f = D.FORM[lang]
    loc_opts  = "".join('<option>%s</option>' % h(o) for o in f["loc_opts"])
    fmt_opts  = "".join('<option>%s</option>' % h(o) for o in f["fmt_opts"])
    lang_opts = "".join('<option>%s</option>' % h(o) for o in f["lang_opts"])
    return (
        '<div class="lf-hero__form lf-rv">\n'
        '<form class="lf-form" id="reserve" method="POST" action="https://formspree.io/f/xrgpkebw">\n'
        '  <input type="hidden" name="_subject" value="ABI Landing — %(id)s">\n'
        '  <input type="hidden" name="campus" value="%(campus)s">\n'
        '  <input type="hidden" name="language" value="%(lang)s">\n'
        '  <h3 class="lf-form__h">%(h)s</h3>\n'
        '  <p class="lf-form__sub">%(sub)s</p>\n'
        '  <div class="lf-form__row lf-form__row--2">'
        '<input type="text" name="first_name" required placeholder="%(first)s" autocomplete="given-name">'
        '<input type="text" name="last_name" required placeholder="%(last)s" autocomplete="family-name"></div>\n'
        '  <div class="lf-form__row lf-form__row--2">'
        '<input type="tel" name="phone" required placeholder="%(phone)s" autocomplete="tel">'
        '<input type="email" name="email" required placeholder="%(email)s" autocomplete="email"></div>\n'
        '  <div class="lf-form__row"><label class="lf-form__label">%(loc_label)s</label>'
        '<select name="campus_pref" required>%(loc_opts)s</select></div>\n'
        '  <div class="lf-form__row"><label class="lf-form__label">%(fmt_label)s</label>'
        '<select name="format" required>%(fmt_opts)s</select></div>\n'
        '  <div class="lf-form__row"><label class="lf-form__label">%(lang_label)s</label>'
        '<select name="preferred_language" required>%(lang_opts)s</select></div>\n'
        '  <div class="lf-form__row"><label class="lf-form__label">%(msg_label)s</label>'
        '<textarea name="message" rows="4" placeholder="%(msg_ph)s"></textarea></div>\n'
        '  <button type="submit" class="lf-btn lf-btn--primary lf-btn--lg lf-form__submit">%(submit)s</button>\n'
        '  <p class="lf-form__fine">%(consent)s</p>\n'
        '</form></div>'
    ) % {
        "id": p["id"], "campus": p["campus"]["slug"], "lang": lang,
        "h": h(f["h"]), "sub": h(f["sub"]),
        "first": h(f["first"]), "last": h(f["last"]),
        "phone": h(f["phone"]), "email": h(f["email"]),
        "loc_label": h(f["loc_label"]), "loc_opts": loc_opts,
        "fmt_label": h(f["fmt_label"]), "fmt_opts": fmt_opts,
        "lang_label": h(f["lang_label"]), "lang_opts": lang_opts,
        "msg_label": h(f["msg_label"]), "msg_ph": h(f["msg_ph"]),
        "submit": h(f["submit"]), "consent": h(f["consent"]),
    }


# ── STATS ────────────────────────────────────────────────────────────
def section_stats(p):
    items = "".join(
        '<div class="lf-stat lf-rv"><div class="lf-stat__n">%s</div>'
        '<span class="lf-stat__label">%s</span></div>' % (h(n), h(l))
        for n, l in D.STATS[p["lang"]]
    )
    return ('<section class="lf-section lf-section--tight"><div class="lf-wrap">'
            '<div class="lf-stats">%s</div></div></section>\n' % items)


# ── ABOUT THE PROGRAM (verbatim, campus-specific) ────────────────────
def section_about(p):
    eb, ti = D.ABOUT_HEAD[p["lang"]]
    paras = D.ABOUT[(p["campus"]["slug"], p["lang"])]
    body = "".join('<p>%s</p>' % h(x) for x in paras)
    addr = p["campus"]["addr_full_es" if p["lang"] == "es" else "addr_full_en"]
    name = p["campus"]["name_es" if p["lang"] == "es" else "name_en"]
    dur_lbl  = "Duración" if p["lang"] == "es" else "Duration"
    tui_lbl  = "Matrícula" if p["lang"] == "es" else "Tuition"
    sch_lbl  = "Horarios" if p["lang"] == "es" else "Schedules"
    dur_val  = "~4 meses" if p["lang"] == "es" else "~4 Months"
    tui_val  = "desde $4,600" if p["lang"] == "es" else "from $4,600"
    sch_val  = ("Mañana · Tarde · Fin de semana" if p["lang"] == "es"
                else "Morning · Afternoon · Weekend")
    return (
        '<section class="lf-section lf-section--alt"><div class="lf-wrap">%s\n'
        '  <div class="lf-about">\n'
        '    <div class="lf-about__body lf-rv">%s</div>\n'
        '    <aside class="lf-about__card lf-rv">\n'
        '      <h3 class="lf-h3">%s</h3>\n'
        '      <p class="lf-about__addr">%s%s</p>\n'
        '      <p class="lf-about__phone"><a href="tel:%s">%s %s</a></p>\n'
        '      <ul class="lf-about__details">'
        '<li><b>%s:</b> %s</li><li><b>%s:</b> %s</li><li><b>%s:</b> %s</li></ul>\n'
        '    </aside>\n'
        '  </div>\n'
        '</div></section>\n'
    ) % (section_head(eb, ti), body, h(name),
         svg("pin", 14), h(addr),
         h(p["phone"][2]), svg("phone", 14), h(p["phone"][1]),
         dur_lbl, dur_val, tui_lbl, tui_val, sch_lbl, sch_val)


# ── SKILLS & TECHNIQUES ──────────────────────────────────────────────
def section_techniques(p):
    eb, ti = D.TECH_HEAD[p["lang"]]
    chips = "".join('<span class="lf-tech">%s%s</span>' % (svg("check", 15), h(t))
                    for t in D.TECHNIQUES[p["lang"]])
    return ('<section class="lf-section"><div class="lf-wrap">%s'
            '<div class="lf-tech-grid lf-rv">%s</div></div></section>\n'
            % (section_head(eb, ti), chips))


# ── COURSE MODULES (curriculum) ──────────────────────────────────────
def section_modules(p):
    eb, ti = D.MODULES_HEAD[p["lang"]]
    cards = ""
    for i, (name, items) in enumerate(D.MODULES[p["lang"]], 1):
        lis = "".join('<li>%s</li>' % h(x) for x in items)
        cards += ('<div class="lf-module lf-rv"><div class="lf-module__n">%02d</div>'
                  '<h3 class="lf-h3">%s</h3><ul class="lf-module__list">%s</ul></div>'
                  % (i, h(name), lis))
    return ('<section class="lf-section lf-section--alt"><div class="lf-wrap">%s'
            '<div class="lf-modules">%s</div></div></section>\n'
            % (section_head(eb, ti), cards))


# ── TUITION ──────────────────────────────────────────────────────────
def section_tuition(p):
    eb, ti = D.TUITION_HEAD[p["lang"]]
    note = D.TUITION_NOTE[p["lang"]]
    popular = "Más Popular" if p["lang"] == "es" else "Most Popular"
    cards = ""
    for pl in D.TUITION[p["lang"]]:
        cls = "lf-plan lf-rv" + (" lf-plan--feature" if pl["feature"] else "")
        badge = ('<span class="lf-plan__badge">%s</span>' % popular) if pl["feature"] else ""
        cards += (
            '<div class="%s">%s<div class="lf-plan__name">%s</div>'
            '<div class="lf-plan__sched">%s</div>'
            '<div class="lf-plan__hours">%s</div>'
            '<div class="lf-plan__price">%s</div>'
            '<div class="lf-plan__terms">%s</div>'
            '<a class="lf-btn lf-btn--primary lf-plan__cta" href="#reserve">%s</a></div>'
            % (cls, badge, h(pl["name"]), h(pl["sched"]), h(pl["hours"]),
               h(pl["price"]), h(pl["terms"]),
               "¡Hagámoslo!" if p["lang"] == "es" else "Let's Do It")
        )
    return ('<section class="lf-section"><div class="lf-wrap">%s'
            '<div class="lf-tuition">%s</div>'
            '<p class="lf-tuition__note lf-rv">%s</p></div></section>\n'
            % (section_head(eb, ti, note if False else None), cards, h(note)))


# ── ENTRANCE REQUIREMENTS ────────────────────────────────────────────
def section_requirements(p):
    eb, ti = D.REQ_HEAD[p["lang"]]
    items = "".join('<li class="lf-req lf-rv">%s<span>%s</span></li>' % (svg("check", 18), h(x))
                    for x in D.REQUIREMENTS[p["lang"]])
    return ('<section class="lf-section lf-section--alt"><div class="lf-wrap">%s'
            '<ul class="lf-reqs">%s</ul></div></section>\n'
            % (section_head(eb, ti), items))


# ── INSIDE ABI (showcase clips) ──────────────────────────────────────
def section_showcase(p):
    eb, ti = D.SHOWCASE_HEAD[p["lang"]]
    lead = D.SHOWCASE_LEAD[p["lang"]]
    cards = ""
    for i, (slug, en_cap, es_cap) in enumerate(D.SHOWCASE_CLIPS, 1):
        cap = es_cap if p["lang"] == "es" else en_cap
        cards += (
            '<div class="lf-clip lf-rv">'
            '<video class="lf-clip__video" muted playsinline loop preload="none"'
            ' poster="/assets/img/lf-showcase-%d.jpg" src="%s%s.mp4"></video>'
            '<button class="lf-clip__play" type="button" aria-label="%s">'
            '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M8 5v14l11-7z"/></svg>'
            '</button><div class="lf-clip__cap">%s</div></div>'
            % (i, D.SHOWCASE_CDN_BASE, slug,
               "Reproducir" if p["lang"] == "es" else "Play", h(cap))
        )
    return ('<section class="lf-section"><div class="lf-wrap">%s'
            '<div class="lf-showcase">%s</div></div></section>\n'
            % (section_head(eb, ti, lead), cards))


# ── reel video block helper (used by student voices + bronx extra) ──
PLAY_BTN = ('<button class="lf-reel__play" type="button" aria-label="Play video">'
            '<svg class="lf-reel__icon-play" viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5v14l11-7z"/></svg>'
            '<svg class="lf-reel__icon-pause" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 5h4v14H6zM14 5h4v14h-4z"/></svg>'
            '</button>')

def _reel_media(vid, poster, label):
    return ('<div class="lf-reel__media"><video class="lf-reel__video" muted loop playsinline'
            ' preload="none" src="/assets/videos/%s" poster="/assets/img/%s"'
            ' aria-label="%s"></video>%s</div>' % (h(vid), h(poster), h(label), PLAY_BTN))


def section_student_voices(p):
    sv = D.STUDENT_VOICES[p["lang"]]
    media = "".join(_reel_media(v, ps, "ABI student testimonial %d" % i)
                    for i, (v, ps) in enumerate(D.STUDENT_VOICES_VIDEOS, 1))
    return (
        '<section class="lf-section lf-section--alt"><div class="lf-wrap">\n'
        '  <div class="lf-reel lf-reel--triple lf-rv">\n'
        '    <div class="lf-section__head" style="margin-bottom:1.2rem">'
        '<span class="lf-eyebrow">%s</span><h2 class="lf-h2">%s</h2>'
        '<p class="lf-lead">%s</p></div>\n'
        '    <div class="lf-reel__grid">%s</div>\n'
        '  </div>\n'
        '</div></section>\n'
    ) % (h(sv["eyebrow"]), h(sv["title"]), h(sv["sub"]), media)


def section_bronx_extra(p):
    if p["campus"]["slug"] != "bronx":
        return ""
    bx = D.BRONX_EXTRA[p["lang"]]
    media = "".join(_reel_media(v, ps, "Bronx student testimonial %d" % i)
                    for i, (v, ps) in enumerate(D.BRONX_EXTRA_VIDEOS, 1))
    return (
        '<section class="lf-section"><div class="lf-wrap">\n'
        '  <div class="lf-reel lf-reel--triple lf-rv">\n'
        '    <div class="lf-section__head" style="margin-bottom:1.2rem">'
        '<span class="lf-eyebrow">%s</span><h2 class="lf-h2">%s</h2>'
        '<p class="lf-lead">%s</p></div>\n'
        '    <div class="lf-reel__grid">%s</div>\n'
        '  </div>\n'
        '</div></section>\n'
    ) % (h(bx["eyebrow"]), h(bx["title"]), h(bx["sub"]), media)


# ── WATCH US (YouTube) ───────────────────────────────────────────────
def section_videos(p):
    eb, ti = D.YT_HEAD[p["lang"]]
    cards = ""
    for vid, en_cap, es_cap in D.YT_CLIPS:
        cap = es_cap if p["lang"] == "es" else en_cap
        cards += (
            '<div class="lf-clip lf-rv">'
            '<a href="https://www.youtube.com/watch?v=%s" target="_blank" rel="noopener">'
            '<img loading="lazy" src="https://i.ytimg.com/vi/%s/hqdefault.jpg" alt="%s"'
            ' width="480" height="360" style="width:100%%;height:100%%;object-fit:cover"></a>'
            '<div class="lf-clip__cap">▶ %s</div></div>'
            % (vid, vid, h(cap), h(cap))
        )
    return ('<section class="lf-section"><div class="lf-wrap">%s'
            '<div class="lf-showcase">%s</div></div></section>\n'
            % (section_head(eb, ti), cards))


# ── GALLERY ──────────────────────────────────────────────────────────
def section_gallery(p):
    eb, ti = D.GALLERY_HEAD[p["lang"]]
    items = "".join(
        '<img loading="lazy" src="/assets/img/%s" alt="ABI clinic floor photo %d" width="600" height="600">'
        % (h(g), i + 1) for i, g in enumerate(D.GALLERY)
    )
    return ('<section class="lf-section lf-section--alt"><div class="lf-wrap">%s'
            '<div class="lf-gallery">%s</div></div></section>\n'
            % (section_head(eb, ti), items))


# ── REVIEWS (split per campus; real Google reviews, no widget) ──────
def section_reviews(p):
    eb, ti = D.REVIEWS_HEAD[p["lang"]]
    lead = D.REVIEWS_LEAD[p["lang"]]
    cards = ""
    campus_slug = p["campus"]["slug"]
    for r in D.REVIEWS_BY_CAMPUS[campus_slug][p["lang"]]:
        ini = "".join(w[0] for w in r["name"].split()[:2]).upper()
        cards += (
            '<div class="lf-review lf-rv"><div class="lf-review__stars">★★★★★</div>'
            '<p class="lf-review__q">“%s”</p>'
            '<div class="lf-review__who"><div class="lf-review__av">%s</div>'
            '<div><div class="lf-review__name">%s</div>'
            '<div class="lf-review__role">%s</div></div></div></div>'
            % (h(r["q"]), h(ini), h(r["name"]), h(r["role"]))
        )
    return ('<section class="lf-section"><div class="lf-wrap">%s'
            '<div class="lf-reviews">%s</div></div></section>\n'
            % (section_head(eb, ti, lead), cards))


# ── CONTACT BOX (campus-aware: Manhattan = 2 numbers, Bronx = 1) ─────
def section_contact(p):
    lang = p["lang"]
    eb, ti = D.CONTACT_HEAD[lang]
    L = D.CONTACT_LABELS[lang]
    campus_slug = p["campus"]["slug"]
    addr = p["campus"]["addr_full_es" if lang == "es" else "addr_full_en"]
    name = p["campus"]["name_es" if lang == "es" else "name_en"]
    lat, lng = p["campus"]["latlng"]
    maps_url = "https://www.google.com/maps/search/?api=1&query=%s,%s" % (lat, lng)

    phone_items = ""
    for ph in D.CONTACT_PHONES_BY_CAMPUS[campus_slug]:
        tag = L[ph["label_key"]]
        phone_items += (
            '<li class="lf-contact__phone">'
            '<a href="tel:%s">%s<span class="lf-contact__num">%s</span></a>'
            '<span class="lf-contact__tag">%s</span></li>'
            % (h(ph["tel"]), svg("phone", 16), h(ph["display"]), h(tag))
        )

    return (
        '<section class="lf-section lf-section--alt" id="contact"><div class="lf-wrap">%s\n'
        '  <div class="lf-contact lf-rv">\n'
        '    <div class="lf-contact__card">\n'
        '      <h3 class="lf-h3">%s</h3>\n'
        '      <p class="lf-contact__row"><span class="lf-contact__label">%s</span>'
        '<span class="lf-contact__val">%s%s · '
        '<a class="lf-contact__map" href="%s" target="_blank" rel="noopener">%s →</a></span></p>\n'
        '      <p class="lf-contact__row"><span class="lf-contact__label">%s</span>'
        '<ul class="lf-contact__phones">%s</ul></p>\n'
        '      <p class="lf-contact__row"><span class="lf-contact__label">%s</span>'
        '<a class="lf-contact__val" href="mailto:%s">%s</a></p>\n'
        '      <p class="lf-contact__row"><span class="lf-contact__label">%s</span>'
        '<span class="lf-contact__val">%s</span></p>\n'
        '    </div>\n'
        '  </div>\n'
        '</div></section>\n'
    ) % (
        section_head(eb, ti),
        h(name),
        h(L["addr"]), svg("pin", 14), h(addr), h(maps_url), h(L["directions"]),
        h(L["phone"]), phone_items,
        h(L["email"]), h(D.CONTACT_EMAIL), h(D.CONTACT_EMAIL),
        h(L["hours"]), h(D.CONTACT_HOURS[lang]),
    )


# ── FAQ ──────────────────────────────────────────────────────────────
def section_faq(p):
    eb, ti = D.FAQ_HEAD[p["lang"]]
    items = "".join(
        '<details class="lf-rv"><summary>%s</summary><div class="lf-faq__a">%s</div></details>'
        % (h(q), h(a)) for q, a in D.faq(p["lang"], p["phone"][1])
    )
    return ('<section class="lf-section lf-section--alt"><div class="lf-wrap">%s'
            '<div class="lf-faq">%s</div></div></section>\n'
            % (section_head(eb, ti), items))


# ── FOOTER (3 CTAs kept here as the single sticky CTA set) ──────────
def footer(p):
    ft = D.FOOTER[p["lang"]]
    tel = p["phone"][2]
    socials = (
        '<a class="lf-soc" href="https://www.facebook.com/Abi.Education/" target="_blank" rel="noopener" aria-label="Facebook"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M13.5 21v-7h2.4l.4-3h-2.8V9.2c0-.9.2-1.5 1.5-1.5h1.4V5.1C16.1 5 15.2 5 14.2 5c-2.2 0-3.7 1.3-3.7 3.8V11H8v3h2.5v7h3z"/></svg></a>'
        '<a class="lf-soc" href="https://www.instagram.com/americanbarberinstitute/" target="_blank" rel="noopener" aria-label="Instagram"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4.2"/><circle cx="17.3" cy="6.7" r="1.1" fill="currentColor" stroke="none"/></svg></a>'
        '<a class="lf-soc" href="https://twitter.com/amerbarberedu" target="_blank" rel="noopener" aria-label="X"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M17.8 3h3l-6.6 7.6L22 21h-6.1l-4.8-6.3L5.6 21h-3l7.1-8.1L2 3h6.3l4.3 5.7L17.8 3z"/></svg></a>'
        '<a class="lf-soc" href="https://www.youtube.com/channel/UCy_pQUDfk2ldEp6_zyaIMhQ" target="_blank" rel="noopener" aria-label="YouTube"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M23 7.2a3 3 0 0 0-2.1-2.1C19 4.5 12 4.5 12 4.5s-7 0-8.9.6A3 3 0 0 0 1 7.2 31 31 0 0 0 .5 12 31 31 0 0 0 1 16.8a3 3 0 0 0 2.1 2.1c1.9.6 8.9.6 8.9.6s7 0 8.9-.6a3 3 0 0 0 2.1-2.1A31 31 0 0 0 23.5 12 31 31 0 0 0 23 7.2zM9.8 15.3V8.7L15.9 12z"/></svg></a>'
        '<a class="lf-soc" href="https://www.pinterest.com/alexzholendz/american-barber-institute/" target="_blank" rel="noopener" aria-label="Pinterest"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2a10 10 0 0 0-3.6 19.3c-.1-.8-.2-2 0-2.9l1.3-5.4s-.3-.7-.3-1.6c0-1.5.9-2.6 2-2.6.9 0 1.4.7 1.4 1.5 0 .9-.6 2.3-.9 3.6-.3 1.1.5 2 1.6 2 1.9 0 3.4-2 3.4-4.9 0-2.6-1.9-4.4-4.5-4.4a4.7 4.7 0 0 0-4.9 4.7c0 .9.4 1.9.8 2.5l-.3 1.1c-.1.4-.3.5-.7.3-1.2-.6-2-2.4-2-3.9 0-3.2 2.3-6.1 6.7-6.1 3.5 0 6.2 2.5 6.2 5.8 0 3.5-2.2 6.3-5.2 6.3-1 0-2-.5-2.3-1.1l-.6 2.4c-.2.9-.8 1.9-1.2 2.6A10 10 0 1 0 12 2z"/></svg></a>'
    )
    addr = p["campus"]["addr_full_es" if p["lang"] == "es" else "addr_full_en"]
    return (
        '<footer class="lf-footer"><div class="lf-wrap">\n'
        '  <h3 class="lf-h2">%s</h3>\n'
        '  <p>%s</p>\n'
        '  <p class="lf-footer__addr">%s%s · <a href="tel:%s">%s</a></p>\n'
        '  <div class="lf-footer__socials">%s</div>\n'
        '  <p class="lf-footer__fine">%s</p>\n'
        '</div></footer>\n'
        '<button class="lf-chat" aria-label="%s">%s</button>\n'
    ) % (
        h(ft["h"]), h(ft["sub"]),
        svg("pin", 14), h(addr), h(p["phone"][2]), h(p["phone"][1]),
        socials, h(ft["fine"]),
        ("Chatear con admisiones" if p["lang"] == "es" else "Chat with admissions"),
        svg("chat", 26),
    )


# ── HEAD ─────────────────────────────────────────────────────────────
def page_head(p):
    es = p["lang"] == "es"
    canonical = SITE + "/" + p["path"]
    alt_url   = SITE + "/" + p["alt"]
    en_url, es_url = (alt_url, canonical) if es else (canonical, alt_url)
    ld = {
        "@context": "https://schema.org",
        "@type": ["TradeSchool", "LocalBusiness", "EducationalOrganization"],
        "name": "American Barber Institute — " + p["campus"]["name_en"],
        "url": canonical, "telephone": p["phone"][2],
        "image": SITE + "/assets/img/lf-og-cover.jpg", "description": p["desc"],
        "foundingDate": "1996",
        "address": {"@type": "PostalAddress",
                    "streetAddress": p["campus"]["addr_full_en"].split(",")[0].strip(),
                    "addressLocality": "Bronx" if p["campus"]["slug"] == "bronx" else "New York",
                    "addressRegion": "NY",
                    "postalCode": "10461" if p["campus"]["slug"] == "bronx" else "10018",
                    "addressCountry": "US"},
        "geo": {"@type": "GeoCoordinates",
                "latitude": p["campus"]["latlng"][0], "longitude": p["campus"]["latlng"][1]},
        "aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.6",
                            "reviewCount": "100", "bestRating": "5", "worstRating": "1"},
        "paymentAccepted": ["Cash", "Credit Card", "Financial Aid", "GI Bill", "ACCES-VR"],
    }
    course = {
        "@context": "https://schema.org", "@type": "Course",
        "name": "500-Hour Master Barber Program", "description": p["desc"],
        "provider": {"@type": "TradeSchool", "name": "American Barber Institute"},
    }
    return (
'<!DOCTYPE html>\n<html lang="%(lang)s">\n<head>\n'
'<meta charset="utf-8">\n'
'<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
'<title>%(title)s</title>\n'
'<meta name="description" content="%(desc)s">\n'
'<link rel="canonical" href="%(canonical)s">\n'
'<link rel="alternate" hreflang="en" href="%(en_url)s">\n'
'<link rel="alternate" hreflang="en-US" href="%(en_url)s">\n'
'<link rel="alternate" hreflang="es" href="%(es_url)s">\n'
'<link rel="alternate" hreflang="es-US" href="%(es_url)s">\n'
'<link rel="alternate" hreflang="x-default" href="%(en_url)s">\n'
'<meta property="og:title" content="%(title)s">\n'
'<meta property="og:description" content="%(desc)s">\n'
'<meta property="og:type" content="website">\n'
'<meta property="og:url" content="%(canonical)s">\n'
'<meta property="og:image" content="%(site)s/assets/img/lf-og-cover.jpg">\n'
'<meta property="og:image:width" content="1200">\n'
'<meta property="og:image:height" content="630">\n'
'<meta property="og:locale" content="%(oglocale)s">\n'
'<meta name="twitter:card" content="summary_large_image">\n'
'<meta name="twitter:title" content="%(title)s">\n'
'<meta name="twitter:description" content="%(desc)s">\n'
'<meta name="twitter:image" content="%(site)s/assets/img/lf-og-cover.jpg">\n'
'<meta name="robots" content="index, follow, max-image-preview:large">\n'
'<meta name="theme-color" content="#1b3bd9">\n'
'<link rel="icon" href="/favicon.ico" sizes="any">\n'
'<link rel="apple-touch-icon" href="/apple-icon.png">\n'
'<link rel="preconnect" href="https://fonts.googleapis.com">\n'
'<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
'<link href="https://fonts.googleapis.com/css2?family=Oswald:wght@400;500;600;700&family=Inter:wght@400;500;600;700&family=Poppins:wght@400;500;600;700;800&display=swap" rel="stylesheet">\n'
'<link rel="stylesheet" href="/assets/css/funnels.css?v=%(cssv)s">\n'
'<script type="application/ld+json">%(ld1)s</script>\n'
'<script type="application/ld+json">%(ld2)s</script>\n'
'</head>\n<body class="lf-page %(theme)s">\n'
    ) % {
        "lang": p["lang"], "title": h(p["title"]), "desc": h(p["desc"]),
        "canonical": h(canonical), "en_url": h(en_url), "es_url": h(es_url),
        "site": SITE, "oglocale": "es_ES" if es else "en_US", "cssv": CSS_V,
        "ld1": json.dumps(ld, ensure_ascii=False),
        "ld2": json.dumps(course, ensure_ascii=False), "theme": p["theme_class"],
    }


CHAT_ICON  = '<path d="M21 12a8.5 8.5 0 0 1-8.5 8.5c-1.6 0-3-.4-4.3-1L3 21l1.6-4.8A8.5 8.5 0 1 1 21 12z"/>'
SCISSORS_I = '<circle cx="6" cy="6" r="3"/><circle cx="6" cy="18" r="3"/><line x1="20" y1="4" x2="8.12" y2="15.88"/><line x1="14.47" y1="14.48" x2="20" y2="20"/><line x1="8.12" y1="8.12" x2="12" y2="12"/>'

def mobile_cta_bar(p):
    es = p["lang"] == "es"
    tel = p["phone"][2]            # +1XXXXXXXXXX
    sms_target = tel               # SMS goes to same campus number
    labels = {
        "call":  "Llamar" if es else "Call Now",
        "text":  "Mensaje" if es else "Text Us",
        "apply": "Aplicar" if es else "Apply Now",
    }
    return (
        '<nav class="lf-mcta" aria-label="%s">\n'
        '  <a class="lf-mcta__btn lf-mcta__btn--call" href="tel:%s">'
        '%s<span>%s</span></a>\n'
        '  <a class="lf-mcta__btn lf-mcta__btn--text" href="sms:%s">'
        '%s<span>%s</span></a>\n'
        '  <a class="lf-mcta__btn lf-mcta__btn--apply" href="#reserve">'
        '%s<span>%s</span></a>\n'
        '</nav>\n'
    ) % (
        "Acciones rápidas" if es else "Quick actions",
        h(tel),       svg("phone", 16),    h(labels["call"]),
        h(sms_target),
        ('<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor"'
         ' stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
         + CHAT_ICON + '</svg>'),
        h(labels["text"]),
        ('<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor"'
         ' stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
         + SCISSORS_I + '</svg>'),
        h(labels["apply"]),
    )


def page_tail():
    return '<script src="/assets/js/funnels.js?v=%s" defer></script>\n</body>\n</html>\n' % JS_V


# ── ASSEMBLE ─────────────────────────────────────────────────────────
def build_page(p):
    parts = [
        page_head(p),
        header(p),
        mobile_hero(p),
        hero(p),
        section_student_voices(p),
        section_stats(p),
        section_about(p),
        section_techniques(p),
        section_modules(p),
        section_tuition(p),
        section_requirements(p),
        section_showcase(p),
    ]
    if p["campus"]["slug"] == "bronx":
        parts.append(section_bronx_extra(p))
    parts += [
        section_videos(p),
        section_gallery(p),
        section_reviews(p),
        section_contact(p),
        section_faq(p),
        footer(p),
        mobile_cta_bar(p),
        page_tail(),
    ]
    out_dir = os.path.join(ROOT, p["path"])
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "index.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("".join(parts))
    return out_path


def main():
    written = [build_page(p) for p in D.PAGES]
    for w in written:
        print("✓", os.path.relpath(w, ROOT))
    print("%d landing pages generated." % len(written))


if __name__ == "__main__":
    main()
