# Desarrollo y validación

Esta guía reúne los comandos y controles técnicos del repositorio. El índice
público del curso está en [README.md](README.md). El detalle del trabajo de
modernización permanece en
[`plans/plan_0001_modernizacion_integral.md`](plans/plan_0001_modernizacion_integral.md).

Todos los comandos se ejecutan desde la raíz del repositorio en PowerShell 7.

## Entorno local

Instala Docker Desktop, Node.js 24, Python 3.12 con `uv`, Git y un navegador con
WebGL. Comprueba el entorno e instala dependencias fijadas:

```powershell
docker version
npm ci
uv sync --frozen
```

No agregues secretos, tokens activos, IPs históricas ni datos sociales en
cuarentena. Los archivos `infra/secrets/*.example` contienen solo valores
ficticios.

## Validación de fuentes y cliente

Ejecuta las comprobaciones que no requieren servicios locales:

```powershell
npm run validate
npm test
npm run --workspace examples/maplibre/app test:e2e -- --project=chromium
```

`npm run validate` comprueba formato, Markdown, HTML, CSS, inventario,
licencias, tipos TypeScript, pruebas unitarias y build Vite. El recorrido E2E
verifica OGC API - Features, errores de red, PMTiles, COG y Axe. Si Chromium no
está instalado, ejecuta `npx playwright install chromium`.

Después de cambiar `docs/assets/css/tokens.css`, sincroniza los tokens del
cliente MapLibre y el ejemplo Leaflet:

```powershell
uv run python scripts/sync_design_tokens.py
uv run python scripts/sync_design_tokens.py --check
```

## Infraestructura local

El stack usa PostGIS, GeoServer y Nginx. GeoServer se configura por REST, sin
pasos manuales en la interfaz administrativa:

```powershell
docker compose -f infra/compose.yaml up -d --build --wait
uv run python scripts/configure_geoserver.py
npm run validate:stack
```

La validación comprueba WMS, WFS, OGC API - Features, MVT, STAC, HTTP Range y
CORS. Las interfaces se exponen solo en `localhost`:

- GeoServer: `http://localhost:18080/geoserver`
- Activos PMTiles y COG: `http://localhost:18081/assets/`

Para detener el stack y eliminar los datos de práctica:

```powershell
docker compose -f infra/compose.yaml down --volumes
```

## Notebooks, backup y restauración

Los notebooks funcionan con fixtures sin red y con el stack local. La prueba de
restauración inserta una fila centinela, crea un backup, elimina volúmenes,
restaura PostGIS y vuelve a configurar GeoServer:

```powershell
uv run python scripts/run_notebooks.py --mode fixtures
uv run python scripts/run_notebooks.py --mode local
uv run python scripts/test_restore.py --compose-file infra/compose.yaml --backup-dir .backups
```

## Activos cloud-native y rendimiento

Los activos de práctica se generan desde fixtures sintéticos con herramientas en
contenedores con digest fijado:

```powershell
npm run data:build:pmtiles
npm run data:build:cog
npm run test:range
npm run benchmark:browser
npm run benchmark -- --route vector --runs 5
npm run benchmark -- --route raster --runs 5
```

Los reportes se escriben en `.reports/` y no se versionan. El benchmark de
navegador mide el tiempo hasta que MapLibre registra una fuente; el benchmark
Python mide transporte HTTP. La aceptación curricular del objetivo de
rendimiento requiere una decisión documentada del instructor.

## Build y vista previa

`npm run build` construye Jekyll, el cliente MapLibre y el artefacto ensamblado
`_site/`, incluyendo Leaflet, MapLibre, PMTiles y COG:

```powershell
npm run build
npm run links:internal
python -m http.server 8000 --directory _site
```

Abre `http://localhost:8000/`. No pruebes ejemplos que usan `fetch` mediante
`file://`.

Para comprobar rutas bajo el prefijo de GitHub Pages:

```powershell
uv run python scripts/build_site.py --baseurl /cartografia_web --output _site_preview_jekyll
uv run python scripts/assemble_site.py --jekyll-site _site_preview_jekyll --leaflet-dir examples/leaflet --maplibre-dist examples/maplibre/app/dist --cloud-assets data/fixtures/cloud --output .preview/cartografia_web
```

## Seguridad

Gitleaks y Trivy se ejecutan desde imágenes fijadas. No añadas secretos para
resolver un fallo:

```powershell
uv run python scripts/security_scan.py --scope worktree
uv run python scripts/security_scan.py --scope dependencies
```

Las excepciones deben ser específicas, justificadas, tener responsable y fecha
de vencimiento en `docs/governance/security-exceptions.yml`. Consulta también la
[guía de seguridad](docs/guias/seguridad.md).

## Clon limpio

Antes de preparar una candidata, crea un clon fuera del repositorio y repite las
validaciones. Mantén el stack local iniciado si usarás `validate:stack`:

```powershell
git clone --no-local . ..\cartografia_web_clean
Set-Location ..\cartografia_web_clean
npm ci
uv sync --frozen
npm run validate
npm test
npm run validate:stack
```

El clon no debe depender de `node_modules`, `.venv`, `_site`, `.preview`,
`.reports` ni otros artefactos del árbol original.

## Publicación

GitHub Pages publica solo el artefacto `_site/` mediante
`.github/workflows/pages.yml`. En GitHub selecciona **Settings > Pages > Source

> GitHub Actions**. Tras el despliegue, comprueba unidades, ejemplos y las
> respuestas HTTP Range de PMTiles/COG desde la URL publicada.

La publicación no incluye PostGIS, GeoServer, contraseñas personales ni datos en
cuarentena. Consulta la [guía de publicación](docs/guias/publicacion.md) y la
[guía de restauración](docs/guias/restauracion.md).

## Piloto y candidata

No simules resultados de piloto. Completa primero:

- `docs/governance/manual-accessibility-review.md`
- `docs/pilot/plan.md`
- `docs/pilot/results.md`
- `docs/pilot/issues.md`
- `docs/pilot/browser-matrix.yml`

El responsable de web y accesibilidad registra teclado, foco, contraste, reflow,
lector de pantalla y Safari real en macOS. El instructor registra participantes,

El gate produce un reporte factual y queda bloqueado hasta que exista toda la

```powershell
uv run python scripts/release_gate.py --mode prepared
```

El reporte queda en `.reports/release-gate.json`. Tags, releases y pushes
requieren autorización explícita.
