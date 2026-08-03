import { expect, test } from "@playwright/test";

test("PMTiles renderiza entidades vectoriales", async ({ page }) => {
  await page.goto("/?asset=pmtiles");
  await expect(page.getByRole("status")).toHaveAttribute("data-protocol-state", "ready");
  await expect.poll(() => page.evaluate(() => {
    const point = window.prototypeMap.project([-74.1, 4.7]);
    return window.prototypeMap.queryRenderedFeatures([[point.x - 12, point.y - 12], [point.x + 12, point.y + 12]], { layers: ["referencia"] }).length;
  })).toBeGreaterThan(0);
});

test("COG alcanza estado listo", async ({ page }) => {
  await page.goto("/?asset=cog");
  await expect(page.getByRole("status")).toHaveAttribute("data-protocol-state", "ready");
  await expect(page.locator("#mapa canvas")).toBeVisible();
});

test("el error de asset se anuncia", async ({ page }) => {
  await page.route("**/referencia.pmtiles", (route) => route.fulfill({ status: 500 }));
  await page.goto("/?asset=pmtiles");
  await expect(page.getByRole("status")).toHaveAttribute("data-protocol-state", "error");
});
