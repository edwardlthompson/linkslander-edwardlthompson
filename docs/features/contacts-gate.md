# Feature: Contacts gate + icon labels + static avatar

## Acceptance criteria

- ✅ Public icons show a one-word label under each circle
- ✅ Locked visit hides Direct Contact, Social Networks, profile card, and VCF endpoints from HTML
- ✅ `/#MyContacts` auto-unlocks; wrong phrase fails closed with an accessible error
- ✅ Profile avatar is static (no float) with locked `aspect-ratio` / `object-fit`
- ✅ Pages deploy encrypts payload and strips `fragments/` + `*.vcf`

## Smoke scenario

1. _Given_ the site is served from `site/`
2. _When_ a visitor opens `/`
3. _Then_ they see Contacts Locked + public sections, and `/#MyContacts` reveals private contacts without typing

## Container map

| Layer | Path |
|-------|------|
| Logic | `site/js/contacts-crypto.js`, `site/js/contacts-gate.js` |
| View | `site/index.html` lock panel + `site/fragments/private-contacts.html` |
| Tests | `site/scripts/test-contacts-crypto.mjs`, `site/e2e/site.spec.ts` |
| Wiring | encrypt script + Pages staging in `.github/workflows/pages.yml` |

## Definition of Done

Gates: unit crypto round-trip, Playwright locked/unlocked/a11y, Pages encrypt+strip.
