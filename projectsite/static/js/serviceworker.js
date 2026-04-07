const CACHE_NAME = 'hangarin-cache-v2';

const PRECACHE_URLS = [
    '/',
    '/static/css/bootstrap.min.css',
    '/static/css/ready.css',
    '/static/css/demo.css',
    '/static/js/core/jquery.3.2.1.min.js',
    '/static/js/core/bootstrap.min.js',
    '/static/js/ready.min.js',
];

self.addEventListener('install', function (e) {
    e.waitUntil(
        caches.open(CACHE_NAME).then(function (cache) {
            return cache.addAll(PRECACHE_URLS);
        }).then(function () {
            return self.skipWaiting();
        })
    );
});

self.addEventListener('activate', function (e) {
    e.waitUntil(
        caches.keys().then(function (cacheNames) {
            return Promise.all(
                cacheNames
                    .filter(function (name) { return name !== CACHE_NAME; })
                    .map(function (name) { return caches.delete(name); })
            );
        }).then(function () {
            return self.clients.claim();
        })
    );
});

self.addEventListener('fetch', function (e) {
    if (e.request.mode === 'navigate') {
        e.respondWith(
            fetch(e.request).catch(function () {
                return caches.match('/');
            })
        );
        return;
    }

    e.respondWith(
        caches.match(e.request).then(function (response) {
            return response || fetch(e.request).then(function (networkResponse) {
                if (
                    networkResponse.ok &&
                    e.request.url.match(/\.(css|js|woff2?|ttf|png|jpg|ico)$/)
                ) {
                    var responseClone = networkResponse.clone();
                    caches.open(CACHE_NAME).then(function (cache) {
                        cache.put(e.request, responseClone);
                    });
                }
                return networkResponse;
            });
        })
    );
});
