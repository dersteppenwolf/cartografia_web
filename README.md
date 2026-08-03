# Publicación de cartografía vía web

Curso en proceso de modernización curricular, editorial y técnica.

## Material mantenido

- [Estado de la modernización](docs/status.md)
- [Inventario de migración](docs/migration-inventory.md)
- [Plan de modernización](UPGRADE_PLAN.md)
- [Plan de ejecución](plans/plan_0001_modernizacion_integral.md)

## Completar el plan 0001

El plan detallado y vivo está en
[`plans/plan_0001_modernizacion_integral.md`](plans/plan_0001_modernizacion_integral.md).
Esta sección ofrece el recorrido operativo resumido. Todos los comandos se
ejecutan desde la raíz del repositorio en PowerShell 7.

### 1. Preparar el entorno

Instala Docker Desktop, Node.js 24, Python 3.12 con `uv`, Git y un navegador con
WebGL. Para el stack local, comprueba que Docker esté disponible:

```powershell
docker version
npm ci
uv sync --frozen
```

El curso no requiere cuentas SaaS, tokens, IPs históricas ni datos sociales en
cuarentena. Los archivos en `infra/secrets/*.example` contienen exclusivamente
valores ficticios.

### 2. Validar material y cliente

Ejecuta las comprobaciones que no requieren servicios locales:

```powershell
npm run validate
npm test
npm run --workspace examples/maplibre/app test:e2e -- --project=chromium
```

`npm run validate` comprueba formato, Markdown, HTML, CSS, inventario,
licencias, tipos TypeScript, pruebas unitarias y build Vite. El recorrido E2E
verifica OGC API - Features, errores de red, PMTiles, COG y Axe.

### 3. Iniciar y validar la infraestructura

El stack local usa PostGIS, GeoServer y Nginx. GeoServer se configura por REST,
sin pasos manuales en la interfaz administrativa:

```powershell
docker compose -f infra/compose.yaml up -d --build --wait
uv run python scripts/configure_geoserver.py
npm run validate:stack
```

La validación del stack comprueba WMS, WFS, OGC API - Features, MVT, STAC, HTTP
Range y CORS. Las interfaces se exponen solo en `localhost`:

- GeoServer: `http://localhost:18080/geoserver`
- Activos PMTiles y COG: `http://localhost:18081/assets/`

### 4. Ejecutar notebooks y restauración

Los notebooks funcionan con fixtures sin red y con el stack local. La prueba de
restauración inserta una fila centinela, crea un backup, elimina volúmenes,
restaura PostGIS y vuelve a configurar GeoServer:

```powershell
uv run python scripts/run_notebooks.py --mode fixtures
uv run python scripts/run_notebooks.py --mode local
uv run python scripts/test_restore.py --compose-file infra/compose.yaml --backup-dir .backups
```

Al terminar, el stack se puede detener y eliminar junto con los datos de
práctica mediante:

```powershell
docker compose -f infra/compose.yaml down --volumes
```

### 5. Generar y medir activos cloud-native

Los activos de práctica se generan a partir de fixtures sintéticos y
herramientas en contenedores con digest fijado:

```powershell
npm run data:build:pmtiles
npm run data:build:cog
npm run test:range
npm run benchmark:browser
npm run benchmark -- --route vector --runs 5
npm run benchmark -- --route raster --runs 5
```

Los reportes de benchmark se guardan en `.reports/` y no se versionan. El
benchmark de navegador mide hasta que MapLibre registra cada fuente; el
benchmark Python mide transporte HTTP. La aceptación curricular del objetivo de
rendimiento requiere que el instructor interprete las mediciones o apruebe una
excepción documentada.

### 6. Construir el artefacto estático

Construye la documentación Jekyll, el cliente MapLibre y el sitio ensamblado con
los ejemplos y activos aprobados:

```powershell
npm run --workspace examples/maplibre/app build
uv run python scripts/build_site.py --output _site_jekyll
uv run python scripts/assemble_site.py --jekyll-site _site_jekyll --leaflet-dir examples/leaflet --maplibre-dist examples/maplibre/app/dist --cloud-assets data/fixtures/cloud --output _site
npm run links:internal
```

Para previsualizarlo, sirve `_site/` por HTTP, nunca mediante `file://`:

```powershell
python -m http.server 8000 --directory _site
```

### 7. Ejecutar controles de seguridad

Gitleaks y Trivy se ejecutan desde imágenes fijadas. No añadas secretos,
credenciales ni tokens activos para resolver un fallo:

```powershell
uv run python scripts/security_scan.py --scope worktree
uv run python scripts/security_scan.py --scope dependencies
```

Las excepciones de seguridad deben ser específicas, justificadas, tener
responsable y vencimiento en `docs/governance/security-exceptions.yml`. Consulta
también [`docs/guias/seguridad.md`](docs/guias/seguridad.md).

### 8. Confirmar reproducibilidad desde un clon limpio

Antes de proponer una candidata, crea un clon nuevo fuera del repositorio y
repite las validaciones. Mantén el stack local iniciado si vas a ejecutar
`validate:stack`:

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

### 9. Preparar y ejecutar el piloto

Los artefactos de piloto no deben llenarse con resultados simulados:

- [`docs/governance/manual-accessibility-review.md`](docs/governance/manual-accessibility-review.md)
- [`docs/pilot/plan.md`](docs/pilot/plan.md)
- [`docs/pilot/results.md`](docs/pilot/results.md)
- [`docs/pilot/issues.md`](docs/pilot/issues.md)
- [`docs/pilot/browser-matrix.yml`](docs/pilot/browser-matrix.yml)

El responsable de web y accesibilidad debe registrar revisión manual de teclado,
foco, contraste, reflow, lector de pantalla y Safari real en macOS. El
instructor debe registrar participantes, horas, entregas, incidencias y la
decisión sobre la meta de rendimiento.

### 10. Preparar la candidata

El gate produce un reporte factual y se bloquea hasta que exista toda la
evidencia anterior:

```powershell
uv run python scripts/release_gate.py --mode prepared
```

El resultado queda en `.reports/release-gate.json`. Solo tras completar el
piloto y recibir autorización explícita para confirmar cambios puede prepararse
una candidata desde un commit limpio. Tags, releases y pushes requieren una
autorización adicional.

## Programa y autor

- [Programa vigente en revisión](Programa.md)
- Juan Carlos Méndez
- juan[~~at~~]gkudos.com

## Material histórico

Las unidades, guías, exportaciones y datos anteriores se mantienen versionados
para inventario y revisión. No se enlazan desde la navegación mantenida ni deben
tratarse como requisitos vigentes hasta que superen las revisiones de licencia,
accesibilidad, seguridad, privacidad y compatibilidad.
