#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ABI Landing Funnels — fresh, isolated page generator.

Produces 4 conversion-focused landing pages under ``landing-funnels/``:

  500-hours-master-barber-program-landing-page/index.html       Manhattan EN
  500-hours-master-barber-program-landing-page/spanish/index.html  Manhattan ES
  master-barber-program-bronx/index.html                        Bronx EN
  master-barber-program-bronx/spanish/index.html                Bronx ES

This script imports NOTHING from the main marketing site's code. Run with::

    python3 src/build.py

(from inside ``landing-funnels/``).
"""
import os
import sys
import json
import datetime
import html
from html import escape as h

# Make ``data.py`` importable when running from anywhere.
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import data as D

SITE = "https://abi-landing-funnels.vercel.app"   # placeholder; overwritten if deployed elsewhere
CSS_V = "3"
JS_V  = "3"


# ── icons (small inline SVG library, no external font icons) ────────
ICONS = {
    "phone":      '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.2a2 2 0 0 1 2.1-.5c.9.3 1.9.6 2.8.7a2 2 0 0 1 1.7 2z"/>',
    "shield":     '<path d="M12 22s8-3.5 8-10V5l-8-3-8 3v7c0 6.5 8 10 8 10z"/><path d="m9 11.5 2 2 4-4.5"/>',
    "scissors":   '<circle cx="6" cy="6" r="3"/><circle cx="6" cy="18" r="3"/><line x1="20" y1="4" x2="8.12" y2="15.88"/><line x1="14.47" y1="14.48" x2="20" y2="20"/><line x1="8.12" y1="8.12" x2="12" y2="12"/>',
    "wallet":     '<rect x="2" y="6" width="20" height="13" rx="2"/><path d="M16 13a2 2 0 1 0 0-4h4v4z"/>',
    "briefcase":  '<rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 7V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v2M2 13h20"/>',
    "graduation": '<path d="m22 9-10-4-10 4 10 4 10-4z"/><path d="M6 11v5a6 6 0 0 0 12 0v-5"/>',
    "store":      '<path d="M3 7h18l-1 5H4z"/><path d="M5 12v9h14v-9"/>',
    "users":      '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>',
    "languages":  '<path d="m5 8 6 6"/><path d="m4 14 6-6 2-3"/><path d="M2 5h12"/><path d="M7 2h1"/><path d="m22 22-5-10-5 10"/><path d="M14 18h6"/>',
    "calendar":   '<rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/>',
    "kit":        '<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M8 7V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/><line x1="12" y1="11" x2="12" y2="15"/><line x1="10" y1="13" x2="14" y2="13"/>',
    "play":       '<polygon points="6 4 20 12 6 20 6 4"/>',
    "mail":       '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/>',
    "chat":       '<path d="M21 12a8.5 8.5 0 0 1-8.5 8.5c-1.6 0-3-.4-4.3-1L3 21l1.6-4.8A8.5 8.5 0 1 1 21 12z"/>',
}

def svg(name, size=22, stroke=True):
    body = ICONS.get(name, "")
    attrs = 'width="%d" height="%d" viewBox="0 0 24 24"' % (size, size)
    if stroke:
        attrs += ' fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"'
    else:
        attrs += ' fill="currentColor"'
    return '<svg %s aria-hidden="true">%s</svg>' % (attrs, body)


# ── date helpers ────────────────────────────────────────────────────
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

NEXT_DATE = next_start()
NEXT_ISO  = NEXT_DATE.isoformat()


# ── SECTION BUILDERS ─────────────────────────────────────────────────

def header(p):
    lang = p["lang"]; es = lang == "es"
    addr = p["campus"]["addr_short_es" if es else "addr_short_en"]
    flag, disp, tel = p["phone"]
    en_active = "is-active" if not es else ""
    es_active = "is-active" if es else ""
    en_href = "/" + p["path"] if not es else "/" + p["alt"]
    es_href = "/" + p["alt"] if not es else "/" + p["path"]
    en_aria = ' aria-current="true"' if not es else ""
    es_aria = ' aria-current="true"' if es else ""
    return (
        '<div class="lf-topbar">%s</div>\n'
        '<header class="lf-hdr"><div class="lf-hdr__in">\n'
        '  <div class="lf-brand">\n'
        '    <img class="lf-brand__logo" src="/assets/img/logo-final.gif"'
        ' alt="American Barber Institute" width="385" height="99" fetchpriority="high">\n'
        '    <div class="lf-brand__addr">%s</div>\n'
        '  </div>\n'
        '  <div class="lf-hdr__right">\n'
        '    <a class="lf-phone" href="tel:%s">%s'
        '<b class="lf-phone__flag">%s</b>'
        '<span class="lf-phone__num">%s</span></a>\n'
        '    <div class="lf-lang" role="group" aria-label="%s">\n'
        '      <a class="%s" href="%s"%s>EN</a>\n'
        '      <a class="%s" href="%s"%s>ES</a>\n'
        '    </div>\n'
        '  </div>\n'
        '</div></header>\n'
    ) % (
        h(p["promo_strip"]), h(addr),
        h(tel), svg("phone", 16), h(flag), h(disp),
        "Idioma" if es else "Language",
        en_active, h(en_href), en_aria,
        es_active, h(es_href), es_aria,
    )


def hero(p):
    lang = p["lang"]; es = lang == "es"
    s = p["hero"]
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
    # CTAs removed from hero on desktop — handled by the fixed mobile bottom bar (.lf-mbar).
    # Desktop visitors convert via the inline form on the right of the hero.
    ctas = ""
    # Lead form (right column, conversion focus)
    name_lbl = "Tu nombre" if es else "Your name"
    phone_lbl = "Teléfono" if es else "Phone"
    email_lbl = "Email"
    msg_lbl   = "Cuéntanos sobre ti (opcional)" if es else "Tell us about yourself (optional)"
    submit    = "Solicitar Llamada" if es else "Request a Call"
    fine      = ("Te llamaremos en menos de 24 horas. Nunca compartimos tus datos."
                 if es else
                 "We'll call within 24 hours. We never share your info.")
    form = (
        '<form class="lf-form" id="reserve" method="POST" action="https://formspree.io/f/xrgpkebw">\n'
        '  <input type="hidden" name="_subject" value="ABI Landing — %(id)s">\n'
        '  <input type="hidden" name="campus" value="%(campus)s">\n'
        '  <input type="hidden" name="language" value="%(lang)s">\n'
        '  <h3 class="lf-form__h">%(h)s</h3>\n'
        '  <p class="lf-form__sub">%(sub)s</p>\n'
        '  <div class="lf-form__row"><input type="text" name="name" required placeholder="%(nm)s"></div>\n'
        '  <div class="lf-form__row lf-form__row--2">\n'
        '    <input type="tel" name="phone" required placeholder="%(ph)s">\n'
        '    <input type="email" name="email" required placeholder="%(em)s">\n'
        '  </div>\n'
        '  <div class="lf-form__row"><textarea name="message" rows="3" placeholder="%(ms)s"></textarea></div>\n'
        '  <button type="submit" class="lf-btn lf-btn--primary lf-btn--lg lf-form__submit">%(sb)s</button>\n'
        '  <p class="lf-form__fine">%(fn)s</p>\n'
        '</form>'
    ) % {
        "id": p["id"], "campus": p["campus"]["slug"], "lang": lang,
        "h": h(p["cta_primary"]),
        "sub": h("Por favor, danos tu información — un asesor te llamará." if es
                 else "Drop your info — an advisor will reach out shortly."),
        "nm": h(name_lbl), "ph": h(phone_lbl), "em": h(email_lbl), "ms": h(msg_lbl),
        "sb": h(submit), "fn": h(fine),
    }
    return (
        '<section class="lf-hero">\n'
        '  <div class="lf-wrap lf-hero__in">\n'
        '    <div class="lf-hero__copy lf-rv">\n'
        '      <h1 class="lf-h1">%s<br>%s <span style="font-family:Georgia,serif;font-weight:400;font-style:italic;color:var(--lf-sky)">%s</span></h1>\n'
        '      <p class="lf-hero__sub">%s</p>\n'
        '      <div class="lf-features">%s</div>\n'
        '      %s\n'
        '      %s\n'
        '    </div>\n'
        '    <div class="lf-hero__form lf-rv">%s</div>\n'
        '  </div>\n'
        '</section>\n'
    ) % (h(s["h1_l1"]), h(s["h1_l2"]), h(s["h1_script"]), s["sub"], feats, ctas, countdown, form)


def section_head(eyebrow, title):
    return ('<div class="lf-section__head lf-rv">'
            '<span class="lf-eyebrow">%s</span>'
            '<h2 class="lf-h2">%s</h2>'
            '</div>') % (h(eyebrow), h(title))


def section_stats(p):
    items = "".join(
        '<div class="lf-stat lf-rv"><div class="lf-stat__n">%s</div>'
        '<span class="lf-stat__label">%s</span></div>' % (h(n), h(l))
        for n, l in D.STATS[p["lang"]]
    )
    return '<section class="lf-section lf-section--tight"><div class="lf-wrap"><div class="lf-stats">%s</div></div></section>\n' % items


def section_pills(p):
    eb, ti = D.SECTION_LABELS[p["lang"]]["pills"]
    cards = "".join(
        '<div class="lf-pill lf-rv"><span class="lf-pill__icon">%s</span><span class="lf-pill__txt">%s</span></div>'
        % (svg(ic, 22), h(t)) for t, ic in D.PILLS[p["lang"]]
    )
    return ('<section class="lf-section lf-pills"><div class="lf-wrap">%s<div class="lf-pills__grid">%s</div></div></section>\n'
            % (section_head(eb, ti), cards))


def section_steps(p):
    eb, ti = D.SECTION_LABELS[p["lang"]]["steps"]
    cards = "".join(
        '<div class="lf-step lf-rv"><div class="lf-step__n">%02d</div><h3 class="lf-h3">%s</h3><p>%s</p></div>'
        % (i + 1, h(t), h(d)) for i, (t, d) in enumerate(D.STEPS[p["lang"]])
    )
    return ('<section class="lf-section lf-section--alt"><div class="lf-wrap">%s<div class="lf-steps">%s</div></div></section>\n'
            % (section_head(eb, ti), cards))


def section_earnings(p):
    eb, ti = D.SECTION_LABELS[p["lang"]]["earnings"]
    cards = "".join(
        '<div class="lf-earn-card lf-rv"><div class="lf-earn-card__amount">%s</div>'
        '<div class="lf-earn-card__role">%s</div>'
        '<div class="lf-earn-card__note">%s</div></div>'
        % (h(a), h(r), h(n)) for a, r, n in D.EARNINGS[p["lang"]]
    )
    return ('<section class="lf-section"><div class="lf-wrap">%s<div class="lf-earn">%s</div></div></section>\n'
            % (section_head(eb, ti), cards))


def section_tuition(p):
    eb, ti = D.SECTION_LABELS[p["lang"]]["tuition"]
    cards = ""
    for pl in D.TUITION[p["lang"]]:
        items = "".join('<li>%s</li>' % h(x) for x in pl["items"])
        cls = "lf-plan lf-rv" + (" lf-plan--feature" if pl["feature"] else "")
        cards += (
            '<div class="%s"><div class="lf-plan__name">%s</div>'
            '<div class="lf-plan__price">%s <span class="lf-plan__per">%s</span></div>'
            '<ul class="lf-plan__list">%s</ul></div>'
            % (cls, h(pl["name"]), h(pl["price"]), h(pl["per"]), items)
        )
    return ('<section class="lf-section lf-section--alt"><div class="lf-wrap">%s<div class="lf-tuition">%s</div></div></section>\n'
            % (section_head(eb, ti), cards))


def section_showcase(p):
    eb, ti = D.SECTION_LABELS[p["lang"]]["showcase"]
    cards = ""
    for i, (slug, en_cap, es_cap) in enumerate(D.SHOWCASE_CLIPS, 1):
        cap = es_cap if p["lang"] == "es" else en_cap
        # Direct src + preload="none" so the browser shows the poster immediately
        # and only fetches video bytes when the user taps Play. Posters are real
        # first-frame JPGs at /assets/img/lf-showcase-1..6.jpg.
        cards += (
            '<div class="lf-clip lf-rv">'
            '<video class="lf-clip__video" muted playsinline loop preload="none"'
            ' poster="/assets/img/lf-showcase-%d.jpg"'
            ' src="%s%s.mp4"></video>'
            '<button class="lf-clip__play" type="button" aria-label="%s">'
            '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M8 5v14l11-7z"/></svg>'
            '</button>'
            '<div class="lf-clip__cap">%s</div></div>'
            % (i, D.SHOWCASE_CDN_BASE, slug,
               "Reproducir" if p["lang"] == "es" else "Play",
               h(cap))
        )
    return ('<section class="lf-section"><div class="lf-wrap">%s<div class="lf-showcase">%s</div></div></section>\n'
            % (section_head(eb, ti), cards))


def section_student_voices(p):
    sv = D.STUDENT_VOICES[p["lang"]]
    media = ""
    for i, (vid, poster) in enumerate(D.STUDENT_VOICES_VIDEOS, 1):
        media += (
            '<div class="lf-reel__media"><video class="lf-reel__video" muted loop playsinline'
            ' preload="none" src="/assets/videos/%s"'
            ' poster="/assets/img/%s" aria-label="ABI student testimonial %d"></video></div>'
            % (h(vid), h(poster), i)
        )
    # Last bullet — replace the dual-campus mention with a campus-specific one,
    # so a Bronx landing page doesn't advertise the Manhattan campus and vice versa.
    is_bx = p["campus"]["slug"] == "bronx"
    if p["lang"] == "es":
        last_bullet = ("Sede del Bronx — 121 Westchester Square" if is_bx
                       else "Sede de Manhattan — 48 West 39th Street")
    else:
        last_bullet = ("Bronx Campus — 121 Westchester Square" if is_bx
                       else "Manhattan Campus — 48 West 39th Street")
    pts = list(sv["points"][:-1]) + [last_bullet]
    points = "".join('<li>%s</li>' % h(x) for x in pts)
    return (
        '<section class="lf-section"><div class="lf-wrap">\n'
        '  <div class="lf-reel lf-reel--triple lf-rv">\n'
        '    <div class="lf-section__head" style="margin-bottom:1.2rem">\n'
        '      <span class="lf-eyebrow">%s</span><h2 class="lf-h2">%s</h2>\n'
        '      <p class="lf-lead">%s</p>\n'
        '    </div>\n'
        '    <div class="lf-reel__grid">%s</div>\n'
        '    <div class="lf-reel__copy"><ul class="lf-reel__points">%s</ul></div>\n'
        '  </div>\n'
        '</div></section>\n'
    ) % (h(sv["eyebrow"]), h(sv["title"]), h(sv["sub"]), media, points)


def section_bronx_extra(p):
    if p["campus"]["slug"] != "bronx":
        return ""
    bx = D.BRONX_EXTRA[p["lang"]]
    media = ""
    for i, (vid, poster) in enumerate(D.BRONX_EXTRA_VIDEOS, 1):
        media += (
            '<div class="lf-reel__media"><video class="lf-reel__video" muted loop playsinline'
            ' preload="none" src="/assets/videos/%s"'
            ' poster="/assets/img/%s" aria-label="Bronx student testimonial %d"></video></div>'
            % (h(vid), h(poster), i)
        )
    return (
        '<section class="lf-section lf-section--alt"><div class="lf-wrap">\n'
        '  <div class="lf-reel lf-reel--triple lf-rv">\n'
        '    <div class="lf-section__head" style="margin-bottom:1.2rem">\n'
        '      <span class="lf-eyebrow">%s</span><h2 class="lf-h2">%s</h2>\n'
        '      <p class="lf-lead">%s</p>\n'
        '    </div>\n'
        '    <div class="lf-reel__grid">%s</div>\n'
        '  </div>\n'
        '</div></section>\n'
    ) % (h(bx["eyebrow"]), h(bx["title"]), h(bx["sub"]), media)


def section_videos(p):
    eb, ti = D.SECTION_LABELS[p["lang"]]["videos"]
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
    return ('<section class="lf-section"><div class="lf-wrap">%s<div class="lf-showcase">%s</div></div></section>\n'
            % (section_head(eb, ti), cards))


def section_gallery(p):
    eb, ti = D.SECTION_LABELS[p["lang"]]["gallery"]
    items = "".join(
        '<img loading="lazy" src="/assets/img/%s" alt="ABI clinic floor photo %d" width="600" height="600">'
        % (h(g), i + 1) for i, g in enumerate(D.GALLERY)
    )
    return ('<section class="lf-section lf-section--alt"><div class="lf-wrap">%s<div class="lf-gallery">%s</div></div></section>\n'
            % (section_head(eb, ti), items))


def section_reviews(p):
    key = (p["campus"]["slug"], p["lang"])
    eb, ti = D.SECTION_LABELS[p["lang"]]["reviews_bx" if p["campus"]["slug"] == "bronx" else "reviews_mh"]
    cards = ""
    for r in D.REVIEWS[key]:
        initials = "".join(w[0] for w in r["name"].split()[:2]).upper()
        cards += (
            '<div class="lf-review lf-rv">'
            '<div class="lf-review__stars">★★★★★</div>'
            '<p class="lf-review__q">"%s"</p>'
            '<div class="lf-review__who"><div class="lf-review__av">%s</div>'
            '<div><div class="lf-review__name">%s</div>'
            '<div class="lf-review__role">%s</div></div></div></div>'
            % (h(r["q"]), h(initials), h(r["name"]), h(r["role"]))
        )
    return ('<section class="lf-section"><div class="lf-wrap">%s<div class="lf-reviews">%s</div></div></section>\n'
            % (section_head(eb, ti), cards))


def section_faq(p):
    eb, ti = D.SECTION_LABELS[p["lang"]]["faq"]
    items = "".join(
        '<details class="lf-rv"><summary>%s</summary><div class="lf-faq__a">%s</div></details>'
        % (h(q), h(a)) for q, a in D.FAQ[p["lang"]]
    )
    return ('<section class="lf-section lf-section--alt"><div class="lf-wrap">%s<div class="lf-faq">%s</div></div></section>\n'
            % (section_head(eb, ti), items))


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
    # The 3 footer CTAs (Request a Call / Apply Now / Speak with Admissions) ARE
    # the sticky-footer CTA set — they live in this footer block, stuck at the
    # end of every page on both desktop and mobile. The earlier `.lf-mbar`
    # duplicate (Call/Text/Apply) has been removed.
    return (
        '<footer class="lf-footer"><div class="lf-wrap">\n'
        '  <h3 class="lf-h2">%s</h3>\n'
        '  <p>%s</p>\n'
        '  <div class="lf-footer__ctas">\n'
        '    <a class="lf-btn lf-btn--primary lf-btn--lg" href="#reserve">%s</a>\n'
        '    <a class="lf-btn lf-btn--secondary lf-btn--lg" href="tel:%s">%s</a>\n'
        '    <a class="lf-btn lf-btn--ghost lf-btn--lg" href="#reserve">%s</a>\n'
        '  </div>\n'
        '  <div class="lf-footer__socials">%s</div>\n'
        '  <p class="lf-footer__fine">%s</p>\n'
        '</div></footer>\n'
        '<button class="lf-chat" aria-label="%s">%s</button>\n'
    ) % (
        h(ft["h"]), h(ft["sub"]),
        h(ft["cta1"]), h(tel), h(ft["cta2"]), h(ft["cta3"]),
        socials, h(ft["fine"]),
        ("Chatear con admisiones" if p["lang"] == "es" else "Chat with admissions"),
        svg("chat", 26),
    )


# ── full page head + body assembly ──────────────────────────────────
def page_head(p):
    es = p["lang"] == "es"
    canonical = SITE + "/" + p["path"]
    alt_url   = SITE + "/" + p["alt"]
    en_url, es_url = (alt_url, canonical) if es else (canonical, alt_url)
    # Structured data: TradeSchool + Course + LocalBusiness for this specific campus
    ld = {
        "@context": "https://schema.org",
        "@type": ["TradeSchool", "LocalBusiness", "EducationalOrganization"],
        "name": "American Barber Institute — " + p["campus"]["name_en"],
        "url": canonical,
        "telephone": p["phone"][2],
        "image": SITE + "/assets/img/lf-og-cover.jpg",
        "description": p["desc"],
        "address": {
            "@type": "PostalAddress",
            "streetAddress": p["campus"]["addr_full_en"].split(",")[0].strip(),
            "addressLocality": "Bronx" if p["campus"]["slug"] == "bronx" else "New York",
            "addressRegion": "NY",
            "postalCode": "10461" if p["campus"]["slug"] == "bronx" else "10018",
            "addressCountry": "US",
        },
        "geo": {"@type": "GeoCoordinates",
                "latitude": p["campus"]["latlng"][0],
                "longitude": p["campus"]["latlng"][1]},
        "aggregateRating": {"@type": "AggregateRating",
                            "ratingValue": "4.6", "reviewCount": "100",
                            "bestRating": "5", "worstRating": "1"},
        "paymentAccepted": ["Cash", "Credit Card", "Financial Aid", "GI Bill", "ACCES-VR"],
    }
    course = {
        "@context": "https://schema.org",
        "@type": "Course",
        "name": "500-Hour Master Barber Program",
        "description": p["desc"],
        "provider": {"@type": "TradeSchool", "name": "American Barber Institute"},
    }
    return (
'<!DOCTYPE html>\n'
'<html lang="%(lang)s">\n'
'<head>\n'
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
'</head>\n'
'<body class="lf-page %(theme)s">\n'
    ) % {
        "lang": p["lang"],
        "title": h(p["title"]),
        "desc": h(p["desc"]),
        "canonical": h(canonical),
        "en_url": h(en_url),
        "es_url": h(es_url),
        "site": SITE,
        "oglocale": "es_ES" if es else "en_US",
        "cssv": CSS_V,
        "ld1": json.dumps(ld, ensure_ascii=False),
        "ld2": json.dumps(course, ensure_ascii=False),
        "theme": p["theme_class"],
    }


def page_tail():
    return (
'<script src="/assets/js/funnels.js?v=%s" defer></script>\n'
'</body>\n'
'</html>\n'
    ) % JS_V


def build_page(p):
    parts = [
        page_head(p),
        header(p),
        hero(p),
        section_stats(p),
        section_pills(p),
        section_steps(p),
        section_earnings(p),
        section_tuition(p),
        section_showcase(p),
    ]
    if p["campus"]["slug"] == "bronx":
        parts.append(section_bronx_extra(p))
    parts += [
        section_student_voices(p),
        section_videos(p),
        section_gallery(p),
        section_reviews(p),
        section_faq(p),
        footer(p),
        page_tail(),
    ]
    out_dir = os.path.join(ROOT, p["path"])
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "index.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("".join(parts))
    return out_path


def main():
    written = []
    for p in D.PAGES:
        written.append(build_page(p))
    for w in written:
        print("✓", os.path.relpath(w, ROOT))
    print("%d landing pages generated." % len(written))


if __name__ == "__main__":
    main()
