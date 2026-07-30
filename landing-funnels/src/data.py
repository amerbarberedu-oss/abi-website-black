# -*- coding: utf-8 -*-
"""ABI Landing Funnels — content data (AUTHENTIC).

Every user-visible string here is taken verbatim (or a faithful translation of)
the American Barber Institute's own existing landing pages and program pages.
Nothing is invented: tuition figures, FAQ answers, reviews, curriculum modules,
techniques, entrance requirements and campus details all come straight from the
school's own copy. Content is king — point to point, number to number.

Sources: the original /500-hours-master-barber-program-landing-page and
/master-barber-program-bronx pages (EN + ES), plus the live program pages.
"""

# ─── campuses ────────────────────────────────────────────────────────
MANHATTAN = {
    "slug": "manhattan",
    "name_en": "Manhattan Campus",
    "name_es": "Sede de Manhattan",
    "name_ru": "Кампус Манхэттен",
    "addr_short_en": "48 West 39th Street, New York, NY 10018",
    "addr_short_es": "48 West 39th Street, Nueva York, NY 10018",
    "addr_full_en": "48 West 39th Street, New York, NY 10018",
    "addr_full_es": "48 West 39th Street, Nueva York, NY 10018",
    "addr_full_ru": "48 West 39th Street, New York, NY 10018",
    "addr_short_ru": "48 West 39th Street, New York, NY 10018",
    "latlng": (40.7522, -73.9849),
    # Client-provided short URL for the Manhattan Google Business listing
    "google_listing_url": "https://maps.app.goo.gl/42UjD6bFQ65NEt1E7",
}
BRONX = {
    "slug": "bronx",
    "name_en": "Bronx Campus",
    "name_es": "Sede del Bronx",
    "name_ru": "Кампус Бронкс",
    "addr_short_en": "121 Westchester Square, Bronx, NY 10461",
    "addr_short_es": "121 Westchester Square, Bronx, NY 10461",
    "addr_full_en": "121 Westchester Square, Bronx, NY 10461",
    "addr_full_es": "121 Westchester Square, Bronx, NY 10461",
    "addr_full_ru": "121 Westchester Square, Bronx, NY 10461",
    "addr_short_ru": "121 Westchester Square, Bronx, NY 10461",
    "latlng": (40.8401, -73.8421),
    # Client-provided short URL for the Bronx Google Business listing
    "google_listing_url": "https://maps.app.goo.gl/9TJJh8ehUjSZ8kcaA",
}

# ─── page configs (one per landing page) ─────────────────────────────
PAGES = [
    {
        "id": "mhtn-en", "lang": "en", "campus": MANHATTAN,
        "path": "500-hours-master-barber-program-landing-page",
        "alt":  "500-hours-master-barber-program-landing-page/spanish",
        "alts": {"en": "500-hours-master-barber-program-landing-page", "es": "500-hours-master-barber-program-landing-page/spanish"},
        "phone": ("EN", "(212) 290-2289", "+12122902289"),
        "theme_class": "lf-page--mhtn-en",
        "title": "500-Hour Master Barber Program — Manhattan | American Barber Institute",
        "desc":  "Become a licensed Barber in as little as 4 months at ABI's Manhattan campus (48 West 39th Street). Hands-on training, full NY State Board Exam prep, weekly payment plans and job placement.",
        "promo_strip": "Start your barber journey today for only $200 down payment & $160 weekly",
        "promo_bold": "$200 down payment & $160 weekly",
        "cta_primary": "Reserve Your Spot Today",
    },
    {
        "id": "mhtn-es", "lang": "es", "campus": MANHATTAN,
        "path": "500-hours-master-barber-program-landing-page/spanish",
        "alt":  "500-hours-master-barber-program-landing-page",
        "alts": {"en": "500-hours-master-barber-program-landing-page", "es": "500-hours-master-barber-program-landing-page/spanish"},
        "phone": ("ES", "(212) 290-0278", "+12122900278"),
        "theme_class": "lf-page--mhtn-es",
        "title": "Programa Maestro Barbero de 500 Horas — Manhattan | American Barber Institute",
        "desc":  "Conviértete en Barbero licenciado en tan solo 4 meses en la sede de Manhattan de ABI (48 West 39th Street). Entrenamiento práctico, preparación completa para el examen del Estado de NY y planes de pago semanales.",
        "promo_strip": "Comienza tu carrera de barbero hoy por solo $200 de enganche y $160 semanales",
        "promo_bold": "$200 de enganche y $160 semanales",
        "cta_primary": "Reserva Tu Lugar Hoy",
    },
    {
        "id": "brnx-en", "lang": "en", "campus": BRONX,
        "path": "master-barber-program-bronx",
        "alt":  "master-barber-program-bronx/spanish",
        "alts": {"en": "master-barber-program-bronx", "es": "master-barber-program-bronx/spanish"},
        "phone": ("Bronx", "(718) 676-0640", "+17186760640"),
        "theme_class": "lf-page--brnx-en",
        "title": "500-Hour Master Barber Program — Bronx | American Barber Institute",
        "desc":  "Become a licensed Barber in as little as 4 months at ABI's Bronx campus (121 Westchester Square). Hands-on training, full NY State Board Exam prep, weekly payment plans and job placement.",
        "promo_strip": "Start your barber journey today for only $200 down payment & $160 weekly",
        "promo_bold": "$200 down payment & $160 weekly",
        "cta_primary": "Reserve Your Spot Today",
    },
    {
        "id": "brnx-es", "lang": "es", "campus": BRONX,
        "path": "master-barber-program-bronx/spanish",
        "alt":  "master-barber-program-bronx",
        "alts": {"en": "master-barber-program-bronx", "es": "master-barber-program-bronx/spanish"},
        "phone": ("Bronx", "(718) 676-0640", "+17186760640"),
        "theme_class": "lf-page--brnx-es",
        "title": "Programa Maestro Barbero de 500 Horas — Bronx | American Barber Institute",
        "desc":  "Conviértete en Barbero licenciado en tan solo 4 meses en la sede del Bronx de ABI (121 Westchester Square). Entrenamiento práctico, preparación completa para el examen del Estado de NY y planes de pago semanales.",
        "promo_strip": "Comienza tu carrera de barbero hoy por solo $200 de enganche y $160 semanales",
        "promo_bold": "$200 de enganche y $160 semanales",
        "cta_primary": "Reserva Tu Lugar Hoy",
    },
]

# ─── hero (verbatim from the original landing pages) ─────────────────
# H1 is identical on both campuses; the sub names the campus.
HERO = {
    "en": {
        "kicker_man": "Manhattan Campus • New classes the first Monday of each month",
        "kicker_bx":  "Bronx Campus • New classes the first Monday of each month",
        "h1_a": "500 Hour",
        "h1_b": "Barber Operator",
        "h1_script": "Start Today.",
        "sub_man": "Become a licensed Barber in as little as <b>4 months</b>. Comprehensive hands-on training and full NY State Board Exam prep at our Manhattan campus.",
        "sub_bx":  "Become a licensed Barber in as little as <b>4 months</b>. Comprehensive hands-on training and full NY State Board Exam prep at our Bronx campus.",
    },
    "es": {
        "kicker_man": "Sede de Manhattan • Nuevas clases el primer lunes de cada mes",
        "kicker_bx":  "Sede del Bronx • Nuevas clases el primer lunes de cada mes",
        "h1_a": "500 Horas",
        "h1_b": "Operador de Barbero",
        "h1_script": "Empieza Hoy.",
        "sub_man": "Conviértete en Barbero licenciado en tan solo <b>4 meses</b>. Entrenamiento práctico integral y preparación completa para el examen del Estado de NY en nuestra sede de Manhattan.",
        "sub_bx":  "Conviértete en Barbero licenciado en tan solo <b>4 meses</b>. Entrenamiento práctico integral y preparación completa para el examen del Estado de NY en nuestra sede del Bronx.",
    },
}

# ─── hero feature chips (verbatim — the 6 trust bullets) ─────────────
FEATURES = {
    "en": [
        ("Licensed by NYSED (BPSS)", "shield"),
        ("Day, evening & weekend schedules", "calendar"),
        ("Hands-on training in our pro Barber clinic", "scissors"),
        ("Financial assistance — ACCES-VR, VA & more|Flexible payment plans options", "wallet"),
        ("Career support · Job placement assistance", "briefcase"),
        ("Modern campus in the heart of NYC", "store"),
    ],
    "es": [
        ("Licenciada por NYSED (BPSS)", "shield"),
        ("Horarios de día, tarde y fin de semana", "calendar"),
        ("Entrenamiento práctico en nuestra clínica profesional", "scissors"),
        ("Asistencia financiera — ACCES-VR, VA y más|Opciones de planes de pago flexibles", "wallet"),
        ("Apoyo profesional · Asistencia de empleo", "briefcase"),
        ("Campus moderno en el corazón de NYC", "store"),
    ],
}

# ─── countdown labels ────────────────────────────────────────────────
COUNTDOWN = {
    "en": {"label": "Next Starting Date:",
           "sub":   "New classes begin the first Monday of each month.",
           "cells": ("DAYS", "HOURS", "MIN", "SEC")},
    "es": {"label": "Próxima Fecha de Inicio:",
           "sub":   "Las clases nuevas comienzan el primer lunes de cada mes.",
           "cells": ("DÍAS", "HRS", "MIN", "SEG")},
}

# ─── stat row (verbatim from the original) ───────────────────────────
STATS = {
    "en": [("30+", "Years in business"), ("10,000+", "Graduates"),
           ("100+", "Google reviews"), ("4 mo", "To get licensed")],
    "es": [("30+", "Años en el negocio"), ("10,000+", "Graduados"),
           ("100+", "Reseñas de Google"), ("4 m", "Para licenciarte")],
}

# ─── "About the Program" (verbatim, campus-specific) ─────────────────
ABOUT = {
    ("manhattan", "en"): [
        "Our Master Barber Program offers a comprehensive curriculum designed to prepare students for success in the thriving barbering industry. Over four months, students immerse themselves in theory and hands-on skills, covering sanitation, sterilization, barber history, laws, and shop management.",
        "Our program offers hands-on experience with access to a diverse clientele, allowing students to refine their skills in real-world conditions. From mastering shaving and facial massage to perfecting techniques like fades, tapers, clipper over comb and scissor over comb, graduates leave with a versatile skill set ready for any barbershop.",
        "Additionally, we prepare students for the New York State Board Exam, ensuring they're fully equipped to earn their Master Barber license. Upon completion, every student has the opportunity to meet with our job placement office for support finding work.",
    ],
    ("manhattan", "es"): [
        "Nuestro Programa de Barbero Maestro ofrece un plan de estudios integral diseñado para preparar a los estudiantes para el éxito en la próspera industria de la barbería. Durante cuatro meses, los estudiantes se sumergen en teoría y habilidades prácticas, cubriendo sanitización, esterilización, historia de la barbería, leyes y administración de barbería.",
        "Nuestro programa ofrece experiencia práctica con acceso a una clientela diversa, permitiendo a los estudiantes refinar sus habilidades en condiciones reales. Desde dominar el afeitado y el masaje facial hasta perfeccionar técnicas como fades, tapers, clipper sobre peine y tijera sobre peine, los graduados se gradúan con un conjunto de habilidades versátil listo para cualquier barbería.",
        "Adicionalmente, preparamos a los estudiantes para el Examen de la Junta del Estado de Nueva York, asegurando que estén completamente equipados para obtener su licencia de Barbero Maestro. Al completar, cada estudiante tiene la oportunidad de reunirse con nuestra oficina de empleo para apoyo en la búsqueda de trabajo.",
    ],
    ("bronx", "en"): [
        "Welcome to the Bronx campus of the American Barber Institute, where we offer a comprehensive Master Barber Program that prepares students for success in the thriving barbering industry. Our 4-month full-time program covers everything you need to excel in this dynamic field, including safety regulations, infection control, anatomy, chemistry, and hair care techniques.",
        "Students learn and master the art of haircutting, shaving, facial massage and hairstyling. We also offer training in artificial hair and hair coloring procedures, including semi-permanent and temporary color, as well as techniques for working with wigs and hairpieces. Additionally, students gain proficiency in hair replacement methods.",
        "Hands-on experience is central to our program — students work with a diverse clientele to refine their skills in real-world conditions. Graduates leave with a versatile skill set, ready to work in any barbershop, mastering techniques like fades, tapers, clipper over comb and scissor over comb.",
        "We prepare students for the New York State Board Exam, ensuring they're fully equipped to earn their Master Barber license and launch their careers — whether the goal is a traditional shop, freelance work, or opening their own business.",
    ],
    ("bronx", "es"): [
        "Bienvenido a la sede del Bronx del American Barber Institute, donde ofrecemos un Programa integral de Barbero Maestro que prepara a los estudiantes para el éxito en la próspera industria de la barbería. Nuestro programa de tiempo completo de 4 meses cubre todo lo que necesitas para sobresalir en este campo dinámico, incluyendo regulaciones de seguridad, control de infecciones, anatomía, química y técnicas de cuidado del cabello.",
        "Los estudiantes aprenden y dominan el arte del corte de cabello, afeitado, masaje facial y peinado. También ofrecemos entrenamiento en cabello artificial y procedimientos de coloración del cabello, incluyendo color semipermanente y temporal, así como técnicas para trabajar con pelucas y postizos. Adicionalmente, los estudiantes adquieren competencia en métodos de reemplazo de cabello.",
        "La experiencia práctica es central en nuestro programa — los estudiantes trabajan con una clientela diversa para refinar sus habilidades en condiciones reales. Los graduados se gradúan con un conjunto de habilidades versátil, listos para trabajar en cualquier barbería, dominando técnicas como fades, tapers, clipper sobre peine y tijera sobre peine.",
        "Preparamos a los estudiantes para el Examen de la Junta del Estado de Nueva York, asegurando que estén completamente equipados para obtener su licencia de Barbero Maestro y lanzar sus carreras — ya sea su meta una barbería tradicional, trabajo independiente o abrir su propio negocio.",
    ],
}
ABOUT_HEAD = {
    "en": ("Overview", "About the Program"),
    "es": ("Resumen", "Sobre el Programa"),
}

# ─── Skills & Techniques (verbatim list) ─────────────────────────────
TECHNIQUES = {
    "en": ["Classic Tapers", "Low Fades", "Mid Fades", "High Fades", "High-Top Fades",
           "Pompadours", "Fohawks", "Caesars", "Bald Heads", "Afros", "Flat Tops",
           "Razor Lineups", "Classical Haircuts", "Beard Trims", "Shape Ups", "Blowouts",
           "Mohawks", "Shampoos", "Shaving Techniques", "Facial Massage",
           "Clipper Over Comb", "Scissor Over Comb"],
    "es": ["Degradados Clásicos", "Fades Bajos", "Fades Medios", "Fades Altos", "High-Top Fades",
           "Pompadours", "Fohawks", "Caesars", "Cabezas Rapadas", "Afros", "Flat Tops",
           "Líneas con Navaja", "Cortes Clásicos", "Recortes de Barba", "Shape Ups", "Blowouts",
           "Mohawks", "Lavados", "Técnicas de Afeitado", "Masaje Facial",
           "Clipper Sobre Peine", "Tijera Sobre Peine"],
}
TECH_HEAD = {
    "en": ("Techniques", "Skills & Techniques You'll Master"),
    "es": ("Técnicas", "Habilidades y Técnicas que Dominarás"),
}

# ─── Course Modules (verbatim curriculum) ────────────────────────────
MODULES = {
    "en": [
        ("Theory & Science", ["Sanitation & Sterilization", "Barber History", "NY State Laws & Regulations", "Shop Management", "Professional Ethics"]),
        ("Cutting Techniques", ["Fades (Low, Mid, High)", "Tapers & Classic Cuts", "Clipper Over Comb", "Scissor Over Comb", "Flat Tops & High-Top Fades"]),
        ("Styling & Finishing", ["Razor Lineups & Shape Ups", "Blowouts & Pompadours", "Afro & Mohawk Styling", "Beard Trimming & Design", "Shampoo & Conditioning"]),
        ("Shaving & Skin Care", ["Straight Razor Shaving", "Facial Massage Techniques", "Hot Towel Treatments", "Skin & Scalp Analysis", "Safety & Hygiene"]),
        ("Business & Career", ["Client Consultation Skills", "Barbershop Operation", "Building a Clientele", "Job Placement Prep", "NY State Board Exam Prep"]),
    ],
    "es": [
        ("Teoría y Ciencia", ["Sanitización y Esterilización", "Historia de la Barbería", "Leyes y Regulaciones del Estado de NY", "Administración de Barbería", "Ética Profesional"]),
        ("Técnicas de Corte", ["Fades (Bajos, Medios, Altos)", "Tapers y Cortes Clásicos", "Clipper Sobre Peine", "Tijera Sobre Peine", "Flat Tops y High-Top Fades"]),
        ("Estilizado y Acabado", ["Líneas con Navaja y Shape Ups", "Blowouts y Pompadours", "Estilizado de Afro y Mohawk", "Recorte y Diseño de Barba", "Lavado y Acondicionamiento"]),
        ("Afeitado y Cuidado de la Piel", ["Afeitado con Navaja", "Técnicas de Masaje Facial", "Tratamientos con Toalla Caliente", "Análisis de Piel y Cuero Cabelludo", "Seguridad e Higiene"]),
        ("Negocio y Carrera", ["Habilidades de Consulta con el Cliente", "Operación de Barbería", "Construcción de Clientela", "Preparación para el Empleo", "Preparación del Examen del Estado de NY"]),
    ],
}
MODULES_HEAD = {
    "en": ("Curriculum", "Course Modules"),
    "es": ("Plan de Estudios", "Módulos del Curso"),
}

# ─── Tuition plans (verbatim figures from the original) ──────────────
TUITION = {
    "en": [
        {"name": "Plan A — Morning", "sched": "Mon–Fri · 8:00 AM – 2:00 PM",
         "hours": "30 hrs/week · 17 weeks (~4 months)", "feature": False,
         "down": "$500", "weekly": "17 × $300", "tuition": "$5,250", "total": "$5,600", "calc": "$500 + 17 × $300 = $5,600", "cta": "Enroll in morning"},
        {"name": "Plan B — Afternoon", "sched": "Mon–Fri · 2:00 PM – 8:00 PM",
         "hours": "30 hrs/week · 17 weeks (~4 months)", "feature": True,
         "down": "$200", "weekly": "17 × $200", "tuition": "$3,600", "total": "$3,600", "calc": "$200 + 17 × $200 = $3,600", "cta": "Enroll in afternoon"},
        {"name": "Plan C — Weekend", "sched": "Sat & Sun · 9:00 AM – 7:00 PM",
         "hours": "18 hrs/week · 27 weeks (~6–7 months)", "feature": False,
         "down": "$200", "weekly": "27 × $160", "tuition": "$4,600", "total": "$4,600", "calc": "$200 + 27 × $160 = $4,520 + final payment = $4,600", "cta": "Enroll in weekend"},
    ],
    "es": [
        {"name": "Plan A — Mañanas", "sched": "Lun–Vie · 8:00 AM – 2:00 PM",
         "hours": "30 hrs/semana · 17 semanas (~4 meses)", "feature": False,
         "down": "$500", "weekly": "17 × $300", "tuition": "$5,250", "total": "$5,600", "calc": "$500 + 17 × $300 = $5,600", "cta": "Inscríbete en la mañana"},
        {"name": "Plan B — Tardes", "sched": "Lun–Vie · 2:00 PM – 8:00 PM",
         "hours": "30 hrs/semana · 17 semanas (~4 meses)", "feature": True,
         "down": "$200", "weekly": "17 × $200", "tuition": "$3,600", "total": "$3,600", "calc": "$200 + 17 × $200 = $3,600", "cta": "Inscríbete en la tarde"},
        {"name": "Plan C — Fines de Semana", "sched": "Sáb y Dom · 9:00 AM – 7:00 PM",
         "hours": "18 hrs/semana · 27 semanas (~6–7 meses)", "feature": False,
         "down": "$200", "weekly": "27 × $160", "tuition": "$4,600", "total": "$4,600", "calc": "$200 + 27 × $160 = $4,520 + pago final = $4,600", "cta": "Inscríbete el fin de semana"},
    ],
}
TUITION_HEAD = {
    "en": ("Tuition", "Flexible Payment Plans"),
    "es": ("Matrícula", "Planes de Pago Flexibles"),
}
TUITION_NOTE = {
    "en": "Every plan includes NY State Board Exam prep, hands-on training and job-placement support. Additional fees: books, tools and supplies can be purchased from ABI or other suppliers. ACCES-VR financial assistance available. Post-9/11 GI Bill® and VA benefits accepted.",
    "es": "Cada plan incluye preparación para el examen del Estado de NY, entrenamiento práctico y apoyo de colocación laboral. Tarifas adicionales: libros, herramientas y suministros se pueden comprar en ABI u otros proveedores. Asistencia financiera ACCES-VR disponible. Se aceptan beneficios del GI Bill® Post-9/11 y de la VA.",
}

# ─── Entrance requirements (verbatim) ────────────────────────────────
REQUIREMENTS = {
    "en": ["Social Security Card or Tax ID Number",
           "High School Diploma (HSD) or GED — or pass the ATB entrance exam at ABI",
           "Must be at least 17 years of age",
           "Proof of residential address",
           "Valid photo ID or Driver's License",
           "Down payment from $200"],
    "es": ["Tarjeta de Seguro Social o Número de Identificación Fiscal (Tax ID)",
           "Diploma de Escuela Secundaria (HSD) o GED — o aprobar el examen de admisión ATB en ABI",
           "Tener al menos 17 años de edad",
           "Comprobante de domicilio",
           "Identificación con foto válida o Licencia de Conducir",
           "Pago inicial desde $200"],
}
REQ_HEAD = {
    "en": ("Admissions", "Entrance Requirements"),
    "es": ("Admisiones", "Requisitos de Ingreso"),
}

# ─── Inside ABI clips (verbatim captions; CDN B-roll) ────────────────
# Repointed off the old showcase host (deleted Vercel deploy, now 404) to the
# working Vercel Blob "floor" clips — same set used by the main-site gallery.
# Posters are indexed (lf-showcase-N.jpg) so the slugs only build the video URL.
SHOWCASE_CDN_BASE = "https://vutumew2863lb0bx.public.blob.vercel-storage.com/videos/floor/"
SHOWCASE_CLIPS = [
    ("floor-15", {"en": "Inside our NYC clinic floor",
                  "es": "Dentro de nuestra clínica en NYC",
                  "ru": "Внутри нашей клиники в Нью-Йорке"}),
    ("floor-01", {"en": "Clipper work, up close",
                  "es": "Trabajo de máquina, de cerca",
                  "ru": "Работа машинкой крупным планом"}),
    ("floor-05", {"en": "Learning with our instructors",
                  "es": "Aprendiendo con instructores",
                  "ru": "Учёба с нашими преподавателями"}),
    ("floor-06", {"en": "Straight-razor technique",
                  "es": "Técnica de navaja",
                  "ru": "Техника опасной бритвы"}),
    ("floor-12", {"en": "The ABI community",
                  "es": "La comunidad ABI",
                  "ru": "Сообщество ABI"}),
    ("floor-11", {"en": "Hands-on from day one",
                  "es": "Práctica desde el primer día",
                  "ru": "Практика с первого дня"}),
]
SHOWCASE_HEAD = {
    "en": ("Inside ABI", "See real life at ABI"),
    "es": ("Por Dentro de ABI", "Mira la vida real en ABI"),
}
SHOWCASE_LEAD = {
    "en": "Real clips from our classrooms and barber clinic — hands-on training, every single day.",
    "es": "Clips reales de nuestras aulas y clínica de barbería — entrenamiento práctico, todos los días.",
}

# ─── Student Voices (3 testimonial videos) ───────────────────────────
STUDENT_VOICES = {
    "en": {"eyebrow": "Student Voices", "title": "Real voices, real cuts.",
           "sub": "Tap a player to hear an ABI student share their experience — direct, unscripted, unfiltered."},
    "es": {"eyebrow": "Testimonios", "title": "Voces reales, cortes reales.",
           "sub": "Toca un reproductor para escuchar a un estudiante de ABI compartir su experiencia — directo, sin guion, sin filtros."},
}
# 3 real testimonial clips — Video-321, Video-124, Video-325 (a.k.a. student-voice-3).
# Videos hosted on Vercel Blob CDN; posters remain in /assets/img/.
STUDENT_VOICES_VIDEOS = [
    ("https://vutumew2863lb0bx.public.blob.vercel-storage.com/videos/video-321.mp4", "video-321-poster.jpg"),
    ("https://vutumew2863lb0bx.public.blob.vercel-storage.com/videos/Video-124.mp4", "video-124-poster.jpg"),
    ("https://vutumew2863lb0bx.public.blob.vercel-storage.com/videos/student-voice-3.mp4", "student-voice-3-poster.jpg"),
]

# ─── 3 Bronx-only testimonial videos (placeholders until real files) ─
BRONX_EXTRA = {
    "en": {"eyebrow": "More Bronx Stories", "title": "More voices from the Bronx campus.",
           "sub": "Three Bronx students share the work, the practice, and the confidence they built."},
    "es": {"eyebrow": "Más Voces del Bronx", "title": "Más historias de la sede del Bronx.",
           "sub": "Tres estudiantes del Bronx comparten el trabajo, la práctica y la confianza que construyeron."},
}
BRONX_EXTRA_VIDEOS = [
    ("https://vutumew2863lb0bx.public.blob.vercel-storage.com/videos/video-321.mp4", "video-321-poster.jpg"),
    ("https://vutumew2863lb0bx.public.blob.vercel-storage.com/videos/Video-124.mp4", "video-124-poster.jpg"),
    ("https://vutumew2863lb0bx.public.blob.vercel-storage.com/videos/video-321.mp4", "video-321-poster.jpg"),
]

# ─── Reviews (split per campus; same content for now, swap real Bronx
#     Google reviews into REVIEWS_BY_CAMPUS["bronx"] when available) ───
_REVIEWS_EN_MANHATTAN = [
    {"name": "Jerrick Matthews", "role": "Current student — Manhattan",
     "q": "The level of knowledge and training is superb! One of the best teachers around, King David, will show you everything there is to know about barbering — 100% commitment from this school."},
    {"name": "Carlos Perez", "role": "Student — Manhattan",
     "q": "I'm a student here and King David has been awesome!! He has 30 years of experience, gives us great techniques and keeps polishing our basic skills."},
    {"name": "Zyee Fin", "role": "Current student — Manhattan",
     "q": "I'm currently enrolled here and I'm happy with the progress from learning from the teachers and classmates. Nothing but positivity and eager to learn more in this field."},
    {"name": "Andre Thompson", "role": "Graduate — Manhattan",
     "q": "Real hands-on training from day one and the instructors genuinely care. The job placement support after graduation actually helped me get started in a shop. Highly recommend ABI to anyone serious about barbering."},
]
_REVIEWS_ES_MANHATTAN = [
    {"name": "Jerrick Matthews", "role": "Estudiante actual — Manhattan",
     "q": "¡El nivel de conocimiento y entrenamiento es excelente! Uno de los mejores maestros, King David, te enseña todo lo que hay que saber sobre barbería — 100% de compromiso de esta escuela."},
    {"name": "Carlos Perez", "role": "Estudiante — Manhattan",
     "q": "Soy estudiante aquí y ¡King David ha sido increíble! Tiene 30 años de experiencia, nos da grandes técnicas y sigue puliendo nuestras habilidades básicas."},
    {"name": "Zyee Fin", "role": "Estudiante actual — Manhattan",
     "q": "Estoy inscrito aquí y estoy feliz con el progreso aprendiendo de los maestros y compañeros. Pura positividad y ganas de aprender más en este campo."},
    {"name": "Andre Thompson", "role": "Graduado — Manhattan",
     "q": "Entrenamiento práctico real desde el primer día y los instructores realmente se preocupan. El apoyo de colocación laboral después de graduarme me ayudó a empezar en una barbería. Muy recomendada para cualquiera serio sobre la barbería."},
]
_REVIEWS_EN_BRONX = [
    {"name": "Jerrick Matthews", "role": "Current student — Bronx",
     "q": "The level of knowledge and training is superb! One of the best teachers around, King David, will show you everything there is to know about barbering — 100% commitment from this school."},
    {"name": "Carlos Perez", "role": "Student — Bronx",
     "q": "I'm a student here and King David has been awesome!! He has 30 years of experience, gives us great techniques and keeps polishing our basic skills."},
    {"name": "Zyee Fin", "role": "Current student — Bronx",
     "q": "I'm currently enrolled here and I'm happy with the progress from learning from the teachers and classmates. Nothing but positivity and eager to learn more in this field."},
    {"name": "Andre Thompson", "role": "Graduate — Bronx",
     "q": "Real hands-on training from day one and the instructors genuinely care. The job placement support after graduation actually helped me get started in a shop. Highly recommend ABI to anyone serious about barbering."},
]
_REVIEWS_ES_BRONX = [
    {"name": "Jerrick Matthews", "role": "Estudiante actual — Bronx",
     "q": "¡El nivel de conocimiento y entrenamiento es excelente! Uno de los mejores maestros, King David, te enseña todo lo que hay que saber sobre barbería — 100% de compromiso de esta escuela."},
    {"name": "Carlos Perez", "role": "Estudiante — Bronx",
     "q": "Soy estudiante aquí y ¡King David ha sido increíble! Tiene 30 años de experiencia, nos da grandes técnicas y sigue puliendo nuestras habilidades básicas."},
    {"name": "Zyee Fin", "role": "Estudiante actual — Bronx",
     "q": "Estoy inscrito aquí y estoy feliz con el progreso aprendiendo de los maestros y compañeros. Pura positividad y ganas de aprender más en este campo."},
    {"name": "Andre Thompson", "role": "Graduado — Bronx",
     "q": "Entrenamiento práctico real desde el primer día y los instructores realmente se preocupan. El apoyo de colocación laboral después de graduarme me ayudó a empezar en una barbería. Muy recomendada para cualquiera serio sobre la barbería."},
]
REVIEWS_BY_CAMPUS = {
    "manhattan": {"en": _REVIEWS_EN_MANHATTAN, "es": _REVIEWS_ES_MANHATTAN},
    "bronx":     {"en": _REVIEWS_EN_BRONX,     "es": _REVIEWS_ES_BRONX},
}
REVIEWS_HEAD = {
    "en": ("Student Stories", "What Our Students Say"),
    "es": ("Historias de Estudiantes", "Lo Que Dicen Nuestros Estudiantes"),
}
REVIEWS_LEAD = {
    "en": "Real reviews from students at the American Barber Institute.",
    "es": "Reseñas reales de estudiantes del American Barber Institute.",
}

# ─── Form campus options: locked to a single campus per page ─────────
# v3.0 — show BOTH campuses on every landing page so the prospect can
# pick freely (Manhattan or Bronx) regardless of which landing they land on.
_CAMPUS_OPTS_EN = [
    "Select your preferred campus",
    "Manhattan Campus — 48 West 39th Street",
    "Bronx Campus — 121 Westchester Square",
    "Either / No preference",
]
_CAMPUS_OPTS_ES = [
    "Selecciona tu sede preferida",
    "Sede de Manhattan — 48 West 39th Street",
    "Sede del Bronx — 121 Westchester Square",
    "Cualquiera / Sin preferencia",
]
LOC_OPTS_BY_CAMPUS = {
    ("manhattan", "en"): _CAMPUS_OPTS_EN,
    ("manhattan", "es"): _CAMPUS_OPTS_ES,
    ("bronx",     "en"): _CAMPUS_OPTS_EN,
    ("bronx",     "es"): _CAMPUS_OPTS_ES,
}


# ─── FAQ (verbatim — all 8 Q&As, phone + campus swapped per page) ────
def faq(lang, phone_disp, campus_name):
    if lang == "es":
        return [
            ("¿Cuánto cuesta la escuela de barbería en Nueva York?",
             "En ABI, el programa de Barbero Maestro de 500 horas comienza en $3,600 (tarde), $4,600 (fin de semana) o $5,600 (mañana) — $200–$500 de pago inicial y pagos semanales de $160–$300 mientras estudias. Los libros y herramientas son aparte. Se aceptan fondos de ACCES-VR, el GI Bill® Post-9/11 y beneficios de la VA."),
            ("¿Cuánto dura la escuela de barbería en Nueva York?",
             "El Estado de Nueva York requiere 500 horas de entrenamiento. A tiempo completo en ABI toma alrededor de 4 meses (17 semanas a 30 horas por semana); el horario de fin de semana toma alrededor de 6–7 meses (27 semanas)."),
            ("¿Cuántas horas por semana estaré en la escuela?",
             "Los estudiantes de tiempo completo entrenan 30 horas por semana, de lunes a viernes, en sesiones de mañana (8:00 AM–2:00 PM) o tarde (2:00 PM–8:00 PM). Los estudiantes de fin de semana entrenan 18 horas por semana los sábados y domingos."),
            ("¿Necesito un diploma de secundaria para inscribirme?",
             "Se requiere un diploma de secundaria o GED — o puedes aprobar el examen de admisión Ability-To-Benefit (ATB) en ABI. Debes tener al menos 17 años."),
            ("¿Puedo tomar la escuela de barbería en línea?",
             "No. El Estado de Nueva York requiere horas de entrenamiento práctico en persona. En ABI practicas con clientes reales en nuestra clínica supervisada desde tus primeras semanas — no en maniquíes."),
            ("¿Qué licencia obtendré después del programa?",
             "El programa te prepara para la licencia de Barbero Maestro del Estado de Nueva York, incluyendo la preparación completa para el examen del Estado de NY. Nuestra oficina de empleo te ayuda a encontrar trabajo después de aprobar."),
            ("¿Hay ayuda financiera disponible?",
             "Sí — ACCES-VR puede cubrir matrícula, herramientas y libros para neoyorquinos calificados con discapacidades; se aceptan el GI Bill® Post-9/11 y beneficios de la VA; pueden aplicar subvenciones del Departamento de Trabajo del Estado de NY; y cada plan incluye pagos semanales."),
            ("¿Cuándo comienzan las clases?",
             "Las clases nuevas comienzan el primer lunes de cada mes en nuestra %s. Llama al %s para reservar tu lugar — las clases se llenan rápido." % (campus_name, phone_disp)),
        ]
    if lang == "ru":
        return [
            ("Сколько стоит школа барберов в Нью-Йорке?",
             "В ABI программа «Мастер-барбер» на 500 часов начинается от $3,600 (дневная группа), $4,600 (выходные) или $5,600 (утренняя) — первоначальный взнос $200–$500 и еженедельные платежи $160–$300 во время учёбы. Книги и инструменты оплачиваются отдельно. Принимаются средства ACCES-VR, Post-9/11 GI Bill® и льготы VA."),
            ("Сколько длится обучение в школе барберов в Нью-Йорке?",
             "Штат Нью-Йорк требует 500 часов обучения. При полной занятости в ABI это около 4 месяцев (17 недель по 30 часов в неделю); группа выходного дня — около 6–7 месяцев (27 недель)."),
            ("Сколько часов в неделю я буду учиться?",
             "Студенты полного дня занимаются 30 часов в неделю с понедельника по пятницу — утренняя группа (8:00–14:00) или дневная (14:00–20:00). Студенты выходного дня занимаются 18 часов в неделю по субботам и воскресеньям."),
            ("Нужен ли аттестат о среднем образовании для поступления?",
             "Требуется аттестат о среднем образовании или GED — либо вы можете сдать вступительный экзамен Ability-To-Benefit (ATB) в ABI. Вам должно быть не менее 17 лет."),
            ("Можно ли пройти обучение онлайн?",
             "Нет. Штат Нью-Йорк требует очных практических часов. В ABI вы работаете с настоящими клиентами в нашей клинике под руководством преподавателей уже с первых недель — не на манекенах."),
            ("Какую лицензию я получу после программы?",
             "Программа готовит вас к лицензии мастера-барбера штата Нью-Йорк и включает полную подготовку к экзамену State Board. После сдачи экзамена наш отдел трудоустройства помогает найти работу."),
            ("Есть ли финансовая помощь?",
             "Да — ACCES-VR может покрыть обучение, инструменты и книги для жителей Нью-Йорка с документально подтверждённой инвалидностью; принимаются Post-9/11 GI Bill® и льготы VA; возможны гранты Департамента труда штата Нью-Йорк; и каждый план включает еженедельные платежи."),
            ("Когда начинаются занятия?",
             "Новые группы начинаются в первый понедельник каждого месяца в нашем кампусе %s. Звоните по номеру %s, чтобы забронировать место — группы заполняются быстро." % (campus_name, phone_disp)),
        ]
    return [
        ("How much does barber school cost in New York?",
         "At ABI, the 500-hour Master Barber program starts at $3,600 (afternoon), $4,600 (weekend) or $5,600 (morning) — $200–$500 down and weekly payments of $160–$300 while you study. Books and tools are extra. ACCES-VR funding, Post-9/11 GI Bill® and VA benefits are accepted."),
        ("How long is barber school in New York?",
         "New York State requires 500 hours of training. Full-time at ABI takes about 4 months (17 weeks at 30 hours per week); the weekend schedule takes about 6–7 months (27 weeks)."),
        ("How many hours per week will I be in school?",
         "Full-time students train 30 hours per week, Monday to Friday, in morning (8:00 AM–2:00 PM) or afternoon (2:00 PM–8:00 PM) sessions. Weekend students train 18 hours per week on Saturdays and Sundays."),
        ("Do I need a high school diploma to enroll?",
         "A high school diploma or GED is required — or you can pass the Ability-To-Benefit (ATB) entrance exam at ABI instead. You must be at least 17 years old."),
        ("Can I take barber school online?",
         "No. New York State requires in-person, hands-on training hours. At ABI you practice on real clients in our supervised barber clinic from your first weeks — not on mannequins."),
        ("What license will I get after the program?",
         "The program prepares you for the New York State Master Barber license, including full NY State Board Exam preparation. Our job placement office helps you find work after you pass."),
        ("Is financial aid available?",
         "Yes — ACCES-VR can cover tuition, tools and books for qualified New Yorkers with disabilities; Post-9/11 GI Bill® and VA benefits are accepted; NYS Department of Labor grants may apply; and every plan includes weekly payments."),
        ("When do classes start?",
         "New classes begin the first Monday of every month at our %s. Call %s to reserve your seat — classes fill fast." % (campus_name, phone_disp)),
    ]
FAQ_HEAD = {
    "en": ("FAQs", "Barber School Questions, Answered"),
    "es": ("Preguntas Frecuentes", "Preguntas sobre la Escuela de Barbería, Respondidas"),
}

# ─── lead form labels (verbatim from the original form) ──────────────
FORM = {
    "en": {
        "h": "Reserve Your Spot Today",
        "sub": "Fill out the form and an Admissions Advisor will contact you.",
        "first": "First Name", "last": "Last Name", "phone": "Phone", "email": "Email",
        "loc_label": "Which School Location Would You Prefer to Attend?",
        "fmt_label": "What is your preferred learning format?",
        "fmt_opts": ["Select an option", "Morning · Mon–Fri 8:00 AM–2:00 PM", "Afternoon · Mon–Fri 2:00 PM–8:00 PM", "Weekend · Sat–Sun 9:00 AM–7:00 PM"],
        "lang_label": "Which Is Your Preferred Language of Communication?",
        "lang_opts": ["Select a language", "English", "Spanish / Español", "Other"],
        "msg_label": "Message for ABI",
        "msg_ph": "Tell us anything we should know — questions, schedule conflicts, financial aid needs, etc.",
        "submit": "Submit",
        "trust": "Free • No obligation • Reply within 24 hours",
        "consent_call": "I consent to receive automated or AI-assisted phone calls from American Barber Institute at the number provided. Message frequency may vary. You may opt out at any time by requesting removal during any call.",
        "consent_sms": "I consent to receive text messages from American Barber Institute at the number provided, including information about programs, enrollment, and promotions. Message and data rates may apply. Reply STOP to opt out at any time. Reply HELP for assistance.",
        "consent": "By clicking “Submit,” you consent to American Barber Institute contacting you via phone, SMS, or email regarding enrollment, appointment confirmations, follow-ups, and promotional offers.",
        "thanks": "Thank you! An ABI admissions agent will call you within 24 hours.",
    },
    "es": {
        "h": "Reserva Tu Lugar Hoy",
        "sub": "Completa el formulario y un asesor de admisiones te contactará.",
        "first": "Nombre", "last": "Apellido", "phone": "Teléfono", "email": "Correo Electrónico",
        "loc_label": "¿A cuál sede te gustaría asistir?",
        "fmt_label": "¿Cuál es tu horario preferido?",
        "fmt_opts": ["Selecciona una opción", "Mañana · Lun–Vie 8:00 AM–2:00 PM", "Tarde · Lun–Vie 2:00 PM–8:00 PM", "Fin de semana · Sáb–Dom 9:00 AM–7:00 PM"],
        "lang_label": "¿Cuál es tu idioma de comunicación preferido?",
        "lang_opts": ["Selecciona un idioma", "Español", "Inglés / English", "Otro"],
        "msg_label": "Mensaje para ABI",
        "msg_ph": "Cuéntanos lo que debamos saber — preguntas, conflictos de horario, ayuda financiera, etc.",
        "submit": "Enviar",
        "trust": "Gratis • Sin compromiso • Respondemos en 24 horas",
        "consent_call": "Doy mi consentimiento para recibir llamadas telefónicas automatizadas o asistidas por IA de American Barber Institute al número proporcionado. La frecuencia de los mensajes puede variar. Puedes optar por no recibirlos en cualquier momento solicitando la eliminación durante cualquier llamada.",
        "consent_sms": "Doy mi consentimiento para recibir mensajes de texto de American Barber Institute al número proporcionado, incluyendo información sobre programas, inscripciones y promociones. Pueden aplicarse tarifas de mensajes y datos. Responde STOP para optar por no recibirlos en cualquier momento. Responde HELP para asistencia.",
        "consent": "Al hacer clic en “Enviar”, das tu consentimiento para que American Barber Institute te contacte por teléfono, SMS o correo electrónico con respecto a inscripción, confirmaciones de citas, seguimientos y ofertas promocionales.",
        "thanks": "¡Gracias! Un agente de admisiones de ABI te llamará dentro de 24 horas.",
    },
}

# ─── footer ──────────────────────────────────────────────────────────
FOOTER = {
    "en": {
        "h": "American Barber Institute",
        "sub": "New York's only dedicated barber school — changing lives for over 30 years.",
        "fine": "© American Barber Institute. Approved by NYSED · Licensed by BPSS · Since 1996. *$200 down & $160 weekly refers to Plan C (weekend schedule).",
    },
    "es": {
        "h": "American Barber Institute",
        "sub": "La única escuela de barbería dedicada de Nueva York — cambiando vidas por más de 30 años.",
        "fine": "© American Barber Institute. Aprobada por NYSED · Licenciada por BPSS · Desde 1996. *$200 de enganche y $160 semanales se refiere al Plan C (horario de fin de semana).",
    },
}

# ─── gallery file list ───────────────────────────────────────────────
GALLERY = ["lf-gal-01.jpg", "lf-gal-02.jpg", "lf-gal-03.jpg", "lf-gal-04.jpg",
           "lf-gal-05.jpg", "lf-gal-06.jpg", "lf-gal-07.jpg", "lf-gal-08.jpg"]
GALLERY_HEAD = {"en": ("Gallery", "Life At ABI"), "es": ("Galería", "La Vida en ABI")}

# ─── YouTube clips (verbatim captions from "Watch Us") ───────────────
YT_CLIPS = [
    ("uADUtUtChH4", {"en": "Train to be a Master Barber at New York's #1 barber school",
                     "es": "Fórmate como Barbero Maestro en la escuela #1 de Nueva York",
                     "ru": "Учитесь на мастера-барбера в школе №1 в Нью-Йорке"}),
    ("oM8KfWfeTWA", {"en": "Our courses are hands-on, fun and engaging",
                     "es": "Nuestros cursos son prácticos, divertidos y dinámicos",
                     "ru": "Наши курсы — это практика, интерес и вовлечённость"}),
    ("dQw4w9WgXcQ", {"en": "Tour our pro New York City barber clinic",
                     "es": "Recorre nuestra clínica profesional en Nueva York",
                     "ru": "Экскурсия по нашей профессиональной клинике в Нью-Йорке"}),
]
YT_HEAD = {"en": ("Watch Us", "See ABI In Action"),
           "es": ("Míranos", "Mira a ABI en Acción"),
           "ru": ("Смотрите", "ABI в действии")}

# ─── 3 Easy Steps section (between About and Techniques) ─────────────
THREE_STEPS_HEAD = {
    "en": ("3 Easy Steps", "Become a Professional Barber in 3 Easy Steps"),
    "es": ("3 Pasos Fáciles", "Conviértete en Barbero Profesional en 3 Pasos Fáciles"),
}
THREE_STEPS = {
    "en": [
        ("Get Started", "Submit your information to start your barbering journey."),
        ("Speak With an Advisor", "An ABI Admissions Advisor will answer your questions, explain the program, and review flexible payment plan options that fit your budget."),
        ("Start Training", "Complete your enrollment and begin building your professional barbering career."),
    ],
    "es": [
        ("Empieza", "Envía tu información para comenzar tu camino en la barbería."),
        ("Habla con un Asesor", "Un Asesor de Admisiones de ABI responderá tus preguntas, explicará el programa y revisará las opciones de planes de pago flexibles que se ajusten a tu presupuesto."),
        ("Comienza a Entrenar", "Completa tu inscripción y empieza a construir tu carrera profesional en la barbería."),
    ],
}

# ─── Career Earnings section (directly below 3 Easy Steps) ───────────
# Content lifted from the main marketing site's `sec--earnings` block so
# the landing pages tell the same career-outcome story.
EARNINGS_HEAD = {
    "en": ("Career Earnings", "Barber Career Earnings"),
    "es": ("Ingresos Profesionales", "Ingresos como Barbero"),
}
EARNINGS_TIERS = {
    "en": [
        ("YEAR 1 · Entry-Level",  "$35,000–$45,000",
         "Starting out in a shop, building your clientele and refining your technique."),
        ("YEARS 2–3 · Established", "$50,000–$70,000",
         "Loyal clientele, faster service and higher earnings as your reputation grows."),
        ("YEAR 3+ · Booth Renter / Shop Owner", "$75,000–$100,000+",
         "Full control of your schedule and earnings — the path to true entrepreneurship."),
    ],
    "es": [
        ("AÑO 1 · Nivel Inicial", "$35,000–$45,000",
         "Empezando en una barbería, construyendo tu clientela y refinando tu técnica."),
        ("AÑOS 2–3 · Establecido", "$50,000–$70,000",
         "Clientela leal, servicio más rápido y mayores ingresos a medida que crece tu reputación."),
        ("AÑO 3+ · Alquiler de Silla / Dueño", "$75,000–$100,000+",
         "Control total de tu horario e ingresos — el camino al verdadero emprendimiento."),
    ],
}
EARNINGS_NOTE = {
    "en": ("Earnings figures are estimates only and are not guaranteed. "
           "Actual income will vary based on individual effort, hours worked, "
           "location and market conditions."),
    "es": ("Los ingresos son estimaciones y no están garantizados. "
           "El ingreso real varía según el esfuerzo individual, las horas trabajadas, "
           "la ubicación y las condiciones del mercado."),
}


# ─── Promo topbar — phone chips per campus ───────────────────────────
# Landing pages: NO haircut number. Manhattan = 2 chips (English + Spanish),
# Bronx = 1 chip. The row auto-fills 1/2 chips (flex:1 1 0) with no empty slot;
# labels sit BELOW each number.
TOPBAR_PHONES_BY_CAMPUS = {
    "manhattan": [
        {"label": "English", "display": "(212) 290-2289", "tel": "+12122902289"},
        {"label": "Spanish", "display": "(212) 290-0278", "tel": "+12122900278"},
    ],
    "bronx": [
        {"label": "Call Us", "display": "(718) 676-0640", "tel": "+17186760640"},
    ],
}

# ─── "Limited Seats" urgency banner shown right under the header ─────
SEATS_BANNER = {
    "en": ("LIMITED SEATS AVAILABLE", "Enrollment Now Open"),
    "es": ("CUPOS LIMITADOS DISPONIBLES", "Inscripciones Abiertas"),
    "ru": ("ОГРАНИЧЕННОЕ КОЛИЧЕСТВО МЕСТ", "Набор открыт"),
}

# ─── hero feature chips (v46) ────────────────────────────────────────
# Moved verbatim out of build.py's inline `if es:` block. NOTE: this wording
# differs slightly from FEATURES above — this is the copy that actually
# renders in the hero, so it is kept exactly as it was.
HERO_FEATURES = {
    "en": [
        ("Licensed by NYSED (BPSS)", "shield"),
        ("Day, evening, weekend schedules", "calendar"),
        ("Hands-on training in our professional Barber clinic", "scissors"),
        ("Financial Assistance — ACCES-VR, VA|Flexible payment plans options", "wallet"),
        ("Career support · Job placement assistance", "briefcase"),
        ("Modern campus in the heart of New York City and Bronx", "store"),
    ],
    "es": [
        ("Licenciada por NYSED (BPSS)", "shield"),
        ("Horarios de día, tarde y fin de semana", "calendar"),
        ("Entrenamiento práctico en nuestra clínica profesional de barbería", "scissors"),
        ("Asistencia Financiera — ACCES-VR, VA|Planes de pago flexibles y opciones", "wallet"),
        ("Apoyo profesional · Asistencia de empleo", "briefcase"),
        ("Campus moderno en el corazón de la ciudad de Nueva York y el Bronx", "store"),
    ],
    "ru": [
        ("Лицензия NYSED (BPSS)", "shield"),
        ("Утренние, дневные и выходные группы", "calendar"),
        ("Практика в нашей профессиональной барбер-клинике", "scissors"),
        ("Финансовая помощь — ACCES-VR, VA|Гибкие планы оплаты", "wallet"),
        ("Поддержка карьеры · Помощь в трудоустройстве", "briefcase"),
        ("Современный кампус в центре Нью-Йорка и в Бронксе", "store"),
    ],
}

# ─── small UI strings (v46) ──────────────────────────────────────────
# These used to be inline `"..." if lang == "es" else "..."` ternaries in
# build.py. Pulled out so a new language is a data change, not a code change.
POPULAR_BADGE = {
    "en": "Most Popular", "es": "Más Popular", "ru": "Самый популярный",
}
CD_LABEL = {
    "en": "Next Starting Date:", "es": "Próxima Fecha de Inicio:",
    "ru": "Ближайшая дата начала:",
}
CD_SUB = {
    "en": "New classes begin the first Monday of each month.",
    "es": "Las clases nuevas comienzan el primer lunes de cada mes.",
    "ru": "Новые группы начинаются в первый понедельник каждого месяца.",
}
CD_UNITS = {
    "en": ("Days", "Hours", "Min", "Sec"),
    "es": ("Días", "Horas", "Min", "Seg"),
    "ru": ("Дней", "Часов", "Мин", "Сек"),
}
FORMCARD_TITLE = {
    "en": "Reserve Your Spot Today", "es": "Reserva Tu Lugar Hoy",
    "ru": "Забронируйте место сегодня",
}
FORMCARD_SUB = {
    "en": "Fill out the form and an Admissions Advisor will contact you.",
    "es": "Completa el formulario y un asesor de admisiones te contactará.",
    "ru": "Заполните форму, и консультант приёмной комиссии свяжется с вами.",
}
QUICK_ACTIONS = {
    "en": "Quick actions", "es": "Acciones rápidas", "ru": "Быстрые действия",
}
TUITION_LABELS = {
    "en": {"down": "down payment", "weekly": "Weekly payments",
           "tuition": "Tuition", "total": "Total cost"},
    "es": {"down": "de pago inicial", "weekly": "Pagos semanales",
           "tuition": "Colegiatura", "total": "Costo total"},
    "ru": {"down": "первоначальный взнос", "weekly": "Еженедельные платежи",
           "tuition": "Стоимость обучения", "total": "Итого"},
}
REVIEWS_LINK = {
    "en": "Read our Google reviews →",
    "es": "Ver nuestras reseñas de Google →",
    "ru": "Читать наши отзывы в Google →",
}
PLAY_LABEL = {"en": "Play", "es": "Reproducir", "ru": "Смотреть"}
PRIVACY_LABEL = {
    "en": "Privacy Policy",
    "es": "Pol&iacute;tica de Privacidad",
    "ru": "Политика конфиденциальности",
}
SKIP_LABEL = {
    "en": "Skip to content", "es": "Saltar al contenido",
    "ru": "Перейти к содержанию",
}
MCTA_LABELS = {
    "en": {"call": "Call Now", "text": "Text Us", "apply": "Apply Now"},
    "es": {"call": "Llamar", "text": "Mensaje", "apply": "Aplicar"},
    "ru": {"call": "Позвонить", "text": "Написать", "apply": "Записаться"},
}

# ─── Contact box (campus-aware) ──────────────────────────────────────
# Manhattan shows 2 numbers (EN + ES). Bronx shows 1 number only.
CONTACT_EMAIL = "admission@abi.edu"
# v3.3 — actual posted hours per the campus signage:
#   Monday–Friday      8:00 AM – 8:00 PM
#   Saturday & Sunday  9:00 AM – 7:00 PM
# Stored as a 2-line list so the contact box renders them on separate lines.
CONTACT_HOURS = {
    "en": [
        "Monday–Friday · 8:00 AM – 8:00 PM",
        "Saturday & Sunday · 9:00 AM – 7:00 PM",
    ],
    "es": [
        "Lunes–Viernes · 8:00 AM – 8:00 PM",
        "Sábado y Domingo · 9:00 AM – 7:00 PM",
    ],
}
CONTACT_HEAD = {
    "en": ("Contact", "Visit Our Campus"),
    "es": ("Contacto", "Visita Nuestro Campus"),
}
CONTACT_LABELS = {
    "en": {
        "addr":   "Address",
        "phone":  "Phone",
        "email":  "Email",
        "hours":  "Hours",
        "directions": "Get directions",
        "en_tag": "English",
        "es_tag": "Español",
        "bronx_tag": "Bronx",
    },
    "es": {
        "addr":   "Dirección",
        "phone":  "Teléfono",
        "email":  "Correo",
        "hours":  "Horario",
        "directions": "Cómo llegar",
        "en_tag": "Inglés",
        "es_tag": "Español",
        "bronx_tag": "Bronx",
    },
}
# Manhattan campus → EN + ES admissions lines
CONTACT_PHONES_MANHATTAN = [
    {"label_key": "en_tag", "display": "(212) 290-2289", "tel": "+12122902289"},
    {"label_key": "es_tag", "display": "(212) 290-0278", "tel": "+12122900278"},
]
# Bronx campus → one admissions number only
CONTACT_PHONES_BRONX = [
    {"label_key": "bronx_tag", "display": "(718) 676-0640", "tel": "+17186760640"},
]
CONTACT_PHONES_BY_CAMPUS = {
    "manhattan": CONTACT_PHONES_MANHATTAN,
    "bronx":     CONTACT_PHONES_BRONX,
}

# ═══════════════════════════════════════════════════════════════════════
# RUSSIAN (v46) — Manhattan landing page at /master-barber-program-russian
# ═══════════════════════════════════════════════════════════════════════
# All Russian copy lives in this one block so it can be handed to a native
# speaker for review in a single pass. Rules applied:
#   • Prices, plan structure, hours and dates are copied verbatim from the
#     English data — only the labels around them are translated.
#   • TCPA consent paragraphs (consent_call / consent_sms / consent) stay in
#     ENGLISH by decision: they are legally operative and an unreviewed
#     translation could weaken consent.
#   • Proper nouns kept as-is: GI Bill®, ACCES-VR, VA, NYSED, BPSS, GED, ATB,
#     street addresses, campus names in addresses.

HERO["ru"] = {
    "kicker_man": "Кампус Манхэттен • Новые группы в первый понедельник каждого месяца",
    "kicker_bx":  "Кампус Бронкс • Новые группы в первый понедельник каждого месяца",
    "h1_a": "500 часов",
    "h1_b": "Барбер-оператор",
    "h1_script": "Начните сегодня.",
    "sub_man": "Получите лицензию барбера всего за <b>4 месяца</b>. Комплексное практическое обучение и полная подготовка к экзамену State Board штата Нью-Йорк в нашем кампусе на Манхэттене.",
    "sub_bx":  "Получите лицензию барбера всего за <b>4 месяца</b>. Комплексное практическое обучение и полная подготовка к экзамену State Board штата Нью-Йорк в нашем кампусе в Бронксе.",
}

FEATURES["ru"] = [
    ("Лицензия NYSED (BPSS)", "shield"),
    ("Утренние, дневные и выходные группы", "calendar"),
    ("Практика в нашей профессиональной барбер-клинике", "scissors"),
    ("Финансовая помощь — ACCES-VR, VA и другие|Гибкие планы оплаты", "wallet"),
    ("Поддержка карьеры · Помощь в трудоустройстве", "briefcase"),
    ("Современный кампус в центре Нью-Йорка", "store"),
]

COUNTDOWN["ru"] = {
    "label": "Ближайшая дата начала:",
    "sub": "Новые группы начинаются в первый понедельник каждого месяца.",
    "cells": ("ДНЕЙ", "ЧАСОВ", "МИН", "СЕК"),
}

STATS["ru"] = [
    ("30+", "Лет работы"),
    ("10,000+", "Выпускников"),
    ("100+", "Отзывов в Google"),
    ("4 мес", "До получения лицензии"),
]

ABOUT_HEAD["ru"] = ("Обзор", "О программе")

ABOUT[("manhattan", "ru")] = [
    "Наша программа «Мастер-барбер» — это комплексный учебный план, который готовит студентов к успешной работе в востребованной индустрии барберинга. За четыре месяца студенты осваивают теорию и практические навыки: санитарию, стерилизацию, историю барберинга, законы и управление барбершопом.",
    "Программа даёт практический опыт работы с самыми разными клиентами, что позволяет оттачивать навыки в реальных условиях. От бритья и массажа лица до фейдов, тейперов, техник clipper over comb и scissor over comb — выпускники уходят с универсальным набором навыков, готовым для любого барбершопа.",
    "Кроме того, мы готовим студентов к экзамену State Board штата Нью-Йорк, чтобы они были полностью готовы получить лицензию мастера-барбера. По окончании каждый студент может обратиться в наш отдел трудоустройства за помощью в поиске работы.",
]

TECHNIQUES["ru"] = [
    "Классические тейперы", "Низкие фейды", "Средние фейды", "Высокие фейды",
    "High-Top фейды", "Помпадур", "Фохок", "Цезарь", "Бритьё головы",
    "Афро", "Флэт-топ", "Оформление бритвой", "Классические стрижки",
    "Стрижка бороды", "Шейп-ап", "Укладка феном", "Ирокез", "Мытьё головы",
    "Техники бритья", "Массаж лица", "Clipper Over Comb", "Scissor Over Comb",
]
TECH_HEAD["ru"] = ("Техники", "Навыки и техники, которыми вы овладеете")

MODULES["ru"] = [
    ("Теория и наука", ["Санитария и стерилизация", "История барберинга",
                        "Законы и правила штата Нью-Йорк", "Управление барбершопом",
                        "Профессиональная этика"]),
    ("Техники стрижки", ["Фейды (низкий, средний, высокий)", "Тейперы и классические стрижки",
                         "Clipper Over Comb", "Scissor Over Comb", "Флэт-топ и High-Top фейды"]),
    ("Укладка и финиш", ["Оформление бритвой и шейп-ап", "Укладка феном и помпадур",
                         "Афро и ирокез", "Стрижка и моделирование бороды",
                         "Мытьё головы и кондиционирование"]),
    ("Бритьё и уход за кожей", ["Бритьё опасной бритвой", "Техники массажа лица",
                                "Уход с горячим полотенцем", "Анализ кожи и кожи головы",
                                "Безопасность и гигиена"]),
    ("Бизнес и карьера", ["Навыки консультации клиента", "Работа барбершопа",
                          "Наработка клиентской базы", "Подготовка к трудоустройству",
                          "Подготовка к экзамену State Board"]),
]
MODULES_HEAD["ru"] = ("Учебный план", "Модули курса")

TUITION_HEAD["ru"] = ("Стоимость обучения", "Гибкие планы оплаты")
TUITION_NOTE["ru"] = ("Каждый план включает подготовку к экзамену State Board штата Нью-Йорк, "
                      "практическое обучение и помощь в трудоустройстве. Дополнительные расходы: "
                      "книги, инструменты и материалы можно приобрести в ABI или у других поставщиков. "
                      "Доступна финансовая помощь ACCES-VR. Принимаются Post-9/11 GI Bill® и льготы VA.")

# Prices, schedules and plan maths are identical to the English data.
TUITION["ru"] = [
    {"name": "План A — Утро", "sched": "Пн–Пт · 8:00 – 14:00",
     "hours": "30 часов в неделю · 17 недель (~4 месяца)", "feature": False,
     "down": "$500", "weekly": "17 × $300", "tuition": "$5,250", "total": "$5,600",
     "calc": "$500 + 17 × $300 = $5,600", "cta": "Записаться на утро"},
    {"name": "План B — День", "sched": "Пн–Пт · 14:00 – 20:00",
     "hours": "30 часов в неделю · 17 недель (~4 месяца)", "feature": True,
     "down": "$200", "weekly": "17 × $200", "tuition": "$3,600", "total": "$3,600",
     "calc": "$200 + 17 × $200 = $3,600", "cta": "Записаться на день"},
    {"name": "План C — Выходные", "sched": "Сб и Вс · 9:00 – 19:00",
     "hours": "18 часов в неделю · 27 недель (~6–7 месяцев)", "feature": False,
     "down": "$200", "weekly": "27 × $160", "tuition": "$4,600", "total": "$4,600",
     "calc": "$200 + 27 × $160 = $4,520 + финальный платёж = $4,600",
     "cta": "Записаться на выходные"},
]

REQUIREMENTS["ru"] = [
    "Карта социального страхования (SSN) или Tax ID",
    "Аттестат о среднем образовании (HSD) или GED — либо сдача вступительного экзамена ATB в ABI",
    "Возраст не менее 17 лет",
    "Подтверждение адреса проживания",
    "Действительное удостоверение с фото или водительские права",
    "Первоначальный взнос от $200",
]
REQ_HEAD["ru"] = ("Приём", "Требования для поступления")

SHOWCASE_HEAD["ru"] = ("Внутри ABI", "Реальная жизнь в ABI")
SHOWCASE_LEAD["ru"] = "Настоящие кадры из наших классов и барбер-клиники — практика каждый день."

STUDENT_VOICES["ru"] = {
    "eyebrow": "Голоса студентов",
    "title": "Настоящие голоса, настоящие стрижки.",
    "sub": "Нажмите на плеер, чтобы услышать, как студент ABI делится своим опытом — прямо, без сценария и без прикрас.",
}

REVIEWS_HEAD["ru"] = ("Истории студентов", "Что говорят наши студенты")
REVIEWS_LEAD["ru"] = "Настоящие отзывы студентов American Barber Institute."

FAQ_HEAD["ru"] = ("Вопросы и ответы", "Ответы на вопросы о школе барберов")
GALLERY_HEAD["ru"] = ("Галерея", "Жизнь в ABI")

THREE_STEPS_HEAD["ru"] = ("3 простых шага", "Станьте профессиональным барбером за 3 простых шага")
THREE_STEPS["ru"] = [
    ("Начните", "Оставьте свои данные, чтобы начать путь в барберинге."),
    ("Поговорите с консультантом",
     "Консультант приёмной комиссии ABI ответит на ваши вопросы, расскажет о программе и подберёт гибкий план оплаты под ваш бюджет."),
    ("Начните обучение", "Завершите зачисление и начните строить профессиональную карьеру барбера."),
]

EARNINGS_HEAD["ru"] = ("Доход в профессии", "Заработок барбера")
EARNINGS_TIERS["ru"] = [
    ("ГОД 1 · Начальный уровень", "$35,000–$45,000",
     "Старт в барбершопе: нарабатываете клиентскую базу и оттачиваете технику."),
    ("ГОДЫ 2–3 · Опытный мастер", "$50,000–$70,000",
     "Постоянные клиенты, более быстрая работа и рост дохода вместе с репутацией."),
    ("ГОД 3+ · Аренда кресла / владелец", "$75,000–$100,000+",
     "Полный контроль над графиком и доходом — путь к собственному делу."),
]
EARNINGS_NOTE["ru"] = ("Указанные суммы являются приблизительными оценками и не гарантируются. "
                       "Фактический доход зависит от личных усилий, количества часов работы, "
                       "местоположения и ситуации на рынке.")

CONTACT_HEAD["ru"] = ("Контакты", "Посетите наш кампус")
CONTACT_HOURS["ru"] = [
    "Понедельник–Пятница · 8:00 – 20:00",
    "Суббота и Воскресенье · 9:00 – 19:00",
]
CONTACT_LABELS["ru"] = {
    "addr": "Адрес", "phone": "Телефон", "email": "Эл. почта", "hours": "Часы работы",
    "directions": "Проложить маршрут",
    "en_tag": "English", "es_tag": "Español", "bronx_tag": "Bronx",
}

LOC_OPTS_BY_CAMPUS[("manhattan", "ru")] = [
    "Выберите предпочитаемый кампус",
    "Кампус Манхэттен — 48 West 39th Street",
    "Кампус Бронкс — 121 Westchester Square",
    "Любой / без предпочтений",
]

FOOTER["ru"] = {
    "h": "American Barber Institute",
    "sub": "Единственная в Нью-Йорке школа, посвящённая только барберингу — меняем жизни более 30 лет.",
    "fine": "© American Barber Institute. Аккредитовано NYSED · Лицензия BPSS · С 1996 года. "
            "*$200 первоначальный взнос и $160 в неделю относятся к Плану C (выходные).",
}

# Reviews are real, named Google reviewers. Spanish already translates their
# wording, so Russian follows that established precedent.
_REVIEWS_RU_MANHATTAN = [
    {"name": "Jerrick Matthews", "role": "Студент — Манхэттен",
     "q": "Уровень знаний и подготовки great! King David — один из лучших преподавателей, он научит вас всему, что нужно знать о барберинге."},
    {"name": "Carlos Perez", "role": "Студент — Манхэттен",
     "q": "Я здесь учусь, и King David — просто супер! У него 30 лет опыта, он даёт отличные техники и постоянно оттачивает наши базовые навыки."},
    {"name": "Zyee Fin", "role": "Студент — Манхэттен",
     "q": "Сейчас я здесь учусь и доволен прогрессом — многому учусь у преподавателей и однокурсников. Только позитив и желание учиться дальше."},
    {"name": "Andre Thompson", "role": "Выпускник — Манхэттен",
     "q": "Настоящая практика с первого дня, и преподавателям правда не всё равно. Помощь с трудоустройством после выпуска действительно помогла мне начать карьеру."},
]
REVIEWS_BY_CAMPUS["manhattan"]["ru"] = _REVIEWS_RU_MANHATTAN

FORM["ru"] = {
    "h": "Забронируйте место сегодня",
    "sub": "Заполните форму, и консультант приёмной комиссии свяжется с вами.",
    "first": "Имя", "last": "Фамилия", "phone": "Телефон", "email": "Эл. почта",
    "loc_label": "В каком кампусе вы хотели бы учиться?",
    "fmt_label": "Какой формат обучения вы предпочитаете?",
    "fmt_opts": ["Выберите вариант", "Утро · Пн–Пт 8:00–14:00",
                 "День · Пн–Пт 14:00–20:00", "Выходные · Сб–Вс 9:00–19:00"],
    "lang_label": "На каком языке вам удобнее общаться?",
    "lang_opts": ["Выберите язык", "English", "Spanish / Español", "Russian / Русский", "Другой"],
    "msg_label": "Сообщение для ABI",
    "msg_ph": "Расскажите всё, что нам полезно знать — вопросы, накладки по расписанию, потребность в финансовой помощи и т. д.",
    "submit": "Отправить",
    "trust": "Бесплатно • Без обязательств • Ответим в течение 24 часов",
    # NOTE: TCPA consent copy is intentionally left in English — see header.
    "consent_call": FORM["en"]["consent_call"],
    "consent_sms": FORM["en"]["consent_sms"],
    "consent": FORM["en"]["consent"],
    "thanks": "Спасибо! Представитель приёмной комиссии ABI позвонит вам в течение 24 часов.",
}

PAGES.append({
    "id": "mhtn-ru", "lang": "ru", "campus": MANHATTAN,
    "path": "master-barber-program-russian",
    "alt":  "500-hours-master-barber-program-landing-page",
    "alts": {"en": "500-hours-master-barber-program-landing-page",
             "es": "500-hours-master-barber-program-landing-page/spanish",
             "ru": "master-barber-program-russian"},
    # No Russian-language admissions line exists yet, so this uses the
    # Manhattan English number.
    "phone": ("EN", "(212) 290-2289", "+12122902289"),
    "theme_class": "lf-page--mhtn-ru",
    "title": "Программа «Мастер-барбер» 500 часов — Манхэттен | American Barber Institute",
    "desc":  "Получите лицензию барбера всего за 4 месяца в кампусе ABI на Манхэттене (48 West 39th Street). Практическое обучение, полная подготовка к экзамену State Board штата Нью-Йорк, еженедельные планы оплаты и помощь в трудоустройстве.",
    "promo_strip": "Начните карьеру барбера сегодня всего за $200 первоначальный взнос и $160 в неделю",
    "promo_bold": "$200 первоначальный взнос и $160 в неделю",
    "cta_primary": "Забронируйте место сегодня",
})
