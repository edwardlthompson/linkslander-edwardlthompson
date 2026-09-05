# ADR 0003: Partial contacts encryption gate

## Status

Accepted — 2026-09-05

## Context

The LinksLander portal previously published Direct Contact, Social Networks, profile photo, and a downloadable VCF on the public GitHub Pages site. The owner wants to share those details via a memorable link without making them trivial to scrape or index, while keeping Other / Adventure / Payments public.

## Decision

Use a **partial-page AES-GCM gate** (Web Crypto, PBKDF2-SHA-256, 100k iterations):

- Source HTML lives in `site/fragments/private-contacts.html` (repo-tracked for editing).
- Build/deploy encrypts it to `site/js/contacts.payload.json` with share phrase `MyContacts`.
- Public `index.html` ships only a lock panel + public sections.
- Visiting `/#MyContacts` (or entering the phrase) decrypts and injects the private block via `DOMParser`.
- VCF is embedded as base64 inside the fragment and downloaded as a Blob after unlock (no public `.vcf` on Pages).
- Avatar is referenced only from the fragment as opaque `img/p.jpg`.
- Pages artifact staging strips `fragments/`, `*.vcf`, and legacy `img/image01.jpg`.

## Consequences

- Search engines and casual HTML scrapers no longer see phone/email/social/VCF in the public document.
- Anyone with the share phrase or git access to the fragment can recover the content (accepted residual).
- Static hosts cannot ACL `img/p.jpg`; omission from public HTML is best-effort.
- Service worker cache bumped; unlock works offline after first payload fetch/cache.
- Honest threat-model docs must describe this as scrape friction, not fortress-grade secrecy.
