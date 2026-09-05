/** Web Crypto helpers for private contacts payload (PBKDF2 + AES-GCM). */
(function (global) {
  const ITERATIONS = 100000;
  const PAYLOAD_VERSION = 1;

  function b64ToBytes(b64) {
    const bin = atob(b64);
    const out = new Uint8Array(bin.length);
    for (let i = 0; i < bin.length; i += 1) out[i] = bin.charCodeAt(i);
    return out;
  }

  function bytesToB64(bytes) {
    let s = "";
    bytes.forEach((b) => {
      s += String.fromCharCode(b);
    });
    return btoa(s);
  }

  function assertPayload(payload) {
    if (!payload || payload.v !== PAYLOAD_VERSION) {
      throw new Error("Unsupported contacts payload");
    }
    if (!payload.salt || !payload.iv || !payload.ciphertext) {
      throw new Error("Corrupt contacts payload");
    }
  }

  async function deriveKey(phrase, saltBytes) {
    const enc = new TextEncoder();
    const baseKey = await crypto.subtle.importKey(
      "raw",
      enc.encode(phrase),
      "PBKDF2",
      false,
      ["deriveKey"]
    );
    return crypto.subtle.deriveKey(
      {
        name: "PBKDF2",
        salt: saltBytes,
        iterations: ITERATIONS,
        hash: "SHA-256",
      },
      baseKey,
      { name: "AES-GCM", length: 256 },
      false,
      ["encrypt", "decrypt"]
    );
  }

  async function encryptContacts(plaintext, phrase) {
    const salt = crypto.getRandomValues(new Uint8Array(16));
    const iv = crypto.getRandomValues(new Uint8Array(12));
    const key = await deriveKey(phrase, salt);
    const cipherBuf = await crypto.subtle.encrypt(
      { name: "AES-GCM", iv },
      key,
      new TextEncoder().encode(plaintext)
    );
    return {
      v: PAYLOAD_VERSION,
      salt: bytesToB64(salt),
      iv: bytesToB64(iv),
      ciphertext: bytesToB64(new Uint8Array(cipherBuf)),
    };
  }

  async function decryptContacts(payload, phrase) {
    assertPayload(payload);
    const salt = b64ToBytes(payload.salt);
    const iv = b64ToBytes(payload.iv);
    const ciphertext = b64ToBytes(payload.ciphertext);
    const key = await deriveKey(phrase, salt);
    const plainBuf = await crypto.subtle.decrypt(
      { name: "AES-GCM", iv },
      key,
      ciphertext
    );
    return new TextDecoder().decode(plainBuf);
  }

  global.ContactsCrypto = {
    ITERATIONS,
    PAYLOAD_VERSION,
    encryptContacts,
    decryptContacts,
    assertPayload,
    b64ToBytes,
    bytesToB64,
  };
})(typeof window !== "undefined" ? window : globalThis);
