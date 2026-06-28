# -*- coding: utf-8 -*-
"""ABI Landing Funnels — content data (EXACT abi.edu replica).

Every string here is scraped verbatim from the live American Barber Institute
landing pages on www.abi.edu:
  /500-hours-master-barber-program-landing-page/         (Manhattan EN)
  /500-hours-master-barber-program-landing-page/spanish/ (Manhattan ES)
  /master-barber-program-bronx/                          (Bronx EN)
  /master-barber-program-bronx/spanish/                  (Bronx ES)
plus /contact/. Content is king — nothing invented, point to point.
"""

# ─── campuses ────────────────────────────────────────────────────────
MANHATTAN = {
    "slug": "manhattan", "name_en": "Manhattan Campus", "name_es": "Sede de Manhattan",
    "addr_en": "48 West 39th Street, New York, NY 10018",
    "addr_es": "48 West 39th Street, Nueva York, NY 10018",
    "latlng": (40.7522, -73.9849),
}
BRONX = {
    "slug": "bronx", "name_en": "Bronx Campus", "name_es": "Sede del Bronx",
    "addr_en": "121 Westchester Square, Bronx, NY 10461",
    "addr_es": "121 Westchester Square, Bronx, NY 10461",
    "latlng": (40.8401, -73.8421),
}

# ─── page configs ────────────────────────────────────────────────────
PAGES = [
    {"id": "mhtn-en", "lang": "en", "campus": MANHATTAN, "theme_class": "lf-page--mhtn-en",
     "path": "500-hours-master-barber-program-landing-page",
     "alt":  "500-hours-master-barber-program-landing-page/spanish",
     "phone": ("EN", "(212) 290-2289", "+12122902289"),
     "phone2": ("ES", "(212) 290-0278", "+12122900278"),
     "title": "500-Hour Master Barber Program — Manhattan | American Barber Institute",
     "desc":  "Become a Master Barber in as little as 4 months at ABI's Manhattan campus (48 West 39th Street). 500-hour NY State program, weekly payments as low as $150, hands-on training and job placement."},
    {"id": "mhtn-es", "lang": "es", "campus": MANHATTAN, "theme_class": "lf-page--mhtn-es",
     "path": "500-hours-master-barber-program-landing-page/spanish",
     "alt":  "500-hours-master-barber-program-landing-page",
     "phone": ("ES", "(212) 290-0278", "+12122900278"),
     "phone2": ("EN", "(212) 290-2289", "+12122902289"),
     "title": "Programa Maestro Barbero de 500 Horas — Manhattan | American Barber Institute",
     "desc":  "Conviértete en Maestro Barbero en nuestra sede de Manhattan (48 West 39th Street). Programa de 500 horas del Estado de NY, pagos semanales desde $150, entrenamiento práctico y colocación laboral."},
    {"id": "brnx-en", "lang": "en", "campus": BRONX, "theme_class": "lf-page--brnx-en",
     "path": "master-barber-program-bronx",
     "alt":  "master-barber-program-bronx/spanish",
     "phone": ("Bronx", "(718) 676-0640", "+17186760640"),
     "phone2": None,
     "title": "Master Barber Program — Bronx | American Barber Institute",
     "desc":  "Become a Master Barber at ABI's Bronx campus (121 Westchester Square). 500-hour NY State program, weekly payments as low as $150, hands-on training and job placement."},
    {"id": "brnx-es", "lang": "es", "campus": BRONX, "theme_class": "lf-page--brnx-es",
     "path": "master-barber-program-bronx/spanish",
     "alt":  "master-barber-program-bronx",
     "phone": ("Bronx", "(718) 676-0640", "+17186760640"),
     "phone2": None,
     "title": "Programa Maestro Barbero — Bronx | American Barber Institute",
     "desc":  "Conviértete en Maestro Barbero en la sede del Bronx de ABI (121 Westchester Square). Programa de 500 horas del Estado de NY, pagos semanales desde $150, entrenamiento práctico y colocación laboral."},
]

# ─── topbar (verbatim) ───────────────────────────────────────────────
TOPBAR = {
    "en": "Schedule your tour today!",
    "es": "¡Agenda tu recorrido hoy!",
}

# ─── HERO (verbatim) ─────────────────────────────────────────────────
HERO = {
    "en": {
        "program": "500 Hour Barber Training Program",
        "h1": "AI Proof Your Career",
        "tagline": "As low as $150 Weekly Payments for Part-Time Schedule!",
        "cd_label": "Next Starting Date",
        "cd_sub": "New Classes Begin On The First Monday Of Each Month.",
        "cells": ("Days", "Hours", "Minutes", "Seconds"),
    },
    "es": {
        "program": "Programa de Capacitación de Barbero de 500 Horas",
        "h1": "Prepara Tu Carrera a Prueba de la IA",
        "tagline": "¡Pagos semanales desde $150 para el horario de medio tiempo!",
        "cd_label": "Próxima fecha de inicio",
        "cd_sub": "Las nuevas clases comienzan el primer lunes de cada mes.",
        "cells": ("Días", "Horas", "Minutos", "Segundos"),
    },
}

# ─── "Get Trained With ABI" form block (verbatim) ────────────────────
FORM = {
    "en": {
        "eyebrow": "Get Trained With ABI",
        "h": "Contact us, We will be happy to guide you!",
        "name": "Name", "email": "Email", "phone": "Phone", "message": "Message",
        "campus_label": "Preferred campus",
        "campus_opts": ["Select a campus", "Manhattan — 48 West 39th Street", "Bronx — 121 Westchester Square"],
        "schedule_label": "Preferred schedule",
        "schedule_opts": ["Select a schedule",
                          "Plan A — Full-Time Morning (Mon–Fri 8AM–2PM)",
                          "Plan B — Full-Time Afternoon (Mon–Fri 2PM–8PM)",
                          "Plan C — Part-Time Weekend (Sat–Sun 9AM–7PM)"],
        "submit": "Get More Info Today",
        "consent": "By submitting, you consent that ABI can contact you via phone, SMS or email about your enrollment.",
        "thanks": "Thank you! An ABI admissions agent will contact you shortly.",
    },
    "es": {
        "eyebrow": "Capacítese con ABI",
        "h": "Contáctanos, ¡estaremos encantados de orientarte!",
        "name": "Nombre", "email": "Correo electrónico", "phone": "Teléfono", "message": "Mensaje",
        "campus_label": "Sede preferida",
        "campus_opts": ["Selecciona una sede", "Manhattan — 48 West 39th Street", "Bronx — 121 Westchester Square"],
        "schedule_label": "Horario preferido",
        "schedule_opts": ["Selecciona un horario",
                          "Plan A — Mañana tiempo completo (Lun–Vie 8AM–2PM)",
                          "Plan B — Tarde tiempo completo (Lun–Vie 2PM–8PM)",
                          "Plan C — Fin de semana medio tiempo (Sáb–Dom 9AM–7PM)"],
        "submit": "Obtén Más Información Hoy",
        "consent": "Al enviar, aceptas que ABI puede contactarte por teléfono, SMS o correo sobre tu inscripción.",
        "thanks": "¡Gracias! Un agente de admisiones de ABI te contactará pronto.",
    },
}

# ─── intro band ("You Only Need 500 Hours...") verbatim ──────────────
INTRO = {
    "en": {
        "h": "You Only Need 500 Hours To Become A Master Barber",
        "p": "If you give us a call, we will assist you with your inquiry. When you come to A.B.I., the first thing you'll find is that our staff is incredibly friendly, and loves sharing their knowledge on a future generation of barbers. Please also feel free to ask them questions about their trade, their philosophy, and what motivates them. If you're interested in barbering classes at A.B.I. please continue to browse through our website, or give us a call. We would love to hear from you today!",
    },
    "es": {
        "h": "Sólo necesitas 500 horas para convertirte en un Maestro Barbero",
        "p": "Si nos llamas, te ayudaremos con tu consulta. Cuando vienes a A.B.I., lo primero que encontrarás es que nuestro personal es increíblemente amigable y le encanta compartir sus conocimientos con una futura generación de barberos. No dudes en hacerles preguntas sobre su oficio, su filosofía y qué los motiva. Si estás interesado en clases de barbería en A.B.I., continúa navegando por nuestro sitio web o llámanos. ¡Nos encantaría saber de ti hoy!",
    },
}

# ─── "500 Hour Master Barber Program" flexible-schedule band ─────────
PROGRAM = {
    "en": {
        "h": "500 Hour Master Barber Program",
        "p": "At ABI, we understand that every student has unique responsibilities and time commitments. To ensure accessibility and flexibility, ABI offers multiple schedule plans (Plans A–F) for students to choose from. Whether you are employed full-time or part-time, managing childcare, or balancing other personal obligations, you can select the schedule that best fits your needs—subject to ABI availability. This flexibility allows students to complete the 500-hour program in as little as 3 months or up to 5 months, depending on the plan selected.",
        "learn": "Learn a wide range of haircuts. We provide our students with all the skills and techniques that will set them apart in their professional careers. Students get to work on a tremendous amount of clients and are taught the art of shaving and hair styling, from:",
        "haircuts": ["classic tapers", "fohawks", "pompadours", "bald heads", "caesars",
                     "low fades", "mid fades", "high fades", "high-top fades", "afro",
                     "flat tops", "razor lineups", "shampoos", "classical haircuts",
                     "beard trims", "shape ups", "blowouts", "mohawks", "and more"],
    },
    "es": {
        "h": "Programa de Maestro Barbero de 500 Horas",
        "p": "En ABI, entendemos que cada estudiante tiene responsabilidades y compromisos de tiempo únicos. Para garantizar accesibilidad y flexibilidad, ABI ofrece múltiples planes de horario (Planes A–F) para que los estudiantes elijan. Ya sea que trabajes a tiempo completo o parcial, cuides a tus hijos o tengas otras obligaciones personales, puedes seleccionar el horario que mejor se adapte a tus necesidades — sujeto a la disponibilidad de ABI. Esta flexibilidad permite a los estudiantes completar el programa de 500 horas en tan solo 3 meses o hasta 5 meses, según el plan seleccionado.",
        "learn": "Aprende una amplia gama de cortes de pelo. Proporcionamos a nuestros estudiantes todas las habilidades y técnicas que los diferenciarán en sus carreras profesionales. Los estudiantes trabajan con una gran cantidad de clientes y aprenden el arte del afeitado y el peinado, desde:",
        "haircuts": ["tapers clásicos", "fohawks", "pompadours", "cabezas rapadas", "caesars",
                     "low fades", "mid fades", "high fades", "high-top fades", "afro",
                     "flat tops", "líneas con navaja", "lavados", "cortes clásicos",
                     "recortes de barba", "shape ups", "blowouts", "mohawks", "y más"],
    },
}

# ─── ABOUT (verbatim, 5 paragraphs) ──────────────────────────────────
ABOUT = {
    "en": {
        "h": "About American Barber Institute",
        "paras": [
            "Our Master Barber Program offers a comprehensive curriculum designed to prepare students for success in the thriving barbering industry. Over four months, students immerse themselves in theory and practical skills, covering sanitation, sterilization, barber history, laws, and shop management.",
            "Our program provides hands-on experience with access to a diverse clientele, allowing students to refine skills under real-world conditions. From mastering shaving and facial massage to perfecting techniques like fades, tapers, clipper over comb, scissor over comb, and much more, graduates leave with a versatile skill set ready for employment in any barber shop.",
            "Additionally, we prepare students for the New York State Board Exam, ensuring they are fully equipped to obtain their Master Barber license and launch their careers.",
            "At American Barber Institute, we're dedicated to grooming education and professional development, aiming to equip aspiring barbers with top-tier training for success. Our programs prepare students to cultivate professionalism and integrity within the barbering community. With a focus on technical skills and business acumen, we empower our students to thrive in the dynamic Barber Industry and launch their careers.",
            "Upon completion of the program, each student will have the opportunity to meet with our job placement office. Our dedicated team assists students in exploring employment opportunities and helps them navigate the next steps in their career journey. Whether students aspire to work in a traditional barbershop, pursue freelance opportunities, or even open their own businesses, we provide the support and resources needed to turn their aspirations into reality.",
            "Join us in shaping the future of grooming professionals, one skilled barber at a time, in a recession-proof industry.",
        ],
    },
    "es": {
        "h": "Acerca del American Barber Institute",
        "paras": [
            "Nuestro programa Master Barber ofrece un plan de estudios integral diseñado para preparar a los estudiantes para el éxito en la próspera industria de la barbería. A lo largo del programa, los estudiantes se sumergen en la teoría y las habilidades prácticas, que abarcan saneamiento, esterilización, historia de la barbería, leyes y gestión de la barbería.",
            "Nuestro programa brinda experiencia práctica con acceso a una clientela diversa, lo que permite a los estudiantes perfeccionar sus habilidades en condiciones del mundo real. Desde dominar el afeitado y el masaje facial hasta perfeccionar técnicas como fades, tapers, maquinilla sobre peine, tijera sobre peine y mucho más, los graduados salen con un conjunto de habilidades versátiles listas para trabajar en cualquier barbería.",
            "Además, preparamos a los estudiantes para el examen de la Junta del Estado de Nueva York, asegurándonos de que estén completamente equipados para obtener su licencia de Master Barber e iniciar sus carreras.",
            "En American Barber Institute, nos dedicamos a la educación en cuidado personal y al desarrollo profesional, con el objetivo de equipar a los aspirantes a barberos con una capacitación de primer nivel para lograr el éxito. Nuestros programas preparan a los estudiantes para cultivar el profesionalismo y la integridad dentro de la comunidad de barberos. Con un enfoque en las habilidades técnicas y la visión para los negocios, capacitamos a nuestros estudiantes para que prosperen en la dinámica industria de la barbería y lancen sus carreras.",
            "Al finalizar el programa, cada estudiante tendrá la oportunidad de reunirse con nuestra oficina de colocación laboral. Nuestro equipo dedicado ayuda a los estudiantes a explorar oportunidades de empleo y los ayuda a navegar los siguientes pasos en su trayectoria profesional. Ya sea que los estudiantes aspiren a trabajar en una barbería tradicional, busquen oportunidades como autónomos o incluso abran sus propios negocios, brindamos el apoyo y los recursos necesarios para convertir sus aspiraciones en realidad.",
            "Únase a nosotros para dar forma al futuro de los profesionales del cuidado personal, un barbero capacitado a la vez, en una industria a prueba de recesiones.",
        ],
    },
}

# ─── Entrance Requirements (verbatim: title + description) ───────────
REQUIREMENTS = {
    "en": {
        "h": "Entrance Requirements",
        "items": [
            ("Social Security Card", "You should provide a Social Security Card."),
            ("High School Diploma", "High School Diploma (HSD) or General Equivalency Diploma (GED). If you don't possess either one, you can take the (ATB) Entrance exam in our Barber Institute."),
            ("Admission Age", "You must be at least 17 years of age."),
            ("Address", "You should provide proof of your residential address."),
            ("Photo Identification", "You should provide valid photo identification or a valid Driver's License."),
            ("Down Payment", "$500 Down Payment."),
        ],
    },
    "es": {
        "h": "Requisitos de Ingreso",
        "items": [
            ("Tarjeta de Seguro Social", "Debes proporcionar una Tarjeta de Seguro Social."),
            ("Diploma de Secundaria", "Diploma de Escuela Secundaria (HSD) o Diploma de Equivalencia General (GED). Si no posees ninguno, puedes tomar el examen de admisión (ATB) en nuestro Instituto de Barbería."),
            ("Edad de Admisión", "Debes tener al menos 17 años de edad."),
            ("Domicilio", "Debes proporcionar comprobante de tu domicilio residencial."),
            ("Identificación con Foto", "Debes proporcionar una identificación con foto válida o una Licencia de Conducir válida."),
            ("Pago Inicial", "$500 de pago inicial."),
        ],
    },
}

# ─── Payment Plans (verbatim financing) ──────────────────────────────
PLANS_HEAD = {
    "en": ("Payment Plans Available", "Students may finish training in as little as 4 months."),
    "es": ("Planes de Pago Disponibles", "Los estudiantes pueden terminar la capacitación en tan solo 4 meses."),
}
PLANS = {
    "en": [
        {"name": "Plan A — Full-Time Morning", "feature": False,
         "sched": "Monday – Friday: 8:00 AM – 2:00 PM (30 hrs/week)", "cost": "$5,600",
         "terms": ["Upon registration, students pay a $500 tuition down payment (includes $100 registration fee).",
                   "The remaining balance is divided into 17 weekly payments of $300.",
                   "Students are responsible for purchasing barbering tools, books, and supplies.",
                   "A list of acceptable tools will be provided upon registration."]},
        {"name": "Plan B — Full-Time Afternoon", "feature": True,
         "sched": "Monday – Friday: 2:00 PM – 8:00 PM (30 hrs/week)", "cost": "$4,600",
         "terms": ["Upon registration, students pay a $500 tuition down payment (includes $100 registration fee).",
                   "The remaining balance is divided into 16 weekly payments of $250.",
                   "Students are responsible for purchasing barbering tools, books, and supplies.",
                   "A list of acceptable tools will be provided upon registration."]},
        {"name": "Plan C — Part-Time Intensive", "feature": False,
         "sched": "Saturday – Sunday: 9:00 AM – 7:00 PM (18 hrs/week) · 27 weeks · 7 months", "cost": "$4,600",
         "terms": ["Registration Fee: $550 down payment.",
                   "Remaining balance $4,050 (27 weekly payments of $150).",
                   "Students are responsible for purchasing barbering tools, books, and supplies.",
                   "A list of acceptable tools will be provided upon registration."]},
    ],
    "es": [
        {"name": "Plan A — Mañana Tiempo Completo", "feature": False,
         "sched": "Lunes – Viernes: 8:00 AM – 2:00 PM (30 hrs/semana)", "cost": "$5,600",
         "terms": ["Al registrarse, los estudiantes pagan $500 de pago inicial (incluye $100 de inscripción).",
                   "El saldo restante se divide en 17 pagos semanales de $300.",
                   "Los estudiantes son responsables de comprar herramientas, libros y suministros de barbería.",
                   "Se proporcionará una lista de herramientas aceptables al registrarse."]},
        {"name": "Plan B — Tarde Tiempo Completo", "feature": True,
         "sched": "Lunes – Viernes: 2:00 PM – 8:00 PM (30 hrs/semana)", "cost": "$4,600",
         "terms": ["Al registrarse, los estudiantes pagan $500 de pago inicial (incluye $100 de inscripción).",
                   "El saldo restante se divide en 16 pagos semanales de $250.",
                   "Los estudiantes son responsables de comprar herramientas, libros y suministros de barbería.",
                   "Se proporcionará una lista de herramientas aceptables al registrarse."]},
        {"name": "Plan C — Medio Tiempo Intensivo", "feature": False,
         "sched": "Sábado – Domingo: 9:00 AM – 7:00 PM (18 hrs/semana) · 27 semanas · 7 meses", "cost": "$4,600",
         "terms": ["Cuota de inscripción: $550 de pago inicial.",
                   "Saldo restante $4,050 (27 pagos semanales de $150).",
                   "Los estudiantes son responsables de comprar herramientas, libros y suministros de barbería.",
                   "Se proporcionará una lista de herramientas aceptables al registrarse."]},
    ],
}
PLANS_EXTRA = {
    "en": {
        "fees_title": "Additional Fees",
        "fees": "Books / Tools / Supplies (can be purchased from ABI or other suppliers).",
        "accessvr_title": "Access-VR financial assistance option",
        "accessvr": "The Access-VR program is a key player in supporting individuals with disabilities in obtaining and maintaining employment. This means that if you qualify, you could receive financial assistance to pursue your passion for barbering.",
        "gibill_title": "Veterans GI Bill®* financial assistance option",
        "gibill": "If you are a veteran, the GI Bill®* opens doors to education and vocational training. At American Barber Institute, we honor and support those who have served our country by offering assistance through the Veterans GI Bill®*, making barbering education accessible to our nation's heroes.",
    },
    "es": {
        "fees_title": "Tarifas Adicionales",
        "fees": "Libros / Herramientas / Suministros (se pueden comprar en ABI u otros proveedores).",
        "accessvr_title": "Opción de asistencia financiera Access-VR",
        "accessvr": "El programa Access-VR es clave para apoyar a las personas con discapacidades en la obtención y el mantenimiento del empleo. Esto significa que, si calificas, podrías recibir asistencia financiera para perseguir tu pasión por la barbería.",
        "gibill_title": "Opción de asistencia financiera Veterans GI Bill®*",
        "gibill": "Si eres veterano, el GI Bill®* abre puertas a la educación y la formación profesional. En American Barber Institute, honramos y apoyamos a quienes han servido a nuestro país ofreciendo asistencia a través del Veterans GI Bill®*, haciendo la educación en barbería accesible para los héroes de nuestra nación.",
    },
}

# ─── Gallery (real ABI student photos) ───────────────────────────────
GALLERY = ["abi/abi-students-006.jpg", "abi/abi-students-007.jpg", "abi/abi-students-008.jpg",
           "abi/abi-students-009.jpg", "abi/abi-students-010.jpg", "abi/abi-students-011.jpg"]
GALLERY_HEAD = {"en": "Our Gallery", "es": "Nuestra Galería"}

# ─── Reviews (verbatim Google reviews — full text) ───────────────────
REVIEWS_HEAD = {
    "en": ("They found a new life path.", "Check out our Google Reviews"),
    "es": ("Encontraron un nuevo camino de vida.", "Mira nuestras Reseñas de Google"),
}
# The site shows the same real reviews on every campus/language (EN text).
REVIEWS = [
    {"name": "Vincybie Lee",
     "q": "Wished to have a trim before we head back to HK. Passed by a barber school for only 3 dollars for a regular haircut. Hehe.. And it's not bad actually. Good that we could help out student trainees practice and also reach their 500 hours required for graduating."},
    {"name": "Jerrick Matthews",
     "q": "I am currently a student at the American Barber Institute! The level of knowledge and training is superb! One of the best teachers around by the name of King David will show you everything there is to know about barbering! Bar none to the standards of Professional Barbering! There is a 100% commitment from this school to promote positive contributions to the community."},
    {"name": "Carlos Perez",
     "q": "I'm a student here and have King David as my instructor and he has been awesome!! He has 30 years of experience and gives us great techniques and also been polishing up on basic skills!!! If you are interested in barbering please come ask for King David!!!"},
    {"name": "Tina Banee",
     "q": "Donovan gave me a great hair cut. He did exactly what I asked him to do. Well worth $3 plus a $7 tip. $10 for a haircut!!! I would give 5 stars but the place was too small for the amount of people inside."},
    {"name": "Zyee Fin",
     "q": "I'm currently enrolled here and I'm happy with the progress from learning from the teachers and classmates. Shoutout my classmates — nothing but positivity and eager to learn more in this field."},
]

# ─── Our Videos (real YouTube IDs in page order) ─────────────────────
VIDEOS_HEAD = {"en": "Our Videos", "es": "Nuestros Videos"}
YT_IDS = ["5tTUkkVqOOE", "IIRSqA7WTww", "TFpNNqsc_EA", "iU0fUj3a8uw", "rkicJ7RdrYg"]

# ─── "Get More Info Today" closing band (verbatim) ───────────────────
CLOSING = {
    "en": {
        "h": "Get More Info Today",
        "p": "When you come for a tour, the first thing you will find is that our staff is incredibly friendly and here to help you. Ask our staff about their love for teaching a new generation of barbers and they will tell you it is their passion for imparting their knowledge. Reserve your seat today — new classes begin the first Monday of each month.",
    },
    "es": {
        "h": "Obtén Más Información Hoy",
        "p": "Cuando vengas a un recorrido, lo primero que encontrarás es que nuestro personal es increíblemente amigable y está aquí para ayudarte. Pregúntales sobre su amor por enseñar a una nueva generación de barberos y te dirán que es su pasión por transmitir sus conocimientos. Reserva tu lugar hoy — las nuevas clases comienzan el primer lunes de cada mes.",
    },
}

# ─── footer ──────────────────────────────────────────────────────────
FOOTER = {
    "en": {"h": "American Barber Institute",
           "sub": "New York's only dedicated barber school — changing lives for over 30 years.",
           "fine": "© American Barber Institute. Licensed by NYSED (BPSS). *GI Bill® is a registered trademark of the U.S. Department of Veterans Affairs. *$150/week refers to the Plan C weekly payment."},
    "es": {"h": "American Barber Institute",
           "sub": "La única escuela de barbería dedicada de Nueva York — cambiando vidas por más de 30 años.",
           "fine": "© American Barber Institute. Licenciada por NYSED (BPSS). *GI Bill® es una marca registrada del Departamento de Asuntos de Veteranos de los EE. UU. *$150/semana se refiere al pago semanal del Plan C."},
}
