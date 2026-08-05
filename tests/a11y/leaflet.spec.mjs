import { expect, test } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';

const mapPagePath = '/examples/leaflet/mapa_basico/';
const minimumPagePath = '/examples/leaflet/pagina_minima/';

test('muestra datos sintéticos y controles accesibles', async ({ page }) => {
  await page.goto(mapPagePath);
  await expect(page.getByRole('status')).toContainText('4 zonas visibles');
  await expect(page.getByRole('table')).toContainText('Zona 1');
  await expect(page.locator('.leaflet-control-attribution')).toContainText(
    'OpenStreetMap',
  );
  await page.getByLabel('Mostrar zonas con valor mínimo').selectOption('30');
  await expect(page.getByRole('status')).toContainText('1 zonas visibles');
  await expect(page.getByRole('table')).toContainText('Zona 4');
  const results = await new AxeBuilder({ page }).analyze();
  expect(results.violations).toEqual([]);
});

test('informa un error de red comprensible', async ({ page }) => {
  await page.route('**/data/referencia.geojson', (route) =>
    route.fulfill({ status: 500 }),
  );
  await page.goto(mapPagePath);
  await expect(page.getByRole('status')).toContainText(
    'No fue posible cargar los datos',
  );
});

test('demuestra un módulo ES en una página mínima accesible', async ({
  page,
}) => {
  await page.goto(minimumPagePath);
  await expect(page.getByRole('status')).toHaveText('Página lista.');
  await page.getByRole('button', { name: 'Actualizar mensaje' }).click();
  await expect(page.getByRole('status')).toHaveText(
    'El módulo ES actualizó este mensaje.',
  );
  const results = await new AxeBuilder({ page }).analyze();
  expect(results.violations).toEqual([]);
});
