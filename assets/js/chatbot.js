/* American Barber Institute — AI admissions assistant.
 * Self-injecting chat widget. Free, no-key AI (Pollinations) with an ABI
 * knowledge base + local keyword fallback so it always answers. */
(function () {
  "use strict";
  if (window.__abiBotLoaded) return;
  window.__abiBotLoaded = true;

  // v4.0 — richer Spanish detection: HTML lang OR URL path contains /es or /spanish
  var ES = (document.documentElement.lang || "en").slice(0, 2) === "es"
        || /(^|\/)(es|spanish)(\/|$)/i.test(location.pathname);

  // ── ABI knowledge base — comprehensive, kept in sync with the site ────────
  var FACTS = [
    // Identity + credentials
    "American Barber Institute (ABI) is New York City's dedicated barber school, established in 1996 — 30+ years of experience and 10,000+ graduates.",
    "ABI is licensed by the New York State Department of Education (NYSED / BPSS). It is a state-approved barber training program with full NY State Board Exam preparation.",
    "ABI has an aggregate 4.6/5 rating across 100+ Google reviews.",

    // Programs
    "Primary program: 500-Hour Master Barber Program, offered at both Manhattan and Bronx campuses. New classes begin the first Monday of every month.",
    "Program length: full-time ~4 months (17 weeks at 30 hrs/week). Weekend track ~6-7 months (27 weeks at 18 hrs/week).",
    "Additional programs (Manhattan only): 50-Hour Barber Refresher for licensed barbers returning to the trade, and a 3-Hour Contagious Diseases Course required for NY State license renewal.",

    // Tuition + payment plans (per plan)
    "Tuition Plan A — Morning: $5,600 total. $500 down + 17 weekly payments of $300. Schedule Mon-Fri 8:00 AM - 2:00 PM.",
    "Tuition Plan B — Afternoon: $4,600 total. $500 down + 16 weekly payments of $250 + a final $100. Schedule Mon-Fri 2:00 PM - 8:00 PM.",
    "Tuition Plan C — Weekend: $4,600 total. Weekly payments from $150/week. Schedule Sat-Sun 9:00 AM - 7:00 PM.",
    "Every plan includes a $100 non-refundable registration fee inside the down payment. Books and tools are extra.",

    // Financial aid
    "Financial aid accepted: ACCES-VR (New York State — covers tuition, tools, and books for qualifying residents with disabilities), Post-9/11 GI Bill(R), VA educational benefits. NYS Department of Labor grants may also apply.",
    "Weekly payment plans from $150/week let students pay while they study.",

    // Curriculum + skills
    "Core skills taught: classic tapers; low, mid, high, and high-top fades; pompadours; caesars; flat tops; afro cuts; razor lineups; hot-towel shaves; beard trims and shaping; scissor-over-comb and clipper-over-comb techniques; scalp/facial massage; shampoos and blowouts.",
    "Additional training: artificial hair and hair coloring (semi-permanent and temporary); wigs and hairpieces; hair replacement techniques.",
    "Business & career modules: client consultation skills, barbershop operations, building clientele, job placement prep, and full NY State Board Exam preparation.",
    "Sanitation & law modules: sanitation and sterilization procedures, barber history, New York State barbering laws, shop management.",

    // Hands-on training + clinic
    "Hands-on training with real clients starts within the first few weeks — students work in a supervised on-campus barber clinic from early in the program.",
    "Students refine skills in real-world conditions from day one with a diverse clientele.",

    // Instructors
    "Every ABI instructor is a former ABI graduate — the school hires from within so instructors know the exact path students are on.",
    "Lead instructor King David has 30+ years of professional barbering experience.",

    // Career + earnings
    "Career earnings for barbers (industry estimates, not guaranteed): Year 1 entry-level $35,000-$45,000. Years 2-3 established $50,000-$70,000. Year 3+ booth renter or shop owner $75,000-$100,000+.",
    "Job-placement assistance is provided on graduation — every student meets with the job placement office to find work after passing the state board exam.",

    // Enrollment requirements
    "Entrance requirements: minimum age 17; High School Diploma or GED OR pass ABI's Ability-To-Benefit (ATB) entrance exam; Social Security card; valid photo ID; proof of address; and $500 down payment to enroll.",
    "Online barber school is NOT allowed in New York — the state requires in-person, hands-on training hours.",

    // Campuses + contact
    "Manhattan campus: 48 West 39th Street, New York, NY 10018. Phone (English): (212) 290-2289. Phone (Spanish): (212) 290-0278. Email: admission@abi.edu.",
    "Bronx campus: 121 Westchester Square, Bronx, NY 10461. Phone: (718) 676-0640.",
    "Both campuses offer bilingual English/Spanish instruction.",
    "Campus hours: Monday-Friday 8:00 AM - 8:00 PM. Saturday & Sunday 9:00 AM - 7:00 PM.",

    // Outcomes
    "Program prepares students for the New York State Master Barber license including full NY State Board Exam preparation.",
    "Career paths after ABI: traditional barbershop employee, freelance/mobile barber, booth renter, or shop/business owner.",

    // How to enroll
    "To enroll: fill out the contact form on this site, OR call (212) 290-2289 (Manhattan English), (212) 290-0278 (Manhattan Spanish), or (718) 676-0640 (Bronx). Then bring $500 down + required documents to begin the next monthly cohort."
  ];
  var SYS = "You are the friendly, professional admissions assistant for the American Barber Institute (ABI) — New York City's dedicated barber school since 1996. " +
    "Your job: answer prospective-student questions accurately using ONLY the FACTS below, and gently encourage them to enroll, call admissions, or fill out the contact form. " +
    "Style: warm, conversational, 2-4 sentences, feel like a real human admissions counselor. Never invent details. " +
    "If a question isn't covered by the FACTS, say honestly that you're not sure and invite them to call (212) 290-2289 (English) / (212) 290-0278 (Spanish) or email admission@abi.edu. " +
    (ES
      ? "IMPORTANT: The visitor is on the Spanish site — reply entirely in natural, friendly Spanish. Use 'tú' (informal you). "
      : "Reply in English by default. If the visitor writes in Spanish, switch to Spanish for that reply. ") +
    "FACTS:\n" + FACTS.join("\n");

  // Local keyword fallback answers (used if the AI endpoint is unreachable)
  var KB = [
    { k: ["tuition", "cost", "price", "how much", "fee", "fees", "expensive", "precio", "costo", "cuánto"],
      a: ES ? "La matrícula es: Mañana $5,600; Tarde $4,600; Fin de semana $4,600. Incluye una cuota de inscripción de $100; se requiere $500 de enganche. Hay planes de pago desde $150/semana y ayuda financiera (ACCES-VR, GI Bill, VA)."
            : "Tuition is Morning $5,600 · Afternoon $4,600 · Weekend $4,600. That includes a $100 registration fee; a $500 down payment enrolls you. Weekly payment plans start at $150/week, and we accept ACCES-VR, GI Bill® and VA benefits." },
    { k: ["schedule", "hours", "time", "morning", "afternoon", "weekend", "evening", "horario", "clases"],
      a: ES ? "Tres horarios: Mañana (Lun–Vie 8:00 AM–2:00 PM), Tarde (Lun–Vie 2:00 PM–8:00 PM) y Fin de semana (Sáb–Dom 9:00 AM–7:00 PM). Las clases nuevas empiezan el primer lunes de cada mes."
            : "We have three schedules: Morning (Mon–Fri 8 AM–2 PM), Afternoon (Mon–Fri 2 PM–8 PM), and Weekend (Sat–Sun 9 AM–7 PM). New classes start the first Monday of every month." },
    { k: ["where", "location", "campus", "address", "manhattan", "bronx", "directions", "dónde", "ubicación", "dirección"],
      a: ES ? "Dos campus: Manhattan — 48 West 39th Street, NY 10018, (212) 290-2289; y Bronx — 121 Westchester Square, Bronx 10461, (718) 676-0640. En español: (212) 290-0278."
            : "Two campuses: Manhattan — 48 West 39th Street, NY 10018, (212) 290-2289; and Bronx — 121 Westchester Square, Bronx, NY 10461, (718) 676-0640. En Español: (212) 290-0278." },
    { k: ["enroll", "apply", "register", "sign up", "start", "join", "inscrib", "matricul", "empezar", "registr"],
      a: ES ? "¡Genial! Para inscribirte necesitas tener 17+ años, diploma/GED (o el examen ATB), identificación y $500 de enganche. Llena el formulario de contacto o llama al (212) 290-2289."
            : "Great! To enroll you'll need to be 17+, have a HS Diploma/GED (or pass our ATB exam), a photo ID, and a $500 down payment. Fill out the contact form or call (212) 290-2289 and we'll get you started." },
    { k: ["require", "need", "diploma", "ged", "age", "old", "requisito", "necesito", "edad"],
      a: ES ? "Requisitos: 17+ años, diploma de prepa o GED (o aprobar el examen ATB), tarjeta de Seguro Social, identificación con foto, comprobante de domicilio y $500 de enganche."
            : "Requirements: at least 17 years old, a High School Diploma or GED (or pass the ATB exam at ABI), Social Security card, photo ID, proof of address, and a $500 down payment." },
    { k: ["program", "course", "master barber", "500", "length", "long", "duration", "programa", "curso", "duración"],
      a: ES ? "Ofrecemos el Programa de Barbero Maestro de 500 horas. Tiempo completo ~4 meses; fin de semana ~6–7 meses. Te prepara para el examen estatal de barbería de NY."
            : "We offer the 500-Hour Master Barber Program. Full-time takes ~4 months; the weekend track ~6–7 months. It fully prepares you for the NY State Barber Board Exam." },
    { k: ["financial", "aid", "payment", "plan", "gi bill", "va", "acces", "scholarship", "ayuda", "pago"],
      a: ES ? "Hay planes de pago semanales desde $150/semana, y aceptamos ACCES-VR, Post-9/11 GI Bill® y beneficios VA."
            : "Yes — weekly payment plans start at $150/week, and we accept ACCES-VR, Post-9/11 GI Bill® and VA benefits." },
    { k: ["tour", "visit", "see", "virtual", "video", "tour", "visitar", "ver"],
      a: ES ? "Puedes ver nuestro Tour Virtual en la página About, o reservar una visita en persona. ¡Te encantará el espacio!"
            : "You can watch our Virtual Tour on the About page, or book an in-person visit — we'd love to show you around!" }
  ];

  function localAnswer(q) {
    var t = q.toLowerCase();
    for (var i = 0; i < KB.length; i++) {
      for (var j = 0; j < KB[i].k.length; j++) {
        if (t.indexOf(KB[i].k[j]) !== -1) return KB[i].a;
      }
    }
    return null;
  }

  // ── Free, no-key AI call (Pollinations) with timeout + fallback ───────────
  function askAI(history, q) {
    var msgs = [{ role: "system", content: SYS }];
    history.slice(-6).forEach(function (m) { msgs.push({ role: m.role, content: m.text }); });
    msgs.push({ role: "user", content: q });
    var ctrl = new AbortController();
    var to = setTimeout(function () { ctrl.abort(); }, 9000);
    return fetch("https://text.pollinations.ai/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ messages: msgs, model: "openai", private: true, referrer: "abi" }),
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

  // ── UI ────────────────────────────────────────────────────────────────────
  var GREET = ES
    ? "👋 ¡Hola! Soy el asistente de admisiones de ABI. Pregúntame lo que quieras sobre convertirte en barbero — o toca una opción:"
    : "👋 Hi! I'm ABI's admissions assistant. Ask me anything about becoming a barber — or tap a question:";
  var CHIPS = ES
    ? ["💸 Matrícula y costos", "🕒 Horarios de clases", "📍 Ubicaciones", "📝 Cómo inscribirme", "🎓 El programa", "💳 Ayuda financiera"]
    : ["💸 Tuition & costs", "🕒 Class schedules", "📍 Campus locations", "📝 How to enroll", "🎓 The program", "💳 Financial aid"];

  var wrap = document.createElement("div");
  wrap.className = "abibot";
  wrap.innerHTML =
    '<button class="abibot-fab" aria-label="' + (ES ? "Abrir el asistente de IA de ABI" : "Open ABI AI Assistant") + '">' +
      '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M21 12a8.5 8.5 0 0 1-8.5 8.5c-1.6 0-3-.4-4.3-1L3 21l1.6-4.8A8.5 8.5 0 1 1 21 12z"/></svg>' +
      '<span class="abibot-fab-badge">AI</span>' +
      '<span class="abibot-fab-label">' + (ES ? "Asistente IA" : "AI Assistant") + '</span></button>' +
    '<div class="abibot-panel" role="dialog" aria-label="ABI assistant" hidden>' +
      '<div class="abibot-head"><span class="abibot-ava">ABI</span>' +
        '<div><b>' + (ES ? "Asistente de ABI" : "ABI Assistant") + '</b><span>' + (ES ? "Normalmente responde al instante" : "Typically replies instantly") + '</span></div>' +
        '<button class="abibot-close" aria-label="' + (ES ? "Cerrar" : "Close") + '">✕</button></div>' +
      '<div class="abibot-log" aria-live="polite"></div>' +
      '<div class="abibot-chips"></div>' +
      '<form class="abibot-input"><input type="text" autocomplete="off" placeholder="' + (ES ? "Escribe tu pregunta…" : "Type your question…") + '" aria-label="Message"><button type="submit" aria-label="Send"><svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M3 11l18-8-8 18-2-7-8-3z"/></svg></button></form>' +
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
    var t = document.createElement("div");
    t.className = "abibot-msg abibot-bot abibot-typing";
    t.innerHTML = "<span></span><span></span><span></span>";
    log.appendChild(t); scroll();
    return t;
  }
  function renderChips() {
    chipsEl.innerHTML = "";
    CHIPS.forEach(function (c) {
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
    var t = typing();
    var done = function (ans) {
      t.remove();
      add("bot", ans);
      history.push({ role: "assistant", text: ans });
    };
    askAI(history, q)
      .then(done)
      .catch(function () {
        done(localAnswer(q) || (ES
          ? "Buena pregunta — para eso es mejor hablar con admisiones: llama al (212) 290-2289 o escribe a admission@abi.edu. ¿Algo más sobre matrícula, horarios o inscripción?"
          : "Great question — admissions can help with that best: call (212) 290-2289 or email admission@abi.edu. Anything else about tuition, schedules, or enrolling?"));
      });
  }

  // v12.4: pre-chat contact gate — name/email/phone before any Q&A
  var contactSubmitted = false;
  try { contactSubmitted = !!sessionStorage.getItem("abibot-contact"); } catch (e) {}

  function renderContactGate() {
    var b = document.createElement("div");
    b.className = "abibot-gate";
    b.innerHTML =
      '<p class="abibot-gate-h">' + (ES
        ? "Hola 👋 Antes de empezar, comparte tus datos de contacto:"
        : "Hi 👋 Before we start, please share your contact info:") + '</p>' +
      '<form class="abibot-gate-form" novalidate>' +
        '<input type="text" name="name" required placeholder="' + (ES ? "Nombre completo" : "Full name") + '" autocomplete="name">' +
        '<input type="email" name="email" required placeholder="' + (ES ? "Correo electrónico" : "Email") + '" autocomplete="email">' +
        '<input type="tel" name="phone" required placeholder="' + (ES ? "Teléfono" : "Phone") + '" autocomplete="tel">' +
        '<button type="submit" class="abibot-gate-btn">' + (ES ? "Comenzar el chat" : "Start chat") + '</button>' +
        '<p class="abibot-gate-note">' + (ES
          ? "Al enviar aceptas recibir SMS o emails de ABI. Pueden aplicar tarifas."
          : "By submitting you agree to receive SMS or emails from ABI. Rates may apply.") + '</p>' +
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
      add("bot", GREET);
      history.push({ role: "assistant", text: GREET });
      renderChips();
      setTimeout(function () {
        add("bot", ES ? "¿Qué horario te interesa más — mañana, tarde o fin de semana? 🙂"
                      : "Which schedule interests you most — morning, afternoon, or weekend? 🙂");
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

  // Proactively invite after a few seconds (once per session)
  try {
    if (!sessionStorage.getItem("abibot-nudged")) {
      setTimeout(function () {
        if (panel.hidden) { fab.classList.add("abibot-nudge"); sessionStorage.setItem("abibot-nudged", "1"); }
      }, 6000);
    }
  } catch (e) {}
})();
