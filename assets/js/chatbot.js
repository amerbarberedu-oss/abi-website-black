/* American Barber Institute — AI admissions assistant (v13, "real AI" upgrade).
 * Free, no-key model (Pollinations openai-fast / GPT-OSS 20B) with:
 *   - Massive knowledge base (80+ facts across every part of the school)
 *   - Per-message language detection (EN↔ES mid-conversation switching)
 *   - Streaming responses so replies feel alive
 *   - Local keyword fallback if the AI endpoint is unreachable
 */
(function () {
  "use strict";
  if (window.__abiBotLoaded) return;
  window.__abiBotLoaded = true;

  // ── Page-language detection (initial UI language only; per-message
  //    detection below overrides for actual answers) ────────────────────────
  var pageLangIsES = (document.documentElement.lang || "en").slice(0, 2) === "es"
                  || /(^|\/)(es|spanish)(\/|$)/i.test(location.pathname);

  // ── ABI KNOWLEDGE BASE — long-form, comprehensive, single source of truth
  //    Kept in sync with the website; edit here to teach the bot new things.
  var FACTS = [
    // Identity + credentials
    "American Barber Institute (ABI) is New York City's dedicated barber school, established in 1996. 30+ years of experience, 10,000+ graduates, aggregate rating 4.6/5 across 100+ Google reviews.",
    "ABI is licensed by the New York State Department of Education (NYSED / Bureau of Proprietary School Supervision, BPSS). It is a state-approved barber training program.",
    "The Master Barber Program at ABI is designed to prepare students to sit and pass the New York State Master Barber license (Board Exam).",
    "Both campuses are bilingual — English and Spanish instruction is offered every day. Roughly half of instruction happens in Spanish across the two campuses combined.",

    // Programs
    "Primary program: the 500-Hour Master Barber Program, offered at both Manhattan and Bronx campuses. New cohorts start the first Monday of every month.",
    "Program length: full-time track ~4 months (17 weeks × 30 hours per week). Weekend track ~6–7 months (27 weeks × 18 hours per week).",
    "Manhattan-only programs: 50-Hour Barber Refresher (for licensed barbers returning to the trade after a break) and a 3-Hour Contagious Diseases course (required for NY barber license renewal).",
    "There is no fully online barber program in New York. NY State requires the 500 practical hours to be in-person and hands-on — this applies to every accredited school in the state, not just ABI.",

    // Tuition + payment plans (per plan)
    "Tuition Plan A — Morning: total $5,600. Down payment $500. 17 weekly payments of $300. Schedule Monday–Friday 8:00 AM to 2:00 PM.",
    "Tuition Plan B — Afternoon: total $4,600. Down payment $500. 16 weekly payments of $250, plus a final payment of $100. Schedule Monday–Friday 2:00 PM to 8:00 PM.",
    "Tuition Plan C — Weekend: total $4,600. Weekly payments start at $150 per week. Schedule Saturday and Sunday 9:00 AM to 7:00 PM.",
    "Every payment plan includes a $100 non-refundable registration fee inside the $500 down payment. Books and tools are extra and can be purchased through the school or independently.",
    "There is no application fee separate from the $500 down payment — the $500 both enrolls the student and secures a seat in the next cohort.",
    "ABI does not charge for the entrance exam (ATB) for students who do not have a high school diploma or GED.",

    // Financial aid
    "Accepted financial aid at ABI: ACCES-VR (a New York State Adult Career and Continuing Education Services program that covers tuition, tools, and books for qualifying NY residents with disabilities), Post-9/11 GI Bill®, and VA educational benefits. New York State Department of Labor grants may also apply case-by-case.",
    "ABI is NOT part of the federal Title IV student loan program — Federal Pell Grants and federal student loans are not available. Payment plans, ACCES-VR, and VA benefits are the primary aid pathways.",
    "How ACCES-VR works: students apply directly with ACCES-VR (a NY State agency, not ABI). If approved, ACCES-VR sends payment directly to the school. ABI's admissions team can guide applicants through the intake steps.",
    "Weekly payment plans as low as $150/week let students pay tuition while they study, without needing loans.",

    // Curriculum — technical
    "Technical skills taught: classic tapers; low, mid, high, and high-top fades; pompadours; caesars; flat tops; afro cuts; razor lineups; hot-towel shaves; beard trims and beard shaping; scissor-over-comb; clipper-over-comb; scalp massage; facial massage; shampoos and blowouts.",
    "Advanced modules: artificial hair techniques, hair coloring (semi-permanent and temporary), wigs and hairpieces, and hair replacement techniques (including systems and integration).",
    "Straight-razor training: students learn traditional straight-razor lineups, hot-towel shaves, and neck/head shaves with sterilization protocols. Straight razors are used in the clinic under instructor supervision.",

    // Curriculum — business + law
    "Business & career modules: client consultation, barbershop operations, building clientele, retail add-ons, tipping etiquette, booth rental vs. employment, and full NY State Board Exam prep.",
    "Sanitation & law modules: sterilization procedures (Barbicide, autoclave for razors), barber history, New York State barbering laws, and shop management.",
    "Board-exam prep includes both the written portion (theory, sanitation, NY law) and the practical portion (haircut, shave, sanitation demonstration) with mock exams before the real test.",

    // Hands-on clinic
    "Hands-on training with real clients starts within the first few weeks — students work in a supervised on-campus barber clinic from early in the program.",
    "Clinic haircuts for the public are offered at both campuses at a discounted rate. This gives students volume, variety, and speed practice on real heads of hair with a diverse clientele.",
    "Instructors supervise every clinic haircut — no student cuts unsupervised until they demonstrate competency and are cleared.",

    // Instructors
    "Every ABI instructor is a former ABI graduate — the school hires from within so instructors know the exact path students are on.",
    "Lead instructor King David has 30+ years of professional barbering experience and heads the Manhattan campus curriculum.",
    "The Bronx campus has its own instructor team, also bilingual (English/Spanish), operating on the same curriculum and same board-exam prep standard.",

    // Career + earnings
    "Career earnings for barbers in the NYC area (industry estimates, not guarantees): Year 1 entry-level $35,000–$45,000. Years 2–3 established $50,000–$70,000. Year 3+ booth renter or shop owner $75,000–$100,000+. Cash tips are common and generally on top of these numbers.",
    "Job-placement assistance is provided on graduation — every student meets with the job-placement office to find work after passing the state board exam.",
    "Common career paths after ABI: employed barber at an established shop, freelance/mobile barber, booth renter (rent a chair inside an existing shop), or shop owner.",
    "Booth-rent economics in NYC: most barbers pay roughly $200–$400/week for a chair and keep 100% of what they cut. Booth renters set their own hours and prices.",

    // Enrollment requirements
    "Entrance requirements to ABI: minimum age 17 years old; a High School Diploma or GED OR pass ABI's Ability-To-Benefit (ATB) entrance exam; a Social Security card; a valid photo ID; proof of address; and the $500 down payment.",
    "ATB (Ability-To-Benefit) exam: a short basic-skills test given at ABI. It lets applicants without a diploma or GED still enroll. There is no separate fee for it.",
    "International students / non-citizens: US work authorization or a valid Social Security number is needed for licensure in NY. Applicants without SSN should contact admissions before enrolling to confirm what documentation is acceptable.",

    // Campuses + contact — Manhattan
    "Manhattan campus address: 48 West 39th Street, New York, NY 10018. Between 5th and 6th Avenue in Midtown Manhattan.",
    "Manhattan campus phone (English): (212) 290-2289. Phone (Spanish): (212) 290-0278. Admissions email: admission@abi.edu.",
    "Manhattan campus is a short walk from Bryant Park, the 42nd Street/Bryant Park subway (B, D, F, M lines) and Times Square (N, Q, R, W, 1, 2, 3, 7 lines).",

    // Campuses + contact — Bronx
    "Bronx campus address: 121 Westchester Square, Bronx, NY 10461. Located in the Westchester Square section of the Bronx.",
    "Bronx campus phone: (718) 676-0640. Same admissions email: admission@abi.edu.",
    "Bronx campus is served by the 6 train (Westchester Square–East Tremont Ave station) and several bus lines.",

    // Campus hours + operations
    "Campus opening hours: Monday–Friday 8:00 AM – 8:00 PM. Saturday & Sunday 9:00 AM – 7:00 PM. Closed on major US holidays.",
    "Cohort start dates: a new cohort begins the first Monday of every month. Applicants who miss a start date roll to the next month automatically.",
    "Class-size philosophy: cohorts are kept small enough for hands-on instruction. Ask admissions for the current cohort size — it varies month to month.",

    // Kit + dress code
    "Student kit: ABI provides guidance on required tools (clippers, trimmers, shears, straight razor, capes, combs, brushes). Students can buy the kit through the school or independently. A basic student kit runs roughly $300–$500 depending on brand choice.",
    "Dress code: neat, professional appearance. All-black is common at both campuses. Closed-toe shoes are required in the clinic for safety.",
    "Attendance policy: barber licensure in NY requires all 500 hours — missed hours must be made up. ABI tracks attendance and offers make-up sessions.",

    // Language + inclusion
    "Bilingual instruction: every technical skill, business module, and exam-prep session is delivered in both English and Spanish at both campuses.",
    "Women barbers are welcomed at ABI — the school actively encourages women to enter the trade and has multiple women graduates now working in NYC shops.",
    "Veterans are actively welcomed and supported. ABI accepts Post-9/11 GI Bill® and VA educational benefits.",

    // NY Board exam
    "New York State Board Exam: administered by the NY State Division of Licensing Services. Two parts — a written test and a practical test. ABI provides in-school mock exams and study materials before the real test.",
    "License endorsement: New York's Master Barber license can also endorse into a number of other states, though rules vary. Ask admissions about specific state transfers.",

    // How to enroll — action steps
    "To enroll at ABI: (1) fill out the contact form on this site, or call the campus you want to attend. (2) Schedule a tour and meet admissions. (3) Bring your ID, SSN card, proof of address, and diploma/GED (or take the ATB exam). (4) Pay the $500 down payment and pick a start Monday. (5) Show up on day one — the school handles the rest.",
    "Same-day enrollment is possible on any weekday — walk into either campus during operating hours with the required documents and the $500 down payment.",
    "Refund and cancellation: ABI follows NY State BPSS refund policy. The $100 registration fee is non-refundable. Ask admissions for the current written policy.",

    // Reviews + social proof
    "Google reviews: 100+ reviews, aggregate 4.6/5. Common themes in reviews: strong instructor mentorship, real clinic experience, and job-ready graduates.",
    "Alumni testimonial theme: 'ABI taught me how to actually cut hair, not just pass a test.' Alumni frequently return to teach or hire new grads.",

    // Common Spanish-user questions
    "Muchos estudiantes son bilingües o hispanohablantes. Todo el temario se enseña en español si el estudiante lo prefiere, incluida la preparación para el examen del estado de NY.",
    "El campus de Manhattan tiene una línea telefónica dedicada al español: (212) 290-0278. El campus del Bronx atiende llamadas en español al (718) 676-0640.",
    "Un estudiante que solo habla español puede estudiar el programa completo en español y presentar el examen estatal — el estado ofrece el examen escrito también en español.",

    // Practical FAQs
    "Do I need barber experience before enrolling? No — most students start with zero cutting experience. The 500-hour curriculum builds skills from the foundations.",
    "How many days a week? Morning and afternoon tracks are Monday–Friday (5 days). The weekend track is Saturday and Sunday only (2 days).",
    "Can I switch tracks? Yes — students can switch between morning, afternoon, and weekend tracks with admissions approval, subject to seat availability.",
    "Can I work while studying? Yes — the weekend track is designed specifically for students who work weekdays. Afternoon track also leaves mornings free.",
    "Is there parking? Manhattan campus is midtown and parking is limited — public transit is easiest. Bronx campus has more street parking nearby.",
    "Is there Wi-Fi? Yes, both campuses have free student Wi-Fi.",
    "Language of the exam: NY State offers the written portion in English and Spanish. Practical is language-neutral.",
    "Age of typical student: mid-teens to mid-40s. There is no upper age limit — ABI has enrolled second-career students in their 50s and 60s.",
    "Do I get a certificate? Yes — graduates receive an ABI diploma. After passing the state exam, students receive their NY State Master Barber license.",

    // Extras + differentiators
    "Why ABI vs other NYC barber schools: 30 years in NYC, bilingual by default, small cohort sizes, instructors who all graduated from ABI, hands-on clinic from week one, and job-placement assistance on graduation.",
    "Chair-time focus: students cut a lot of hair. The clinic model means every student leaves with hundreds of hours of real-client experience, not just mannequin heads.",
    "Networking: NYC is one of the biggest barbering markets in the world. Graduates leave with a network of instructors, alumni, and local shop connections.",
    "Continuing education: ABI's 3-hour Contagious Diseases course meets NY's continuing-ed requirement for license renewal. The 50-hour Refresher helps returning barbers rebuild speed and pass the renewal.",

    // Emergency / redirects
    "For anything the assistant is unsure about — call Manhattan (English) (212) 290-2289 / (Spanish) (212) 290-0278, or Bronx (718) 676-0640, or email admission@abi.edu. Admissions replies same-day during operating hours."
  ];

  // ── MEGA SYSTEM PROMPT — one prompt, both languages, per-message switching
  var SYS = [
    "You are the friendly, professional admissions assistant for the American Barber Institute (ABI) — New York City's dedicated barber school since 1996.",
    "",
    "IDENTITY & MISSION",
    "- You represent ABI. Speak as a warm, knowledgeable admissions counselor, not a generic AI.",
    "- Your goal is to answer prospective-student questions accurately, build trust, and gently encourage the visitor to take the next step (schedule a call, visit a campus, fill out the contact form, or pay the $500 down payment to enroll).",
    "- Never invent facts. If a question is not covered by the FACTS below, say honestly you don't have that detail and invite them to call admissions.",
    "",
    "LANGUAGE HANDLING (very important)",
    "- Detect the language of each individual user message.",
    "- If the user writes in Spanish, reply entirely in natural, friendly Spanish (use the informal 'tú' form).",
    "- If the user writes in English, reply in English.",
    "- Mid-conversation switches are welcome — if they switch language, switch with them for that message and every message after until they switch back.",
    "- Never mix languages inside one reply.",
    (pageLangIsES
      ? "- The visitor started on the Spanish site, so default to Spanish until they clearly switch to English."
      : "- The visitor started on the English site, so default to English until they clearly switch to Spanish."),
    "",
    "STYLE",
    "- Warm, human, professional. Sound like a real admissions counselor, not corporate.",
    "- Reply in 2–4 short sentences by default. Use a bullet list only when the user asks for a comparison or a list of options.",
    "- Use plain text. No markdown headings, no bold, no code blocks. Emojis sparingly (0–1 per message).",
    "- Address the visitor directly ('you' / 'tú'). Never refer to them in the third person.",
    "",
    "ANSWER RULES",
    "- Use ONLY the FACTS below. Do not speculate about pricing, dates, or policies not written here.",
    "- When you cite tuition, always mention the payment plan option and the $500 down payment.",
    "- When you mention enrolling, include the phone number of the campus they're asking about.",
    "- If they ask about something not covered (e.g. federal financial aid, exact class size this month, specific instructor names besides King David), say you'll connect them with admissions and give the phone/email.",
    "- End most replies with a soft next step: 'Want me to check the next open cohort?' or 'Would you like the direct line?' — but not every reply, don't be pushy.",
    "",
    "FACTS (source of truth — do not contradict):",
    FACTS.join("\n- ")
  ].join("\n");

  // ── Local keyword fallback (used only if the AI endpoint is unreachable)
  var KB_EN = [
    { k: ["tuition","cost","price","how much","fee","fees","expensive"],
      a: "Tuition is $5,600 for the Morning plan and $4,600 for Afternoon or Weekend. A $500 down payment enrolls you (that includes the $100 registration fee). Weekly payment plans start at $150/week, and we accept ACCES-VR, Post-9/11 GI Bill®, and VA benefits." },
    { k: ["schedule","hours","time","morning","afternoon","weekend","evening"],
      a: "We run three tracks: Morning Mon–Fri 8 AM–2 PM, Afternoon Mon–Fri 2 PM–8 PM, and Weekend Sat–Sun 9 AM–7 PM. New cohorts start the first Monday of every month at both campuses." },
    { k: ["where","location","campus","address","manhattan","bronx","directions"],
      a: "We have two campuses. Manhattan is at 48 West 39th Street, NY 10018 — (212) 290-2289 English / (212) 290-0278 Spanish. Bronx is at 121 Westchester Square, NY 10461 — (718) 676-0640." },
    { k: ["enroll","apply","register","sign up","start","join"],
      a: "To enroll you'll need to be 17+, have a HS Diploma or GED (or pass our ATB exam), a photo ID, proof of address, Social Security card, and a $500 down payment. Call (212) 290-2289 or fill out the contact form and we'll get you into the next cohort." },
    { k: ["require","need","diploma","ged","age","old"],
      a: "Requirements: 17+ years old, a High School Diploma or GED (or pass our free ATB exam), Social Security card, valid photo ID, proof of address, and a $500 down payment." },
    { k: ["program","course","master barber","500","length","long","duration"],
      a: "The 500-Hour Master Barber Program is our flagship. Full-time takes about 4 months; the weekend track takes about 6–7 months. It fully prepares you for the New York State Master Barber license." },
    { k: ["financial","aid","payment","plan","gi bill","va","acces","scholarship","loan"],
      a: "We accept ACCES-VR, Post-9/11 GI Bill®, and VA benefits. Weekly payment plans start at $150/week. We're not part of federal Title IV, so Pell Grants aren't available." },
    { k: ["tour","visit","see","virtual","video"],
      a: "You can watch our Virtual Tour on the About page, or visit either campus in person any weekday from 8 AM to 8 PM. Just call ahead and we'll show you around." },
    { k: ["online","remote","distance","virtual class"],
      a: "New York State requires all 500 hours to be in-person — no barber school in NY can be fully online. But both our campuses are open 6 days a week with multiple schedule options." },
    { k: ["job","career","earn","salary","income","placement","work"],
      a: "Barbers in NYC typically earn $35–45K starting, $50–70K established, and $75K–$100K+ as booth renters or owners (plus tips). Every graduate meets with our job placement office before leaving." }
  ];
  var KB_ES = [
    { k: ["matrícula","matricula","costo","precio","cuánto","cuanto","tarifa","caro"],
      a: "La matrícula es $5,600 para el plan de mañana y $4,600 para tarde o fin de semana. Con $500 de enganche te inscribes (incluye la cuota de inscripción de $100). Los planes semanales empiezan desde $150 por semana y aceptamos ACCES-VR, GI Bill® y beneficios VA." },
    { k: ["horario","clases","mañana","manana","tarde","fin de semana","noche"],
      a: "Tenemos tres horarios: Mañana Lun–Vie 8:00 AM–2:00 PM, Tarde Lun–Vie 2:00 PM–8:00 PM, y Fin de semana Sáb–Dom 9:00 AM–7:00 PM. Las clases nuevas empiezan el primer lunes de cada mes en los dos campus." },
    { k: ["dónde","donde","ubicación","ubicacion","campus","dirección","direccion","manhattan","bronx"],
      a: "Tenemos dos campus. Manhattan está en 48 West 39th Street, NY 10018 — (212) 290-2289 inglés / (212) 290-0278 español. Bronx está en 121 Westchester Square, NY 10461 — (718) 676-0640." },
    { k: ["inscrib","matricul","empezar","registr","aplicar"],
      a: "Para inscribirte necesitas tener 17+ años, diploma de prepa o GED (o aprobar nuestro examen ATB), identificación con foto, comprobante de domicilio, tarjeta de Seguro Social y $500 de enganche. Llama al (212) 290-2289 o llena el formulario y te llamamos." },
    { k: ["requisit","necesito","diploma","ged","edad"],
      a: "Requisitos: 17+ años, diploma de prepa o GED (o aprobar el examen ATB gratis en ABI), tarjeta de Seguro Social, identificación con foto, comprobante de domicilio y $500 de enganche." },
    { k: ["programa","curso","500","duración","duracion","cuánto dura","cuanto dura"],
      a: "El Programa de Barbero Maestro de 500 horas es el principal. Tiempo completo dura ~4 meses; el fin de semana ~6–7 meses. Te prepara para el examen estatal de NY." },
    { k: ["ayuda","financier","gi bill","va","acces","beca","préstamo","prestamo"],
      a: "Aceptamos ACCES-VR, Post-9/11 GI Bill® y beneficios VA. Los planes de pago semanales empiezan desde $150/semana. No participamos en el Título IV federal, así que Pell Grants no aplica." },
    { k: ["tour","visita","ver","virtual"],
      a: "Puedes ver el Tour Virtual en la página About, o visitar cualquier campus de lunes a viernes 8 AM–8 PM. Llama antes y te mostramos las instalaciones." },
    { k: ["online","en línea","en linea","virtual","a distancia"],
      a: "El estado de Nueva York requiere que las 500 horas sean presenciales — ninguna escuela de barbería en NY puede ser 100% online. Pero abrimos 6 días por semana con varios horarios." },
    { k: ["trabajo","empleo","salario","ganar","colocación","colocacion"],
      a: "Los barberos en NYC ganan típicamente $35–45K de principiante, $50–70K establecidos, y $75K–$100K+ como booth renter o dueño (además de propinas). Cada graduado se reúne con nuestra oficina de colocación laboral antes de graduarse." }
  ];

  // Simple per-message language detection: counts distinctive Spanish tokens.
  var ES_TOKENS = /(\b(hola|gracias|por|favor|quiero|necesito|quisiera|cuánto|cuanto|dónde|donde|cuándo|cuando|clases|horario|precio|matrícula|matricula|inscrib|matricul|ayuda|financier|programa|estudiar|barber[oi]a?|escuela|preguntar|puedo|debo|tengo|soy|estoy|para|con|sobre|acerca|información|informacion)\b|[¿¡]|ñ)/i;
  function detectES(text) {
    return ES_TOKENS.test(text || "");
  }

  function localAnswer(q, useES) {
    var t = (q || "").toLowerCase();
    var kb = useES ? KB_ES : KB_EN;
    for (var i = 0; i < kb.length; i++) {
      for (var j = 0; j < kb[i].k.length; j++) {
        if (t.indexOf(kb[i].k[j]) !== -1) return kb[i].a;
      }
    }
    return null;
  }

  // ── Streaming AI call with fallback to non-streaming ────────────────────
  function askAIStream(history, question, onDelta) {
    var msgs = [{ role: "system", content: SYS }];
    history.slice(-8).forEach(function (m) { msgs.push({ role: m.role, content: m.text }); });
    msgs.push({ role: "user", content: question });

    var ctrl = new AbortController();
    var to = setTimeout(function () { ctrl.abort(); }, 20000);

    return fetch("https://text.pollinations.ai/", {
      method: "POST",
      headers: { "Content-Type": "application/json", "Accept": "text/event-stream" },
      body: JSON.stringify({
        messages: msgs,
        model: "openai",
        stream: true,
        private: true,
        referrer: "abi-v13"
      }),
      signal: ctrl.signal
    }).then(function (r) {
      if (!r.ok || !r.body || !r.body.getReader) {
        clearTimeout(to);
        // Fall back to non-streaming plain-text endpoint if streaming isn't supported
        return askAIPlain(history, question);
      }
      var reader = r.body.getReader();
      var decoder = new TextDecoder();
      var buffer = "";
      var full = "";
      return (function readLoop() {
        return reader.read().then(function (chunk) {
          if (chunk.done) { clearTimeout(to); return full.trim() || askAIPlain(history, question); }
          buffer += decoder.decode(chunk.value, { stream: true });
          var lines = buffer.split("\n");
          buffer = lines.pop() || "";
          lines.forEach(function (line) {
            line = line.trim();
            if (!line.indexOf("data:")) {
              var payload = line.slice(5).trim();
              if (payload === "[DONE]") return;
              try {
                var j = JSON.parse(payload);
                var delta = (j.choices && j.choices[0] && (j.choices[0].delta && j.choices[0].delta.content || j.choices[0].text || j.choices[0].message && j.choices[0].message.content)) || "";
                if (delta) { full += delta; onDelta(full); }
              } catch (e) { /* ignore malformed SSE chunk */ }
            }
          });
          return readLoop();
        });
      })();
    });
  }

  function askAIPlain(history, question) {
    var msgs = [{ role: "system", content: SYS }];
    history.slice(-8).forEach(function (m) { msgs.push({ role: m.role, content: m.text }); });
    msgs.push({ role: "user", content: question });
    var ctrl = new AbortController();
    var to = setTimeout(function () { ctrl.abort(); }, 15000);
    return fetch("https://text.pollinations.ai/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ messages: msgs, model: "openai", private: true, referrer: "abi-v13" }),
      signal: ctrl.signal
    }).then(function (r) {
      clearTimeout(to);
      if (!r.ok) throw new Error("bad");
      return r.text();
    }).then(function (txt) {
      txt = (txt || "").trim();
      if (!txt || txt.length < 2 || /^\s*</.test(txt)) throw new Error("empty");
      return txt;
    });
  }

  // ── UI (bilingual by page-lang initial state) ───────────────────────────
  var UI = {
    greet_en: "👋 Hi! I'm ABI's admissions assistant. Ask me anything about becoming a barber — or tap a question:",
    greet_es: "👋 ¡Hola! Soy el asistente de admisiones de ABI. Pregúntame lo que quieras sobre convertirte en barbero — o toca una opción:",
    chips_en: ["💸 Tuition & costs", "🕒 Class schedules", "📍 Campus locations", "📝 How to enroll", "🎓 The program", "💳 Financial aid"],
    chips_es: ["💸 Matrícula y costos", "🕒 Horarios de clases", "📍 Ubicaciones", "📝 Cómo inscribirme", "🎓 El programa", "💳 Ayuda financiera"],
    open_en: "Open ABI AI Assistant", open_es: "Abrir el asistente de IA de ABI",
    close_en: "Close", close_es: "Cerrar",
    typing_en: "Typing…", typing_es: "Escribiendo…",
    title_en: "ABI Assistant", title_es: "Asistente de ABI",
    status_en: "Real AI · replies in seconds", status_es: "IA real · responde en segundos",
    fab_en: "AI Assistant", fab_es: "Asistente IA",
    ph_en: "Type your question…", ph_es: "Escribe tu pregunta…",
    followup_en: "Which schedule interests you most — morning, afternoon, or weekend? 🙂",
    followup_es: "¿Qué horario te interesa más — mañana, tarde o fin de semana? 🙂",
    gate_h_en: "Hi 👋 Before we start, share your contact info:",
    gate_h_es: "Hola 👋 Antes de empezar, comparte tus datos de contacto:",
    gate_name_en: "Full name", gate_name_es: "Nombre completo",
    gate_email_en: "Email", gate_email_es: "Correo electrónico",
    gate_phone_en: "Phone", gate_phone_es: "Teléfono",
    gate_btn_en: "Start chat", gate_btn_es: "Comenzar el chat",
    gate_note_en: "By submitting you agree to receive SMS or emails from ABI. Rates may apply.",
    gate_note_es: "Al enviar aceptas recibir SMS o emails de ABI. Pueden aplicar tarifas.",
    err_en: "Great question — admissions can help with that best: call (212) 290-2289 or email admission@abi.edu. Anything else about tuition, schedules, or enrolling?",
    err_es: "Buena pregunta — para eso es mejor hablar con admisiones: llama al (212) 290-2289 o escribe a admission@abi.edu. ¿Algo más sobre matrícula, horarios o inscripción?"
  };
  function t(k) { return UI[k + (pageLangIsES ? "_es" : "_en")]; }

  var wrap = document.createElement("div");
  wrap.className = "abibot";
  wrap.innerHTML =
    '<button class="abibot-fab" aria-label="' + t("open") + '">' +
      '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M21 12a8.5 8.5 0 0 1-8.5 8.5c-1.6 0-3-.4-4.3-1L3 21l1.6-4.8A8.5 8.5 0 1 1 21 12z"/></svg>' +
      '<span class="abibot-fab-badge">AI</span>' +
      '<span class="abibot-fab-label">' + t("fab") + '</span></button>' +
    '<div class="abibot-panel" role="dialog" aria-label="ABI assistant" hidden>' +
      '<div class="abibot-head"><span class="abibot-ava">ABI</span>' +
        '<div><b>' + t("title") + '</b><span>' + t("status") + '</span></div>' +
        '<button class="abibot-close" aria-label="' + t("close") + '">✕</button></div>' +
      '<div class="abibot-log" aria-live="polite"></div>' +
      '<div class="abibot-chips"></div>' +
      '<form class="abibot-input"><input type="text" autocomplete="off" placeholder="' + t("ph") + '" aria-label="Message"><button type="submit" aria-label="Send"><svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M3 11l18-8-8 18-2-7-8-3z"/></svg></button></form>' +
    '</div>';
  document.body.appendChild(wrap);

  var fab = wrap.querySelector(".abibot-fab");
  var panel = wrap.querySelector(".abibot-panel");
  var log = wrap.querySelector(".abibot-log");
  var chipsEl = wrap.querySelector(".abibot-chips");
  var form = wrap.querySelector(".abibot-input");
  var input = form.querySelector("input");
  var history = [];
  var greeted = false;

  function scroll() { log.scrollTop = log.scrollHeight; }
  function add(role, text) {
    var b = document.createElement("div");
    b.className = "abibot-msg abibot-" + role;
    b.textContent = text;
    log.appendChild(b); scroll();
    return b;
  }
  function typing() {
    var t2 = document.createElement("div");
    t2.className = "abibot-msg abibot-bot abibot-typing";
    t2.innerHTML = "<span></span><span></span><span></span>";
    log.appendChild(t2); scroll();
    return t2;
  }
  function renderChips() {
    chipsEl.innerHTML = "";
    var chips = pageLangIsES ? UI.chips_es : UI.chips_en;
    chips.forEach(function (c) {
      var btn = document.createElement("button");
      btn.className = "abibot-chip";
      btn.textContent = c;
      btn.addEventListener("click", function () { send(c.replace(/^[^A-Za-zÀ-ÿ]+/, "")); });
      chipsEl.appendChild(btn);
    });
  }

  function send(q) {
    q = (q || "").trim();
    if (!q) return;
    add("user", q);
    history.push({ role: "user", text: q });
    input.value = "";
    chipsEl.style.display = "none";
    var tip = typing();
    var bubble = null;

    var msgIsES = detectES(q);

    var onDelta = function (fullSoFar) {
      if (!bubble) { tip.remove(); bubble = add("bot", ""); }
      bubble.textContent = fullSoFar;
      scroll();
    };

    askAIStream(history, q, onDelta)
      .then(function (final) {
        // If streaming didn't produce a bubble (fell back to plain), place final now.
        if (!bubble) { tip.remove(); bubble = add("bot", ""); }
        if (typeof final === "string" && final.trim() && final.trim() !== bubble.textContent) {
          bubble.textContent = final.trim();
        }
        history.push({ role: "assistant", text: bubble.textContent });
        scroll();
      })
      .catch(function () {
        try { tip.remove(); } catch (e) {}
        var fallback = localAnswer(q, msgIsES) || (msgIsES ? UI.err_es : UI.err_en);
        if (!bubble) bubble = add("bot", "");
        bubble.textContent = fallback;
        history.push({ role: "assistant", text: fallback });
      });
  }

  // Pre-chat contact gate
  var contactSubmitted = false;
  try { contactSubmitted = !!sessionStorage.getItem("abibot-contact"); } catch (e) {}

  function renderContactGate() {
    var b = document.createElement("div");
    b.className = "abibot-gate";
    b.innerHTML =
      '<p class="abibot-gate-h">' + t("gate_h") + '</p>' +
      '<form class="abibot-gate-form" novalidate>' +
        '<input type="text" name="name" required placeholder="' + t("gate_name") + '" autocomplete="name">' +
        '<input type="email" name="email" required placeholder="' + t("gate_email") + '" autocomplete="email">' +
        '<input type="tel" name="phone" required placeholder="' + t("gate_phone") + '" autocomplete="tel">' +
        '<button type="submit" class="abibot-gate-btn">' + t("gate_btn") + '</button>' +
        '<p class="abibot-gate-note">' + t("gate_note") + '</p>' +
      '</form>';
    log.appendChild(b);
    var gf = b.querySelector("form");
    gf.addEventListener("submit", function (e) {
      e.preventDefault();
      var data = {
        name: gf.name.value.trim(),
        email: gf.email.value.trim(),
        phone: gf.phone.value.trim(),
        ts: new Date().toISOString(),
        page: location.pathname
      };
      if (!data.name || !data.email || !data.phone) return;
      try { sessionStorage.setItem("abibot-contact", JSON.stringify(data)); } catch (e) {}
      contactSubmitted = true;
      b.remove();
      form.style.display = "";
      chipsEl.style.display = "";
      startChat();
    });
  }

  function startChat() {
    if (!greeted) {
      greeted = true;
      var g = pageLangIsES ? UI.greet_es : UI.greet_en;
      add("bot", g);
      history.push({ role: "assistant", text: g });
      renderChips();
      setTimeout(function () {
        add("bot", pageLangIsES ? UI.followup_es : UI.followup_en);
      }, 900);
    }
    setTimeout(function () { input.focus(); }, 120);
  }

  function open() {
    panel.hidden = false;
    fab.classList.add("is-open");
    if (!contactSubmitted) {
      form.style.display = "none";
      chipsEl.style.display = "none";
      if (!log.querySelector(".abibot-gate")) renderContactGate();
    } else {
      form.style.display = "";
      startChat();
    }
  }
  function close() { panel.hidden = true; fab.classList.remove("is-open"); }

  fab.addEventListener("click", function () { panel.hidden ? open() : close(); });
  wrap.querySelector(".abibot-close").addEventListener("click", close);
  form.addEventListener("submit", function (e) { e.preventDefault(); send(input.value); });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape" && !panel.hidden) close(); });

  // Proactive nudge after 6 seconds (once per session)
  try {
    if (!sessionStorage.getItem("abibot-nudged")) {
      setTimeout(function () {
        if (panel.hidden) { fab.classList.add("abibot-nudge"); sessionStorage.setItem("abibot-nudged", "1"); }
      }, 6000);
    }
  } catch (e) {}
})();
