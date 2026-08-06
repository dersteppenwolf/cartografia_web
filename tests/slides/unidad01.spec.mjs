import { expect, test } from '@playwright/test';

const basePath = '/cartografia_web';
const deckPath = `${basePath}/presentaciones/unidad-01/`;

test('la guía enlaza la presentación publicada de la Unidad 1', async ({
  page,
}) => {
  await page.goto(`${basePath}/unidades/01-web-git-publicacion/`);
  const presentation = page.getByRole('link', {
    name: 'Abrir presentación de la Unidad 1',
  });
  await expect(presentation).toHaveAttribute('href', deckPath);
  await presentation.click();
  await expect(page).toHaveURL(`http://127.0.0.1:8011${deckPath}`);
});

test('sirve citas y diagramas de la presentación bajo el prefijo publicado', async ({
  page,
}) => {
  const failedResponses = [];
  page.on('response', (response) => {
    const url = new URL(response.url());
    if (url.pathname.startsWith(deckPath) && response.status() >= 400) {
      failedResponses.push(`${response.status()} ${url.pathname}`);
    }
  });

  await page.goto(`${deckPath}#/11`);
  await expect(
    page.getByRole('heading', {
      name: 'Conectividad global: contexto, no garantía de acceso',
    }),
  ).toBeVisible();
  await expect(page.getByText('Gozzi et al., 2024')).toBeVisible();
  await expect(
    page.locator('img[alt^="Gráfico propio de conectividad mundial"]'),
  ).toHaveAttribute(
    'src',
    `${deckPath}assets/generated/connectividad_2025.svg`,
  );

  await page.goto(`${deckPath}#/31`);
  await expect(
    page.getByRole('heading', {
      name: 'Un mapa es una interfaz, no una imagen',
    }),
  ).toBeVisible();
  await expect(page.getByText('Manu, Burghardt y Hauthal, 2025')).toBeVisible();

  await page.goto(`${deckPath}#/32`);
  await expect(
    page.getByRole('heading', {
      name: 'Publicar una ubicación también tiene riesgos',
    }),
  ).toBeVisible();
  await expect(page.getByText('Tiwari et al., 2023')).toBeVisible();
  await expect(page.getByText('Li et al., 2025')).toBeVisible();

  await page.goto(`${deckPath}#/37`);
  await expect(
    page.getByRole('heading', { name: 'Referencias científicas incorporadas' }),
  ).toBeVisible();
  for (const doi of [
    '10.1140/epjds/s13688-024-00508-8',
    '10.1111/tgis.70075',
    '10.1007/s42489-025-00189-x',
    '10.1108/DTS-04-2024-0054',
    '10.4081/gh.2023.1205',
  ]) {
    await expect(page.getByText(doi)).toBeVisible();
  }
  expect(failedResponses).toEqual([]);
});
