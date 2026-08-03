import { expect, test } from "@playwright/test";
import AxeBuilder from "@axe-core/playwright";

const pagePath = "/examples/leaflet/mapa_basico/";

test("muestra datos sintéticos y controles accesibles", async ({ page }) => {
  await page.goto(pagePath);
  await expect(page.getByRole("status")).toContainText("4 zonas visibles");
  await expect(page.getByRole("table")).toContainText("Zona 1");
  await page.getByLabel("Mostrar zonas con valor mínimo").selectOption("30");
  await expect(page.getByRole("status")).toContainText("1 zonas visibles");
  await expect(page.getByRole("table")).toContainText("Zona 4");
  const results = await new AxeBuilder({ page }).analyze();
  expect(results.violations).toEqual([]);
});

test("informa un error de red comprensible", async ({ page }) => {
  await page.route("**/data/referencia.geojson", (route) => route.fulfill({ status: 500 }));
  await page.goto(pagePath);
  await expect(page.getByRole("status")).toContainText("No fue posible cargar los datos");
});
