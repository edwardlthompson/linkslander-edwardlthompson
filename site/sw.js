const CACHE_NAME = 'matrix-cache-v42';
const ASSETS = [
  './',
  'index.html',
  'word-connections.html',
  'apps.html',
  'manifest.json',
  'browserconfig.xml',
  'robots.txt',
  'mstile-150x150.png',
  'ms-icon-70x70.png',
  'ms-icon-150x150.png',
  'ms-icon-310x310.png',
  'img/icon-192.png',
  'img/icon-512.png',
  'img/p.jpg',
  'css/modules/animations.css',
  'css/modules/base.css',
  'css/modules/glass.css',
  'css/modules/icons.css',
  'css/modules/identity.css',
  'css/modules/language-roots.css',
  'css/modules/apps-store.css',
  'css/modules/responsive.css',
  'js/matrix.js',
  'js/contacts-crypto.js',
  'js/contacts-gate.js',
  'js/contacts.payload.json',
  'js/apps-catalog.json',
  'js/apps-store.js',
  'vendor/bootstrap-5.3.3/css/bootstrap.min.css',
  'vendor/bootstrap-5.3.3/js/bootstrap.bundle.min.js',
  'img/brands/call.svg',
  'img/brands/iwwyv.svg',
  'img/brands/ihprt.svg',
  'img/word-connections.png',
  'img/brands/telegram.svg',
  'img/brands/whatsapp.svg',
  'img/brands/messenger.svg',
  'img/brands/discord.svg',
  'img/brands/snapchat.svg',
  'img/brands/gmail.svg',
  'img/brands/x.svg',
  'img/brands/instagram.svg',
  'img/brands/facebook.svg',
  'img/brands/bereal.svg',
  'img/brands/tiktok.svg',
  'img/brands/xiaohongshu.svg',
  'img/brands/linkedin.svg',
  'img/brands/youtube.svg',
  'img/brands/steam.svg',
  'img/brands/imdb.svg',
  'img/brands/upwork.svg',
  'img/brands/github.svg',
  'img/brands/paypal.svg',
  'img/brands/venmo.svg',
  'img/brands/bitcoin.svg',
  'img/brands/ethereum.svg',
  'img/brands/tripadvisor.svg',
  'img/brands/words.svg',
  'img/brands/apps.svg',
  'img/apps/3d-game-optimizer.svg',
  'img/apps/AstroAlarm.svg',
  'img/apps/DevPulse.svg',
  'img/apps/ExpeditionGauge.png',
  'img/apps/Google-Messages-For-Desktop.svg',
  'img/apps/HermesLauncher.png',
  'img/apps/JanusBoot.svg',
  'img/apps/MultiAppShare-.png',
  'img/apps/OBDForge.png',
  'img/apps/OpenShouter.png',
  'img/apps/QRaft.svg',
  'img/apps/QuickMediaIngest.png',
  'img/apps/SyncMark.png',
  'img/apps/aetherfeed.svg',
  'img/apps/agent-project-bootstrap.svg',
  'img/apps/chromaflow.svg',
  'img/apps/continuum-calendar.png',
  'img/apps/hover-icons.svg',
  'img/apps/linear-trend-spotter.svg',
  'img/apps/point-and-shoot.png',
  'img/apps/screen-wakelock-detector.png',
  'img/apps/selfchronicle.png',
  'img/apps/starrupture-city-planner.svg',
  'img/apps/takein-sms.svg',
  'img/apps/trendalgo-bot.svg',
  'img/apps/vault-organizer.svg',
];

self.addEventListener('install', (e) => {
  e.waitUntil(
    caches.open(CACHE_NAME).then((cache) =>
      Promise.allSettled(ASSETS.map((url) => cache.add(url)))
    ).then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', (e) => {
  e.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(keys.filter((k) => k !== CACHE_NAME).map((k) => caches.delete(k)))
    ).then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (e) => {
  if (e.request.mode === 'navigate') {
    e.respondWith(
      fetch(e.request)
        .then((res) => {
          const copy = res.clone();
          caches.open(CACHE_NAME).then((cache) => cache.put(e.request, copy));
          return res;
        })
        .catch(async () => {
          const cached = await caches.match(e.request);
          if (cached) return cached;
          const path = new URL(e.request.url).pathname.replace(/^\//, '') || 'index.html';
          return caches.match(path) || caches.match('./');
        })
    );
    return;
  }

  e.respondWith(
    caches.match(e.request).then((res) => res || fetch(e.request))
  );
});
