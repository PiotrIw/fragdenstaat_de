window.addEventListener("message", (e) => {
  if (e.origin !== "https://okfde.github.io" && e.origin !== "http://127.0.0.1:8001") { return; }
  if (e.data[0] !== "setIframeHeight") { return; }
  const iframeId = e.data[1];
  const iframe = document.getElementById(iframeId);
  if (iframe !== null) {
    iframe.style.height = e.data[2] + "px";
  }
}, false);

window.document.addEventListener("securitypolicyviolation", (e) => {
  if (e.violatedDirective.indexOf("script") !== -1 && e.blockedURI.indexOf("https://data1.") !== -1) {
    window.alert(`Liebe/r Nutzer/in,\noffenbar versucht eine Ihrer Browser-Erweiterungen Sie vermutlich ohne
    Ihre Kenntnis zu tracken.
    \n\nWir raten Ihnen Browser-Erweiterungen zu deinstallieren, die Sie nicht nutzen.`);
  }
});

const pauseModalVideo = function (this: HTMLVideoElement) {
  const video = this.querySelector('video')
  if (video) {
    video.pause()
  }
}

const videoModals = document.querySelectorAll('[data-modal="video"]')
Array.from(videoModals).forEach((videoModal) => {
  videoModal.addEventListener('hidden.bs.modal', pauseModalVideo)
})

let referenceData: undefined | any

function getReferenceData () {
  if (referenceData) {
    return referenceData
  }
  if (!URLSearchParams) {
    return {}
  }
  let urlParams = new URLSearchParams(window.location.search);
  let reference = urlParams.get('pk_campaign') || ''
  let keyword = urlParams.get('pk_keyword') || document.referrer || document.location.href
  referenceData = {
    reference, keyword
  }
  return referenceData
}
const formsWithReference = document.querySelectorAll('form[data-reference]')
Array.from(formsWithReference).forEach(form => {
  let referenceData = getReferenceData()
  for (let key in referenceData) {
    const input = document.createElement('input')
    input.type = 'hidden'
    input.name = key
    input.value = referenceData[key]
    form.appendChild(input)
  }
})

if (document.body.dataset.user) {
  const userFillInputs = document.querySelectorAll('form[data-userfill] input');
  (Array.from(userFillInputs) as HTMLInputElement[]).forEach(input => {
    let name = input.name
    let val = document.body.dataset[`user${name}`]
    if (val) {
      input.value = val
    }
  })
}

// tslint:disable-next-line: interface-name
interface Window { _paq: Array<Array<string | string[]>>; }

const MATOMO_DOMAIN = "https://traffic.okfn.de";

window._paq = window._paq || [];
window._paq.push(["trackPageView"]);
window._paq.push(["enableLinkTracking"]);
window._paq.push(["setDomains", ["*.fragdenstaat.de"]]);
window._paq.push(["setTrackerUrl", `${MATOMO_DOMAIN}/matomo.php`]);
window._paq.push(['disableCookies']);
window._paq.push(["setSiteId", "25"]);

if (document.location.hostname.indexOf(".onion") !== -1) {
  // document.body.classList.add("darkmode");
  document.body.classList.add("onion-site");
  const root = document.getElementsByTagName("html")[0];
  root.setAttribute("class", "darkmode");
} else {
  const script = document.createElement("script");
  script.type = "text/javascript";
  script.async = true;
  script.defer = true;
  script.src = `${MATOMO_DOMAIN}/matomo.js`;
  document.body.appendChild(script);
}
