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

test("passes accessibility audit", async ({ page }) => {
  await page.goto("/");
  const results = await new AxeBuilder({ page }).analyze();
  expect(results.violations).toEqual([]);
});
