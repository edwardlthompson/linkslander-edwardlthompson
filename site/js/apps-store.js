(() => {
  const root = document.getElementById("apps-root");
  const modalEl = document.getElementById("apps-modal");
  if (!root || !modalEl || typeof bootstrap === "undefined") return;

  const modal = new bootstrap.Modal(modalEl);
  const titleEl = document.getElementById("apps-modal-title");
  const descEl = document.getElementById("apps-modal-desc");
  const platformsEl = document.getElementById("apps-modal-platforms");
  const forkEl = document.getElementById("apps-modal-fork");
  const primaryEl = document.getElementById("apps-modal-primary");
  const repoEl = document.getElementById("apps-modal-repo");
  let triggerEl = null;

  modalEl.addEventListener("hidden.bs.modal", () => {
    if (triggerEl && typeof triggerEl.focus === "function") triggerEl.focus();
    triggerEl = null;
  });

  function slug(text) {
    return String(text).toLowerCase().replace(/[^a-z0-9]+/g, "-");
  }

  function escapeHtml(value) {
    return String(value)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  function openApp(app, trigger) {
    if (modalEl.classList.contains("show")) return;
    triggerEl = trigger;
    titleEl.textContent = app.name;
    descEl.textContent = app.description;
    const chips = [app.category, ...(app.platforms || [])].filter(Boolean);
    platformsEl.innerHTML = chips
      .map((p) => `<span class="apps-chip">${escapeHtml(p)}</span>`)
      .join("");
    if (app.forkOf) {
      forkEl.hidden = false;
      forkEl.innerHTML = `Desktop client based on <a href="${escapeHtml(app.forkOf)}" target="_blank" rel="noopener noreferrer">upstream Google Messages for Desktop</a>.`;
    } else {
      forkEl.hidden = true;
      forkEl.textContent = "";
    }
    repoEl.href = app.repoUrl;
    if (app.releaseStatus === "available") {
      primaryEl.hidden = false;
      primaryEl.href = app.releasesUrl;
      primaryEl.textContent = "View releases";
    } else {
      primaryEl.hidden = true;
      primaryEl.removeAttribute("href");
    }
    modal.show();
  }

  function tileHtml(app) {
    return `<button type="button" class="apps-tile" data-app-id="${escapeHtml(app.id)}" aria-haspopup="dialog" aria-controls="apps-modal">
      <span class="apps-tile-logo"><img src="${escapeHtml(app.logo)}" alt="" loading="lazy" width="64" height="64"></span>
      <span class="apps-tile-tag">${escapeHtml(app.category)}</span>
      <span class="apps-tile-name">${escapeHtml(app.name)}</span>
      <span class="apps-tile-tagline">${escapeHtml(app.tagline)}</span>
    </button>`;
  }

  function render(catalog) {
    const apps = catalog.apps || [];
    const groupOrder = catalog.groupOrder || [];
    const categoryOrder = catalog.categoryOrder || {};
    const byGroup = new Map();
    for (const app of apps) {
      if (!app.name || !app.tagline) continue;
      if (!byGroup.has(app.group)) byGroup.set(app.group, []);
      byGroup.get(app.group).push(app);
    }

    const nav = groupOrder
      .filter((g) => byGroup.has(g))
      .map((g) => `<a href="#group-${slug(g)}">${escapeHtml(g)}</a>`)
      .join("");

    let body = `<nav class="apps-jump" aria-label="App groups">${nav}</nav>`;
    for (const group of groupOrder) {
      const list = byGroup.get(group);
      if (!list || !list.length) continue;
      const order = categoryOrder[group] || [];
      list.sort((a, b) => {
        const ai = order.indexOf(a.category);
        const bi = order.indexOf(b.category);
        const ax = ai === -1 ? 999 : ai;
        const bx = bi === -1 ? 999 : bi;
        if (ax !== bx) return ax - bx;
        return String(a.name).localeCompare(String(b.name));
      });
      body += `<section class="apps-group" id="group-${slug(group)}">`;
      body += `<h2 class="apps-group-title matrix-header">${escapeHtml(group)}</h2>`;
      body += `<div class="apps-grid">${list.map(tileHtml).join("")}</div>`;
      body += `</section>`;
    }
    root.innerHTML = body;

    const byId = new Map(apps.map((a) => [a.id, a]));
    root.querySelectorAll(".apps-tile").forEach((btn) => {
      btn.addEventListener("click", () => {
        const app = byId.get(btn.getAttribute("data-app-id"));
        if (app) openApp(app, btn);
      });
    });
  }

  fetch("js/apps-catalog.json")
    .then((res) => {
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      return res.json();
    })
    .then(render)
    .catch(() => {
      root.innerHTML = `<p class="apps-error" role="alert">Could not load catalog.</p>`;
    });
})();
