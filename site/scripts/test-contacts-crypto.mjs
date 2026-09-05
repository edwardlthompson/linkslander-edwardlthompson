#!/usr/bin/env node
import { readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import { webcrypto } from "node:crypto";

const cryptoSubtle = webcrypto;
Object.defineProperty(globalThis, "crypto", { value: cryptoSubtle });
globalThis.atob = (s) => Buffer.from(s, "base64").toString("binary");
globalThis.btoa = (s) => Buffer.from(s, "binary").toString("base64");

const __dirname = dirname(fileURLToPath(import.meta.url));
const siteRoot = join(__dirname, "..");
const src = readFileSync(join(siteRoot, "js", "contacts-crypto.js"), "utf8");
(0, eval)(src);

const phrase = "MyContacts";
const sample = '<div id="t">hello contacts</div>';

const payload = await ContactsCrypto.encryptContacts(sample, phrase);
const round = await ContactsCrypto.decryptContacts(payload, phrase);
if (round !== sample) {
  console.error("round-trip mismatch");
  process.exit(1);
}
let failed = false;
try {
  await ContactsCrypto.decryptContacts(payload, "wrong");
  failed = true;
} catch {
  // expected
}
if (failed) {
  console.error("wrong phrase should fail");
  process.exit(1);
}

const committed = JSON.parse(
  readFileSync(join(siteRoot, "js", "contacts.payload.json"), "utf8")
);
const html = await ContactsCrypto.decryptContacts(committed, phrase);
if (!html.includes("download-contact-card") || !html.includes("Direct Contact")) {
  console.error("committed payload decrypt content unexpected");
  process.exit(1);
}
if (html.includes("matrix-identity") || html.includes('src="img/p.jpg"')) {
  console.error("identity should be public HTML, not in encrypted payload");
  process.exit(1);
}
console.log("contacts-crypto tests passed");
