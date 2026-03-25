# Edward Lee Thompson – Links Lander

A modern, responsive personal landing page for Edward Lee Thompson, providing quick access to all direct contact methods and social profiles in one place.

## Features

- **Official App Icons:** All contact and social links use official, high-quality icons for brand consistency and trust.
- **Responsive Design:** Looks great on desktop, tablet, and mobile devices.
- **Animated Matrix Background:** Interactive Matrix-style effect with mouse and ripple interactions, now with improved layering, glassmorphism, and performance (debounced resize, wide character rendering).
- **Dark Mode Only:** Site is now always in dark mode for optimal Matrix effect and legibility.
- **Rich Aesthetics:** Modern glassmorphism panels and dynamic brand-colored glowing hover effects.
- **Accessible:** Large, touch-friendly icons, semantic HTML, and Bootstrap tooltips for screen readers.
- **Downloadable vCard:** One-click download of Edward's contact card.
- **PWA Support:** Includes manifest for mobile home screen installation.

## Live Preview
Hosted via GitHub Pages or your preferred static site host. Just open `docs/index.html` in your browser.

## Project Structure

```
linkslander-edwardlthompson/
├── docs/
│   ├── index.html         # Main landing page
│   ├── css/
│   │   └── style.css     # Custom styles and animations
│   ├── img/              # Official app icons and profile image
│   ├── manifest.json     # PWA manifest
│   └── edward_lee_thompson_.vcf # Downloadable contact card
├── README.md             # Project documentation
```



## How to Use
1. Clone or download this repository.
2. Open `docs/index.html` in your browser to view the site locally.
3. For real-time editing, use the "Live Preview" or "Live Server" extension in VS Code for instant browser updates as you work.
4. To deploy, upload the `docs/` folder to your static hosting provider (e.g., GitHub Pages, Netlify).

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