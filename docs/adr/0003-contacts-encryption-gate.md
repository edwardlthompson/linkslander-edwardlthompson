# ADR 0003: Partial contacts encryption gate

## Status

Accepted — 2026-09-05

## Context

The LinksLander portal previously published Direct Contact, Social Networks, profile photo, and a downloadable VCF on the public GitHub Pages site. The owner wants to share those details via a memorable link without making them trivial to scrape or index, while keeping Other / Adventure / Payments public.

## Decision

Use a **partial-page AES-GCM gate** (Web Crypto, PBKDF2-SHA-256, 100k iterations):

- Source HTML lives in `site/fragments/private-contacts.html` (repo-tracked for editing).
- Build/deploy encrypts it to `site/js/contacts.payload.json` with share phrase `MyContacts`.
- Public `index.html` ships lock panel + public identity (photo/name) + public sections.
- Visiting `/#MyContacts` (or entering the phrase) decrypts and injects the private block via `DOMParser`.
- VCF is embedded as base64 inside the fragment and downloaded as a Blob after unlock (no public `.vcf` on Pages).
- Avatar `img/p.jpg` is public; only Direct Contact / Social / VCF stay behind the gate.
- Pages artifact staging strips `fragments/`, `*.vcf`, and legacy `img/image01.jpg`.

## Consequences

- Search engines and casual HTML scrapers no longer see phone/email/social/VCF in the public document.
- Photo and display name are intentionally public.
- Anyone with the share phrase or git access to the fragment can recover private contact content (accepted residual).
- Service worker cache bumped; unlock works offline after first payload fetch/cache.
- Honest threat-model docs must describe this as scrape friction, not fortress-grade secrecy.
