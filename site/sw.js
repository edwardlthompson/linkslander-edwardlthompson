const CACHE_NAME = 'matrix-cache-v7';
const CSS_MODULES = [
  'css/modules/base.css',
  'css/modules/glass.css',
  'css/modules/identity.css',
  'css/modules/icons.css',
  'css/modules/responsive.css',
  'css/modules/animations.css',
];
const ASSETS = [
  './',
  'index.html',
  'word-connections.html',
  ...CSS_MODULES,
  'css/modules/language-roots.css',
  'js/matrix.js',
  'manifest.json',
  'browserconfig.xml',
  'robots.txt',
  'edward_lee_thompson_.vcf',
  'vendor/bootstrap-5.3.3/css/bootstrap.min.css',
  'vendor/bootstrap-5.3.3/js/bootstrap.bundle.min.js',
  'mstile-150x150.png',
  'ms-icon-70x70.png',
  'ms-icon-150x150.png',
  'ms-icon-310x310.png',
  'img/image01.jpg',
  'img/icon-192.png',
  'img/icon-512.png',
  'img/Telegram_Official.png',
  'img/WhatsApp_Official.png',
  'img/facebook-messenger-2020.svg',
  'img/Discord2.png',
  'img/Snapchat_Official.ico',
  'img/GV.webp',
  'img/Gmail.png',
  'img/Twitter_Official.png',
  'img/Instagram_Official.png',
  'img/Facebook_Official.png',
  'img/BeReal.webp',
  'img/TikTok_Official2.ico',
  'img/RedNote.png',
  'img/LinkedIn_Official.ico',
  'img/YouTube_Official.ico',
  'img/Steam.png',
  'img/IMDb.png',
  'img/UpWork.png',
  'img/GitHub_Logo.png',
  'img/heart_transparent.png',
  'img/IWWYV.jpg',
  'img/PayPal.png',
  'img/Venmo.png',
  'img/Bitcoin.webp',
  'img/Ethereum.png',
  'img/word-connections.png',
];

self.addEventListener('install', (e) => {
  e.waitUntil(
    caches.open(CACHE_NAME).then((cache) =>
      Promise.allSettled(ASSETS.map((url) => cache.add(url)))
    )
  );
});

self.addEventListener('activate', (e) => {
  e.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(keys.filter((k) => k !== CACHE_NAME).map((k) => caches.delete(k)))
    )
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
        .catch(() => caches.match(e.request))
    );
    return;
  }

  e.respondWith(
    caches.match(e.request).then((res) => res || fetch(e.request))
  );
});
