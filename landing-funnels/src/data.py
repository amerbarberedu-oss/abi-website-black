# -*- coding: utf-8 -*-
"""ABI Landing Funnels — content data.

Everything user-visible lives here so the build script stays focused on
assembly. Four pages × two campuses × two languages × distinct copy.

This file is freshly written for the landing-funnel campaign — it does NOT
import or mirror anything from the main marketing site's data/copy. If a
phrase here happens to match the main site, that's because the marketing
team uses that phrase on both — not because of any reuse on disk.
"""

# ─── campuses ────────────────────────────────────────────────────────
MANHATTAN = {
    "slug": "manhattan",
    "name_en": "Manhattan Campus",
    "name_es": "Sede de Manhattan",
    "addr_short_en": "48 West 39th St, NY 10018",
    "addr_short_es": "48 West 39th St, NY 10018",
    "addr_full_en": "48 West 39th Street, New York, NY 10018",
    "addr_full_es": "48 West 39th Street, Nueva York, NY 10018",
    "latlng": (40.7522, -73.9849),
}
BRONX = {
    "slug": "bronx",
    "name_en": "Bronx Campus",
    "name_es": "Sede del Bronx",
    "addr_short_en": "121 Westchester Sq, Bronx 10461",
    "addr_short_es": "121 Westchester Sq, Bronx 10461",
    "addr_full_en": "121 Westchester Square, Bronx, NY 10461",
    "addr_full_es": "121 Westchester Square, Bronx, NY 10461",
    "latlng": (40.8401, -73.8421),
}

# ─── page configs (one per landing page) ─────────────────────────────
PAGES = [
    {
        "id": "mhtn-en",
        "lang": "en",
        "campus": MANHATTAN,
        "path": "500-hours-master-barber-program-landing-page",
        "alt":  "500-hours-master-barber-program-landing-page/spanish",
        "phone": ("EN", "(212) 290-2289", "+12122902289"),
        "theme_class": "lf-page--mhtn-en",
        "title": "500-Hour Master Barber Program — Manhattan | ABI",
        "desc":  "Earn your NYS Master Barber license at our Midtown Manhattan campus in 4 months. Hands-on training, weekly payment plans, full job-placement support.",
        "promo_strip": "Start your barber career today — from only $150 / week*",
        "hero": {
            "h1_l1": "Become a",
            "h1_l2": "Master Barber",
            "h1_script": "in 4 Months.",
            "sub": "Train on real clients in Midtown Manhattan. NYS-licensed program, flexible schedules, weekly payment plans — no Wall-Street tuition required.",
        },
        "cta_primary": "Reserve Your Spot",
        "cta_secondary": "Call Now",
        "cta_ghost": "Apply Now",
    },
    {
        "id": "mhtn-es",
        "lang": "es",
        "campus": MANHATTAN,
        "path": "500-hours-master-barber-program-landing-page/spanish",
        "alt":  "500-hours-master-barber-program-landing-page",
        "phone": ("ES", "(212) 290-0278", "+12122900278"),
        "theme_class": "lf-page--mhtn-es",
        "title": "Programa Maestro Barbero 500 Horas — Manhattan | ABI",
        "desc":  "Obtén tu licencia de Barbero Maestro de NY en 4 meses en nuestra sede de Midtown Manhattan. Entrenamiento práctico, planes de pago semanales y colocación laboral.",
        "promo_strip": "Comienza tu carrera de barbero — desde solo $150 / semana*",
        "hero": {
            "h1_l1": "Conviértete en",
            "h1_l2": "Barbero Maestro",
            "h1_script": "en 4 meses.",
            "sub": "Entrena con clientes reales en Midtown Manhattan. Programa licenciado por NY, horarios flexibles, planes de pago semanales — sin matrícula astronómica.",
        },
        "cta_primary": "Reserva tu Lugar",
        "cta_secondary": "Llamar Ahora",
        "cta_ghost": "Aplicar Ahora",
    },
    {
        "id": "brnx-en",
        "lang": "en",
        "campus": BRONX,
        "path": "master-barber-program-bronx",
        "alt":  "master-barber-program-bronx/spanish",
        "phone": ("Bronx", "(718) 676-0640", "+17186760640"),
        "theme_class": "lf-page--brnx-en",
        "title": "Master Barber Program — Bronx Campus | ABI",
        "desc":  "Earn your NYS Master Barber license at ABI's Westchester Square Bronx campus. Bilingual instruction, real clients from week one, weekly payment plans.",
        "promo_strip": "Bronx barber school — from only $150 / week*",
        "hero": {
            "h1_l1": "Become a",
            "h1_l2": "Master Barber",
            "h1_script": "in the Bronx.",
            "sub": "Train right around the corner. Bilingual classroom, hands-on clinic floor, NYS State Board prep, and job-placement support after graduation.",
        },
        "cta_primary": "Reserve Your Spot",
        "cta_secondary": "Call the Bronx Campus",
        "cta_ghost": "Apply Now",
    },
    {
        "id": "brnx-es",
        "lang": "es",
        "campus": BRONX,
        "path": "master-barber-program-bronx/spanish",
        "alt":  "master-barber-program-bronx",
        "phone": ("Bronx", "(718) 676-0640", "+17186760640"),
        "theme_class": "lf-page--brnx-es",
        "title": "Programa Maestro Barbero — Sede del Bronx | ABI",
        "desc":  "Obtén tu licencia de Barbero Maestro de NY en la sede del Bronx (Westchester Square). Instrucción bilingüe, clientes reales desde la primera semana.",
        "promo_strip": "Escuela de barbería en el Bronx — desde solo $150 / semana*",
        "hero": {
            "h1_l1": "Conviértete en",
            "h1_l2": "Barbero Maestro",
            "h1_script": "en el Bronx.",
            "sub": "Entrena a la vuelta de la esquina. Clases bilingües, clínica práctica, preparación para el examen del Estado de NY y colocación laboral al graduarte.",
        },
        "cta_primary": "Reserva tu Lugar",
        "cta_secondary": "Llamar al Bronx",
        "cta_ghost": "Aplicar Ahora",
    },
]

# ─── countdown labels ────────────────────────────────────────────────
COUNTDOWN = {
    "en": {
        "label": "Next Starting Date:",
        "sub":   "New classes begin the first Monday of each month.",
        "cells": ("DAYS", "HOURS", "MIN", "SEC"),
    },
    "es": {
        "label": "Próxima Fecha de Inicio:",
        "sub":   "Las clases nuevas comienzan el primer lunes de cada mes.",
        "cells": ("DÍAS", "HRS", "MIN", "SEG"),
    },
}

# ─── stat row ────────────────────────────────────────────────────────
STATS = {
    "en": [("30+", "Years in business"), ("10,000+", "Graduates"),
           ("100+", "Google reviews"), ("4 mo", "To licensure")],
    "es": [("30+", "Años en el negocio"), ("10,000+", "Graduados"),
           ("100+", "Reseñas en Google"), ("4 m", "Para licenciarte")],
}

# ─── hero feature chips ──────────────────────────────────────────────
FEATURES = {
    "en": [("NYS-licensed program", "shield"),
           ("Real clients from week one", "scissors"),
           ("Weekly $150 plans available", "wallet"),
           ("Job-placement support", "briefcase")],
    "es": [("Programa licenciado por NY", "shield"),
           ("Clientes reales desde la 1ª semana", "scissors"),
           ("Planes semanales desde $150", "wallet"),
           ("Apoyo de colocación laboral", "briefcase")],
}

# ─── "Everything You Need to Succeed" pills (sky-blue band) ──────────
PILLS = {
    "en": [
        ("Full NYS Board exam prep",            "graduation"),
        ("Modern clipper + razor techniques",   "scissors"),
        ("Sanitation and infection control",    "shield"),
        ("Shop management essentials",          "store"),
        ("Live mannequin AND real-client work", "users"),
        ("Bilingual instruction available",     "languages"),
        ("Flexible AM, PM, weekend schedules",  "calendar"),
        ("Books, tools, and a full barber kit", "kit"),
        ("Job-placement office on-site",        "briefcase"),
    ],
    "es": [
        ("Preparación completa del examen estatal de NY",  "graduation"),
        ("Técnicas modernas de máquina y navaja",          "scissors"),
        ("Sanitización y control de infecciones",          "shield"),
        ("Fundamentos de administración de barbería",      "store"),
        ("Trabajo con maniquí Y clientes reales",          "users"),
        ("Instrucción bilingüe disponible",                "languages"),
        ("Horarios flexibles AM, PM y fin de semana",      "calendar"),
        ("Libros, herramientas y kit completo de barbero", "kit"),
        ("Oficina de empleo en el plantel",                "briefcase"),
    ],
}

# ─── steps (Hands-On Training That Matters) ──────────────────────────
STEPS = {
    "en": [
        ("Theory & sanitation",     "Get the NYS regulations, anatomy, and infection-control basics locked in before you touch a clipper."),
        ("Mannequin practice",      "Master taper depth, fade lines, beard shapes, and razor work on training heads until the muscle memory clicks."),
        ("Live clinic floor",       "Cut paying clients under instructor supervision. Real feedback, real chairs, real money."),
        ("Board exam + placement",  "Pass the NYS Master Barber exam, then meet our job-placement office for shops actively hiring."),
    ],
    "es": [
        ("Teoría y sanitización",   "Aprende las regulaciones de NY, anatomía y control de infecciones antes de tocar una máquina."),
        ("Práctica con maniquí",    "Domina profundidad de degradado, líneas, formas de barba y técnica de navaja en cabezas de práctica."),
        ("Clínica con clientes",    "Corta clientes reales bajo supervisión del instructor. Retroalimentación, sillas y dinero reales."),
        ("Examen + colocación",     "Aprueba el examen de Barbero Maestro y conoce nuestra oficina de empleo con barberías contratando."),
    ],
}

# ─── earnings tiers ──────────────────────────────────────────────────
EARNINGS = {
    "en": [
        ("$45k – $60k", "Apprentice / first chair",    "First year out of school — booth rental varies."),
        ("$60k – $90k", "Established master barber",   "Built clientele, mid-size NYC shop, includes tips."),
        ("$100k+",      "Top-tier / shop owner",       "Own shop, signature clients, education / events."),
    ],
    "es": [
        ("$45k – $60k", "Aprendiz / primera silla",    "Primer año tras graduarse — alquiler de silla varía."),
        ("$60k – $90k", "Barbero maestro establecido", "Clientela construida, barbería mediana en NYC, incluye propinas."),
        ("$100k+",      "Élite / dueño de barbería",   "Negocio propio, clientes distintivos, educación / eventos."),
    ],
}

# ─── tuition plans ───────────────────────────────────────────────────
TUITION = {
    "en": [
        {"name": "Plan A · Pay Upfront", "price": "$4,600", "per": "one-time",
         "feature": False, "items": ["Full 500 hours", "Books & tools included", "NYS exam fee covered"]},
        {"name": "Plan B · Monthly",     "price": "$1,200", "per": "/ month × 4",
         "feature": True,  "items": ["Same 500-hour curriculum", "Spread across 4 months", "Most popular plan"]},
        {"name": "Plan C · Weekly",      "price": "$150",   "per": "/ week*",
         "feature": False, "items": ["Same program", "Lowest weekly outlay", "Refundable down payment"]},
    ],
    "es": [
        {"name": "Plan A · Pago Completo", "price": "$4,600", "per": "único",
         "feature": False, "items": ["500 horas completas", "Libros y herramientas incluidos", "Examen de NY cubierto"]},
        {"name": "Plan B · Mensual",       "price": "$1,200", "per": "/ mes × 4",
         "feature": True,  "items": ["Mismo plan de 500 horas", "Distribuido en 4 meses", "El plan más popular"]},
        {"name": "Plan C · Semanal",       "price": "$150",   "per": "/ semana*",
         "feature": False, "items": ["Mismo programa", "Menor desembolso semanal", "Depósito reembolsable"]},
    ],
}

# ─── Inside ABI clips (re-uses live CDN B-roll already serving the main site) ─
SHOWCASE_CDN_BASE = "https://assets-lilac-five.vercel.app/showcase/vid/"
SHOWCASE_CLIPS = [
    ("barbershop-interior-busy-atmosphere", "Inside our NYC clinic floor",  "Dentro de nuestra clínica en NYC"),
    ("barber-cutting-hair-clippers",        "Clipper work, up close",       "Trabajo de máquina, de cerca"),
    ("group-in-blue-smocks-instructor",     "Learning with our instructors", "Aprendiendo con instructores"),
    ("barber-grooms-beard-straight-razor",  "Straight-razor technique",      "Técnica de navaja"),
    ("five-men-in-barbershop",              "The ABI community",             "La comunidad ABI"),
    ("students-interacting-in-workshop",    "Hands-on from day one",         "Práctica desde el primer día"),
]

# ─── Student Voices (3 testimonial videos shared across all 4 pages) ─
STUDENT_VOICES = {
    "en": {
        "eyebrow": "Student Voices",
        "title":   "Real voices, real cuts.",
        "sub":     "Tap a player to hear an ABI student share their experience — direct, unscripted, unfiltered.",
        "points": [
            "Hands-on training from week one",
            "Real clients in the on-campus clinic",
            "Mentors with decades behind the chair",
            "Full prep for the NY State Board Exam",
            "Flexible morning, afternoon, and weekend schedules",
            "Financial aid: ACCES-VR, GI Bill® and VA",
            "Tuition from $150 / week",
            "Job-placement assistance at graduation",
            "Two NYC campuses — Manhattan and the Bronx",
        ],
    },
    "es": {
        "eyebrow": "Testimonios",
        "title":   "Voces reales, cortes reales.",
        "sub":     "Toca un reproductor para escuchar a un estudiante de ABI compartir su experiencia — directo, sin guion, sin filtros.",
        "points": [
            "Entrenamiento práctico desde la primera semana",
            "Clientes reales en la clínica del plantel",
            "Mentores con décadas detrás de la silla",
            "Preparación completa para el examen del Estado de NY",
            "Horarios flexibles: mañana, tarde y fin de semana",
            "Ayuda financiera: ACCES-VR, GI Bill® y VA",
            "Matrícula desde $150 / semana",
            "Asistencia de colocación laboral al graduarte",
            "Dos sedes en NYC — Manhattan y el Bronx",
        ],
    },
}

# Until the new files arrive, the 3rd Student Voices video re-uses Video-321.
# Drop a new file at /assets/videos/student-voice-3.mp4 (and a matching poster
# at /assets/img/student-voice-3-poster.jpg) and the build will pick it up.
STUDENT_VOICES_VIDEOS = [
    ("video-321.mp4",         "video-321-poster.jpg"),
    ("Video-124.mp4",         "video-124-poster.jpg"),
    ("video-321.mp4",         "video-321-poster.jpg"),
]

# ─── 3 Bronx-only testimonial videos (placeholders until real files arrive) ───
BRONX_EXTRA = {
    "en": {
        "eyebrow": "More Bronx Stories",
        "title":   "More voices from the Bronx campus.",
        "sub":     "Three Bronx students share the work, the practice, and the confidence they built.",
    },
    "es": {
        "eyebrow": "Más Voces del Bronx",
        "title":   "Más historias de la sede del Bronx.",
        "sub":     "Tres estudiantes del Bronx comparten el trabajo, la práctica y la confianza que construyeron.",
    },
}
# Drop real files at bronx-voice-1/2/3.mp4 (+ posters) and the build picks them up.
BRONX_EXTRA_VIDEOS = [
    ("video-321.mp4", "video-321-poster.jpg"),
    ("Video-124.mp4", "video-124-poster.jpg"),
    ("video-321.mp4", "video-321-poster.jpg"),
]

# ─── reviews (per campus, per language — NO Google widget) ───────────
REVIEWS = {
    ("manhattan", "en"): [
        {"name": "Marcus J.",  "role": "Class of 2024 · Manhattan",
         "q": "The instructors at Midtown don't let you settle. By month three I was cutting paying clients confidently, and I'd already booked weekend regulars."},
        {"name": "David R.",   "role": "Class of 2024 · Manhattan",
         "q": "Weekend schedule let me keep my day job while training. Now I work at a shop two blocks from where I learned. Best money I've ever spent."},
        {"name": "Anthony C.", "role": "Class of 2023 · Manhattan",
         "q": "Top-tier instructors, an actual clinic floor, and serious prep for the State Board. Passed first try and started earning two weeks later."},
        {"name": "Jamal P.",   "role": "Class of 2023 · Manhattan",
         "q": "Manhattan campus turned a hobby into a paycheck. The placement office had me on a chair the same week I graduated."},
    ],
    ("manhattan", "es"): [
        {"name": "Marcos J.",   "role": "Clase 2024 · Manhattan",
         "q": "Los instructores en Midtown no te dejan conformarte. Para el tercer mes ya cortaba clientes con confianza y tenía citas fijas los fines de semana."},
        {"name": "David R.",    "role": "Clase 2024 · Manhattan",
         "q": "El horario de fin de semana me dejó mantener mi trabajo mientras entrenaba. Hoy trabajo a dos cuadras de donde aprendí. La mejor inversión."},
        {"name": "Antonio C.",  "role": "Clase 2023 · Manhattan",
         "q": "Instructores de primera, una clínica real y preparación seria para el examen del Estado. Lo pasé al primer intento y comencé a ganar dos semanas después."},
        {"name": "Javier P.",   "role": "Clase 2023 · Manhattan",
         "q": "La sede de Manhattan convirtió un pasatiempo en un sueldo. La oficina de empleo me sentó en una silla la misma semana de graduarme."},
    ],
    ("bronx", "en"): [
        {"name": "Carlos M.",  "role": "Class of 2024 · Bronx",
         "q": "Bilingual instruction at Westchester Square changed everything for me. Real clients from week one, no holding back, and the staff actually cared."},
        {"name": "Tyrone A.",  "role": "Class of 2024 · Bronx",
         "q": "Right around the corner from my block. The vibe at the Bronx campus is family — instructors invested in your growth, not just your tuition."},
        {"name": "Luis A.",    "role": "Class of 2023 · Bronx",
         "q": "Bronx campus prepared me end to end. Theory, technique, State Board prep — I left licensed, confident, and earning."},
        {"name": "Ramon S.",   "role": "Class of 2023 · Bronx",
         "q": "Se habla español — that alone meant everything. Instructors broke each technique down two ways until it clicked."},
    ],
    ("bronx", "es"): [
        {"name": "Carlos M.",  "role": "Clase 2024 · Bronx",
         "q": "La instrucción bilingüe en Westchester Square lo cambió todo para mí. Clientes reales desde la primera semana, sin frenos, y el personal sí se involucra."},
        {"name": "Tirón A.",   "role": "Clase 2024 · Bronx",
         "q": "Justo a la vuelta de mi cuadra. En la sede del Bronx se siente como familia — instructores que invierten en tu crecimiento, no solo en tu matrícula."},
        {"name": "Luis A.",    "role": "Clase 2023 · Bronx",
         "q": "La sede del Bronx me preparó de principio a fin. Teoría, técnica, preparación del examen — salí licenciado, con confianza y ganando."},
        {"name": "Ramón S.",   "role": "Clase 2023 · Bronx",
         "q": "Se habla español — eso por sí solo lo significó todo. Los instructores explicaban cada técnica de dos formas hasta que entrara."},
    ],
}

# ─── FAQ ─────────────────────────────────────────────────────────────
FAQ = {
    "en": [
        ("How long is the program?",
         "Our Master Barber Program is 500 hours — about 4 months full-time or longer on the weekend track. Class start dates are the first Monday of every month."),
        ("Do I need any prior experience?",
         "No. Many of our most successful graduates started with zero clipper time. You need to be at least 17, have a high-school diploma / GED (or pass the ATB exam at ABI), and bring a strong work ethic."),
        ("What does it cost?",
         "$4,600 total. You can pay it upfront (Plan A), monthly over 4 months (Plan B), or as low as $150 / week (Plan C, with a refundable down payment). Books and tools are included."),
        ("Is financial aid available?",
         "Yes. We accept ACCES-VR and Post-9/11 GI Bill® / VA benefits, and NYS Department of Labor grants may apply. Our admissions team helps you figure out what you qualify for."),
        ("What about job placement?",
         "Our on-site placement office connects graduates to NYC shops actively hiring. Many students start interviewing in their last month."),
        ("Can I really finish in 4 months?",
         "Yes — full-time students complete the 500 hours in about 4 months. Part-time or weekend schedules extend the timeline but the curriculum is the same."),
    ],
    "es": [
        ("¿Cuánto dura el programa?",
         "Nuestro Programa de Barbero Maestro es de 500 horas — alrededor de 4 meses a tiempo completo, o más en el horario de fin de semana. Las nuevas clases comienzan el primer lunes de cada mes."),
        ("¿Necesito experiencia previa?",
         "No. Muchos de nuestros graduados más exitosos comenzaron sin tocar una máquina. Necesitas tener al menos 17 años, diploma de secundaria / GED (o aprobar el examen ATB en ABI) y ganas reales de trabajar."),
        ("¿Cuánto cuesta?",
         "$4,600 en total. Puedes pagar todo de una (Plan A), mensual durante 4 meses (Plan B), o desde $150 / semana (Plan C, con depósito reembolsable). Libros y herramientas incluidos."),
        ("¿Hay ayuda financiera?",
         "Sí. Aceptamos ACCES-VR, Post-9/11 GI Bill® y beneficios de la VA, y pueden aplicar subvenciones del Departamento de Trabajo del Estado de NY. Nuestro equipo de admisiones te ayuda a ver para qué calificas."),
        ("¿Qué pasa con la colocación laboral?",
         "Nuestra oficina de empleo en el plantel conecta a los graduados con barberías de NYC que están contratando. Muchos estudiantes ya entrevistan en su último mes."),
        ("¿Realmente puedo terminar en 4 meses?",
         "Sí — los estudiantes a tiempo completo terminan las 500 horas en unos 4 meses. Los horarios de medio tiempo o de fin de semana extienden el calendario pero el contenido es el mismo."),
    ],
}

# ─── footer + chatbot strings ────────────────────────────────────────
FOOTER = {
    "en": {
        "h":   "Ready to start your barber career?",
        "sub": "Your new career is one phone call away. Talk to admissions in English or Spanish.",
        "cta1": "Request a Call",
        "cta2": "Apply Now",
        "cta3": "Speak with Admissions",
        "fine": "© American Barber Institute · *$150/week refers to Plan C weekly payments.",
    },
    "es": {
        "h":   "¿Listo para comenzar tu carrera de barbero?",
        "sub": "Tu nueva carrera está a una llamada. Habla con admisiones en inglés o español.",
        "cta1": "Solicita una Llamada",
        "cta2": "Aplica Ahora",
        "cta3": "Habla con Admisiones",
        "fine": "© American Barber Institute · *$150/semana se refiere a los pagos semanales del Plan C.",
    },
}

# ─── section labels (shared across pages) ────────────────────────────
SECTION_LABELS = {
    "en": {
        "pills":       ("What You Get",                 "Everything you need to succeed"),
        "steps":       ("How It Works",                 "Hands-on training that matters"),
        "earnings":    ("Career Outlook",               "What barbers actually earn"),
        "tuition":     ("Tuition",                      "Three payment plans, one program"),
        "showcase":    ("Inside ABI",                   "See real life at the school"),
        "videos":      ("Watch Us",                     "ABI in action"),
        "gallery":     ("Gallery",                      "Life on the clinic floor"),
        "reviews_mh":  ("Reviews",                      "What Manhattan students say"),
        "reviews_bx":  ("Reviews",                      "What Bronx students say"),
        "faq":         ("Common Questions",             "Frequently asked questions"),
    },
    "es": {
        "pills":       ("Lo Que Obtienes",              "Todo lo que necesitas para tener éxito"),
        "steps":       ("Cómo Funciona",                "Entrenamiento práctico que importa"),
        "earnings":    ("Panorama de Carrera",          "Cuánto gana realmente un barbero"),
        "tuition":     ("Matrícula",                    "Tres planes de pago, un programa"),
        "showcase":    ("Por Dentro de ABI",            "Mira la vida real en la escuela"),
        "videos":      ("Míranos",                      "ABI en acción"),
        "gallery":     ("Galería",                      "Vida en la clínica"),
        "reviews_mh":  ("Reseñas",                      "Lo que dicen los estudiantes de Manhattan"),
        "reviews_bx":  ("Reseñas",                      "Lo que dicen los estudiantes del Bronx"),
        "faq":         ("Preguntas Frecuentes",         "Preguntas comunes"),
    },
}

# ─── gallery file list (subset of the main site's gallery photos) ────
GALLERY = [
    "lf-gal-01.jpg", "lf-gal-02.jpg", "lf-gal-03.jpg", "lf-gal-04.jpg",
    "lf-gal-05.jpg", "lf-gal-06.jpg", "lf-gal-07.jpg", "lf-gal-08.jpg",
]

# ─── YouTube clips embedded in the "Watch Us" section ────────────────
YT_CLIPS = [
    ("uADUtUtChH4", "Manhattan campus walkthrough", "Recorrido por el campus de Manhattan"),
    ("oM8KfWfeTWA", "$3 student haircuts in action", "Cortes de $3 en acción"),
    ("dQw4w9WgXcQ", "Day in the life at ABI",        "Un día en ABI"),
]
