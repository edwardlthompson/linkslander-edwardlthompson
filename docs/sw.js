const CACHE_NAME = 'matrix-cache-v2';
const ASSETS = [
  'index.html',
  'css/style.css',
  'js/matrix.js',
  'manifest.json',
  'img/profile.jpg',
  'img/icon-192.png',
  'img/icon-512.png'
];

self.addEventListener('install', (e) => {
  e.waitUntil(caches.open(CACHE_NAME).then(cache => cache.addAll(ASSETS)));
});

self.addEventListener('fetch', (e) => {
  e.respondWith(caches.match(e.request).then(res => res || fetch(e.request)));
});
