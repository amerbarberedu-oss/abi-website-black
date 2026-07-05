/* ============================================================
   ABI — Analytics loader
   ------------------------------------------------------------
   ONE dependency: Google Tag Manager container GTM-NKLLGPC.
   Everything else (GA4 G-J6BNX36TS3, Meta Pixel 580471737041846,
   Microsoft Clarity k5fxn2irko, CallRail company 169987046,
   ClickCease, Google Ads AW-949292069 when configured) is managed
   inside the GTM web UI at tagmanager.google.com — never touch
   this file to add/remove/tweak tags.

   This file only:
     1. Boots the GTM container on every page.
     2. Pushes semantic custom events into dataLayer that the
        GTM tags listen for:
          - "phone_click"    → GA4 phone-click conversion
          - "generate_lead"  → GA4 lead conversion
        (Trigger names inside GTM: "CE - phone_click", "CE - generate_lead")
   ============================================================ */
(function () {
  var GTM_ID = "GTM-NKLLGPC";

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

  // ---- Custom events wired to existing GTM triggers ----
  function push(event, extra) {
    window.dataLayer.push(Object.assign({ event: event }, extra || {}));
  }

  document.addEventListener(
    "click",
    function (e) {
      var a = e.target.closest && e.target.closest("a");
      if (!a) return;
      var href = a.getAttribute("href") || "";
      if (href.indexOf("tel:") === 0) {
        push("phone_click", { phone_number: href.slice(4) });
      } else if (href.indexOf("mailto:") === 0) {
        push("email_click", { email: href.slice(7) });
      }
    },
    true
  );

  // Any native <form> submit counts as a lead. GHL iframe forms
  // won't reach this listener — those need a GHL webhook / thank-you
  // page dataLayer push to be measured.
  document.addEventListener(
    "submit",
    function (e) {
      var form = e.target;
      var id = (form && form.id) || "";
      var name = (form && form.getAttribute("name")) || "";
      push("generate_lead", { form_id: id, form_name: name, source: "native_form" });
    },
    true
  );
})();
