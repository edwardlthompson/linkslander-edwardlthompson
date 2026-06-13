const CACHE_NAME = 'matrix-cache-v3';
const ASSETS = [
  'index.html',
  'css/style.css',
  'js/matrix.js',
  'manifest.json',
  'edward_lee_thompson_.vcf',
  'img/image01.jpg',
  'img/icon-192.png',
  'img/icon-512.png',
  'img/facebook-messenger-2020.svg',
];

self.addEventListener('install', (e) => {
  e.waitUntil(caches.open(CACHE_NAME).then((cache) => cache.addAll(ASSETS)));
});

self.addEventListener('activate', (e) => {
  e.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(keys.filter((k) => k !== CACHE_NAME).map((k) => caches.delete(k)))
    )
  );
});

self.addEventListener('fetch', (e) => {
  e.respondWith(caches.match(e.request).then((res) => res || fetch(e.request)));
});
