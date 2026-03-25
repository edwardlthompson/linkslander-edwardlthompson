# Edward Lee Thompson – Digital Portal V2.0

A high-performance, interactive personal landing page and PWA. This portal features a custom-built Matrix-style physics engine, glassmorphism UI, and offline accessibility.

## 🚀 Advanced Features

* **Persistent 3D-Grid Engine:** A custom HTML5 Canvas background where characters stay in fixed 3D space, revealed only by falling "data drops."
* **Gravitational Singularity:** The background reacts to cursor movement, physically warping and "swallowing" data characters near the pointer.
* **Tactile Interaction:** Clicking triggers a high-velocity "Ripple" shockwave with synchronized "Whoosh" audio feedback.
* **PWA Core:** Fully installable as a standalone app on iOS and Android with offline caching via Service Workers.
* **Retro-Tech Aesthetic:** CRT-style scanlines, phosphor-green color grading, and wide-body terminal typography.
* **Dual-Contact vCard:** Integrated .vcf download with primary (+1-787) and secondary (+1-469) line support.

## 🛠️ Tech Stack
* **Engine:** Vanilla JavaScript / HTML5 Canvas API
* **Audio:** Web Audio API (OscillatorNode/GainNode)
* **UI:** Bootstrap 5 + Custom CSS Glassmorphism
* **PWA:** Service Worker (Cache-First Strategy) + Web App Manifest

## 📱 Mobile Optimization
* **Thumb-Friendly:** All touch targets meet 48x48px accessibility standards.
* **Dynamic Scaling:** Profile and Name panels scale proportionally for mobile devices.
* **Battery Conscious:** Optimized render loop for stable frame rates.

---
**Maintained by Edward Lee Thompson.**

## Customization
- To update contact links or add new platforms, edit `docs/index.html` and add the appropriate icon to `docs/img/`.
- To change the Matrix background effect, glassmorphism, or color scheme, edit `docs/js/matrix.js` and `docs/css/style.css`.

## Credits
- All app icons are official assets from their respective brands.
- Built with [Bootstrap 5](https://getbootstrap.com/) and custom CSS.

## Recent Improvements
- Removed theme toggle; site is now always dark mode.
- Fixed Matrix z-index and glassmorphism for better readability and accessibility.
- Debounced Matrix resize for smoother performance.
- Cleaned up merge artifacts and ensured no missing asset references.

**Created and maintained by Edward Lee Thompson.**