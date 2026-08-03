import { expect, test } from "@playwright/test";
import AxeBuilder from "@axe-core/playwright";

test("loads the collection and writes the filter to the URL", async ({ page }) => {
  await page.goto("/");
  await expect(page.locator("#estado")).toContainText("entidades cargadas");
  await expect.poll(() => page.evaluate(() => Boolean((window as { courseMap?: { getSource: (id: string) => unknown } }).courseMap?.getSource("osm")))).toBe(true);
  await page.locator("#valor-minimo").fill("18");
  await page.locator("#aplicar-filtro").click();
  await expect(page).toHaveURL(/min=18/);
  await expect(page.locator("#tabla-datos tr")).toHaveCount(4);
});

test("announces a network error", async ({ page }) => {
  await page.route("**/collections/curso:referencia/items", (route) => route.abort());
  await page.goto("/");
  await expect(page.locator("#estado")).toContainText("No fue posible cargar los datos");
});

for (const source of ["pmtiles", "cog"]) {
  test(`renders the ${source.toUpperCase()} source`, async ({ page }) => {
    await page.goto("/");
    await page.locator("#fuente").selectOption(source);
    await expect(page.locator("#estado")).toContainText("entidades cargadas");
    await expect.poll(() => page.evaluate(() => Boolean((window as { courseMap?: { getSource: (id: string) => unknown } }).courseMap?.getSource("referencia")))).toBe(true);
  });
}

test("has no automated accessibility violations", async ({ page }) => {
  await page.goto("/");
  await expect(page.locator("#estado")).toContainText("entidades cargadas");
  const results = await new AxeBuilder({ page }).analyze();
  expect(results.violations).toEqual([]);
});
