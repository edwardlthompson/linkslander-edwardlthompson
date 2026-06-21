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
