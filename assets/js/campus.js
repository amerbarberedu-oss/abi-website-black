/**
 * campus.js — ABI Campus Switcher (v5)
 * ════════════════════════════════════
 * Manages Manhattan ↔ Bronx campus switching across the entire site.
 *
 * ARCHITECTURE:
 *   - HTML phone links use data-campus-phone, data-mn-*, data-bx-* attributes
 *   - Manhattan-only elements (ES phone links) use data-mn-only (hidden on Bronx)
 *   - body.bx-gold CSS class toggles the gold theme for Bronx
 *   - Campus preference is stored in localStorage("abi-campus")
 *
 * PHONE NUMBERS:
 *   Manhattan: EN (212) 290-2289 | ES (212) 290-0278 | Haircut (856) 316-1551
 *   Bronx:    (718) 676-0640 (single number) | Haircut (856) 316-1551
 *
 * Modified: July 2026 — Kazi
 */
(function(){

/* ── Campus phone config (only mbar hrefs needed; topbar/MHX/footer use data attrs) ── */
var MN_PHONES={mbar:{call:"+12122902289",text:"+12122902289"}};
var BX_PHONES={mbar:{call:"+17186760640",text:"+17186760640"}};

/* ── Page detection helpers ── */
function isBronxPage(){return document.body.classList.contains("bx-gold")}
function isProgramsPage(){var p=location.pathname;return /\/programs\//.test(p)||/\/programs$/.test(p);}
function isBronxProgramsPage(){var p=location.pathname;return /\/programs\/bronx(\.html)?$/.test(p)||/\/500-hour-master-barber-bronx/.test(p);}
function isManhattanProgramsPage(){var p=location.pathname;return /\/programs\/manhattan(\.html)?$/.test(p)||(/\/programs\/500-hour-master-barber(\.html)?$/.test(p))||/\/50-hour-barber-refresher/.test(p);}

function getCampus(){
  if(isBronxPage()) return "bronx";
  if(isBronxProgramsPage()) return "bronx";
  if(isManhattanProgramsPage()) return "manhattan";
  try{return localStorage.getItem("abi-campus")||"manhattan";}catch(e){return "manhattan";}
}
function setCampus(c){try{localStorage.setItem("abi-campus",c);}catch(e){}}

/* ── Smooth crossfade overlay for campus transitions ── */
function withFade(applyFn,campus){
  var bg=campus==="bronx"?"#1a1400":"#0c1020";
  var ov=document.createElement("div");
  ov.style.cssText="position:fixed;inset:0;z-index:9999;background:"+bg+";opacity:0;pointer-events:none;transition:opacity .28s ease";
  document.body.appendChild(ov);
  ov.offsetWidth; // force reflow
  ov.style.opacity="1";
  setTimeout(function(){
    applyFn();
    ov.style.opacity="0";
    ov.addEventListener("transitionend",function(){ov.remove();});
    setTimeout(function(){if(ov.parentNode) ov.remove();},600); // safety cleanup
  },300);
}

/* ── Apply campus theme + phones + nav links ── */
function _applyBronx(){
  document.body.classList.add("bx-gold");
  updateLocToggle("bronx");
  swapPhones(BX_PHONES);
  rewriteProgramsLinks("bronx");
}
function _applyManhattan(){
  document.body.classList.remove("bx-gold");
  updateLocToggle("manhattan");
  swapPhones(MN_PHONES);
  rewriteProgramsLinks("manhattan");
}
function applyBronx(){ withFade(_applyBronx,"bronx"); }
function applyManhattan(){ withFade(_applyManhattan,"manhattan"); }

/**
 * rewriteProgramsLinks — Rewrites /programs/ nav links to campus-specific pages.
 * e.g. /programs/ → /programs/manhattan.html or /programs/bronx.html
 */
function rewriteProgramsLinks(campus){
  var target=campus==="bronx"?"bronx.html":"manhattan.html";
  document.querySelectorAll('a[href]').forEach(function(a){
    var href=a.getAttribute("href")||"";
    var raw=href.split("?")[0].split("#")[0];
    if(/(^|\/)programs\/?(index\.html)?$/.test(raw)){
      var base=raw.replace(/(index\.html)?$/, "").replace(/\/$/, "");
      var newHref=base+"/"+target;
      if(href.charAt(0)==="/"&&newHref.charAt(0)!=="/") newHref="/"+newHref;
      a.setAttribute("href", newHref);
      a.setAttribute("data-abi-programs-rewritten", campus);
    }
  });
}

/**
 * updateLocToggle — Highlights the active campus tab in the loc-toggle pill.
 */
function updateLocToggle(campus){
  var toggle=document.querySelector(".loc-toggle");
  if(!toggle) return;
  toggle.querySelectorAll("a").forEach(function(a){
    var t=a.textContent.trim().toLowerCase();
    var isMN=(t==="mn"||t==="manhattan");
    var isBX=(t==="bx"||t==="bronx");
    if((campus==="manhattan"&&isMN)||(campus==="bronx"&&isBX)){
      a.classList.add("is-active");
      a.setAttribute("aria-current","true");
    }else{
      a.classList.remove("is-active");
      a.removeAttribute("aria-current");
    }
  });
}

/**
 * swapPhones — Updates all phone numbers, labels, and visibility for the active campus.
 *
 * How it works:
 *   1. Elements with [data-mn-only] are hidden when Bronx is active (ES phone links).
 *      Bronx has only 1 admissions number, so the ES duplicate is removed.
 *   2. Elements with [data-campus-phone] get their href and visible text updated
 *      from data-mn-* or data-bx-* attributes.
 *   3. Topbar flag text (EN ↔ BX) is updated via data-mn-flag / data-bx-flag.
 *   4. MHX label text (ENGLISH ↔ BRONX) is updated via data-mn-lab / data-bx-lab.
 *   5. Call sheet language label (English ↔ Bronx) via data-mn-cs-lang / data-bx-cs-lang.
 *   6. Mobile bottom bar call/text hrefs are updated.
 */
function swapPhones(data){
  var isBx=(data===BX_PHONES);
  var campus=isBx?"bx":"mn";

  /* 1. Show/hide Manhattan-only elements */
  document.querySelectorAll("[data-mn-only]").forEach(function(el){
    el.style.display=isBx?"none":"";
  });

  /* 2-5. Update phone links: href, number text, flag, label */
  document.querySelectorAll("[data-campus-phone]").forEach(function(el){
    var href=el.getAttribute("data-"+campus+"-href");
    var num=el.getAttribute("data-"+campus+"-num");
    if(href) el.href=href;
    if(num){
      var numEl=el.querySelector(".tb-num,.mhx-num,.cs-num");
      if(numEl) numEl.textContent=num;
      else if(!el.querySelector("span")&&!el.querySelector("b")) el.textContent=num;
    }
    /* Topbar flag (EN ↔ BX) */
    var flag=el.getAttribute("data-"+campus+"-flag");
    if(flag){var flagEl=el.querySelector(".tb-flag"); if(flagEl) flagEl.textContent=flag;}
    /* MHX label (ENGLISH ↔ BRONX) */
    var lab=el.getAttribute("data-"+campus+"-lab");
    if(lab){var labEl=el.querySelector(".mhx-lab-text"); if(labEl) labEl.textContent=lab;}
    /* Call sheet label (English ↔ Bronx) */
    var csLang=el.getAttribute("data-"+campus+"-cs-lang");
    if(csLang){var csEl=el.querySelector(".cs-lang"); if(csEl) csEl.textContent=csLang;}
  });

  /* 6. Mobile bottom bar */
  var mbarCall=document.querySelector(".mbar-call");
  var mbarText=document.querySelector(".mbar-text");
  if(mbarCall) mbarCall.href="tel:"+data.mbar.call;
  if(mbarText) mbarText.href="sms:"+data.mbar.text;
}

/**
 * init — Runs on DOMContentLoaded.
 * Sets campus preference and applies correct phone numbers + theme.
 */
function init(){
  /* Programs pages auto-set campus preference */
  if(isBronxProgramsPage()){setCampus("bronx");}
  else if(isManhattanProgramsPage()){setCampus("manhattan");}

  /* Apply campus on page load */
  if(isBronxPage()){
    setCampus("bronx");
    swapPhones(BX_PHONES);
    rewriteProgramsLinks("bronx");
  } else {
    var campus=getCampus();
    if(campus==="bronx") _applyBronx();
    else {
      swapPhones(MN_PHONES);
      rewriteProgramsLinks("manhattan");
    }
  }

  /* Campus toggle click handler */
  document.addEventListener("click",function(e){
    var a=e.target.closest(".loc-toggle a");
    if(!a) return;
    e.preventDefault();
    var txt=a.textContent.trim().toLowerCase();
    var here=location.pathname;
    var esPrefix=/\/es\//.test(here)?"/es":"";

    if(txt==="bronx"||txt==="bx"){
      setCampus("bronx");
      if(isProgramsPage()){
        window.location.href=esPrefix+"/programs/bronx.html";
      }else if(a.href&&a.href.indexOf("/bronx")!==-1){
        window.location.href=a.href;
      }else{
        applyBronx();
      }
    }else if(txt==="manhattan"||txt==="mn"){
      setCampus("manhattan");
      if(isProgramsPage()){
        window.location.href=esPrefix+"/programs/manhattan.html";
      }else if(here==="/bronx"||here==="/bronx.html"||here==="/es/bronx"||here==="/es/bronx.html"){
        window.location.href=esPrefix+"/";
      }else{
        applyManhattan();
      }
    }
  });
}

if(document.readyState==="loading") document.addEventListener("DOMContentLoaded",init);
else init();
})();
