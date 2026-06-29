import { test, expect } from "@playwright/test";
import AxeBuilder from "@axe-core/playwright";

test("renders identity heading", async ({ page }) => {
  await page.goto("/");
  await expect(page.locator("h1.matrix-identity")).toHaveText("Edward Lee Thompson");
});

test("contact card download link is present", async ({ page }) => {
  await page.goto("/");
  await expect(page.getByRole("button", { name: /download contact card/i })).toHaveAttribute(
    "href",
    "edward_lee_thompson_.vcf"
  );
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
  await page.goto("/");
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
  await expect(page.locator('link[rel="stylesheet"][href*="vendor/bootstrap-5.3.3/css/bootstrap.min.css"]')).toHaveCount(1);
});

test("renders offline after first load", async ({ page, context }) => {
  await page.goto("/");
  await page.waitForLoadState("networkidle");
  await context.setOffline(true);
  await page.reload();
  await expect(page.locator("h1.matrix-identity")).toBeVisible();
});

test("passes accessibility audit", async ({ page }) => {
  await page.goto("/");
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
  await expect(page.locator("h1.matrix-identity")).toHaveText("Edward Lee Thompson");
});

test("word connections page passes accessibility audit", async ({ page }) => {
  await page.goto("/word-connections.html");
  const results = await new AxeBuilder({ page }).analyze();
  expect(results.violations).toEqual([]);
});
