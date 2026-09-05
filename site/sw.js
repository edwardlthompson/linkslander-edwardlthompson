const CACHE_NAME = 'matrix-cache-v9';
const ASSETS = [
  './',
  'index.html',
  'word-connections.html',
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
  'css/modules/responsive.css',
  'js/matrix.js',
  'js/contacts-crypto.js',
  'js/contacts-gate.js',
  'js/contacts.payload.json',
  'vendor/bootstrap-5.3.3/css/bootstrap.min.css',
  'vendor/bootstrap-5.3.3/js/bootstrap.bundle.min.js',
  'img/Bitcoin.webp',
  'img/Ethereum.png',
  'img/GitHub_Logo.png',
  'img/IMDb.png',
  'img/IWWYV.jpg',
  'img/PayPal.png',
  'img/Steam.png',
  'img/UpWork.png',
  'img/Venmo.png',
  'img/YouTube_Official.ico',
  'img/heart_transparent.png',
  'img/word-connections.png',
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
