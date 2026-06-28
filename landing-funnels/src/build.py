#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ABI Landing Funnels — generator (exact abi.edu replica).

4 pages under landing-funnels/:
  500-hours-master-barber-program-landing-page/index.html        Manhattan EN
  500-hours-master-barber-program-landing-page/spanish/index.html  Manhattan ES
  master-barber-program-bronx/index.html                         Bronx EN
  master-barber-program-bronx/spanish/index.html                 Bronx ES

Section order mirrors the live abi.edu pages:
  hero → Get-Trained form → 500-Hours intro → Program/haircuts → About →
  Entrance Requirements → Payment Plans (+Access-VR +GI Bill) → Gallery →
  Student Voices reel → [Bronx extra] → Our Videos (YouTube) → Reviews →
  Get-More-Info closing → footer (NO Request-a-Call / Apply / Speak CTAs).
"""
import os, sys, json, datetime
from html import escape as h

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import data as D

SITE = "https://abi-landing-funnels.vercel.app"
CSS_V = "7"
JS_V  = "7"

ICONS = {
    "phone":   '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.2a2 2 0 0 1 2.1-.5c.9.3 1.9.6 2.8.7a2 2 0 0 1 1.7 2z"/>',
    "check":   '<path d="M20 6 9 17l-5-5"/>',
    "pin":     '<path d="M12 22s7-6.2 7-12a7 7 0 1 0-14 0c0 5.8 7 12 7 12z"/><circle cx="12" cy="10" r="2.6"/>',
    "chat":    '<path d="M21 12a8.5 8.5 0 0 1-8.5 8.5c-1.6 0-3-.4-4.3-1L3 21l1.6-4.8A8.5 8.5 0 1 1 21 12z"/>',
    "wallet":  '<rect x="2" y="6" width="20" height="13" rx="2"/><path d="M16 13a2 2 0 1 0 0-4h4v4z"/>',
    "shield":  '<path d="M12 22s8-3.5 8-10V5l-8-3-8 3v7c0 6.5 8 10 8 10z"/><path d="m9 11.5 2 2 4-4.5"/>',
}
def svg(name, size=22, stroke=True):
    a = 'width="%d" height="%d" viewBox="0 0 24 24"' % (size, size)
    a += (' fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"'
          if stroke else ' fill="currentColor"')
    return '<svg %s aria-hidden="true">%s</svg>' % (a, ICONS.get(name, ""))


# ── countdown date (rolls forward indefinitely) ─────────────────────
def first_monday_next_month(after):
    y, m = after.year, after.month + 1
    if m > 12: m, y = 1, y + 1
    d = datetime.date(y, m, 1)
    while d.weekday() != 0: d += datetime.timedelta(days=1)
    return d
def next_start():
    today = datetime.date.today()
    d = datetime.date(today.year, today.month, 1)
    while d.weekday() != 0: d += datetime.timedelta(days=1)
    return d if d > today else first_monday_next_month(today)
NEXT_ISO = next_start().isoformat()


def addr(p):   return p["campus"]["addr_es" if p["lang"] == "es" else "addr_en"]
def cname(p):  return p["campus"]["name_es" if p["lang"] == "es" else "name_en"]

def head_block(eyebrow, title, lead=None):
    out = '<div class="lf-section__head lf-rv">'
    if eyebrow: out += '<span class="lf-eyebrow">%s</span>' % h(eyebrow)
    out += '<h2 class="lf-h2">%s</h2>' % h(title)
    if lead: out += '<p class="lf-lead">%s</p>' % h(lead)
    return out + '</div>'


# ── HEADER ───────────────────────────────────────────────────────────
def header(p):
    es = p["lang"] == "es"
    en_href = "/" + p["path"] if not es else "/" + p["alt"]
    es_href = "/" + p["alt"] if not es else "/" + p["path"]
    phones = '<a class="lf-phone" href="tel:%s">%s<b class="lf-phone__flag">%s</b><span class="lf-phone__num">%s</span></a>' % (
        p["phone"][2], svg("phone", 16), h(p["phone"][0]), h(p["phone"][1]))
    if p.get("phone2"):
        phones += '<a class="lf-phone" href="tel:%s">%s<b class="lf-phone__flag">%s</b><span class="lf-phone__num">%s</span></a>' % (
            p["phone2"][2], svg("phone", 16), h(p["phone2"][0]), h(p["phone2"][1]))
    return (
        '<div class="lf-topbar">%s</div>\n'
        '<header class="lf-hdr"><div class="lf-hdr__in">\n'
        '  <div class="lf-brand">'
        '<img class="lf-brand__logo" src="/assets/img/logo-final.gif" alt="American Barber Institute — %s" width="385" height="99" fetchpriority="high">'
        '<div class="lf-brand__addr">%s%s</div></div>\n'
        '  <div class="lf-hdr__right"><div class="lf-phones">%s</div>'
        '<div class="lf-lang" role="group" aria-label="%s">'
        '<a class="%s" href="%s"%s>EN</a><a class="%s" href="%s"%s>ES</a></div></div>\n'
        '</div></header>\n'
    ) % (
        h(D.TOPBAR[p["lang"]]), h(addr(p)), svg("pin", 14), h(addr(p)), phones,
        "Idioma" if es else "Language",
        "is-active" if not es else "", h(en_href), ' aria-current="true"' if not es else "",
        "is-active" if es else "", h(es_href), ' aria-current="true"' if es else "",
    )


# ── lead form ("Get Trained With ABI") ──────────────────────────────
def lead_form(p, anchor="reserve"):
    f = D.FORM[p["lang"]]
    camp = "".join('<option>%s</option>' % h(o) for o in f["campus_opts"])
    sched = "".join('<option>%s</option>' % h(o) for o in f["schedule_opts"])
    return (
        '<form class="lf-form" id="%s" method="POST" action="https://formspree.io/f/xrgpkebw">\n'
        '  <input type="hidden" name="_subject" value="ABI Landing — %s">\n'
        '  <input type="hidden" name="campus" value="%s">\n'
        '  <input type="hidden" name="language" value="%s">\n'
        '  <span class="lf-form__eyebrow">%s</span>\n'
        '  <h3 class="lf-form__h">%s</h3>\n'
        '  <div class="lf-form__row"><input type="text" name="name" required placeholder="%s"></div>\n'
        '  <div class="lf-form__row lf-form__row--2">'
        '<input type="tel" name="phone" required placeholder="%s">'
        '<input type="email" name="email" required placeholder="%s"></div>\n'
        '  <div class="lf-form__row"><label class="lf-form__label">%s</label><select name="campus_pref" required>%s</select></div>\n'
        '  <div class="lf-form__row"><label class="lf-form__label">%s</label><select name="schedule" required>%s</select></div>\n'
        '  <div class="lf-form__row"><textarea name="message" rows="3" placeholder="%s"></textarea></div>\n'
        '  <button type="submit" class="lf-btn lf-btn--primary lf-btn--lg lf-form__submit">%s</button>\n'
        '  <p class="lf-form__fine">%s</p>\n'
        '</form>'
    ) % (
        anchor, p["id"], p["campus"]["slug"], p["lang"],
        h(f["eyebrow"]), h(f["h"]), h(f["name"]), h(f["phone"]), h(f["email"]),
        h(f["campus_label"]), camp, h(f["schedule_label"]), sched, h(f["message"]),
        h(f["submit"]), h(f["consent"]),
    )


# ── HERO ─────────────────────────────────────────────────────────────
def hero(p):
    H_ = D.HERO[p["lang"]]
    cells = "".join('<div class="lf-cd__cell"><b data-cd-%s>0</b><span>%s</span></div>' % (k, h(lbl))
                    for k, lbl in zip("dhms", H_["cells"]))
    countdown = (
        '<div class="lf-cd" data-target="%s">'
        '<h2 class="lf-cd__h"><span class="lf-cd__label">%s</span> <span class="lf-cd__date"></span></h2>'
        '<p class="lf-cd__sub">%s</p><div class="lf-cd__grid">%s</div></div>'
    ) % (NEXT_ISO, h(H_["cd_label"]), h(H_["cd_sub"]), cells)
    return (
        '<section class="lf-hero"><div class="lf-wrap lf-hero__in">\n'
        '  <div class="lf-hero__copy lf-rv">'
        '<p class="lf-hero__program">%s</p>'
        '<h1 class="lf-h1">%s</h1>'
        '<p class="lf-hero__tagline">%s</p>'
        '%s</div>\n'
        '  <div class="lf-hero__form lf-rv">%s</div>\n'
        '</div></section>\n'
    ) % (h(H_["program"]), h(H_["h1"]), h(H_["tagline"]), countdown, lead_form(p, "reserve"))


# ── intro band ───────────────────────────────────────────────────────
def section_intro(p):
    it = D.INTRO[p["lang"]]
    return ('<section class="lf-section lf-section--tight"><div class="lf-wrap lf-prose lf-rv">'
            '<h2 class="lf-h2">%s</h2><p>%s</p></div></section>\n') % (h(it["h"]), h(it["p"]))


# ── program / learn-haircuts band ────────────────────────────────────
def section_program(p):
    pr = D.PROGRAM[p["lang"]]
    chips = "".join('<span class="lf-tech">%s%s</span>' % (svg("check", 15), h(x)) for x in pr["haircuts"])
    return (
        '<section class="lf-section lf-section--alt"><div class="lf-wrap">'
        '<div class="lf-section__head lf-rv"><h2 class="lf-h2">%s</h2></div>'
        '<div class="lf-prose lf-rv" style="max-width:880px;margin:0 auto 1.4rem"><p>%s</p><p><b>%s</b></p></div>'
        '<div class="lf-tech-grid lf-rv">%s</div></div></section>\n'
    ) % (h(pr["h"]), h(pr["p"]), h(pr["learn"]), chips)


# ── About ─────────────────────────────────────────────────────────────
def section_about(p):
    ab = D.ABOUT[p["lang"]]
    body = "".join('<p>%s</p>' % h(x) for x in ab["paras"])
    return ('<section class="lf-section"><div class="lf-wrap">%s'
            '<div class="lf-prose lf-prose--2col lf-rv">%s</div></div></section>\n') % (
        head_block(None, ab["h"]), body)


# ── Entrance Requirements ────────────────────────────────────────────
def section_requirements(p):
    rq = D.REQUIREMENTS[p["lang"]]
    cards = "".join(
        '<div class="lf-req lf-rv"><div class="lf-req__icon">%s</div>'
        '<div><h3 class="lf-req__t">%s</h3><p class="lf-req__d">%s</p></div></div>' % (svg("check", 18), h(t), h(d))
        for t, d in rq["items"])
    return ('<section class="lf-section lf-section--alt"><div class="lf-wrap">%s'
            '<div class="lf-reqs">%s</div></div></section>\n') % (head_block(None, rq["h"]), cards)


# ── Payment Plans ─────────────────────────────────────────────────────
def section_plans(p):
    eb, ti = D.PLANS_HEAD[p["lang"]]
    ex = D.PLANS_EXTRA[p["lang"]]
    popular = "Más Popular" if p["lang"] == "es" else "Most Popular"
    cards = ""
    for pl in D.PLANS[p["lang"]]:
        cls = "lf-plan lf-rv" + (" lf-plan--feature" if pl["feature"] else "")
        badge = '<span class="lf-plan__badge">%s</span>' % popular if pl["feature"] else ""
        terms = "".join('<li>%s</li>' % h(x) for x in pl["terms"])
        cards += (
            '<div class="%s">%s<div class="lf-plan__name">%s</div>'
            '<div class="lf-plan__sched">%s</div>'
            '<div class="lf-plan__price">%s</div>'
            '<ul class="lf-plan__list">%s</ul>'
            '<a class="lf-btn lf-btn--primary lf-plan__cta" href="#reserve">%s</a></div>'
        ) % (cls, badge, h(pl["name"]), h(pl["sched"]), h(pl["cost"]), terms,
             "¡Hagámoslo!" if p["lang"] == "es" else "Let's Do It")
    extras = (
        '<div class="lf-finance lf-rv">'
        '<div class="lf-finance__card"><h4>%s</h4><p>%s</p></div>'
        '<div class="lf-finance__card"><h4>%s%s</h4><p>%s</p></div>'
        '<div class="lf-finance__card"><h4>%s%s</h4><p>%s</p></div>'
        '</div>'
    ) % (h(ex["fees_title"]), h(ex["fees"]),
         svg("wallet", 16), h(" " + ex["accessvr_title"]), h(ex["accessvr"]),
         svg("shield", 16), h(" " + ex["gibill_title"]), h(ex["gibill"]))
    return ('<section class="lf-section"><div class="lf-wrap">%s'
            '<div class="lf-tuition">%s</div>%s</div></section>\n') % (head_block(eb, ti), cards, extras)


# ── Gallery (real ABI photos) ────────────────────────────────────────
def section_gallery(p):
    items = "".join(
        '<img loading="lazy" src="/assets/img/%s" alt="ABI students at the clinic %d" width="600" height="450">'
        % (h(g), i + 1) for i, g in enumerate(D.GALLERY))
    return ('<section class="lf-section lf-section--alt"><div class="lf-wrap">%s'
            '<div class="lf-gallery">%s</div></div></section>\n') % (
        head_block(None, D.GALLERY_HEAD[p["lang"]]), items)


# ── reel media helper ────────────────────────────────────────────────
PLAY_BTN = ('<button class="lf-reel__play" type="button" aria-label="Play video">'
            '<svg class="lf-reel__icon-play" viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5v14l11-7z"/></svg>'
            '<svg class="lf-reel__icon-pause" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 5h4v14H6zM14 5h4v14h-4z"/></svg>'
            '</button>')
def _reel(vid, poster, label):
    return ('<div class="lf-reel__media"><video class="lf-reel__video" muted loop playsinline preload="none"'
            ' src="/assets/videos/%s" poster="/assets/img/%s" aria-label="%s"></video>%s</div>') % (
        h(vid), h(poster), h(label), PLAY_BTN)

STUDENT_VOICES_VIDEOS = [("video-321.mp4", "video-321-poster.jpg"),
                         ("Video-124.mp4", "video-124-poster.jpg"),
                         ("video-321.mp4", "video-321-poster.jpg")]
BRONX_EXTRA_VIDEOS = [("video-321.mp4", "video-321-poster.jpg"),
                      ("Video-124.mp4", "video-124-poster.jpg"),
                      ("video-321.mp4", "video-321-poster.jpg")]

def section_student_voices(p):
    es = p["lang"] == "es"
    eb = "Testimonios" if es else "Student Voices"
    ti = "Voces reales, cortes reales." if es else "Real voices, real cuts."
    sub = ("Toca un reproductor para escuchar a un estudiante de ABI." if es
           else "Tap a player to hear an ABI student share their experience.")
    media = "".join(_reel(v, ps, "ABI student testimonial %d" % i)
                    for i, (v, ps) in enumerate(STUDENT_VOICES_VIDEOS, 1))
    return ('<section class="lf-section"><div class="lf-wrap"><div class="lf-reel lf-reel--triple lf-rv">'
            '<div class="lf-section__head" style="margin-bottom:1.2rem"><span class="lf-eyebrow">%s</span>'
            '<h2 class="lf-h2">%s</h2><p class="lf-lead">%s</p></div>'
            '<div class="lf-reel__grid">%s</div></div></div></section>\n') % (h(eb), h(ti), h(sub), media)

def section_bronx_extra(p):
    if p["campus"]["slug"] != "bronx": return ""
    es = p["lang"] == "es"
    eb = "Más Voces del Bronx" if es else "More Bronx Stories"
    ti = "Más historias de la sede del Bronx." if es else "More voices from the Bronx campus."
    sub = ("Tres estudiantes del Bronx comparten su experiencia." if es
           else "Three Bronx students share their experience.")
    media = "".join(_reel(v, ps, "Bronx student testimonial %d" % i)
                    for i, (v, ps) in enumerate(BRONX_EXTRA_VIDEOS, 1))
    return ('<section class="lf-section lf-section--alt"><div class="lf-wrap"><div class="lf-reel lf-reel--triple lf-rv">'
            '<div class="lf-section__head" style="margin-bottom:1.2rem"><span class="lf-eyebrow">%s</span>'
            '<h2 class="lf-h2">%s</h2><p class="lf-lead">%s</p></div>'
            '<div class="lf-reel__grid">%s</div></div></div></section>\n') % (h(eb), h(ti), h(sub), media)


# ── Our Videos (real YouTube) ────────────────────────────────────────
def section_videos(p):
    cards = ""
    for vid in D.YT_IDS:
        cards += (
            '<div class="lf-clip lf-rv" data-yt="%s">'
            '<img loading="lazy" class="lf-clip__thumb" src="/assets/img/abi/yt-%s.jpg" alt="ABI video" width="480" height="360">'
            '<button class="lf-clip__play" type="button" aria-label="Play video">'
            '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M8 5v14l11-7z"/></svg></button>'
            '</div>'
        ) % (vid, vid)
    return ('<section class="lf-section"><div class="lf-wrap">%s'
            '<div class="lf-showcase">%s</div></div></section>\n') % (
        head_block(None, D.VIDEOS_HEAD[p["lang"]]), cards)


# ── Reviews (5 real Google reviews) ──────────────────────────────────
def section_reviews(p):
    eb, ti = D.REVIEWS_HEAD[p["lang"]]
    cards = ""
    for r in D.REVIEWS:
        ini = "".join(w[0] for w in r["name"].split()[:2]).upper()
        cards += ('<div class="lf-review lf-rv"><div class="lf-review__stars">★★★★★</div>'
                  '<p class="lf-review__q">“%s”</p><div class="lf-review__who">'
                  '<div class="lf-review__av">%s</div><div class="lf-review__name">%s</div></div></div>') % (
            h(r["q"]), h(ini), h(r["name"]))
    return ('<section class="lf-section lf-section--alt"><div class="lf-wrap">%s'
            '<div class="lf-reviews lf-reviews--5">%s</div></div></section>\n') % (head_block(eb, ti), cards)


# ── Closing band ("Get More Info Today") ─────────────────────────────
def section_closing(p):
    cl = D.CLOSING[p["lang"]]
    call = "Llamar ahora" if p["lang"] == "es" else "Call now"
    return ('<section class="lf-section lf-closing"><div class="lf-wrap lf-rv" style="text-align:center;max-width:780px">'
            '<h2 class="lf-h2">%s</h2><p class="lf-lead">%s</p>'
            '<a class="lf-btn lf-btn--primary lf-btn--lg" href="tel:%s">%s%s</a>'
            '</div></section>\n') % (h(cl["h"]), h(cl["p"]), p["phone"][2], svg("phone", 18), " " + h(call))


# ── footer (NO Request-a-Call / Apply / Speak CTAs) ──────────────────
def footer(p):
    ft = D.FOOTER[p["lang"]]
    socials = (
        '<a class="lf-soc" href="https://www.facebook.com/Abi.Education/" target="_blank" rel="noopener" aria-label="Facebook"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M13.5 21v-7h2.4l.4-3h-2.8V9.2c0-.9.2-1.5 1.5-1.5h1.4V5.1C16.1 5 15.2 5 14.2 5c-2.2 0-3.7 1.3-3.7 3.8V11H8v3h2.5v7h3z"/></svg></a>'
        '<a class="lf-soc" href="https://www.instagram.com/americanbarberinstitute/" target="_blank" rel="noopener" aria-label="Instagram"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4.2"/><circle cx="17.3" cy="6.7" r="1.1" fill="currentColor" stroke="none"/></svg></a>'
        '<a class="lf-soc" href="https://twitter.com/amerbarberedu" target="_blank" rel="noopener" aria-label="X"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M17.8 3h3l-6.6 7.6L22 21h-6.1l-4.8-6.3L5.6 21h-3l7.1-8.1L2 3h6.3l4.3 5.7L17.8 3z"/></svg></a>'
        '<a class="lf-soc" href="https://www.youtube.com/channel/UCy_pQUDfk2ldEp6_zyaIMhQ" target="_blank" rel="noopener" aria-label="YouTube"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M23 7.2a3 3 0 0 0-2.1-2.1C19 4.5 12 4.5 12 4.5s-7 0-8.9.6A3 3 0 0 0 1 7.2 31 31 0 0 0 .5 12 31 31 0 0 0 1 16.8a3 3 0 0 0 2.1 2.1c1.9.6 8.9.6 8.9.6s7 0 8.9-.6a3 3 0 0 0 2.1-2.1A31 31 0 0 0 23.5 12 31 31 0 0 0 23 7.2zM9.8 15.3V8.7L15.9 12z"/></svg></a>'
    )
    return (
        '<footer class="lf-footer"><div class="lf-wrap">'
        '<h3 class="lf-h2">%s</h3><p>%s</p>'
        '<p class="lf-footer__addr">%s%s · <a href="tel:%s">%s</a></p>'
        '<div class="lf-footer__socials">%s</div>'
        '<p class="lf-footer__fine">%s</p></div></footer>\n'
        '<button class="lf-chat" aria-label="%s">%s</button>\n'
    ) % (h(ft["h"]), h(ft["sub"]),
         svg("pin", 14), h(addr(p)), p["phone"][2], h(p["phone"][1]),
         socials, h(ft["fine"]),
         "Chatear con admisiones" if p["lang"] == "es" else "Chat with admissions", svg("chat", 26))


# ── HEAD ─────────────────────────────────────────────────────────────
def page_head(p):
    es = p["lang"] == "es"
    canonical = SITE + "/" + p["path"]; alt_url = SITE + "/" + p["alt"]
    en_url, es_url = (alt_url, canonical) if es else (canonical, alt_url)
    ld = {"@context": "https://schema.org", "@type": ["TradeSchool", "LocalBusiness", "EducationalOrganization"],
          "name": "American Barber Institute — " + p["campus"]["name_en"], "url": canonical,
          "telephone": p["phone"][2], "image": SITE + "/assets/img/abi/500-Hour-Master-Barber-Program.jpg",
          "description": p["desc"], "foundingDate": "1996",
          "address": {"@type": "PostalAddress", "streetAddress": p["campus"]["addr_en"].split(",")[0],
                      "addressLocality": "Bronx" if p["campus"]["slug"] == "bronx" else "New York",
                      "addressRegion": "NY", "postalCode": "10461" if p["campus"]["slug"] == "bronx" else "10018",
                      "addressCountry": "US"},
          "geo": {"@type": "GeoCoordinates", "latitude": p["campus"]["latlng"][0], "longitude": p["campus"]["latlng"][1]},
          "aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.6", "reviewCount": "100", "bestRating": "5", "worstRating": "1"},
          "paymentAccepted": ["Cash", "Credit Card", "Financial Aid", "GI Bill", "ACCES-VR"]}
    course = {"@context": "https://schema.org", "@type": "Course", "name": "500-Hour Master Barber Program",
              "description": p["desc"], "provider": {"@type": "TradeSchool", "name": "American Barber Institute"}}
    return (
'<!DOCTYPE html>\n<html lang="%(lang)s">\n<head>\n<meta charset="utf-8">\n'
'<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
'<title>%(title)s</title>\n<meta name="description" content="%(desc)s">\n'
'<link rel="canonical" href="%(canonical)s">\n'
'<link rel="alternate" hreflang="en" href="%(en_url)s">\n'
'<link rel="alternate" hreflang="en-US" href="%(en_url)s">\n'
'<link rel="alternate" hreflang="es" href="%(es_url)s">\n'
'<link rel="alternate" hreflang="es-US" href="%(es_url)s">\n'
'<link rel="alternate" hreflang="x-default" href="%(en_url)s">\n'
'<meta property="og:title" content="%(title)s">\n<meta property="og:description" content="%(desc)s">\n'
'<meta property="og:type" content="website">\n<meta property="og:url" content="%(canonical)s">\n'
'<meta property="og:image" content="%(site)s/assets/img/abi/500-Hour-Master-Barber-Program.jpg">\n'
'<meta property="og:locale" content="%(oglocale)s">\n'
'<meta name="twitter:card" content="summary_large_image">\n'
'<meta name="robots" content="index, follow, max-image-preview:large">\n'
'<meta name="theme-color" content="#1b3bd9">\n'
'<link rel="icon" href="/favicon.ico" sizes="any">\n<link rel="apple-touch-icon" href="/apple-icon.png">\n'
'<link rel="preconnect" href="https://fonts.googleapis.com">\n'
'<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
'<link href="https://fonts.googleapis.com/css2?family=Oswald:wght@400;500;600;700&family=Inter:wght@400;500;600;700&family=Poppins:wght@400;500;600;700;800&display=swap" rel="stylesheet">\n'
'<link rel="stylesheet" href="/assets/css/funnels.css?v=%(cssv)s">\n'
'<script type="application/ld+json">%(ld1)s</script>\n'
'<script type="application/ld+json">%(ld2)s</script>\n'
'</head>\n<body class="lf-page %(theme)s">\n'
    ) % {"lang": p["lang"], "title": h(p["title"]), "desc": h(p["desc"]),
         "canonical": h(canonical), "en_url": h(en_url), "es_url": h(es_url), "site": SITE,
         "oglocale": "es_ES" if es else "en_US", "cssv": CSS_V,
         "ld1": json.dumps(ld, ensure_ascii=False), "ld2": json.dumps(course, ensure_ascii=False),
         "theme": p["theme_class"]}

def page_tail():
    return '<script src="/assets/js/funnels.js?v=%s" defer></script>\n</body>\n</html>\n' % JS_V


def build_page(p):
    parts = [page_head(p), header(p), hero(p), section_intro(p), section_program(p),
             section_about(p), section_requirements(p), section_plans(p), section_gallery(p),
             section_student_voices(p)]
    if p["campus"]["slug"] == "bronx":
        parts.append(section_bronx_extra(p))
    parts += [section_videos(p), section_reviews(p), section_closing(p), footer(p), page_tail()]
    out_dir = os.path.join(ROOT, p["path"]); os.makedirs(out_dir, exist_ok=True)
    out = os.path.join(out_dir, "index.html")
    with open(out, "w", encoding="utf-8") as f:
        f.write("".join(parts))
    return out

def main():
    for w in [build_page(p) for p in D.PAGES]:
        print("✓", os.path.relpath(w, ROOT))
    print("%d landing pages generated." % len(D.PAGES))

if __name__ == "__main__":
    main()
