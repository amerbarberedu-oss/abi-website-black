/* ============================================================
   ABI — Analytics + Consent loader   (v2)
   ------------------------------------------------------------
   ONE dependency: Google Tag Manager container GTM-NKLLGPC.
   GA4 (G-J6BNX36TS3), Meta Pixel (580471737041846), Microsoft
   Clarity (k5fxn2irko), CallRail (169987046), ClickCease, and
   Google Ads (AW-949292069) are all configured INSIDE the GTM
   web UI — never add/remove those tags here.

   What this file does:
     1. Sets Google Consent Mode v2 defaults BEFORE GTM boots.
        - Opt-in regions (EEA/UK/CH): all denied until the user
          accepts (GDPR).
        - Everywhere else incl. US/NY: granted by default, with a
          banner offering opt-out (CCPA "opt-out" model). A stored
          user choice always wins.
     2. Boots the GTM container.
     3. Pushes semantic events into dataLayer for GTM triggers:
          - "phone_click"    (tel: taps)          → GA4/Ads call conv.
          - "email_click"    (mailto: taps)
          - "generate_lead"  (form submissions)   → GA4/Ads/Meta lead
        GHL forms are cross-origin iframes, so leads are captured via
        (a) a GHL postMessage listener (best-effort) and (b) the
        thank-you page (reliable — requires the GHL form redirect to
        point at /thank-you; see marker below).
     4. Injects an accessible cookie-consent banner + a manager that
        the footer "Do Not Sell or Share My Personal Information"
        link ([data-abi-privacy-choices]) reopens.

   Trigger names to create in GTM: "CE - phone_click",
   "CE - generate_lead" (both already referenced by the container).
   ============================================================ */
(function () {
  "use strict";

  var GTM_ID = "GTM-NKLLGPC";
  var STORE_KEY = "abi-consent-v1"; // persisted user choice: "granted" | "denied"

  var w = window,
    d = document;
  w.dataLayer = w.dataLayer || [];
  function gtag() {
    w.dataLayer.push(arguments);
  }

  // ---- Consent Mode v2 : defaults (must run before GTM boot) ----
  // Regions that require prior opt-in (GDPR/UK GDPR/Switzerland).
  var OPT_IN_REGIONS = [
    "AT", "BE", "BG", "HR", "CY", "CZ", "DK", "EE", "FI", "FR", "DE",
    "GR", "HU", "IE", "IT", "LV", "LT", "LU", "MT", "NL", "PL", "PT",
    "RO", "SK", "SI", "ES", "SE", "IS", "LI", "NO", "GB", "CH"
  ];
  var DENIED = {
    ad_storage: "denied",
    ad_user_data: "denied",
    ad_personalization: "denied",
    analytics_storage: "denied"
  };
  var GRANTED = {
    ad_storage: "granted",
    ad_user_data: "granted",
    ad_personalization: "granted",
    analytics_storage: "granted"
  };
  // security_storage/functionality_storage stay granted (essential).
  gtag("consent", "default", assign({ region: OPT_IN_REGIONS, wait_for_update: 500 }, DENIED));
  gtag("consent", "default", assign({}, GRANTED)); // default for all other regions (US, etc.)

  // Apply a previously stored choice (overrides region default everywhere).
  var stored = readChoice();
  if (stored === "granted") gtag("consent", "update", assign({}, GRANTED));
  else if (stored === "denied") gtag("consent", "update", assign({}, DENIED));

  // ---- GTM install (Google's official snippet, inlined) ----
  (function (w, d, s, l, i) {
    w[l] = w[l] || [];
    w[l].push({ "gtm.start": new Date().getTime(), event: "gtm.js" });
    var f = d.getElementsByTagName(s)[0],
      j = d.createElement(s),
      dl = l !== "dataLayer" ? "&l=" + l : "";
    j.async = true;
    j.src = "https://www.googletagmanager.com/gtm.js?id=" + i + dl;
    f.parentNode.insertBefore(j, f);
  })(window, document, "script", "dataLayer", GTM_ID);

  // ---- semantic click events ----
  function push(event, extra) {
    w.dataLayer.push(assign({ event: event }, extra || {}));
  }
  d.addEventListener(
    "click",
    function (e) {
      var a = e.target.closest && e.target.closest("a");
      if (!a) return;
      var href = a.getAttribute("href") || "";
      if (href.indexOf("tel:") === 0) push("phone_click", { phone_number: href.slice(4) });
      else if (href.indexOf("mailto:") === 0) push("email_click", { email: href.slice(7) });
    },
    true
  );

  // Native <form> submit (if any page ever ships one).
  d.addEventListener(
    "submit",
    function (e) {
      var form = e.target;
      push("generate_lead", {
        form_id: (form && form.id) || "",
        form_name: (form && form.getAttribute("name")) || "",
        source: "native_form"
      });
    },
    true
  );

  // ---- GHL cross-origin lead capture ----
  var leadFired = false;
  function fireLead(source, extra) {
    if (leadFired) return; // de-dupe within a pageview
    leadFired = true;
    push("generate_lead", assign({ source: source || "ghl_form" }, extra || {}));
  }

  // (a) best-effort: listen for GoHighLevel/LeadConnector submit messages.
  //     Only fires on a clear submit signal — resize/height messages are ignored.
  w.addEventListener("message", function (e) {
    var o = e.origin || "";
    if (!/leadconnectorhq\.com|msgsndr\.com/.test(o)) return;
    var data = e.data;
    var text = typeof data === "string" ? data : "";
    if (data && typeof data === "object") {
      text = (data.type || data.event || data.action || data.eventName || "") + "";
    }
    if (/form[_-]?submit|formsubmit|submitted|onformsubmit|lead[_-]?captured|form_completed/i.test(text)) {
      fireLead("ghl_postmessage");
    }
  });

  // (b) reliable: a thank-you page fires the conversion on load.
  //     GHL form "On submit → Redirect" must point at /thank-you (or /gracias),
  //     or add data-abi-thankyou to any confirmation page.  <<EXTERNAL: set GHL redirect>>
  ready(function () {
    var p = location.pathname.replace(/\/+$/, "");
    if (/\/(thank-you|thankyou|gracias)$/i.test(p) || d.querySelector("[data-abi-thankyou]")) {
      fireLead("thank_you_page");
    }
  });

  // ---- Consent banner + manager ----
  function saveChoice(v) {
    try { localStorage.setItem(STORE_KEY, v); } catch (e) {}
  }
  function readChoice() {
    try { return localStorage.getItem(STORE_KEY); } catch (e) { return null; }
  }
  function applyConsent(v) {
    gtag("consent", "update", assign({}, v === "granted" ? GRANTED : DENIED));
    push(v === "granted" ? "consent_granted" : "consent_denied");
  }

  var BANNER_CSS =
    ".abi-consent{position:fixed;left:0;right:0;bottom:0;z-index:2147483000;" +
    "background:#0d1117;color:#f2f4f8;border-top:2px solid #1b2fd9;" +
    "box-shadow:0 -8px 30px rgba(0,0,0,.35);font-family:inherit;" +
    "padding:16px clamp(14px,4vw,40px);display:flex;gap:16px;align-items:center;" +
    "flex-wrap:wrap;justify-content:center}" +
    ".abi-consent[hidden]{display:none}" +
    ".abi-consent__txt{flex:1 1 320px;min-width:260px;font-size:13.5px;line-height:1.5;margin:0}" +
    ".abi-consent__txt a{color:#8ea2ff;text-decoration:underline}" +
    ".abi-consent__btns{display:flex;gap:10px;flex:0 0 auto;flex-wrap:wrap}" +
    ".abi-consent__btn{font:600 13.5px/1 inherit;padding:11px 20px;border-radius:8px;" +
    "border:1px solid transparent;cursor:pointer;white-space:nowrap}" +
    ".abi-consent__btn--accept{background:#1b2fd9;color:#fff}" +
    ".abi-consent__btn--accept:hover{background:#1626b0}" +
    ".abi-consent__btn--decline{background:transparent;color:#f2f4f8;border-color:#3a4152}" +
    ".abi-consent__btn--decline:hover{border-color:#8ea2ff}" +
    ".abi-consent__btn:focus-visible{outline:2px solid #8ea2ff;outline-offset:2px}" +
    "@media(max-width:560px){.abi-consent{flex-direction:column;align-items:stretch;text-align:center}" +
    ".abi-consent__btns{justify-content:center}.abi-consent__btn{flex:1 1 auto}}";

  function injectStyleOnce() {
    if (d.getElementById("abi-consent-css")) return;
    var st = d.createElement("style");
    st.id = "abi-consent-css";
    st.textContent = BANNER_CSS;
    (d.head || d.documentElement).appendChild(st);
  }

  function buildBanner() {
    injectStyleOnce();
    var bar = d.createElement("div");
    bar.className = "abi-consent";
    bar.setAttribute("role", "dialog");
    bar.setAttribute("aria-live", "polite");
    bar.setAttribute("aria-label", "Privacy & cookie consent");
    bar.innerHTML =
      '<p class="abi-consent__txt">We use cookies and similar tools for analytics and advertising ' +
      "(Google, Meta) to improve your experience and measure our ads. You can accept or decline. " +
      'See our <a href="/privacy-and-policy">Privacy Policy</a>.</p>' +
      '<div class="abi-consent__btns">' +
      '<button type="button" class="abi-consent__btn abi-consent__btn--decline" data-abi-consent="denied">Decline</button>' +
      '<button type="button" class="abi-consent__btn abi-consent__btn--accept" data-abi-consent="granted">Accept</button>' +
      "</div>";
    bar.addEventListener("click", function (e) {
      var b = e.target.closest && e.target.closest("[data-abi-consent]");
      if (!b) return;
      var v = b.getAttribute("data-abi-consent");
      saveChoice(v);
      applyConsent(v);
      bar.setAttribute("hidden", "");
    });
    (d.body || d.documentElement).appendChild(bar);
    return bar;
  }

  var bannerEl = null;
  function showBanner() {
    if (bannerEl) { bannerEl.removeAttribute("hidden"); return; }
    ready(function () { bannerEl = buildBanner(); });
  }

  // Public API — footer "Do Not Sell or Share" / cookie-settings link reopens it.
  w.abiConsent = {
    open: showBanner,
    accept: function () { saveChoice("granted"); applyConsent("granted"); if (bannerEl) bannerEl.setAttribute("hidden", ""); },
    decline: function () { saveChoice("denied"); applyConsent("denied"); if (bannerEl) bannerEl.setAttribute("hidden", ""); }
  };

  // Footer opt-out link → open the consent manager (falls back to /privacy-and-policy if JS off).
  d.addEventListener("click", function (e) {
    var el = e.target.closest && e.target.closest("[data-abi-privacy-choices]");
    if (!el) return;
    e.preventDefault();
    showBanner();
  });

  // Show the banner on first visit (no stored choice).
  if (!stored) showBanner();

  // ---- tiny helpers ----
  function assign(target) {
    for (var i = 1; i < arguments.length; i++) {
      var s = arguments[i];
      for (var k in s) if (Object.prototype.hasOwnProperty.call(s, k)) target[k] = s[k];
    }
    return target;
  }
  function ready(fn) {
    if (d.readyState === "loading") d.addEventListener("DOMContentLoaded", fn);
    else fn();
  }
})();
