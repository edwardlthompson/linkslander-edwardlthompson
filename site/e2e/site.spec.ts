import { test, expect } from "@playwright/test";
import AxeBuilder from "@axe-core/playwright";

async function unlockContacts(page: import("@playwright/test").Page) {
  await page.goto("/#MyContacts");
  await expect(page.locator("h1.matrix-identity")).toHaveText("Edward Lee Thompson", {
    timeout: 10_000,
  });
}

test("locked portal shows contacts lock and public sections only", async ({ page }) => {
  await page.goto("/");
  await expect(page.getByRole("heading", { name: /contacts locked/i })).toBeVisible();
  await expect(page.locator("h1.matrix-identity")).toHaveCount(0);
  await expect(page.getByRole("heading", { name: "Other" })).toBeVisible();
  await expect(page.getByRole("heading", { name: "Book Your Next Adventure" })).toBeVisible();
  await expect(page.getByRole("heading", { name: "Payments / Tips" })).toBeVisible();
  const html = await page.content();
  expect(html).not.toMatch(/t\.me\//);
  expect(html).not.toMatch(/wa\.me\//);
  expect(html).not.toMatch(/tel:\+/);
  expect(html).not.toMatch(/mailto:/);
});

test("public icons show one-word labels", async ({ page }) => {
  await page.goto("/");
  await expect(page.locator(".icons .label", { hasText: "YouTube" })).toBeVisible();
  await expect(page.locator(".icons .label", { hasText: "Words" })).toBeVisible();
  await expect(page.locator(".icons .label", { hasText: "PayPal" })).toBeVisible();
});

test("share hash #MyContacts unlocks private contacts", async ({ page }) => {
  await unlockContacts(page);
  await expect(page.getByRole("heading", { name: "Direct Contact" })).toBeVisible();
  await expect(page.getByRole("heading", { name: "Social Networks" })).toBeVisible();
  await expect(page.locator(".icons .label", { hasText: "Telegram" })).toBeVisible();
  await expect(page.locator(".icons .label", { hasText: "Messenger" })).toBeVisible();
  await expect(page.locator(".icons .label", { hasText: "Voice" })).toBeVisible();
  await expect(page.locator("img.profile-img")).toBeVisible();
  await expect(page.getByRole("heading", { name: /contacts locked/i })).toBeHidden();
});

test("wrong phrase fails closed", async ({ page }) => {
  await page.goto("/");
  await page.locator("#contacts-phrase").fill("not-the-phrase");
  await page.getByRole("button", { name: /unlock contacts/i }).click();
  await expect(page.locator("#contacts-unlock-error")).toBeVisible();
  await expect(page.locator("#contacts-unlock-error")).toHaveText(/did not work/i);
  await expect(page.locator("h1.matrix-identity")).toHaveCount(0);
  await expect(page.getByRole("heading", { name: /contacts locked/i })).toBeVisible();
});

test("unlocked contact card download uses blob not public vcf path", async ({ page }) => {
  await unlockContacts(page);
  const btn = page.locator("#download-contact-card");
  await expect(btn).toBeVisible();
  await expect(btn).not.toHaveAttribute("href", /edward_lee_thompson_\.vcf/);
  const downloadPromise = page.waitForEvent("download");
  await btn.click();
  const download = await downloadPromise;
  expect(download.suggestedFilename()).toMatch(/\.vcf$/i);
});

test("registers service worker", async ({ page }) => {
  await page.goto("/");
  const registered = await page.evaluate(async () => {
    if (!("serviceWorker" in navigator)) return false;
    await navigator.serviceWorker.ready;
    return (await navigator.serviceWorker.getRegistrations()).length > 0;
  });
  expect(registered).toBe(true);
});

test("external links use noopener", async ({ page }) => {
  await unlockContacts(page);
  const blankLinks = page.locator('a[target="_blank"]');
  const count = await blankLinks.count();
  expect(count).toBeGreaterThan(0);
  for (let i = 0; i < count; i++) {
    const rel = (await blankLinks.nth(i).getAttribute("rel")) ?? "";
    expect(rel).toMatch(/noopener/);
  }
});

test("loads Bootstrap from local vendor path", async ({ page }) => {
  const cdnRequests: string[] = [];
  page.on("request", (req) => {
    if (req.url().includes("cdn.jsdelivr.net")) cdnRequests.push(req.url());
  });
  await page.goto("/");
  await page.waitForLoadState("networkidle");
  expect(cdnRequests).toEqual([]);
  await expect(
    page.locator('link[rel="stylesheet"][href*="vendor/bootstrap-5.3.3/css/bootstrap.min.css"]')
  ).toHaveCount(1);
});

test("renders offline after first load", async ({ page, context }) => {
  await page.goto("/");
  await page.waitForLoadState("networkidle");
  await page.evaluate(async () => {
    if (!("serviceWorker" in navigator)) return;
    await navigator.serviceWorker.ready;
  });
  await context.setOffline(true);
  await page.reload({ waitUntil: "domcontentloaded" });
  await expect(page.getByRole("heading", { name: /contacts locked/i })).toBeVisible();
});

test("passes accessibility audit when locked", async ({ page }) => {
  await page.goto("/");
  const results = await new AxeBuilder({ page }).analyze();
  expect(results.violations).toEqual([]);
});

test("passes accessibility audit when unlocked", async ({ page }) => {
  await unlockContacts(page);
  const results = await new AxeBuilder({ page }).analyze();
  expect(results.violations).toEqual([]);
});

test("word connections link in Other section", async ({ page }) => {
  await page.goto("/");
  const link = page.getByRole("link", { name: "Word Connections" });
  await expect(link).toHaveAttribute("href", "word-connections.html");
});

test("word connections page has sticky header and column order", async ({ page }) => {
  await page.goto("/word-connections.html");
  const thead = page.locator("thead.roots-sticky-head");
  await expect(thead).toBeVisible();
  const headers = thead.locator("th");
  await expect(headers).toHaveCount(7);
  await expect(headers.nth(0)).toHaveText("Category");
  await expect(headers.nth(1)).toHaveText("English");
  await expect(headers.nth(2)).toHaveText("German");
  await expect(headers.nth(3)).toHaveText("Spanish");
  await expect(headers.nth(4)).toHaveText("Portuguese");
  await expect(headers.nth(5)).toHaveText("Italian");
  await expect(headers.nth(6)).toHaveText("French");
  const headerSticky = await thead.locator("th").first().evaluate((el) => getComputedStyle(el).position);
  expect(headerSticky).toBe("sticky");
});

test("word connections Sun group is first and aligned across languages", async ({ page }) => {
  await page.goto("/word-connections.html");
  const firstGroup = page.locator("tbody.roots-group").first();
  const rootRow = firstGroup.locator("tr.roots-root-row");
  const cells = rootRow.locator("td");
  await expect(cells.nth(0)).toHaveText("Sun");
  await expect(cells.nth(1)).toHaveText("Sonne");
  await expect(cells.nth(2)).toHaveText("Sol");
  await expect(cells.nth(3)).toHaveText("Sol");
  await expect(cells.nth(4)).toHaveText("Sole");
  await expect(cells.nth(5)).toHaveText("Soleil");
});

test("word connections lengua cluster spans all languages", async ({ page }) => {
  await page.goto("/word-connections.html");
  const tongueGroup = page.locator("tbody.roots-group").filter({ hasText: "Tongue" });
  await expect(tongueGroup.locator("tr").filter({ hasText: "linguist" })).toHaveCount(1);
  const linguistRow = tongueGroup.locator("tr").filter({ hasText: "linguist" });
  const cells = linguistRow.locator("td");
  await expect(cells.nth(0)).toHaveText("linguist");
  await expect(cells.nth(1)).toHaveText("Linguist");
  await expect(cells.nth(2)).toHaveText("lingüista");
  await expect(cells.nth(3)).toHaveText("linguista");
  await expect(cells.nth(4)).toHaveText("linguista");
  await expect(cells.nth(5)).toHaveText("linguiste");
});

test("word connections has at least 40 word groups", async ({ page }) => {
  await page.goto("/word-connections.html");
  await expect(page.locator("tbody.roots-group")).toHaveCount(51);
});

test("word connections back link returns to portal", async ({ page }) => {
  await page.goto("/word-connections.html");
  await page.getByRole("button", { name: /back to portal/i }).click();
  await expect(page).toHaveURL(/\/(index\.html)?$/);
  await expect(page.getByRole("heading", { name: /contacts locked/i })).toBeVisible();
});

test("word connections shows English column legend", async ({ page }) => {
  await page.goto("/word-connections.html");
  const legend = page.getByRole("list", { name: /english column color meanings/i });
  await expect(legend).toBeVisible();
  await expect(legend.getByText(/Break/i)).toBeVisible();
  await expect(legend.getByText(/Borrowed/i)).toBeVisible();
  await expect(legend.getByText(/Aligned/i)).toBeVisible();
});

test("word connections registers service worker", async ({ page }) => {
  await page.goto("/word-connections.html");
  const registered = await page.evaluate(async () => {
    if (!("serviceWorker" in navigator)) return false;
    await navigator.serviceWorker.ready;
    return (await navigator.serviceWorker.getRegistrations()).length > 0;
  });
  expect(registered).toBe(true);
});

test("word connections renders offline after first load", async ({ page, context }) => {
  await page.goto("/word-connections.html");
  await page.waitForLoadState("networkidle");
  await page.evaluate(async () => {
    if ("serviceWorker" in navigator) await navigator.serviceWorker.ready;
  });
  await page.goto("/word-connections.html");
  await page.waitForLoadState("networkidle");
  await page.evaluate(async () => {
    if ("serviceWorker" in navigator) await navigator.serviceWorker.ready;
  });
  await context.setOffline(true);
  await page.reload({ waitUntil: "domcontentloaded" });
  await expect(page.getByRole("heading", { name: /Language Comparison/i })).toBeVisible();
});

test("word connections page passes accessibility audit", async ({ page }) => {
  await page.goto("/word-connections.html");
  const results = await new AxeBuilder({ page }).analyze();
  expect(results.violations).toEqual([]);
});
