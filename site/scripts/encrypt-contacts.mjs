#!/usr/bin/env node
/**
 * Encrypt site/fragments/private-contacts.html -> site/js/contacts.payload.json
 * Share phrase: MyContacts (URL hash #MyContacts)
 */
import { readFileSync, writeFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { webcrypto } from 'node:crypto';

const crypto = webcrypto;
const __dirname = dirname(fileURLToPath(import.meta.url));
const siteRoot = join(__dirname, '..');
const PHRASE = process.env.CONTACTS_PHRASE || 'MyContacts';
const ITERATIONS = 100000;
const VERSION = 1;

function bytesToB64(bytes) {
  return Buffer.from(bytes).toString('base64');
}

async function deriveKey(phrase, saltBytes) {
  const baseKey = await crypto.subtle.importKey(
    'raw',
    new TextEncoder().encode(phrase),
    'PBKDF2',
    false,
    ['deriveKey']
  );
  return crypto.subtle.deriveKey(
    { name: 'PBKDF2', salt: saltBytes, iterations: ITERATIONS, hash: 'SHA-256' },
    baseKey,
    { name: 'AES-GCM', length: 256 },
    false,
    ['encrypt']
  );
}

async function main() {
  const fragmentPath = join(siteRoot, 'fragments', 'private-contacts.html');
  const outPath = join(siteRoot, 'js', 'contacts.payload.json');
  const plaintext = readFileSync(fragmentPath, 'utf8');
  const salt = crypto.getRandomValues(new Uint8Array(16));
  const iv = crypto.getRandomValues(new Uint8Array(12));
  const key = await deriveKey(PHRASE, salt);
  const cipherBuf = await crypto.subtle.encrypt(
    { name: 'AES-GCM', iv },
    key,
    new TextEncoder().encode(plaintext)
  );
  const payload = {
    v: VERSION,
    salt: bytesToB64(salt),
    iv: bytesToB64(iv),
    ciphertext: bytesToB64(new Uint8Array(cipherBuf)),
  };
  writeFileSync(outPath, `${JSON.stringify(payload, null, 2)}\n`, 'utf8');
  console.log(`Wrote ${outPath} (${payload.ciphertext.length} b64 ciphertext chars)`);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
