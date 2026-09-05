/** Single-flight unlock gate for private contacts (#MyContacts). */
(function () {
  const PHRASE = "MyContacts";
  const HASH = "#MyContacts";
  const SESSION_KEY = "linkslander.contacts.phrase";
  const PAYLOAD_URL = "js/contacts.payload.json";

  let unlocked = false;
  let unlockInFlight = null;
  let payloadCache = null;
  let objectUrl = null;

  const lockEl = () => document.getElementById("contacts-lock");
  const rootEl = () => document.getElementById("private-contacts-root");
  const formEl = () => document.getElementById("contacts-unlock-form");
  const inputEl = () => document.getElementById("contacts-phrase");
  const errorEl = () => document.getElementById("contacts-unlock-error");

  function setError(message) {
    const err = errorEl();
    const input = inputEl();
    if (!err || !input) return;
    if (!message) {
      err.hidden = true;
      err.textContent = "";
      input.removeAttribute("aria-invalid");
      return;
    }
    err.hidden = false;
    err.textContent = message;
    input.setAttribute("aria-invalid", "true");
    input.focus();
  }

  function clearMount() {
    const root = rootEl();
    if (root) {
      root.innerHTML = "";
      root.hidden = true;
    }
  }

  function showLock() {
    const lock = lockEl();
    if (lock) lock.hidden = false;
  }

  function hideLock() {
    const lock = lockEl();
    if (lock) lock.hidden = true;
  }

  async function loadPayload() {
    if (payloadCache) return payloadCache;
    const res = await fetch(PAYLOAD_URL, { cache: "no-cache" });
    if (!res.ok) throw new Error("Missing contacts payload");
    const data = await res.json();
    ContactsCrypto.assertPayload(data);
    payloadCache = data;
    return data;
  }

  function initTooltips(scope) {
    if (typeof bootstrap === "undefined" || !bootstrap.Tooltip) return;
    scope.querySelectorAll('[data-bs-toggle="tooltip"]').forEach((el) => {
      bootstrap.Tooltip.getOrCreateInstance(el);
    });
  }

  function wireVcardDownload(scope) {
    const btn = scope.querySelector("#download-contact-card");
    if (!btn) return;
    btn.addEventListener("click", () => {
      const b64 = btn.getAttribute("data-vcf-b64");
      if (!b64) return;
      const bytes = ContactsCrypto.b64ToBytes(b64);
      const blob = new Blob([bytes], { type: "text/vcard" });
      if (objectUrl) URL.revokeObjectURL(objectUrl);
      objectUrl = URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = objectUrl;
      a.download = "edward-lee-thompson.vcf";
      document.body.appendChild(a);
      a.click();
      a.remove();
    });
  }

  function injectHtml(html) {
    const root = rootEl();
    if (!root) throw new Error("Missing private contacts root");
    const doc = new DOMParser().parseFromString(html, "text/html");
    root.replaceChildren(...Array.from(doc.body.childNodes));
    root.hidden = false;
    hideLock();
    initTooltips(root);
    wireVcardDownload(root);
  }

  async function unlock(phrase) {
    if (unlocked) return true;
    if (unlockInFlight) return unlockInFlight;

    unlockInFlight = (async () => {
      try {
        if (!phrase || !String(phrase).trim()) {
          setError("Enter the access phrase");
          clearMount();
          showLock();
          return false;
        }
        const payload = await loadPayload();
        const html = await ContactsCrypto.decryptContacts(
          payload,
          String(phrase).trim()
        );
        injectHtml(html);
        sessionStorage.setItem(SESSION_KEY, String(phrase).trim());
        if (location.hash !== HASH) {
          history.replaceState(null, "", HASH);
        }
        setError("");
        unlocked = true;
        return true;
      } catch (err) {
        console.warn("contacts unlock failed", err);
        clearMount();
        showLock();
        setError("That phrase did not work");
        return false;
      } finally {
        unlockInFlight = null;
      }
    })();

    return unlockInFlight;
  }

  function phraseFromHash() {
    if (location.hash === HASH) return PHRASE;
    return "";
  }

  function boot() {
    const form = formEl();
    if (form) {
      form.addEventListener("submit", (e) => {
        e.preventDefault();
        unlock(inputEl()?.value || "");
      });
    }

    window.addEventListener("hashchange", () => {
      const fromHash = phraseFromHash();
      if (fromHash) unlock(fromHash);
    });

    window.addEventListener("pagehide", () => {
      if (objectUrl) URL.revokeObjectURL(objectUrl);
    });

    const initial = phraseFromHash() || sessionStorage.getItem(SESSION_KEY) || "";
    if (initial) unlock(initial);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();
