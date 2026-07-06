(function(){
var MN_PHONES={
  topbar:[
    {flag:"EN",label:"Call Admissions",num:"(212) 290-2289",tel:"+12122902289"},
    {flag:"ES",label:"En Español",num:"(212) 290-0278",tel:"+12122900278"}
  ],
  mhx:[
    {num:"(212) 290-2289",lab:"ENGLISH",tel:"+12122902289",icon:"phone"},
    {num:"(856) 316-1551",lab:"HAIRCUT",tel:"+18563161551",icon:"scissors"},
    {num:"(212) 290-0278",lab:"SPANISH",tel:"+12122900278",icon:"phone"}
  ],
  footer:[
    {text:"(212) 290-2289 · English",tel:"+12122902289"},
    {text:"(212) 290-0278 · Español",tel:"+12122900278"},
    {text:"(718) 676-0640 · Bronx",tel:"+17186760640"}
  ],
  mbar:{call:"+12122902289",text:"+12122902289"}
};

var BX_PHONES={
  topbar:[
    {flag:"BX",label:"Call Admissions",num:"(718) 676-0640",tel:"+17186760640"},
    {flag:"✂",label:"Book a Haircut",num:"(856) 316-1551",tel:"+18563161551"}
  ],
  mhx:[
    {num:"(718) 676-0640",lab:"BRONX",tel:"+17186760640",icon:"phone"},
    {num:"(856) 316-1551",lab:"HAIRCUT",tel:"+18563161551",icon:"scissors"}
  ],
  footer:[
    {text:"(718) 676-0640 · Bronx Admissions",tel:"+17186760640"},
    {text:"(856) 316-1551 · Book a Haircut",tel:"+18563161551"}
  ],
  mbar:{call:"+17186760640",text:"+17186760640"}
};

var PHONE_SVG='<svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.8 19.8 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.08 4.18 2 2 0 0 1 4.06 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.22a2 2 0 0 1 2.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/></svg>';
var SCISSORS_SVG='<svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="6" cy="6" r="3"/><circle cx="6" cy="18" r="3"/><path d="M20 4 8.12 15.88"/><path d="M14.47 14.48 20 20"/><path d="M8.12 8.12 12 12"/></svg>';

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

function applyBronx(){
  document.body.classList.add("bx-gold");
  updateLocToggle("bronx");
  swapPhones(BX_PHONES);
  rewriteProgramsLinks("bronx");
}
function applyManhattan(){
  document.body.classList.remove("bx-gold");
  updateLocToggle("manhattan");
  swapPhones(MN_PHONES);
  rewriteProgramsLinks("manhattan");
}

// Rewrite any "Programs" nav link (points at the general /programs/ or /programs/index.html)
// to the campus-specific programs page. Handles EN + ES paths, absolute + relative hrefs.
// Runs on every campus switch AND on init, so a Manhattan-context visitor always sees the
// Manhattan programs page, and Bronx-context sees the Bronx programs page.
function rewriteProgramsLinks(campus){
  var target=campus==="bronx"?"bronx.html":"manhattan.html";
  // Selectors: any anchor whose text is "Programs"/"Programas" OR whose href points at the
  // general programs index. Skip anchors already pointing at a specific /programs/* sub-page
  // (like /programs/500-hour-master-barber) so we don't stomp on those.
  var links=document.querySelectorAll('a[href]');
  links.forEach(function(a){
    var href=a.getAttribute("href")||"";
    var raw=href.split("?")[0].split("#")[0];
    // Match paths ending in /programs, /programs/, /programs/index.html
    // (both root-absolute and relative forms)
    if(/(^|\/)programs\/?(index\.html)?$/.test(raw)){
      // ES vs EN
      var isEs=/\/es\/programs/.test(raw)||/^es\/programs/.test(raw)||document.documentElement.lang==="es"||/\/es\//.test(location.pathname);
      var base=raw.replace(/(index\.html)?$/, "").replace(/\/$/, "");
      var newHref=base+"/"+target;
      // If original was root-absolute or contains full path, preserve leading slash
      if(href.charAt(0)==="/"&&newHref.charAt(0)!=="/") newHref="/"+newHref;
      a.setAttribute("href", newHref);
      a.setAttribute("data-abi-programs-rewritten", campus);
    }
  });
}

function updateLocToggle(campus){
  var toggle=document.querySelector(".loc-toggle");
  if(!toggle) return;
  var links=toggle.querySelectorAll("a");
  links.forEach(function(a){
    var isMN=a.textContent.trim()==="MN";
    var isBX=a.textContent.trim()==="BX";
    if((campus==="manhattan"&&isMN)||(campus==="bronx"&&isBX)){
      a.classList.add("is-active");
      a.setAttribute("aria-current","true");
    }else{
      a.classList.remove("is-active");
      a.removeAttribute("aria-current");
    }
  });
}

function swapPhones(data){
  var tb=document.querySelector(".tb-calls");
  if(tb){
    tb.innerHTML=data.topbar.map(function(p){
      return '<a class="tb-call" href="tel:'+p.tel+'"><b class="tb-flag">'+p.flag+'</b><span class="tb-label">'+p.label+'</span><span class="tb-num">'+p.num+'</span></a>';
    }).join("");
  }

  var mhx=document.querySelector(".mhx-phones");
  if(mhx){
    mhx.innerHTML=data.mhx.map(function(p){
      var svg=p.icon==="scissors"?SCISSORS_SVG:PHONE_SVG;
      return '<a class="mhx-phone" href="tel:'+p.tel+'"><span class="mhx-num">'+p.num+'</span><span class="mhx-lab">'+svg+p.lab+'</span></a>';
    }).join("\n");
  }

  var ftrVisit=document.querySelector(".ftr-grid");
  if(ftrVisit){
    var divs=ftrVisit.querySelectorAll("div");
    divs.forEach(function(d){
      var h4=d.querySelector("h4");
      if(h4&&h4.textContent.trim()==="Visit Us"){
        var phoneLinks=d.querySelectorAll('a[href^="tel:"]');
        phoneLinks.forEach(function(a){a.remove();});
        var emailLink=d.querySelector('a[href^="mailto:"]');
        data.footer.forEach(function(p){
          var a=document.createElement("a");
          a.href="tel:"+p.tel;
          a.textContent=p.text;
          if(emailLink) d.insertBefore(a,emailLink);
          else d.appendChild(a);
        });
      }
    });
  }

  var mbarCall=document.querySelector(".mbar-call");
  var mbarText=document.querySelector(".mbar-text");
  if(mbarCall) mbarCall.href="tel:"+data.mbar.call;
  if(mbarText) mbarText.href="sms:"+data.mbar.text;
}

function init(){
  // Programs pages are campus-specific: visiting one sets that campus preference.
  if(isBronxProgramsPage()){setCampus("bronx");}
  else if(isManhattanProgramsPage()){setCampus("manhattan");}

  if(isBronxPage()){
    setCampus("bronx");
    rewriteProgramsLinks("bronx");
    return;
  }
  var campus=getCampus();
  if(campus==="bronx") applyBronx();
  else rewriteProgramsLinks("manhattan");

  document.addEventListener("click",function(e){
    var a=e.target.closest(".loc-toggle a");
    if(!a) return;
    e.preventDefault();
    var txt=a.textContent.trim();
    // If we're on a programs page, toggling campus takes the user to the OTHER campus's
    // programs page — not the campus home. This is what "Manhattan/Bronx programs stay
    // synced to campus toggle" means.
    var here=location.pathname;
    var esPrefix=/\/es\//.test(here)?"/es":"";
    if(txt==="BX"){
      setCampus("bronx");
      if(isProgramsPage()){
        window.location.href=esPrefix+"/programs/bronx.html";
      }else if(a.href&&a.href.indexOf("/bronx")!==-1){
        window.location.href=a.href;
      }else{
        applyBronx();
      }
    }else if(txt==="MN"){
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
