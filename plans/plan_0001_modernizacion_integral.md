# plan_0001 - Implementar integralmente la modernizacion del curso

**Fecha**: 2026-08-03
**Ambito**: documentacion, curriculo, datos, ejemplos web, notebooks, infraestructura, pruebas, seguridad, accesibilidad y publicacion
**Estado**: propuesto; implementacion no iniciada
**Prioridad**: bloqueante y secuencial

Este ExecPlan es un documento vivo. Las secciones `Progress`, `Surprises & Discoveries`, `Decision Log` y `Outcomes & Retrospective` deben mantenerse actualizadas durante la ejecucion. Este documento se mantiene conforme a `PLANS.md`; tambien debe respetar `AGENTS.md`, `UPGRADE_PLAN.md` y `DESIGN.md`.

## Proposito / Panorama general

El proposito es transformar el material historico de 2020 en un curso que pueda ejecutarse y verificarse desde un clon limpio, sin depender de servidores de cohortes anteriores, cuentas personales, tokens activos ni datos personales sin autorizacion. Al completar este plan, una persona podra recorrer ocho unidades actualizadas, preparar datos mediante un proceso reproducible, comparar WFS con OGC API - Features, levantar PostGIS y GeoServer localmente, usar un cliente TypeScript con MapLibre, consumir PMTiles y COG mediante solicitudes HTTP parciales, producir un artefacto web estatico y ejecutar localmente las mismas validaciones que usa la integracion continua.

El resultado visible no sera una sola aplicacion que reemplace al curso. El repositorio conservara cuatro tipos de artefactos claramente separados: documentacion docente, ejemplos pequenos mantenidos, datos de practica con manifiestos y servicios locales reproducibles. Leaflet seguira siendo la introduccion de bajo umbral. MapLibre sera el cliente del proyecto integrador. WMS y WFS se conservaran para compatibilidad, OGC API Common y OGC API - Features formaran el nucleo moderno, y STAC estatico describira los activos espaciotemporales. Cada proyecto elegira una sola ruta optimizada: MVT dentro de PMTiles para datos vectoriales o COG para datos raster.

La implementacion debe caber en el contrato curricular de 32 horas presenciales y 40 horas autonomas. Records, Processes, EDR, Coverages, Zarr, GeoParquet, OpenLayers avanzado y 3D permaneceran como panorama o material electivo y no podran bloquear la finalizacion del nucleo.

## Progress

- [x] (2026-08-03T14:08:57Z) Se leyeron `PLANS.md`, `AGENTS.md`, `UPGRADE_PLAN.md` y `DESIGN.md`, y se inspecciono el arbol historico para preparar este ExecPlan.
- [x] (2026-08-03T14:08:57Z) Se confirmo que no existia otro ExecPlan en `plans/` y se asigno el consecutivo `0001`.
- [x] (2026-08-03T14:08:57Z) Se creo este ExecPlan; no se inicio ningun hito de implementacion.
- [x] (2026-08-03T14:19:52Z) Se reviso el ExecPlan contra `PLANS.md` y se cerraron decisiones, dependencias entre prototipos, validadores y recorridos de recuperacion.
- [x] (2026-08-03T14:37:11Z) Se completo una revision operativa final de workspaces, Jekyll, Range/MapLibre, restauracion, licencias, seguridad y gate de candidato.
- [x] (2026-08-03T14:53:47Z) Se crearon los artefactos locales de Hito 0 y `uv run python scripts/validate_resources.py` validó 30 entradas contra 263 archivos versionados.
- [x] (2026-08-03T15:14:58Z) Se fijaron digests de Gitleaks/Trivy, se sanitizaron cinco tokens del árbol actual y ambos escaneos completaron sin hallazgos bloqueantes del árbol actual.
- [x] (2026-08-03T15:14:58Z) Se asignó al instructor del curso como autoridad de los cuatro roles y aprobador de excepciones.
- [x] (2026-08-03T15:14:58Z) Se confirmó la baja de la cuenta Mapbox que emitía los tokens históricos y se registró la revocación.
- [x] (2026-08-03T15:14:58Z) Se completó el Hito 0: inventario, cuarentena, licencias, secretos, matriz de versiones, autoridad y escaneos iniciales.
- [x] (2026-08-03T15:44:52Z) Se completó el Hito 1: sitio Jekyll mínimo, exclusión temporal del material histórico, validadores locales, CI de referencia y pruebas negativas.
- [x] (2026-08-03T15:59:01Z) Se completó el Hito 2: programa de ocho unidades, rúbricas, prerrequisitos, trazabilidad y fixtures sintéticos con checksum estable.
- [x] (2026-08-03T16:13:02Z) Se completó el Hito 3: unidades fundamentales, mapa Leaflet accesible, pipeline GeoJSON→GeoPackage determinista y pruebas de navegador.
- [x] (2026-08-03T16:38:43Z) Se completó el Hito 4: WFS/OGC API/OpenAPI, STAC estático y tres notebooks deterministas en modo fixtures.
- [x] (2026-08-03T18:07:19Z) Se completó el Hito 5A: GeoServer/PostGIS, WMS/WFS/Features/MVT, COG, PMTiles, Range/CORS y MapLibre validados en prototipos aislados.
- [x] (2026-08-03T18:18:15Z) Se completó el Hito 5B: Compose reconstruye PostGIS, GeoServer y Nginx; los notebooks pasan en modos fixtures/local y la restauración preserva una fila centinela.
- [ ] Hito 6 en curso: workspace TypeScript/Vite/MapLibre carga OGC API - Features, mantiene estado URL, tabla equivalente, diálogo con foco y E2E en Chromium/Firefox/WebKit; falta revisión WCAG manual y evidencia Safari real del piloto.
- [ ] Hito 7 en curso: PMTiles y COG se regeneran con contenedores fijados, STAC, Range/CORS, conmutación MapLibre y benchmark HTTP de cinco repeticiones pasan; falta instrumentación de renderizado en navegador y criterio comparativo de aceptación.
- [ ] Completar el Hito 6: cliente TypeScript/Vite/MapLibre mantenible.
- [ ] Completar el Hito 7: PMTiles, COG, STAC y benchmark reproducible.
- [ ] Completar el Hito 8: seguridad, CI, build, restauracion y documentacion operativa.
- [ ] Completar el Hito 9: piloto, ajustes de carga y version candidata.
- [ ] Actualizar este plan despues de cada punto de pausa con estado, evidencia, decisiones y resultados reales.
- [ ] Crear commits solo si el usuario autoriza explicitamente confirmarlos durante esta ejecucion.

## Surprises & Discoveries

- Observacion: el repositorio mezcla documentacion Markdown, ocho PDF docentes, datos, notebooks, capturas, HTML mantenido y dos arboles QGIS2Web generados. No existe una separacion actual entre fuente docente, salida generada y material historico.
  Evidencia: `01_Fundamentos/`, `02_Conceptos/ejemplo_qgis2web/`, `02_Conceptos/qgis2web_world_borders/`, `04_Servicios_Web_Geoservicios_OGC/` y los directorios `05` a `08`.

- Observacion: los datos sociales no son fixtures pequenos. `03_Cartografia/example/geotweets.csv`, `03_Cartografia/example/geotweets.geojson`, `03_Cartografia/example/kepler.gl.html` y `07_Servicios_Cloud/datos/tweets_2018_shp.zip` contienen o reproducen informacion geolocalizada que debe permanecer en cuarentena.
  Evidencia: los encabezados y muestras contienen identificadores, usuarios, fechas y coordenadas; `AGENTS.md` prohibe copiarlos o transformarlos mientras no se resuelva su uso.

- Observacion: hay tokens Mapbox y endpoints HTTP historicos en ejemplos y documentacion. Eliminar el texto del arbol no revoca una credencial, y revisar el historial no autoriza reescribirlo.
  Evidencia: `01_Fundamentos/ejemplo_leaflet.html`, `02_Conceptos/html/leaflet_geojson_simple.html`, `03_Cartografia/example/kepler.gl.html`, `04_Servicios_Web_Geoservicios_OGC/html/leaflet_wms_2.html`, `05_Servidores_Mapas/Readme.md` y varias referencias en `Programa.md`.

- Observacion: `package.json` no describe una aplicacion. El unico script es `npm run precommit`, que escribe Markdown y ejecuta `git add`; por tanto no se puede reutilizar como validacion de solo lectura.
  Evidencia: `package.json` y `package-lock.json`.

- Observacion: no existen actualmente `docs/`, `examples/`, `infra/`, `data/`, `.github/`, scripts SQL/Python, `compose.yaml`, PMTiles, COG, STAC, OpenAPI ni cliente TypeScript.
  Evidencia: inspeccion del arbol versionado al redactar este plan.

- Observacion: los notebooks historicos conservan salidas y dependencias antiguas, dependen de red y al menos uno desactiva la verificacion TLS. No son una base determinista para CI.
  Evidencia: `04_Servicios_Web_Geoservicios_OGC/ejemplo_python_wfs.ipynb` y `04_Servicios_Web_Geoservicios_OGC/ejemplo_wms.ipynb`.

- Observacion: `DESIGN.md` propone `#a3a3a3` como texto auxiliar sobre blanco y una presentacion sin estados visibles. Esas decisiones no cumplen automaticamente WCAG 2.2 AA.
  Evidencia: `AGENTS.md` ya restringe el uso de `#a3a3a3`, exige foco visible, enlaces distinguibles y alternativas para mapas.

- Observacion: el validador inicial de recursos cubre los 263 archivos versionados sin copiar datos sociales ni valores de tokens.
  Evidencia: `uv run python scripts/validate_resources.py` informo "Validated 30 inventory entries and 263 tracked files." el 2026-08-03T14:50:40Z.

- Observacion: Docker Desktop no tiene servidor disponible en este equipo, por lo que Gitleaks y Trivy fijados en contenedores no se pueden ejecutar todavia.
  Evidencia: `docker info --format '{{.ServerVersion}}'` devolvio que no existe la tuberia `//./pipe/docker_engine` el 2026-08-03T14:50:40Z.

- Observacion: el usuario declaró que los tokens Mapbox históricos ya fueron revocados, pero eligió mantener roles genéricos y no aportó evidencia de revocación. Docker seguía sin servidor después de indicar que lo iniciaría.
  Evidencia: respuestas del usuario y `docker info --format '{{.ServerVersion}}'` del 2026-08-03T14:53:47Z.

- Observacion: Docker se habilitó posteriormente. Gitleaks escaneó 305 commits y reportó tres tokens históricos más dos falsos positivos de `Leaflet.VectorGrid`; el árbol actual pasó después de retirar cinco valores de token. Trivy no reportó hallazgos altos o críticos.
  Evidencia: Gitleaks con digest `sha256:b5918eb...9ebc4` y Trivy con digest `sha256:029e99...2ceac` completados el 2026-08-03T15:14:58Z.

- Observacion: la construcción Jekyll desde la raíz confirma que las exclusiones temporales omiten los nueve directorios históricos. El tema histórico Hacker emite avisos de deprecación Sass.
  Evidencia: construcción con `ruby@sha256:347edd...113c5` del 2026-08-03T15:50:21Z; no se encontró ningún directorio histórico en `.preview/root`.

- Observacion: el primer intento de generar el fixture GeoTIFF falló porque Rasterio leyó una base PROJ antigua de la instalación local de PostGIS.
  Evidencia: `proj.db` en `C:\Program Files\PostgreSQL\15\share\contrib\postgis-3.4\proj` tenía una versión de layout incompatible el 2026-08-03T15:54:53Z.

- Observacion: forzar `PROJ_DATA` y `PROJ_LIB` al paquete Rasterio resolvió la colisión de PROJ. Los tres fixtures se generan dos veces con checksums idénticos.
  Evidencia: `uv run pytest tests/data` pasó y `scripts/generate_fixtures.py` produjo los SHA-256 registrados el 2026-08-03T15:59:01Z.

- Observacion: el primer GeoPackage generado por GDAL no fue binariamente determinista porque incluía una fecha interna variable.
  Evidencia: dos conversiones idénticas produjeron SHA-256 diferentes el 2026-08-03; se fijó `OGR_CURRENT_DATE` para estabilizar el metadato.

- Observacion: el ensamblador inicial omitía el directorio Leaflet y Linkinator detectó un enlace roto desde la Unidad 1.
  Evidencia: `_site/examples/leaflet/mapa_basico` devolvió 404 antes de que `build_site.py` copiara el ejemplo el 2026-08-03.

- Observacion: los fixtures locales permiten explicar WFS, OGC API - Features y OpenAPI sin consultar servicios externos.
  Evidencia: `data/fixtures/responses/ogc-clasico/`, `data/fixtures/responses/ogc-api-features/` y `data/fixtures/openapi/features.json` se validaron como JSON o XML bien formado el 2026-08-03T16:23:29Z.

- Observacion: `stac-valid` 4.2.1 instaló un ejecutable que no encontró su módulo interno en este entorno Windows.
  Evidencia: `uv run stac-valid --help` devolvió `ModuleNotFoundError`; `stac-validator` 4.1.2 validó Catalog, Collection e Item correctamente.

- Observacion: las imágenes oficiales candidatas de GeoServer 3.0.0 y PostGIS 17-3.5 se descargaron correctamente.
  Evidencia: digests `sha256:d8ff66...50ee7` y `sha256:45f2a6...48ea9` registrados el 2026-08-03.

- Observacion: GeoServer 3.0.0 oficial inició con PostGIS y vector tiles, pero `/geoserver/ogc/features/v1` devolvió HTTP 404.
  Evidencia: prototipo `infra/prototypes/geoserver/compose.yaml` y log del 2026-08-03T16:46:44Z; la configuración no se promovió.

- Observacion: el Dockerfile alternativo con el plugin OGC API - Features verificado respondió HTTP 200 en `/geoserver/ogc/features/v1`.
  Evidencia: build `cartografia-web/geoserver-ogcapi-features:3.0.0-prototype` y Compose saludable el 2026-08-03.

- Observacion: el COG sintético se sirvió correctamente con HTTP 206 y CORS restringido mediante Nginx.
  Evidencia: `infra/prototypes/range/validate_range.py` pasó contra `referencia.cog.tif` el 2026-08-03.

- Observacion: Planetiler generó y el CLI oficial verificó `referencia.pmtiles`, que Nginx sirvió con HTTP 206 y CORS restringido.
  Evidencia: `infra/prototypes/tools/build_pmtiles.py` y `validate_range.py --asset referencia.pmtiles` pasaron el 2026-08-03.

- Observacion: WMS, WFS y OGC API - Features pasaron el smoke test, pero MVT devolvió HTTP 400 por formato no soportado.
  Evidencia: `infra/prototypes/geoserver/smoke.py` del 2026-08-03.

- Observacion: el endpoint MVT correcto es WMS GetMap con `format=application/vnd.mapbox-vector-tile`, no la ruta GeoWebCache usada inicialmente.
  Evidencia: HTTP 200, 159 bytes y `Content-Type: application/vnd.mapbox-vector-tile` el 2026-08-03T18:07:19Z.

- Observacion: el stack promovido reconstruyó el workspace, datastore, capa y estilo desde un volumen PostGIS vacío.
  Evidencia: `docker compose -f infra/compose.yaml up -d --build --wait`, `scripts/configure_geoserver.py` y `infra/smoke/smoke_stack.py` pasaron el 2026-08-03.

- Observacion: la restauración limpia preservó la fila centinela y recuperó WMS, WFS, OGC API - Features, MVT, Range y CORS.
  Evidencia: `scripts/test_restore.py --compose-file infra/compose.yaml --backup-dir .backups` pasó el 2026-08-03.

## Decision Log

- Decision: ejecutar los hitos en el orden de este plan y tratar Hito 0, Hito 1 y Hito 5A como puertas bloqueantes.
  Justificacion: las fases posteriores no deben reutilizar datos, licencias o servicios cuya seguridad y compatibilidad aun no se hayan demostrado.
  Fecha/Autor: 2026-08-03 / OpenCode.

- Decision: conservar Jekyll como generador de la documentacion y alojar la aplicacion Vite en `examples/maplibre/app/` como artefacto separado. El prototipo corregira rutas y configuracion; no elegira otro generador.
  Justificacion: `_config.yml` demuestra el flujo editorial actual; fijar una sola herramienta evita trasladar una decision de arquitectura al ejecutor y separar Vite evita convertir todo el curso en una aplicacion.
  Fecha/Autor: 2026-08-03 / OpenCode.

- Decision: crear primero un fixture sintetico y no migrar ningun dataset historico a `data/fixtures/` hasta completar su manifiesto.
  Justificacion: ningun dataset actual documenta todavia fuente, propietario, version, checksum, licencia, CRS, esquema y sensibilidad en un unico registro verificable.
  Fecha/Autor: 2026-08-03 / OpenCode.

- Decision: no mover los datos sociales a `archive/`; solo se excluiran del build mientras permanezcan en cuarentena.
  Justificacion: mover o copiar sigue siendo tratamiento y redistribucion. Una eventual eliminacion del arbol o reescritura del historial requiere una decision legal y, para el historial, autorizacion explicita.
  Fecha/Autor: 2026-08-03 / OpenCode.

- Decision: usar TypeScript, Vite, MapLibre y CSS nativo sin React, Vue, Svelte ni Tailwind en el nucleo.
  Justificacion: es el contrato de `AGENTS.md`, reduce dependencias curriculares y permite aplicar directamente los tokens de `DESIGN.md`.
  Fecha/Autor: 2026-08-03 / OpenCode.

- Decision: el primer candidato sera GeoServer 3.0.0 con Java 21 y `postgis/postgis:17-3.5`. Se probara primero la imagen oficial GeoServer con extensiones de la misma version. Si no permite instalar OGC API - Features y Vector Tiles, la unica alternativa sera un Dockerfile propio con el WAR 3.0.0 y los ZIP oficiales de esas extensiones. No se probaran servidores distintos dentro de este plan.
  Justificacion: la compatibilidad de OGC API - Features y Vector Tiles con la imagen es el principal riesgo tecnico y debe observarse, no suponerse.
  Fecha/Autor: 2026-08-03 / OpenCode.

- Decision: usar Nginx como servidor estatico definitivo para HTTP Range y CORS; no se introduce Caddy como alternativa en este plan.
  Justificacion: Nginx sirve archivos con Range de forma conocida y permite una configuracion CORS pequena, versionada y observable.
  Fecha/Autor: 2026-08-03 / OpenCode.

- Decision: hacer de `npm run validate` el contrato agregado de validacion local. Puede generar builds unicamente dentro de un directorio temporal del sistema que elimina al terminar; no modifica fuentes, lockfiles, fixtures, indice Git ni artefactos persistentes. Los comandos de escritura, limpieza de volumenes o regeneracion tendran nombres separados.
  Justificacion: Linkinator necesita un build, pero la comprobacion normal debe dejar el arbol exactamente como estaba.
  Fecha/Autor: 2026-08-03 / OpenCode.

- Decision: usar npm workspaces en la raiz. Hito 5A registrara `infra/prototypes/maplibre-protocols` y Hito 6 agregara `examples/maplibre/app`. Ambos permanecen hasta cerrar el plan y comparten un solo `package-lock.json`; los scripts raiz los invocan mediante `npm run --workspace`.
  Justificacion: un unico lockfile permite que `npm ci` y `npm run validate` instalen y validen todo el frontend sin comandos condicionales ni dependencias ocultas.
  Fecha/Autor: 2026-08-03 / OpenCode.

- Decision: implementar los generadores, validadores, configuracion GeoServer, backup, restauracion, smoke tests y benchmark como scripts Python con interfaces de linea de comandos. Los scripts pueden invocar contenedores fijados, pero no se crearan variantes PowerShell y shell de la misma operacion.
  Justificacion: una implementacion Python unica reduce divergencias entre Windows, macOS y Linux y permite pruebas con pytest.
  Fecha/Autor: 2026-08-03 / OpenCode.

- Decision: configurar GeoServer exclusivamente mediante `scripts/configure_geoserver.py` y la REST API. El repositorio no versionara un data directory completo.
  Justificacion: los scripts idempotentes hacen explicita la configuracion, evitan credenciales dentro del data directory y permiten reconstruir desde volumenes vacios.
  Fecha/Autor: 2026-08-03 / OpenCode.

- Decision: `data/manifests/datasets.yml` sera la unica fuente de verdad para datasets y fixtures. `docs/governance/resource-inventory.yml` referenciara sus IDs y no duplicara metadatos de datasets.
  Justificacion: una sola fuente evita divergencias entre inventario, archivos, STAC y documentacion.
  Fecha/Autor: 2026-08-03 / OpenCode.

- Decision: usar Gitleaks 8.24.2 y Trivy 0.59.1 como candidatos iniciales ejecutados desde contenedores. Hito 0 registrara sus digests antes de usarlos como controles bloqueantes.
  Justificacion: fijar version y digest hace repetible el significado de un escaneo; el escaneo del arbol sera bloqueante y la auditoria historica sera informativa con evidencia de revocacion.
  Fecha/Autor: 2026-08-03 / OpenCode.

- Decision: mantener `Programa.md` como fuente curricular canonica. `scripts/sync_program.py` generara `docs/programa.md` y una validacion impedira divergencias.
  Justificacion: `AGENTS.md` y `UPGRADE_PLAN.md` ya reconocen `Programa.md` como fuente de verdad; conservarlo evita cambiar ese contrato durante la misma migracion.
  Fecha/Autor: 2026-08-03 / OpenCode.

- Decision: Playwright WebKit sera una deteccion temprana y Safari real se validara en Hito 9. El responsable web debe conseguir dos entornos macOS con las dos ultimas versiones estables disponibles antes del piloto.
  Justificacion: WebKit automatizado no sustituye Safari, y esta dependencia externa debe ser visible antes de aceptar el curso.
  Fecha/Autor: 2026-08-03 / OpenCode.

- Decision: distinguir tres estados finales. `candidate-prepared` significa cambios sin confirmar validados en el arbol actual; `candidate-ready` exige un commit autorizado y reproduccion desde un clon o worktree limpio; `released` exige autorizacion adicional para tag, release o push.
  Justificacion: una prueba literal desde clon no puede incluir cambios sin confirmar, pero las restricciones Git impiden crear el commit sin permiso.
  Fecha/Autor: 2026-08-03 / OpenCode.

- Decision: no crear commits, tags, releases o pushes sin autorizacion explicita del usuario.
  Justificacion: `AGENTS.md` limita las operaciones Git aunque `PLANS.md` recomiende commits frecuentes durante una ejecucion autorizada.
  Fecha/Autor: 2026-08-03 / OpenCode.

- Decision: pausar Hito 0 despues de completar los artefactos que no requieren autoridad externa.
  Justificacion: la asignacion de responsables institucionales, la evidencia de revocacion de tokens y la disponibilidad del servidor Docker son condiciones expresas de aceptacion que un agente no puede declarar por cuenta propia.
  Fecha/Autor: 2026-08-03 / OpenCode.

- Decision: registrar la revocacion declarada como `claimed-revoked-evidence-pending` y los cuatro responsables como roles genericos sin autoridad.
  Justificacion: conserva la afirmacion del usuario sin convertirla en evidencia verificable ni habilitar aprobaciones institucionales inexistentes.
  Fecha/Autor: 2026-08-03 / OpenCode.

- Decision: asignar al instructor del curso como responsable curricular, de datos/licencias, web/accesibilidad e infraestructura/seguridad, y como aprobador de excepciones.
  Justificacion: el usuario estableció que la autoridad corresponde al instructor del curso.
  Fecha/Autor: 2026-08-03 / OpenCode.

- Decision: considerar revocados los tokens históricos de Mapbox mediante la baja confirmada de la cuenta que los emitía.
  Justificacion: el usuario confirmó la baja de la cuenta, el instructor del curso es la autoridad asignada y los valores se retiraron del árbol actual. El historial permanece sin reescritura.
  Fecha/Autor: 2026-08-03 / OpenCode.

- Decision: conservar `_config.yml` en la raíz como barrera temporal de exclusión del material histórico hasta que Hito 8 publique el sitio ensamblado aprobado.
  Justificacion: eliminarlo después de dos builds de `docs/` reactivaría la publicación raíz de rutas históricas. La exclusión explícita protege datos y recursos pendientes mientras el despliegue definitivo se implementa.
  Fecha/Autor: 2026-08-03 / OpenCode.

- Decision: mantener `jekyll-theme-hacker` solo para la barrera temporal de exclusión de la raíz y no usarlo para el sitio mantenido construido desde `docs/`.
  Justificacion: permite que la configuración raíz se construya y excluya material histórico, mientras el sitio mantenido usa la plantilla y CSS accesibles definidos en Hito 1.
  Fecha/Autor: 2026-08-03 / OpenCode.

- Decision: fijar `PROJ_DATA` y `PROJ_LIB` al directorio `rasterio/proj_data` del entorno virtual antes de importar Rasterio.
  Justificacion: evita que el fixture reproducible dependa de una instalación local incompatible de PostGIS o PROJ.
  Fecha/Autor: 2026-08-03 / OpenCode.

- Decision: adoptar la ponderación propuesta de 20% ejercicios y diagnósticos, 10% quizzes, 20% Entrega 1, 20% Entrega 2 y 30% Entrega 3.
  Justificacion: el instructor del curso es la autoridad curricular asignada y no indicó una ponderación alternativa.
  Fecha/Autor: 2026-08-03 / OpenCode.

- Decision: fijar `OGR_CURRENT_DATE` en la conversión GDAL del fixture GeoPackage.
  Justificacion: la marca temporal interna variable impedía comprobar determinismo mediante checksum.
  Fecha/Autor: 2026-08-03 / OpenCode.

- Decision: hacer que `build_site.py` ensamble automáticamente Leaflet cuando exista.
  Justificacion: garantiza que las unidades mantenidas no enlacen ejemplos ausentes del artefacto estático final.
  Fecha/Autor: 2026-08-03 / OpenCode.

- Decision: usar temporalmente `stac-validator` 4.1.2 en lugar de `stac-valid` 4.2.1.
  Justificacion: el reemplazo anunciado falló durante su inicialización en el entorno fijado, mientras que 4.1.2 validó los tres documentos STAC. Se reevaluará antes de Hito 8.
  Fecha/Autor: 2026-08-03 / OpenCode.

- Decision: descartar la imagen oficial de GeoServer 3.0.0 con solo `vectortiles` para el prototipo OGC API.
  Justificacion: el endpoint obligatorio OGC API - Features no existe en esa configuración. Se debe construir la alternativa con el módulo específico antes de promover cualquier stack.
  Fecha/Autor: 2026-08-03 / OpenCode.

- Decision: promover provisionalmente el Dockerfile con el plugin OGC API - Features a la prueba de configuración REST.
  Justificacion: el checksum del ZIP fue verificado y la landing page OGC API respondió HTTP 200; faltan capa y smoke tests para aprobar el hito.
  Fecha/Autor: 2026-08-03 / OpenCode.

- Decision: usar Planetiler y el CLI oficial PMTiles como ruta estática vectorial en lugar de Tippecanoe.
  Justificacion: Planetiler produce PMTiles directamente desde GeoJSON/GeoPackage con una imagen pública accesible y Apache-2.0; la imagen Tippecanoe candidata requirió acceso no disponible.
  Fecha/Autor: 2026-08-03 / OpenCode.

- Decision: permitir recomendar herramientas de software libre con licencia compatible para uso personal sin aprobación o licenciamiento adicional.
  Justificacion: el usuario confirmó que las herramientas sugeridas se ejecutan en computadores personales. La excepción no cubre datos, imágenes, fuentes, PDF, código vendorizado ni SaaS de terceros, que conservan su revisión de procedencia y licencia.
  Fecha/Autor: 2026-08-03 / OpenCode.

- Decision: añadir `.gitleaksignore` solo para las dos huellas de falsos positivos del código QGIS2Web generado; no incluir los tokens Mapbox históricos en la allowlist.
  Justificacion: mantiene el escaneo del árbol útil sin suprimir credenciales históricas que requieren evidencia de revocación.
  Fecha/Autor: 2026-08-03 / OpenCode.

## Outcomes & Retrospective

La planificación inicial y los Hitos 0 a 4 están completos. El repositorio tiene inventario, esquemas, políticas iniciales, candidatos de versión, cuarentena declarativa, un validador ejecutable, escaneos de seguridad con digests fijados, autoridad asignada al instructor y revocación Mapbox confirmada. El sitio mínimo se construye mediante Jekyll en un contenedor Ruby, se ensambla sin material histórico y supera formato, lint, validación estructurada, pruebas negativas y enlaces internos. El currículo de ocho unidades, las rúbricas, los prerrequisitos y los fixtures sintéticos son verificables. El ejemplo Leaflet funciona sin token ni jQuery y presenta filtro, estado, tabla y pruebas de accesibilidad. WFS, OGC API - Features, OpenAPI y STAC se enseñan con fixtures y notebooks sin red. La infraestructura reproducible y los ejemplos de APIs modernas aún no existen. Al cerrar cada hito, esta sección debe indicar qué comportamiento nuevo quedó disponible, qué criterios pasaron, qué trabajo se descartó o pospuso, cuánto tiempo curricular consumió y qué lección cambia los hitos posteriores.

## Contexto y orientacion

La raiz de trabajo es `C:\opt\work\personal\cartografia_web`. Todos los comandos de este plan se ejecutan desde esa ruta salvo que se indique expresamente otro directorio mediante `workdir`. Las rutas nombradas en el resto del documento son relativas a esa raiz.

`UPGRADE_PLAN.md` es la hoja de ruta curricular y tecnica. `PLANS.md` define la forma de este ExecPlan. `AGENTS.md` contiene reglas bloqueantes sobre seguridad, privacidad, licencias, accesibilidad, Git y alcance. `DESIGN.md` es una referencia visual subordinada a la semantica, la funcion cartografica y WCAG 2.2 AA. `Programa.md` y los `Readme.md` de las unidades representan el curso historico que debe migrarse, no copiarse literalmente.

El arbol actual usa `00_Intro/` a `08_Arquitectura_SIG/`. `01_Fundamentos/` contiene HTML y Leaflet; `02_Conceptos/` contiene datos y dos exportaciones QGIS2Web; `03_Cartografia/` contiene teoria cartografica y datos sociales en cuarentena; `04_Servicios_Web_Geoservicios_OGC/` contiene notebooks y WMS/WFS; `05_Servidores_Mapas/` y `Geoserver.md` describen infraestructura manual antigua; `06_Simbologia/` contiene SLD y vector tiles; `07_Servicios_Cloud/` contiene SaaS y datos; `08_Arquitectura_SIG/` contiene arquitectura, GeoNode y Kepler. El contenido historico debe seguir disponible en Git mientras se construye la nueva ruta, pero no necesariamente formar parte del sitio publico.

Un fixture es un archivo pequeno y estable creado para ejercicios y pruebas. Un manifiesto de dataset es un registro que declara procedencia, version, checksum, licencia, sistema de coordenadas, esquema y sensibilidad. Un checksum es una huella calculada del archivo que permite comprobar que no cambio. Un CRS es el sistema de referencia de coordenadas. Un smoke test es una prueba corta que confirma que un sistema arranca y responde en sus rutas esenciales.

OGC API - Features es una API HTTP moderna para consultar colecciones de entidades geograficas. WFS es el servicio OGC clasico equivalente que se conserva para compatibilidad. STAC es un conjunto de documentos JSON enlazados que describe activos espaciotemporales. MVT es una codificacion de entidades vectoriales por tesela. PMTiles empaqueta muchas teselas en un solo archivo. COG es un GeoTIFF ordenado para leer solo los bytes necesarios. HTTP Range es la capacidad de solicitar un intervalo de bytes y recibir `206 Partial Content`; PMTiles y COG dependen de ella para evitar descargar el archivo completo.

Jekyll es el generador que convierte Markdown y plantillas del directorio `docs/` en HTML estatico. Vite es la herramienta que compila la aplicacion TypeScript del directorio `examples/maplibre/app/`. CI, o integracion continua, es la ejecucion automatica de las mismas validaciones locales ante cambios del repositorio. Un lockfile registra versiones exactas de dependencias. Un digest identifica de forma inmutable una imagen de contenedor. Docker Compose describe y levanta varios contenedores como un solo stack.

CORS son cabeceras HTTP que autorizan a una pagina de un origen a solicitar recursos de otro. CSP es una politica del navegador que limita desde donde puede cargarse codigo o contenido. TLS cifra las conexiones HTTPS. REST es una forma de configurar o consultar recursos mediante HTTP. OpenAPI es un documento procesable que describe rutas, parametros y respuestas de una API. CQL2 es un lenguaje OGC para expresar filtros. Un kernel de notebook es el proceso Python que ejecuta sus celdas.

SLD es un documento XML que define como dibujar una capa. GiST es el tipo de indice que PostGIS usa para acelerar consultas espaciales. WebGL es la capacidad del navegador usada por MapLibre para renderizar. Playwright automatiza navegadores; Axe detecta algunos problemas de accesibilidad, pero no demuestra conformidad completa. RPO es la cantidad maxima de datos que se acepta perder tras un incidente y RTO es el tiempo objetivo para restaurar el servicio.

La distribucion curricular es fija para el primer piloto. Las unidades 1 a 8 tienen cuatro horas presenciales cada una. El trabajo autonomo por unidad es, en ese orden, 4, 5, 4, 5, 6, 6, 5 y 5 horas. El nucleo obligatorio incluye HTML semantico, JavaScript moderno, Leaflet, QGIS, GeoPackage, GeoJSON, calidad y procedencia, cartografia accesible, HTTP, WMS/WFS, OGC API Common/Features, PostGIS, GeoServer, Docker Compose, TypeScript, Vite, MapLibre, STAC estatico y una ruta PMTiles o COG.

La referencia visual usa fondo blanco, texto principal negro, bandas `#e5e5e5` y `#d4d4d4`, superficies oscuras `#0a0a0a` y `#171717`, una familia sans serif con pesos 400/500, apariencia base `0.875rem`, interlineado 1.43, espaciado 6/8/12/48, radios cero y ausencia de sombras o degradados. No se usa `#a3a3a3` como texto sobre blanco. La interfaz mantiene encabezados semanticos, foco visible, enlaces distinguibles, reflow, controles cartograficos, leyenda, atribucion, estados y alternativa tabular aunque eso se aparte de la composicion de portafolio.

La estructura objetivo se creara gradualmente. `docs/` sera el origen mantenido del sitio; `examples/leaflet/mapa_basico/` contendra el ejemplo introductorio; `examples/maplibre/app/` sera la aplicacion principal; `notebooks/` contendra notebooks limpios; `infra/` contendra Compose, PostGIS, GeoServer, Nginx y smoke tests; `data/fixtures/` y `data/manifests/` contendran datos aprobados; `scripts/` contendra generacion y validacion; `archive/` solo recibira material que pueda conservarse legal y seguramente; `.github/workflows/` sera el adaptador CI de referencia.

No se haran movimientos masivos al crear esa estructura. Primero se publicara `docs/migration-inventory.md` con una decision por ruta o agrupacion generada. Durante la transicion, `README.md` seguira siendo el indice de la raiz y enlazara tanto la documentacion nueva como el material historico que siga autorizado.

## Plan de trabajo

### Hito 0: resolver gobierno, cuarentena, licencias, secretos y versiones

Este hito convierte riesgos actualmente implicitos en decisiones versionadas. Crear `pyproject.toml`, `uv.lock`, `docs/governance/resource-inventory.yml`, `docs/governance/third-party.yml`, `docs/governance/security-exceptions.yml`, `docs/governance/gitleaks-history-allowlist.yml`, `data/manifests/datasets.yml`, sus esquemas JSON, `docs/governance/licenses.md`, `THIRD_PARTY_NOTICES.md`, `docs/governance/security.md`, `docs/governance/revocations.md`, `docs/governance/roles.md`, `docs/governance/cohort-maintenance.md` y `docs/governance/version-matrix.yml`. El entorno Python inicial incluye PyYAML, jsonschema y pytest para validar estos artefactos; hitos posteriores amplian el mismo lockfile. El inventario debe cubrir archivos, agrupaciones generadas, enlaces, endpoints, tokens, datos, imagenes, PDF, fuentes y codigo de terceros. Para cada elemento registrara conservar, sustituir, archivar, eliminar o bloquear, junto con el motivo, licencia, responsable y hito.

`docs/governance/roles.md` definira y asignara cuatro roles: responsable curricular, responsable de datos/licencias, responsable web/accesibilidad y responsable de infraestructura/seguridad. Tambien registrara quien puede aprobar una excepcion de privacidad, licencia, rendimiento o vulnerabilidad; la politica institucional de cuentas y costes; y si existe un entorno de demostracion institucional. Los nombres pueden requerir informacion externa, pero Hito 0 queda bloqueado hasta que el usuario o la institucion los asigne. `docs/governance/cohort-maintenance.md` fijara una revision antes de cada cohorte para versiones, enlaces, datasets, costes y proveedores.

Los archivos `03_Cartografia/example/geotweets.csv`, `03_Cartografia/example/geotweets.geojson`, `03_Cartografia/example/kepler.gl.html` y `07_Servicios_Cloud/datos/tweets_2018_shp.zip` se marcaran `quarantine` y quedaran excluidos del futuro build. No se copiaran ni transformaran. Las capturas o fragmentos que muestren usuarios o coordenadas, incluidos `07_Servicios_Cloud/Readme.md` y `08_Arquitectura_SIG/Readme.md`, tambien recibiran una decision explicita.

Se ejecutara un escaneo del arbol y del historial con Gitleaks. Los valores encontrados se registraran por ruta y estado de revocacion sin copiar el secreto al inventario. El responsable de infraestructura/seguridad coordinara la revocacion con el propietario de la cuenta. `docs/governance/revocations.md` aceptara como evidencia la fecha, proveedor, identificador no sensible o ultimos cuatro caracteres, persona que confirmo la revocacion y referencia a una captura o ticket almacenado fuera del repositorio. Si no se puede confirmar, el estado sera `unverified`, el valor se retirara del arbol y ninguna publicacion o version candidata podra aprobarse. No se reescribira el historial.

La matriz de versiones registrara candidatos y soporte. El punto de partida sera QGIS 3.44 LTR, Node.js 24 LTS, Python 3.12, Ruby 3.3.6, Bundler 2.6.2, Jekyll 4.3.4, Java 21, GeoServer 3.0.0, `postgis/postgis:17-3.5` y `nginx:1.28.0-alpine`. GDAL, rio-cogeo, Tippecanoe, PMTiles CLI y las extensiones GeoServer se seleccionaran en este hito en una lista ordenada de candidatos con version exacta y fuente oficial; Hito 5A solo decidira promover el primer candidato o su alternativa ya indicada. Ningun ejecutor elegira una herramienta nueva fuera de esa lista.

`data/manifests/datasets.yml` sera la fuente canonica de metadatos. El inventario de recursos solo almacenara `dataset_id` cuando una ruta sea un dato. `docs/governance/third-party.yml` registrara nombre, version/digest, origen, licencia, tipo y uso para dependencias npm, Python, Ruby, contenedores, WAR, extensiones, herramientas, fuentes, imagenes y codigo vendorizado. Una licencia desconocida o incompatible bloquea redistribucion. `scripts/validate_resources.py` comprobara esquemas, IDs duplicados, archivos sin inventario, archivos publicos sin licencia, datos sin manifiesto, dependencias presentes en lockfiles pero ausentes del registro, imagenes no registradas y referencias STAC inexistentes. `npm run validate:licenses` invocara ese script y comprobara que `THIRD_PARTY_NOTICES.md` refleja el registro.

`docs/governance/security-exceptions.yml` exigira identificador, alcance, severidad, responsable, aprobador, justificacion y fecha de vencimiento; el vencimiento hace fallar la validacion. No admite secretos ni vulnerabilidades criticas directas. `gitleaks-history-allowlist.yml` solo contendra huellas no sensibles y referencias a `revocations.md`, nunca valores completos.

El hito termina cuando las cuatro responsabilidades estan asignadas, las politicas institucionales estan registradas, el validador lee los YAML, cada dataset redistribuido tiene manifiesto completo, cada recurso publico tiene licencia resuelta, Gitleaks no detecta secretos en el arbol actual, los hallazgos historicos tienen estado de revocacion y todo elemento en cuarentena tiene una exclusion explicita. Las decisiones tecnicas aun pendientes quedan limitadas a promover o descartar candidatos cerrados en Hito 5A, no a buscar alternativas abiertas.

### Hito 1: crear estructura editorial, sitio minimo y controles base

Este hito crea una ruta publica pequena sin mover todavia las unidades historicas. Crear `.ruby-version` con Ruby 3.3.6, `docs/index.md`, `docs/status.md`, `docs/_config.yml`, `docs/_layouts/default.html`, `docs/assets/css/tokens.css`, `docs/assets/css/site.css`, `Gemfile`, `Gemfile.lock` con Bundler 2.6.2 y Jekyll 4.3.4, `scripts/build_site.py` y `scripts/assemble_site.py`. Registrar esas versiones en la matriz y en prerrequisitos. Cada Markdown bajo `docs/` tendra front matter YAML con al menos `layout`, `title` y `permalink`; `docs/_config.yml` definira defaults equivalentes, pero no se confiara en defaults para procesar archivos sin front matter. Jekyll es la decision final; la prueba corrige rutas o configuracion, no selecciona otro generador. Despues de dos builds correctos, eliminar `_config.yml` de la raiz y configurar el workflow para publicar exclusivamente el artefacto ensamblado; no reemplazar YAML por texto arbitrario.

`tokens.css` definira los nombres de `DESIGN.md`: blanco y negro principales, bandas `#e5e5e5` y `#d4d4d4`, superficies oscuras y texto secundario permitido. Usara `0.875rem` como apariencia base, pesos 400/500, interlineado 1.43 para prosa, espacios 6/8/12/48, radios cero y ninguna sombra o degradado. No cargara ABC Oracle sin licencia; usara la pila del sistema. Los enlaces de prosa estaran subrayados y los controles tendran foco visible. No se usara `#a3a3a3` como texto sobre blanco.

Crear `docs/migration-inventory.md` con la disposicion de cada ruta actual y cada arbol generado. Corregir en `README.md` el enlace de la Unidad 8. Revisar `Programa.md`, todos los `Readme.md`, HTML y `Geoserver.md` para clasificar y programar la eliminacion de fechas de 2020, emergencia/COVID obligatorio, cuentas o issues personales, IPs historicas, HTTP inseguro, bibliografia obsoleta y recursos locales faltantes. Rotular Mapbox.js, ArcMap, Cartogram, CARTO/CartoCSS, GeoNode antiguo y QGIS2Web como historicos u optativos. Registrar individualmente la decision de cada PDF. No borrar todavia los directorios `00_Intro` a `08_Arquitectura_SIG`.

`scripts/assemble_site.py` recibira `--jekyll-site`, `--output` y los argumentos opcionales `--leaflet-dir`, `--maplibre-dist` y `--cloud-assets`. Copiara el build Jekyll, Leaflet a `examples/leaflet/`, MapLibre a `examples/maplibre/` y PMTiles/COG aprobados a `assets/data/` cuando esas entradas existan. En Hito 1 aun no existe ningun ejemplo nuevo, por lo que se pasan solo Jekyll y output. Para la vista local, Jekyll construira con `baseurl: ""` en `_site_local_jekyll/` y ensamblara en `_site/`. Para simular GitHub Pages, construira en `_site_preview_jekyll/` con `--baseurl /cartografia_web` y ensamblara en `.preview/cartografia_web/`. Todos los enlaces internos usaran `relative_url`; los ejemplos usaran rutas relativas. El artefacto candidato es siempre el sitio completo `_site/` o `.preview/cartografia_web/`, no el `dist/` intermedio de Vite.

Ampliar `pyproject.toml`/`uv.lock` con lxml. Actualizar `package.json` y `package-lock.json` para reemplazar el hook antiguo por comandos no mutantes e instalar desde este hito Playwright y Axe para el ejemplo Leaflet. El contrato inicial sera `format:check`, `lint:markdown`, `lint:html`, `lint:css`, `links:internal`, `validate:json`, `validate:xml`, `validate:licenses` y `validate:structured`; este ultimo sera un agregador de JSON, XML y licencias. Prettier comprobara formato, markdownlint-cli2 revisara Markdown, html-validate revisara HTML, Stylelint revisara CSS, AJV validara JSON/YAML contra esquemas, un script Python con lxml validara XML/SLD contra esquemas locales, y Linkinator comprobara enlaces internos del build. Crear fixtures invalidos en `tests/fixtures/invalid/`, excluidos de los globs normales, y `tests/validation/test_invalid_fixtures.py` debe invocar cada validador y esperar codigo distinto de cero. Crear `.github/workflows/validate.yml` con permisos `contents: read`, acciones fijadas por SHA y sin secretos. Cada paso ejecutara el mismo script local.

La prueba Jekyll construira una pagina, CSS y un enlace al estado del futuro cliente bajo el prefijo `/cartografia_web/`. Si una ruta falla, se corregiran `baseurl`, filtros `relative_url` o el ensamblador hasta que ambas variantes pasen. No se introducira otro generador.

El hito termina con un sitio minimo navegable y una validacion que falla de forma demostrable ante Markdown, HTML, CSS, JSON, XML/SLD, enlace o licencia invalidos. `README.md` debe explicar como construir y servir las variantes local y `/cartografia_web/`. La revision manual confirma encabezados semanticos, contraste en cada superficie, foco visible, enlaces distinguibles, zoom/reflow al 200%, texto alternativo y ausencia de bandas decorativas que desplacen contenido. La navegacion publica no contiene material en cuarentena, fechas/cohortes obligatorias de 2020, cuentas personales, IPs historicas ni recursos locales rotos.

### Hito 2: publicar programa, evaluacion, prerrequisitos y fixtures

Actualizar `Programa.md` como fuente canonica y crear `scripts/sync_program.py`, `docs/evaluacion/rubricas.md`, `docs/evaluacion/entrega_1.md`, `docs/evaluacion/entrega_2.md`, `docs/evaluacion/entrega_3.md`, `docs/guias/prerrequisitos.md`, `docs/guias/uso_responsable_ia.md` y `docs/governance/curriculum-traceability.yml`. `sync_program.py` generara `docs/programa.md` anteponiendo front matter Jekyll fijo al cuerpo exacto de `Programa.md`; `validate:curriculum` retirara ese front matter y fallara si el cuerpo difiere. El programa tendra ocho unidades de cuatro horas presenciales y distribuira las horas autonomas 4, 5, 4, 5, 6, 6, 5 y 5. Cada competencia nombrara la actividad, ejercicio, artefacto y criterio de rubrica que la demuestra.

Las entregas no requeriran cuentas SaaS. La primera producira un mapa publicable y accesible con uno o dos datasets. La segunda comparara WFS y OGC API - Features sobre la misma coleccion local. La tercera producira un sitio estatico ensamblado y elegira PMTiles o COG. Las rubricas evaluaran cartografia, calidad de datos, interoperabilidad, WCAG 2.2 AA, seguridad, rendimiento, reproducibilidad y comunicacion. La evaluacion propuesta sera: ejercicios y diagnosticos 20%, quizzes conceptuales 10%, Entrega 1 20%, Entrega 2 20% y Entrega 3 30%. El responsable curricular debe aprobarla en `docs/governance/roles.md`; Hito 2 queda bloqueado si la institucion exige otra ponderacion, que debera registrarse en `Decision Log` antes de cambiarla.

Ampliar `pyproject.toml` y `uv.lock`, crear `scripts/generate_fixtures.py` y pruebas en `tests/data/`. El generador producira una coleccion vectorial sintetica pequena en GeoJSON, una tabla CSV sin personas reales y un GeoTIFF sintetico sin optimizar. La salida vectorial usara EPSG:4326, identificadores estables y atributos suficientes para filtros y clasificacion. El raster tendra CRS, resolucion, NoData y fecha deterministas. Todos se registraran en la fuente canonica `data/manifests/datasets.yml` y validaran contra `data/schemas/dataset-manifest.schema.json`.

`docs/governance/curriculum-traceability.yml` enumerara por unidad los temas obligatorios, archivo docente, ejercicio, prueba y rubrica. Incluira modulos ES, `fetch`, GeoPackage, GeoJSON, CRS, orden de coordenadas, precision, procedencia, clasificacion, incertidumbre, paletas no dependientes solo del color, WCAG, HTTP, OGC, PostGIS, GeoServer, TypeScript, MapLibre, PMTiles/COG, STAC, seguridad y operacion. `scripts/validate_curriculum.py` comprobara que cada tema obligatorio aparece exactamente una vez como nucleo y tiene ejercicio y rubrica.

`docs/guias/prerrequisitos.md` declarara como equipo de referencia al menos cuatro nucleos de CPU, 16 GB de RAM, SSD con 20 GB libres, virtualizacion habilitada, puertos, Node, Python, Ruby/Bundler/Jekyll, Docker, Git, navegador y WebGL. Tambien explicara que Safari necesita un equipo macOS real durante el piloto, pero no es un requisito individual de cada estudiante. Cada unidad tendra una actividad diagnostica breve y un ejercicio verificable registrado en la trazabilidad.

El hito termina cuando los fixtures vectorial y raster pueden regenerarse dos veces con los mismos checksums, la trazabilidad curricular pasa, las especificaciones de las tres entregas no exigen SaaS y cada requisito futuro apunta a un artefacto local planificado. La demostracion de que las entregas se completan realmente se pospone hasta Hitos 7 a 9. La suma debe ser exactamente 32 horas presenciales y 40 autonomas.

### Hito 3: modernizar fundamentos, datos y cartografia accesible

Crear `docs/unidades/01_web_git_publicacion.md`, `docs/unidades/02_datos_calidad.md` y `docs/unidades/03_cartografia_accesible.md`. Reutilizar conceptos correctos de `01_Fundamentos/Readme.md`, `02_Conceptos/Readme.md`, `03_Cartografia/Readme.md` y `06_Simbologia/Readme.md`, pero reescribir instrucciones que dependan de interfaces de 2020, cuentas personales o SaaS. La Unidad 1 cubrira HTML semantico, CSS responsive, modulos ES, `fetch`, `async/await`, errores HTTP y hosting estatico neutral. La Unidad 2 cubrira QGIS, GeoPackage, GeoJSON, TopoJSON como comparacion, CRS, orden de coordenadas, precision, geometria valida, procedencia y manifiestos. La Unidad 3 cubrira clasificacion, normalizacion, incertidumbre, leyenda, escala, paletas no dependientes solo del color y WCAG 2.2 AA.

Crear `examples/leaflet/mapa_basico/index.html`, `styles.css`, `main.js` y `tests/a11y/leaflet.spec.ts`. Usar una version Leaflet fijada, APIs nativas `fetch`/`async` y un mapa base que no requiera token. El ejemplo cargara el fixture sintetico, mostrara leyenda, atribucion, filtro, estado de carga y error, y una tabla equivalente. Todos los controles tendran etiqueta y foco visible. La pagina funcionara a 320 CSS px de ancho y con zoom de texto. El test Playwright/Axe instalado desde Hito 1 comprobara la ruta y el error, pero la lista manual seguira siendo obligatoria.

Crear `scripts/prepare_vector_data.py` para invocar GDAL/OGR desde el contenedor de herramientas fijado, validar CRS, propiedades y geometria, convertir GeoJSON a GeoPackage y producir una version simplificada sin cambiar el archivo fuente. El script aceptara rutas de entrada y salida por argumentos, no descargara datos y sera idempotente. Sus pruebas estaran en `tests/data/test_prepare_vector_data.py`.

QGIS2Web se explicara como prototipo generado, no como patron mantenible. No editar sus 128 archivos internamente. Los PDF historicos se retiraran de la navegacion publica hasta tener fuente, licencia y alternativa accesible; permaneceran en sus rutas Git mientras se decide su archivo.

El hito termina cuando el mapa se sirve por HTTP sin jQuery, token ni recurso local roto; los tests regeneran datos validos; y la lista manual WCAG confirma teclado, foco, reflow, leyenda, estado y alternativa tabular.

### Hito 4: implementar interoperabilidad y notebooks deterministas

Crear `docs/unidades/04_apis_interoperabilidad.md`, `notebooks/ogc_clasico.ipynb`, `notebooks/ogc_api_features.ipynb`, `notebooks/stac_estatico.ipynb`, `data/fixtures/responses/ogc-clasico/`, `data/fixtures/responses/ogc-api-features/`, `data/fixtures/openapi/` y `data/fixtures/stac/`. La unidad definira HTTP, codigos 200/400/404/500, REST, OpenAPI, landing page, declaracion de conformidad, colecciones, items, paginacion y CQL2 basico. Comparara WFS con OGC API - Features y mantendra WMS como servicio de mapas. WCS, CSW y WPS seran panorama; WPS se comparara conceptualmente con Processes. Coverages se rotulara como especificacion candidata.

Los notebooks obligatorios usaran respuestas locales saneadas o el stack local cuando este disponible. No instalaran paquetes dentro de celdas, no usaran `verify=False` y no dependeran de Internet para aprobar. Las celdas remotas seran una seccion informativa claramente excluida de CI. Ampliar `pyproject.toml` y `uv.lock` con OWSLib, Requests, Jupyter, nbclient y nbmake fijados. Guardar una descripcion OpenAPI valida del fixture y respuestas de exito y error que permitan explicar codigos HTTP sin red.

El fixture STAC contendra un Catalog, una Collection y Items que enlacen los activos sinteticos. La licencia, extension espacial, fechas y assets seran coherentes con `data/manifests/datasets.yml`. Un validador STAC fijado comprobara todos los documentos.

Los notebooks leeran `COURSE_DATA_MODE`, con valores `fixtures` y `local`. En `fixtures` leeran respuestas grabadas y aprobaran sin red. En `local` consultaran URLs definidas en `notebooks/config.local.json`, archivo generado desde una plantilla sin secretos. Al finalizar Hito 5B se ejecutaran ambos modos y se comprobara que WFS y OGC API - Features describen la misma coleccion. Hito 4 termina inicialmente cuando todos los notebooks pasan en modo `fixtures` y el catalogo STAC pasa validacion.

### Hito 5A: ejecutar prototipos de riesgo

Este hito no produce aun la infraestructura docente definitiva. Crear `infra/prototypes/geoserver/compose.yaml`, `infra/prototypes/geoserver/Dockerfile`, `infra/prototypes/geoserver/init.sql`, `infra/prototypes/geoserver/configure.py`, `infra/prototypes/geoserver/reference.sld`, `infra/prototypes/geoserver/smoke.py`, `infra/prototypes/range/compose.yaml`, `infra/prototypes/range/nginx.conf`, `infra/prototypes/range/validate_range.py`, `infra/prototypes/tools/compose.yaml`, `infra/prototypes/tools/build_vector_tiles.py`, `infra/prototypes/tools/build_cog.py`, `infra/prototypes/maplibre-protocols/package.json`, `infra/prototypes/maplibre-protocols/vite.config.ts`, `infra/prototypes/maplibre-protocols/playwright.config.ts`, `infra/prototypes/maplibre-protocols/vector.html`, `infra/prototypes/maplibre-protocols/raster.html`, `infra/prototypes/maplibre-protocols/src/vector.ts`, `infra/prototypes/maplibre-protocols/src/raster.ts`, `infra/prototypes/maplibre-protocols/tests/protocols.spec.ts`, `infra/prototypes/maplibre-protocols/tests/expected-raster.png` y `docs/governance/prototype-results.md`. Registrar `infra/prototypes/maplibre-protocols` en los workspaces raiz y regenerar el unico lockfile. Cada prototipo usa los fixtures de Hito 2 y registra comando, version, digest, salida y decision. `playwright.config.ts` usara `webServer` para iniciar Vite en `localhost:4173` antes de las pruebas y detenerlo al terminar.

El prototipo GeoServer levantara `postgis/postgis:17-3.5` y GeoServer 3.0.0 con Java 21 usando secretos ficticios por archivo, nunca credenciales reales o defaults reutilizables. Primero probara la imagen oficial y su mecanismo documentado de extensiones. Si no instala OGC API - Features y Vector Tiles 3.0.0, se usara el Dockerfile propio con el WAR y ZIP oficiales 3.0.0, cuyos SHA-256 se registraran antes del build. `init.sql` cargara la tabla, `configure.py` creara workspace/store/capa/SLD y `smoke.py` demostrara WMS, WFS, landing page, conformance, collections, items y MVT. Debe repetir la prueba desde volumenes vacios. No se probara otro servidor ni se degradara OGC API - Features a electivo.

El prototipo de herramientas generara `infra/prototypes/assets/referencia.pmtiles` desde el GeoJSON sintetico y `infra/prototypes/assets/referencia.cog.tif` desde el GeoTIFF sintetico. El prototipo Range usara Nginx fijado para servirlos desde un origen distinto al cliente. Debe responder `206 Partial Content`, `Accept-Ranges: bytes`, `Content-Range` valido y CORS permitido. Si la imagen Nginx seleccionada no cumple, se corregira `nginx.conf`; no se cambiara de servidor dentro de este plan.

El prototipo MapLibre se servira en `http://localhost:4173` y registrara el paquete `pmtiles` y `@geomatico/maplibre-cog-protocol` en dos paginas minimas. Nginx se servira en `http://localhost:8081`, permitira ese origen, metodos GET/HEAD/OPTIONS y expondra `Accept-Ranges`, `Content-Range`, `Content-Length` y `ETag`. Cada pagina visualizara el fixture correspondiente, tendra una region `role="status"` con `data-protocol-state="ready|error"` y mostrara un error comprensible cuando el archivo no este disponible. Playwright comprobara respuestas parciales reales; para vector exigira `querySourceFeatures(...).length > 0`. La pagina raster no cargara mapa base: el COG sera la unica capa visible, y Playwright comparara una captura del canvas con `expected-raster.png` mediante `pixelmatch`/`pngjs` dentro de una tolerancia fijada. Tambien comprobara atribucion y estado `error`. El prototipo de herramientas usara Tippecanoe/PMTiles CLI y GDAL/rio-cogeo desde contenedores fijados.

El hito termina solo cuando `docs/governance/version-matrix.yml` contiene versiones promovidas y checksums/digests, y cuando los recorridos observables pasan: WFS/OGC API, MVT, PMTiles desde Range hasta MapLibre y COG desde Range hasta MapLibre. Si no pasan, Hito 5B, Hito 6 y Hito 7 quedan bloqueados. Los scripts definitivos de Hito 7 se derivaran de las implementaciones promovidas, no al contrario. El workspace de protocolos permanece como evidencia ejecutable y sigue cubierto por el lockfile raiz.

### Hito 5B: construir el stack reproducible

Crear `infra/compose.yaml`, `infra/.env.example`, `infra/secrets/*.example`, `infra/postgis/init/`, `infra/geoserver/`, `infra/static/nginx.conf`, `infra/smoke/` y `docs/unidades/05_servicios_infraestructura.md`. Los secretos reales se ignoraran; los archivos `.example` contendran solo valores ficticios. PostGIS no publicara su puerto fuera de localhost. La administracion de GeoServer se enlazara a localhost.

Los scripts SQL crearan base, extensiones, esquemas, roles de administracion y lectura, tablas de fixtures e indices GiST de forma idempotente. `scripts/configure_geoserver.py` configurara exclusivamente mediante REST y reconstruira workspace, store, capa, estilo SLD y grupo sin clics manuales. El script aceptara URL y archivos de secretos, comprobara existencia antes de crear y fallara con mensajes accionables. No se versionara un data directory completo.

Crear `infra/smoke/smoke_stack.py` para verificar PostGIS, WMS, WFS, OGC API - Features, MVT, Range y CORS. Crear `scripts/backup_stack.py` y `scripts/restore_stack.py`. El primero ejecutara `pg_dump` en formato custom mediante `docker compose exec`, guardara `.backups/curso.dump` y `.backups/manifest.json` con SHA-256, fecha y versiones. El segundo verificara el checksum, restaurara PostGIS, ejecutara `scripts/configure_geoserver.py` y repetira smoke tests. La configuracion GeoServer vive en el script y archivos SLD versionados, por lo que no se respalda un data directory. No incluir caches regenerables.

El recorrido de aceptacion levantara servicios, configurara GeoServer, ejecutara smoke tests y los notebooks en modos `fixtures` y `local`. Despues insertara con `INSERT ... ON CONFLICT DO UPDATE` una fila centinela con UUID conocido, ejecutara `scripts/backup_stack.py` y comprobara manifiesto/checksum. `scripts/test_restore.py` orquestara destruccion, arranque vacio, restauracion, configuracion GeoServer, consulta de la fila centinela y smoke tests. Ante fallo parcial escribira `.reports/restore-state.json`, detendra y eliminara solo los volumenes parciales, levantara un stack vacio y mostrara el comando exacto de reanudacion; nunca alterara `.backups/`. Debe completar la preparacion inicial en menos de 60 minutos en el equipo de referencia sin contar descargas.

### Hito 6: crear el cliente TypeScript/Vite/MapLibre

Crear `examples/maplibre/app/package.json`, `examples/maplibre/app/tsconfig.json`, `examples/maplibre/app/vite.config.ts`, `examples/maplibre/app/index.html`, `examples/maplibre/app/src/`, `examples/maplibre/app/tests/`, `scripts/sync_design_tokens.py` y `docs/unidades/06_cliente_web.md`. Registrar el paquete en `workspaces` del `package.json` raiz y regenerar el unico `package-lock.json`. Los scripts raiz ejecutaran `npm run --workspace examples/maplibre/app <script>`. `docs/assets/css/tokens.css` sera la fuente visual canonica; `sync_design_tokens.py` copiara una version generada a `examples/maplibre/app/src/styles/tokens.css`, y `validate` fallara si hay divergencia.

En `src/config.ts` definir `AppConfig` con URL OGC API, URL de assets, coleccion y atribucion. En `src/state.ts` definir `MapState`, `readStateFromUrl()` y `writeStateToUrl()` para vista y filtros compartibles. En `src/map.ts` definir la inicializacion de MapLibre, fuentes y capas. En `src/status.ts` centralizar mensajes de carga, exito, vacio y error. `src/main.ts` conectara estos modulos sin framework.

La primera version consumira GeoJSON y OGC API - Features, no PMTiles/COG. El control principal de capas y filtros estara fuera del canvas del mapa; solo atribucion, navegacion y controles exigidos por MapLibre podran superponerse. Implementara consulta por clic y teclado, popup con foco administrado, URL compartible y tabla equivalente. Aplicara `docs/assets/css/tokens.css` y las restricciones visuales sin eliminar controles ni estados.

Usar Vitest para funciones puras y Playwright para carga, filtro, consulta y fallo de red. Integrar Axe solo como apoyo; la aceptacion WCAG requiere lista manual. El build generara `examples/maplibre/app/dist/`, que permanecera ignorado y se publicara como artefacto de CI.

El hito termina cuando `npm ci`, lint, tests y build pasan desde un clon limpio; Chromium y Firefox ejecutan el flujo completo y Playwright WebKit sirve como deteccion temprana. Safari real se acepta exclusivamente en el piloto del Hito 9.

### Hito 7: integrar PMTiles, COG, STAC y rendimiento

Crear `docs/unidades/07_rendimiento_cloud_native.md`, `scripts/build_vector_tiles.py`, `scripts/build_cog.py`, `scripts/validate_range.py`, `scripts/benchmark/run_benchmark.py` y activos pequenos en `data/fixtures/cloud/`. Todos los scripts seran Python e invocaran contenedores fijados para que su resultado no dependa de una instalacion nativa. Los activos aprobados se agregaran al sitio mediante `assemble_site.py --cloud-assets data/fixtures/cloud`.

El cliente registrara ambos protocolos promovidos en Hito 5A y permitira cambiar entre un PMTiles de referencia y un COG de referencia. Todo el alumnado consumira ambos; cada proyecto generara y medira solo uno. La ruta vectorial producira MVT y PMTiles con niveles de zoom y generalizacion documentados. La ruta raster producira GeoTIFF base y COG con overviews. Ambos activos se registraran en STAC.

El benchmark recibira dataset, ruta, navegador, perfil de red y numero de repeticiones. Registrara checksum, hardware, cache fria/caliente, bytes, solicitudes, tiempo hasta mapa utilizable y memoria aproximada. Ejecutara al menos cinco repeticiones y reportara mediana. La ruta vectorial comparara GeoJSON, MVT servido y PMTiles; la raster comparara GeoTIFF convencional, COG y WMS. Una excepcion al 30% de reduccion requiere evidencia y aprobacion registrada en la rubrica.

El hito termina cuando los dos fixtures se visualizan de extremo a extremo desde Range, los validadores PMTiles/COG/STAC pasan y un informe reproducible demuestra la comparacion de cada ruta sin confundir formato, contenedor, catalogo y servicio.

### Hito 8: completar seguridad, CI, build y recuperacion

Crear o completar `.github/workflows/validate.yml`, `.github/workflows/external-links.yml`, `docs/unidades/08_operacion_publicacion.md`, `docs/guias/seguridad.md`, `docs/guias/publicacion.md`, `docs/guias/restauracion.md`, `docs/guias/accesibilidad.md`, `docs/guias/revision_entregas.md` y `docs/guias/costes_limites.md`. `npm run validate` agregara validaciones editoriales, datos, notebooks, frontend y configuracion. Las pruebas de Compose que requieran contenedores se ejecutaran localmente y en un job separado.

Los workflows de pull request usaran permisos de solo lectura, no recibiran secretos, no usaran `pull_request_target`, no haran checkout de codigo no confiable en runners privilegiados y fijaran acciones de terceros por SHA. El workflow de enlaces externos sera programado o informativo. El workflow de Pages publicara unicamente el sitio ensamblado `_site/` como artefacto y nunca el arbol historico de la raiz. Antes de usar cualquier hosting para los ejemplos cloud-native, `scripts/validate_range.py` debe confirmar Range y CORS contra la URL desplegada; si el proveedor no cumple, la documentacion se publica pero los activos permanecen en el servidor Nginx local de referencia. El despliegue solo ocurrira desde una rama o entorno aprobado y no desplegara PostGIS o GeoServer con credenciales personales.

La guia de seguridad documentara HTTPS, CORS, CSP, cabeceras, limites de peticion, autenticacion administrativa y rotacion. La guia de restauracion definira que se respalda, que se regenera y como comprobar la recuperacion. Para un futuro entorno institucional propondra RPO de 24 horas y RTO de 4 horas; para el curso exigira reconstruccion local completa. La unidad mostrara healthchecks, logs y errores del cliente como observabilidad minima. `costes_limites.md` registrara almacenamiento, transferencia, minutos CI y limites del hosting de referencia sin exigir una cuenta. `revision_entregas.md` reunira la comprobacion cartografica, de datos, accesibilidad, privacidad, seguridad, rendimiento y reproducibilidad.

Despues de cualquier cambio en `package-lock.json`, `uv.lock`, `Gemfile.lock`, imagenes, WAR o extensiones, `scripts/validate_resources.py` debe exigir la correspondiente entrada en `third-party.yml` y regenerar de forma comprobable `THIRD_PARTY_NOTICES.md`. `scripts/security_scan.py` usara imagenes por digest leidas de la matriz; no ejecutara tags mutables. Las excepciones y allowlist historica se validaran contra sus esquemas y revocaciones.

El hito termina cuando la validacion local y CI coinciden, Gitleaks y auditorias no encuentran secretos ni vulnerabilidades criticas directas, el sitio ensamblado se sirve desde un hosting estatico generico y una restauracion completa pasa los smoke tests.

### Hito 9: ejecutar piloto y cerrar version candidata

Crear `docs/pilot/plan.md`, `docs/pilot/results.md`, `docs/pilot/issues.md`, `docs/pilot/browser-matrix.yml`, `CHANGELOG.md` y `scripts/release_gate.py`. El piloto incluira participantes con niveles distintos y equipos Windows, macOS y Linux representativos. Medira por unidad horas presenciales, horas autonomas, fallos de instalacion, solicitudes de soporte y criterios de rubrica. La revision WCAG incluira teclado, zoom/reflow, contraste, lector de pantalla y alternativas de datos. El responsable web debe asegurar antes del piloto dos entornos macOS con las dos ultimas versiones estables disponibles de Safari. La matriz registrara Safari, macOS, hardware/WebGL, artefacto probado y resultado del flujo carga, filtro, consulta y error; Playwright WebKit no sustituye esta evidencia.

El piloto se acepta si al menos 80% completa el nucleo, 70% completa el proyecto, la mediana presencial no supera 32 horas y la mediana autonoma no supera 40. Si se excede el tiempo, se recorta alcance obligatorio; no se aumenta la carga silenciosamente. Toda incidencia bloqueante se corrige y vuelve a probar.

`scripts/release_gate.py --mode prepared` ejecutara bootstrap, build Jekyll/Vite, ensamblado, validaciones, notebooks fixtures/local, stack, restauracion, Range/MapLibre, seguridad, licencias y comprobacion de evidencia manual/Safari. Si pasa en el arbol sin confirmar, el estado es `candidate-prepared`. Para `candidate-ready`, el usuario debe autorizar un commit; despues se clona ese commit en una ruta temporal limpia y se ejecuta `release_gate.py --mode ready`. El gate exigira arbol limpio, leera `HEAD` al iniciar y guardara el hash probado solo en `.reports/release-gate.json`, que no se versiona. Tag, release y push requieren una autorizacion adicional. Si no se concede el commit, el resultado queda `candidate-prepared`, no se afirma que paso desde clon.

Actualizar `Progress`, `Surprises & Discoveries`, `Decision Log` y `Outcomes & Retrospective` con el resultado real y preparar notas de version. Registrar cada autorizacion Git o su ausencia en `Progress`.

## Pasos concretos

Todos los comandos siguientes se ejecutan desde `C:\opt\work\personal\cartografia_web` en PowerShell 7. Las herramientas que aun no existen se introducen en el hito que las menciona. Cada vez que se agregue un comando al repositorio, actualizar `README.md` y esta seccion con el nombre real.

Antes de iniciar un hito, comprobar estado y releer este documento:

    git status --short
    git diff --check
    git log --oneline -10

El resultado esperado antes de editar es un arbol sin cambios ajenos. Si hay cambios no relacionados, no revertirlos; limitar el hito a sus archivos. Si hay un conflicto directo en una ruta necesaria, detenerse y pedir una decision.

Para Hito 0, obtener primero los digests de los candidatos y registrarlos en la matriz. Despues crear `scripts/security_scan.py`, que ejecutara los contenedores fijados. El escaneo del arbol es bloqueante; la auditoria historica escribe un reporte saneado y no falla por hallazgos conocidos revocados:

    uv sync --frozen
    uv run python scripts/security_scan.py --scope worktree
    uv run python scripts/security_scan.py --scope history --report .reports/gitleaks-history.json
    uv run python scripts/validate_resources.py

El primer comando debe devolver cero solo cuando el arbol no tenga hallazgos prohibidos. El segundo puede devolver cero con hallazgos historicos si todos coinciden con una allowlist de huellas no sensibles y `docs/governance/revocations.md` los marca revocados. `security_scan.py` debe ocultar valores y fallar si aparece un hallazgo nuevo. No se usara `git grep` como prueba de ausencia porque su codigo cero significa que encontro coincidencias.

Despues de Hito 1, la validacion editorial debe poder ejecutarse sin escribir archivos:

    bundle _2.6.2_ install
    npm ci
    uv sync --frozen
    npm exec playwright install chromium
    npm run format:check
    npm run lint:markdown
    npm run lint:html
    npm run lint:css
    npm run validate:json
    npm run validate:xml
    npm run validate:licenses
    npm run validate:structured

Se espera codigo de salida cero. Crear temporalmente un archivo Markdown invalido debe hacer fallar `lint:markdown`; retirarlo debe restaurar el resultado verde. No usar `npm run precommit` durante la migracion.

Construir las dos variantes Jekyll y ensamblar ejemplos aprobados con:

    bundle install
    bundle exec jekyll build --source docs --destination _site_local_jekyll --baseurl ""
    python scripts/assemble_site.py --jekyll-site _site_local_jekyll --output _site
    bundle exec jekyll build --source docs --destination _site_preview_jekyll --baseurl /cartografia_web
    python scripts/assemble_site.py --jekyll-site _site_preview_jekyll --output .preview/cartografia_web
    npm run links:internal -- --site .preview/cartografia_web
    python -m http.server 8000 --directory .preview

Abrir `http://localhost:8000/cartografia_web/` y verificar portada, navegacion, foco, CSS y ausencia de material en cuarentena. Para la variante local, servir `_site/` y abrir `/`. `_site/` y `.preview/` son generados y no se versionan.

Despues de Hito 2, regenerar y validar fixtures:

    uv sync --frozen
    uv run python scripts/generate_fixtures.py
    uv run pytest tests/data
    uv run python scripts/validate_curriculum.py
    git diff --exit-code -- data/fixtures data/manifests

El ultimo comando debe quedar sin diferencias despues de una segunda generacion. Si cambia, el generador no es determinista y el hito no pasa.

Despues de Hito 3, servir el ejemplo Leaflet y ejecutar validaciones:

    python -m http.server 8000
    npm run test:a11y -- --project=leaflet
    uv run pytest tests/data/test_prepare_vector_data.py

Abrir `http://localhost:8000/examples/leaflet/mapa_basico/`. Se debe poder navegar, filtrar y consultar sin raton; desconectar el fixture debe mostrar un error textual y no una pagina vacia.

Despues de Hito 4, ejecutar todos los notebooks y STAC sin red:

    uv sync --frozen
    $env:COURSE_DATA_MODE = "fixtures"
    uv run pytest --nbmake notebooks
    npm run validate:openapi
    npm run validate:stac

Se espera que cada notebook termine sin instalar paquetes, sin `verify=False` y sin solicitar endpoints de terceros en su camino obligatorio.

Durante Hito 5A, ejecutar cada prototipo con sus propios archivos:

    docker compose -f infra/prototypes/tools/compose.yaml run --rm tools python infra/prototypes/tools/build_vector_tiles.py
    docker compose -f infra/prototypes/tools/compose.yaml run --rm tools python infra/prototypes/tools/build_cog.py
    docker compose -f infra/prototypes/geoserver/compose.yaml config --quiet
    docker compose -f infra/prototypes/geoserver/compose.yaml up -d --wait
    uv run python infra/prototypes/geoserver/configure.py
    uv run python infra/prototypes/geoserver/smoke.py
    docker compose -f infra/prototypes/range/compose.yaml up -d --wait
    uv run python infra/prototypes/range/validate_range.py --base-url http://localhost:8081/assets --origin http://localhost:4173
    npm ci
    npm run --workspace infra/prototypes/maplibre-protocols test

Se espera que las herramientas produzcan `infra/prototypes/assets/referencia.pmtiles` y `referencia.cog.tif`; el smoke test prueba WMS, WFS, OGC API y MVT; y Playwright prueba 206, capa visible, atribucion y error accesible para PMTiles y COG. Al terminar:

    docker compose -f infra/prototypes/range/compose.yaml down --volumes
    docker compose -f infra/prototypes/geoserver/compose.yaml down --volumes

Durante Hito 5B, validar el stack promovido con:

    docker compose -f infra/compose.yaml config --quiet
    docker compose -f infra/compose.yaml up -d --wait
    uv run python scripts/configure_geoserver.py --base-url http://localhost:8080/geoserver --secret-file infra/secrets/geoserver_password
    uv run python infra/smoke/smoke_stack.py
    $env:COURSE_DATA_MODE = "fixtures"
    uv run pytest --nbmake notebooks
    $env:COURSE_DATA_MODE = "local"
    uv run pytest --nbmake notebooks
    docker compose -f infra/compose.yaml ps

La salida de `ps` debe mostrar servicios saludables. Las rutas exactas de OGC API se fijaran en `infra/smoke/config.yml` despues del prototipo. Como minimo los smoke tests deben consultar WMS GetCapabilities, WFS GetCapabilities, landing page, conformance, collections, items y un MVT.

El cliente del prototipo se sirve en `http://localhost:4173` y Nginx en `http://localhost:8081`. Nginx permitira `GET`, `HEAD` y `OPTIONS` para ese origen y expondra `Accept-Ranges`, `Content-Range`, `Content-Length` y `ETag`. Comprobar HTTP Range y CORS con:

    curl.exe -sS -D - -o NUL -H "Origin: http://localhost:4173" -H "Range: bytes=0-15" http://localhost:8081/assets/referencia.pmtiles
    curl.exe -sS -D - -o NUL -H "Origin: http://localhost:4173" -H "Range: bytes=0-15" http://localhost:8081/assets/referencia.cog.tif

Cada respuesta debe incluir `206 Partial Content`, `Accept-Ranges: bytes`, `Content-Range` y la cabecera CORS esperada.

La prueba destructiva se ejecuta mediante un unico orquestador que aborta si backup o checksum fallan:

    uv run python scripts/test_restore.py --compose-file infra/compose.yaml --secret-dir infra/secrets --backup-dir .backups

`test_restore.py` inserta la fila centinela, crea y verifica backup, encadena las operaciones y solo entonces elimina volumenes. `restore_stack.py` usa `pg_restore --clean --if-exists --no-owner` sobre la base inicializada, recibe `--secret-dir`, restaura ACL mediante los SQL idempotentes y llama a `configure_geoserver.py`. La consulta final debe encontrar la fila centinela y los smoke tests deben producir el mismo conjunto de endpoints. Si falla, conservar backup y logs, registrar el hallazgo y no continuar a Hito 6.

Despues de un fallo parcial, reanudar unicamente con el stack vacio que deja el orquestador:

    uv run python scripts/restore_stack.py --compose-file infra/compose.yaml --manifest .backups/manifest.json --secret-dir infra/secrets --resume
    uv run python infra/smoke/smoke_stack.py

Si `restore-state.json` no indica `empty-stack-ready`, `restore_stack.py --resume` debe negarse a continuar y pedir ejecutar de nuevo `test_restore.py`; no intentara restaurar sobre un volumen de estado desconocido.

En Hito 6, instalar desde la raiz y usar el workspace del cliente:

    npm ci
    npm run --workspace examples/maplibre/app lint
    npm run --workspace examples/maplibre/app test
    npm run --workspace examples/maplibre/app test:e2e
    npm run --workspace examples/maplibre/app build
    python scripts/sync_design_tokens.py --check
    python scripts/assemble_site.py --jekyll-site _site_local_jekyll --leaflet-dir examples/leaflet --maplibre-dist examples/maplibre/app/dist --output _site

Se espera `examples/maplibre/app/dist/index.html`, `_site/examples/leaflet/` y `_site/examples/maplibre/` con rutas relativas compatibles con un subdirectorio. Playwright debe probar carga, filtro, consulta y error de red; Linkinator debe recorrer ambos ejemplos dentro del sitio ensamblado.

En Hito 7, ejecutar los scripts Python definidos por este plan mediante los comandos raiz:

    npm run data:build:pmtiles
    npm run data:build:cog
    npm run validate:cloud
    npm run test:range
    npm run benchmark -- --route vector --runs 5
    npm run benchmark -- --route raster --runs 5
    python scripts/assemble_site.py --jekyll-site _site_local_jekyll --leaflet-dir examples/leaflet --maplibre-dist examples/maplibre/app/dist --cloud-assets data/fixtures/cloud --output _site

`validate:cloud` debe validar PMTiles, COG y STAC. `test:range` debe probar Range, CORS y visualizacion end-to-end. Cada benchmark debe escribir un informe JSON procesable y un resumen Markdown sin modificar el fixture fuente.

En Hito 8, ejecutar el contrato completo desde la raiz:

    bundle _2.6.2_ install
    npm ci
    uv sync --frozen
    npm exec playwright install --with-deps chromium firefox webkit
    npm run validate
    uv run python scripts/security_scan.py --scope worktree
    npm audit --audit-level=critical
    uv run pip-audit
    uv run python scripts/security_scan.py --scope dependencies

El resultado esperado es codigo cero. Un hallazgo que no pueda corregirse debe quedar como excepcion temporal con responsable, justificacion, alcance y fecha de vencimiento; una vulnerabilidad critica directa o un secreto no admite excepcion para publicar.

En Hito 9, ejecutar el gate completo sobre el arbol actual:

    uv run python scripts/release_gate.py --mode prepared

Si pasa, registrar `candidate-prepared`. Solo despues de autorizacion explicita para confirmar cambios, crear el commit correspondiente, clonarlo en una ruta temporal fuera del workspace y ejecutar desde el clon:

    uv run python scripts/release_gate.py --mode ready

El modo `ready` debe comprobar que `git status --short` esta limpio y registrar el `HEAD` probado en `.reports/release-gate.json`. Si no existe autorizacion de commit, omitir este paso y mantener el estado `candidate-prepared`.

Al finalizar cada hito, ejecutar:

    git status --short
    git diff --check
    git diff --stat

Actualizar este ExecPlan antes de pausar. No ejecutar `git add`, `git commit`, `git tag` o `git push` salvo autorizacion explicita del usuario.

## Validacion y aceptacion

La aceptacion global requiere demostrar un recorrido completo, no solo que los archivos existen. Desde un clon limpio y con prerrequisitos documentados, una persona instala dependencias fijadas, genera fixtures, construye documentacion y cliente, levanta el stack, configura GeoServer, ejecuta notebooks y corre `npm run validate`. Despues abre el sitio, usa el mapa Leaflet, compara WFS con OGC API - Features, usa el cliente MapLibre, visualiza PMTiles y COG desde Range y consulta la alternativa tabular.

El Hito 0 pasa cuando los cuatro roles tienen responsable, las politicas institucionales estan registradas, el arbol actual no contiene secretos, la cuarentena esta fuera del build, cada dataset redistribuido tiene manifiesto completo y cada recurso publico tiene licencia y entrada en `THIRD_PARTY_NOTICES.md` cuando corresponda. Hallazgos del historial solo son aceptables con revocacion documentada; si la revocacion no puede confirmarse, la publicacion queda bloqueada. Este plan no permite reescritura.

El Hito 1 pasa cuando las variantes local y `/cartografia_web/` se construyen, las rutas internas responden, la Unidad 8 esta correctamente enlazada, el material historico no aprobado queda fuera del build y una entrada invalida por formato o licencia hace fallar tanto el comando local como CI. La navegacion publica no conserva dependencias obligatorias de 2020, cuentas personales, IPs, HTTP inseguro o recursos rotos, y la revision visual/accesible del sitio minimo pasa.

El Hito 2 pasa cuando el programa define exactamente ocho unidades, las horas son 32+40 con distribucion autonoma 4/5/4/5/6/6/5/5, y la trazabilidad tema-competencia-actividad-ejercicio-prueba-rubrica esta completa. Las tres especificaciones no exigen SaaS. Los fixtures vectorial y raster deben regenerarse con checksums estables. Su ejecucion completa se valida en hitos posteriores.

El Hito 3 pasa cuando Leaflet funciona a 320 CSS px, con zoom/reflow, teclado, foco, leyenda, atribucion, estados y alternativa de datos. Todos los criterios WCAG 2.2 AA aplicables deben quedar satisfechos; Axe no sustituye la revision manual.

El Hito 4 pasa cuando los notebooks obligatorios terminan sin red, la misma coleccion se puede interpretar por WFS y OGC API - Features y el Catalog, Collection e Items STAC pasan validacion.

El Hito 5A pasa cuando la matriz registra versiones exactas y se observan WMS, WFS, OGC API - Features y MVT; ademas, Playwright confirma para PMTiles y COG respuesta 206, protocolo cargado, capa visible, atribucion y error accesible. Un modulo incompatible bloquea la promocion.

El Hito 5B pasa cuando `docker compose up -d --wait` deja servicios saludables y la destruccion/reconstruccion desde volumenes vacios reproduce PostGIS, workspace, store, capa, SLD, grupo y endpoints. No puede existir configuracion manual no documentada.

El Hito 6 pasa cuando el cliente compila, conserva estado en URL, maneja errores y Playwright cubre carga, filtro, consulta y fallo de red. La interfaz satisface WCAG 2.2 AA y aplica `DESIGN.md` sin ocultar funcion cartografica.

El Hito 7 pasa cuando ambos fixtures se visualizan desde Range y la ruta seleccionada por cada proyecto se genera y mide reproduciblemente. El benchmark usa cinco repeticiones y mediana; la excepcion al 30% necesita aprobacion documentada.

El Hito 8 pasa cuando `npm run validate` y CI coinciden, los workflows no reciben secretos en pull requests, `dist/` se puede servir en hosting estatico generico y backup/restauracion vuelven a dejar los smoke tests verdes.

El Hito 9 pasa funcionalmente cuando 80% del piloto completa el nucleo, 70% completa el proyecto, la mediana presencial no supera 32 horas y la autonoma no supera 40. El flujo completo pasa en las dos ultimas versiones estables disponibles de Safari real y `release_gate.py --mode prepared` termina con codigo cero. Todas las incidencias bloqueantes deben cerrarse y volver a probarse. El estado es `candidate-prepared` hasta que el usuario autorice un commit y el mismo gate pase desde un clon limpio; entonces cambia a `candidate-ready`. Tag y release siguen siendo operaciones opcionales autorizadas por separado.

## Idempotencia y recuperacion

Los generadores de fixtures, SQL y configuracion GeoServer deben comprobar estado antes de crear y producir el mismo resultado al repetirse. Los validadores no escriben archivos. Los comandos que regeneran datos escriben primero en una ruta temporal y solo reemplazan la salida despues de validar. Los artefactos `_site/`, `dist/`, logs y resultados de benchmark son regenerables y deben ignorarse salvo los resumenes seleccionados como evidencia.

Antes de mover documentacion, copiar primero el contenido aprobado a `docs/`, construir y verificar enlaces; retirar la ruta historica solo en un cambio posterior y con la matriz actualizada. Los arboles QGIS2Web se tratan como unidades completas. No editar centenares de archivos generados para aparentar modernizacion.

Antes de `docker compose down --volumes`, crear un backup, verificar su SHA-256 y comprobar que el dump no esta vacio. Si la restauracion falla, mantener el backup, conservar logs y reconstruir con la ultima configuracion conocida; no borrar una segunda vez. `scripts/configure_geoserver.py` y los SQL deben permitir volver a un estado limpio sin depender de un data directory persistente.

Si una dependencia no es compatible, mantener el prototipo aislado, registrar evidencia y probar la siguiente version candidata. No incorporar un workaround permanente al nucleo sin actualizar `Decision Log`, la matriz de versiones, los comandos y las pruebas.

Los secretos reales viven fuera de Git. Si uno se expone, detener publicacion, revocarlo y documentar el incidente. Reescribir el historial es una operacion separada que requiere aprobacion explicita y no esta autorizada por este plan.

Los cambios curriculares son aditivos hasta el piloto. Si las horas exceden los limites, mover contenido a electivo o eliminarlo del nucleo; no aumentar silenciosamente la carga. Conservar los resultados de medicion que justifican el ajuste.

## Artefactos y notas

El inventario inicial debe registrar como minimo los tokens y endpoints historicos sin copiar valores sensibles, los datos sociales en cuarentena, los ocho PDF, los cinco ZIP, las capturas, fuentes y arboles QGIS2Web. Debe diferenciar una URL HTTP insegura de un namespace XML que contiene `http://` y no admite reemplazo mecanico.

La estructura final esperada se reconoce por estas rutas principales:

    docs/
      index.md
      programa.md
      unidades/
      evaluacion/
      guias/
      governance/
      assets/css/
    examples/
      leaflet/mapa_basico/
      maplibre/app/
    notebooks/
    data/
      fixtures/
      manifests/
      schemas/
    infra/
      compose.yaml
      postgis/
      geoserver/
      static/
      smoke/
    scripts/
    tests/
    archive/
    .github/workflows/

La evidencia concisa de cada hito debe guardarse en la seccion correspondiente de este ExecPlan y, cuando sea util para estudiantes, en `docs/governance/prototype-results.md`, informes de benchmark o resultados del piloto. No versionar logs voluminosos, secretos, salidas completas de notebooks ni binarios duplicados.

## Interfaces y dependencias

El repositorio tendra un contrato raiz de comandos npm. `package.json` debe exponer `format:check`, `lint:markdown`, `lint:html`, `lint:css`, `links:internal`, `validate:json`, `validate:xml`, `validate:licenses`, `validate:structured`, `validate:curriculum`, `validate:openapi`, `validate:stac`, `validate:data`, `validate:cloud`, `validate:notebooks`, `validate:security`, `lint`, `test`, `test:e2e`, `test:a11y`, `build` y `validate`. `validate:structured` agrega JSON, XML, OpenAPI y STAC. `validate` ejecuta comprobaciones de solo lectura. Los comandos `data:build:*`, `format:write`, `infra:reset` o equivalentes deben estar claramente separados por ser mutantes o destructivos. La raiz usa npm workspaces y un solo `package-lock.json`.

`data/schemas/dataset-manifest.schema.json` definira como requeridos `id`, `title`, `source`, `owner`, `version`, `retrieved_at`, `checksum`, `license`, `crs`, `schema`, `sensitivity` y `files`. `data/manifests/datasets.yml` debe validar contra ese contrato antes de que un archivo entre al sitio o a un ejercicio. `docs/governance/resource-inventory.yml` tendra `path`, `kind`, `decision`, `license_status`, `sensitivity`, `owner`, `target` y `dataset_id` opcional. `scripts/validate_resources.py` rechazara duplicados, rutas publicas no inventariadas, licencias sin resolver y referencias a dataset inexistentes.

`scripts/generate_fixtures.py` expondra `main() -> int` y recibira `--output-dir`; producira GeoJSON, CSV y GeoTIFF base deterministas. `scripts/prepare_vector_data.py` recibira `--input`, `--output`, `--target-crs` y `--simplify-tolerance`; devolvera codigo distinto de cero y mensaje claro ante geometria, CRS o esquema invalido.

`scripts/build_site.py` recibira `--baseurl` y `--output`. Ejecutara Jekyll, sincronizara tokens, construira el workspace MapLibre cuando exista y llamara a `assemble_site.py`; `npm run build` invocara este script sobre `_site/`. `scripts/validate_site.py` creara un directorio con `tempfile.TemporaryDirectory`, ejecutara el mismo build y Linkinator alli y lo eliminara incluso ante error. `npm run validate` usara `validate_site.py`, no `_site/`, de modo que la validacion no deje cambios persistentes.

`scripts/configure_geoserver.py` expondra funciones idempotentes `ensure_workspace`, `ensure_postgis_store`, `ensure_style`, `ensure_feature_type` y `ensure_layer_group`. Recibira URL y rutas a secretos por argumentos o variables de entorno locales no versionadas. No registrara contrasenas.

`infra/smoke/smoke_stack.py` comprobara funciones separadas para PostGIS, WMS, WFS, OGC API - Features, MVT, PMTiles Range y COG Range. Cada fallo debe indicar endpoint, codigo esperado, codigo observado y cuerpo truncado sin secretos.

`scripts/backup_stack.py` recibira `--compose-file` y `--output`, creara un dump custom de PostgreSQL y un manifiesto JSON con checksum. Su modo `--verify-only` rechazara un dump vacio o alterado. `scripts/restore_stack.py` recibira `--compose-file`, `--manifest` y `--secret-dir`; usara `pg_restore --clean --if-exists --no-owner`, reaplicara SQL de roles/ACL, ejecutara la configuracion REST y terminara con smoke tests. `scripts/test_restore.py` recibira los mismos paths, insertara una fila centinela, verificara backup, encadenara los pasos destructivos solo tras exito y confirmara la fila al final.

En `examples/maplibre/app/src/config.ts`, `AppConfig` contendra `ogcApiBaseUrl`, `staticBaseUrl`, `collectionId` y `attribution`. En `src/state.ts`, `MapState` contendra centro, zoom, capas visibles y filtros; `readStateFromUrl` y `writeStateToUrl` seran funciones puras comprobadas con Vitest. En `src/map.ts`, la inicializacion recibira `AppConfig` y `MapState` en vez de leer variables globales. En `src/status.ts`, los mensajes se reflejaran en una region accesible.

La ruta PMTiles usara el paquete `pmtiles` y registrara su protocolo una sola vez. La ruta COG usara `@geomatico/maplibre-cog-protocol`. Sus versiones exactas quedaran en el lockfile. El servidor estatico debe mantener Range y CORS; una pagina que solo funciona descargando el archivo completo no cumple el contrato.

`scripts/release_gate.py` recibira `--mode prepared|ready`. Ejecutara en orden validaciones, builds, ensamblado, notebooks, stack, restauracion, protocolos, seguridad y licencias; comprobara que existe evidencia del piloto y Safari. En modo `ready` exigira arbol Git limpio, leera `HEAD` y lo escribira solo en `.reports/release-gate.json` no versionado. Un fallo detiene inmediatamente el gate y conserva logs saneados bajo `.reports/`.

Jekyll y Bundler son dependencias obligatorias de documentacion. Las dependencias Node son TypeScript, Vite, MapLibre, `pmtiles`, `@geomatico/maplibre-cog-protocol`, Vitest, Playwright, Axe, pixelmatch, pngjs, ESLint, Prettier, markdownlint-cli2, html-validate, Stylelint, AJV, `@redocly/cli`, Linkinator, `@mapbox/vector-tile`, `pbf` y `@maplibre/maplibre-gl-style-spec`. Las dependencias Python gestionadas por uv son pytest, nbmake, OWSLib, Requests, lxml, jsonschema, Shapely, rasterio, rio-cogeo, stac-validator y pip-audit. Docker Compose ejecuta PostGIS, GeoServer, Nginx y contenedores fijados de GDAL, Tippecanoe, PMTiles CLI, Gitleaks y Trivy. Cada dependencia queda fijada en un lockfile, imagen por digest o archivo de checksums.

`validate:json` usara AJV y jsonschema para los esquemas versionados; `validate:xml` usara lxml y XSD locales para XML/SLD; `validate:openapi` usara Redocly; `validate:stac` recorrera cada Catalog, Collection e Item con stac-validator y comprobara assets contra `datasets.yml`; `validate:data` usara Shapely/GDAL para GeoJSON y geometria; `validate:cloud` usara PMTiles CLI, rio-cogeo, `@mapbox/vector-tile`/`pbf` para decodificar una tesela y `@maplibre/maplibre-gl-style-spec` para estilos; `validate:licenses` usara `scripts/validate_resources.py`; y `validate:security` usara los contenedores Gitleaks/Trivy mediante `scripts/security_scan.py`. Cada comando tendra un fixture invalido en `tests/fixtures/invalid/`, excluido de la validacion normal y ejercitado por `tests/validation/test_invalid_fixtures.py`, que espera codigo distinto de cero.

## Nota de revision

2026-08-03: se creo la revision inicial de este ExecPlan para convertir las fases de `UPGRADE_PLAN.md` en una secuencia autocontenida, verificable y recuperable. Se resolvieron las decisiones base sobre estructura, separacion Jekyll/Vite, fixtures sinteticos, prototipos bloqueantes, comandos locales, interfaces y criterios por hito. No se inicio la implementacion ni se autorizo crear commits.

2026-08-03: se reviso el plan despues de una validacion formal. Se fijo Jekyll, npm workspaces, scripts Python, configuracion REST de GeoServer, candidatos iniciales de contenedores, un unico manifiesto de datasets, gobierno y revocacion, fixtures vector/raster previos a prototipos, comandos independientes para Hito 5A, backup/restauracion, Safari real y validadores por formato. La revision elimina decisiones abiertas que antes recaian en la persona ejecutora.

2026-08-03: se cerro la revision operativa. Los prototipos recibieron scripts y workspaces propios; el ensamblado Jekyll/Vite usa entradas y salidas separadas; Ruby/Jekyll y front matter quedaron fijados; `Programa.md` conserva autoridad; restore usa centinela y reanudacion segura; Range/CORS y render COG tienen aserciones concretas; las dependencias y excepciones tienen registros procesables; y el cierre distingue `candidate-prepared`, `candidate-ready` y `released` sin autorreferencias Git.

2026-08-03: se inicio Hito 0. Se agregaron el entorno Python bloqueado, manifiestos y esquemas, inventario de recursos, politicas iniciales de licencias/seguridad, registro de revocaciones, roles pendientes, mantenimiento por cohorte y matriz de versiones. El validador cubrio 263 archivos versionados. Hito 0 queda pausado hasta que se asignen roles, se confirme la revocacion de tokens y Docker permita ejecutar los escaneos fijados.

2026-08-03: el usuario indicó mantener roles genéricos, declaró tokens Mapbox revocados e indicó que iniciaría Docker. Se registró la revocación como pendiente de evidencia, los roles como no autorizados y se comprobó que Docker seguía sin servidor. El Hito 0 continúa pausado.

2026-08-03: Docker quedó disponible. Se fijaron los digests de Gitleaks 8.24.2 y Trivy 0.59.1, se retiraron cinco valores de token del árbol actual, se limitaron dos falsos positivos generados y se ejecutaron ambos escáneres. El Hito 0 sigue pausado únicamente por autoridad institucional y evidencia de revocación.

2026-08-03: el usuario asignó al instructor del curso como autoridad de los cuatro roles y aprobador de excepciones. La evidencia de revocación Mapbox es el único bloqueo restante del Hito 0.

2026-08-03: el usuario confirmó que se dio de baja la cuenta Mapbox. Se registró la revocación y se cerró Hito 0; Hito 1 queda habilitado.

2026-08-03: se completó Hito 1. Se incorporaron el sitio Jekyll mínimo, CSS basado en `DESIGN.md`, configuración de exclusión temporal, ensamblador, lockfiles, scripts de validación, fixtures negativos y workflow de referencia. Se conservó `_config.yml` en la raíz como barrera de exclusión hasta que el despliegue del sitio ensamblado esté disponible en Hito 8.

2026-08-03: se verificó la construcción Jekyll de raíz y confirmó que las exclusiones no publican los directorios históricos. El workflow de referencia se amplió para ejecutar las validaciones, pruebas negativas, build y enlaces internos. Los avisos Sass del tema Hacker quedan aceptados solo durante la transición de la raíz.

2026-08-03: se completó Hito 2. `Programa.md` quedó como fuente curricular canónica, se generó su copia Jekyll, se publicaron rúbricas y guías, se validó la trazabilidad de ocho unidades y se generaron fixtures vectorial, tabular y ráster sin datos personales. Se aisló una colisión local de PROJ para que la generación ráster siga siendo determinista.

2026-08-03: se completó Hito 3. Se publicaron las tres unidades iniciales, se creó un mapa Leaflet local y accesible, se añadió la distribución Leaflet 1.9.4 con licencia registrada y se creó la conversión GDAL reproducible a GeoPackage. Se fijó la fecha interna de GDAL para estabilizar checksums y se corrigió el ensamblado para incluir el ejemplo en el sitio estático.

2026-08-03: se inició Hito 4. Se añadió la unidad de interoperabilidad y fixtures locales de WFS, landing page, conformance, collections, items y OpenAPI. Los notebooks y STAC quedan pendientes para el siguiente incremento del hito.

2026-08-03: se completó Hito 4. Se añadieron Catalog, Collection e Item STAC con activo local, validación OpenAPI y STAC, y tres notebooks que se ejecutan con nbmake en modo `fixtures`. El modo `local` permanece pendiente del stack de Hito 5B.

2026-08-03: se inició Hito 5A. Se descargaron GeoServer 3.0.0 y PostGIS 17-3.5 y se registraron sus digests; los prototipos aislados quedan pendientes.

2026-08-03: el primer prototipo GeoServer/PostGIS inició correctamente y se limpió con volúmenes vacíos. Vector tiles quedó disponible, pero OGC API - Features devolvió 404. La alternativa Dockerfile con módulo OGC API queda pendiente y bloquea Hito 5B.

2026-08-03: el Dockerfile alternativo descargó y verificó el plugin OGC API - Features 3.0.0. El endpoint respondió HTTP 200 y el prototipo se limpió. Falta configurar y consultar una capa antes de promover Hito 5A.

2026-08-03: se generó un COG sintético con GDAL y se validó HTTP Range/CORS sobre Nginx. PMTiles, MapLibre y los smoke tests integrados siguen pendientes.

2026-08-03: Planetiler generó PMTiles desde el GeoJSON sintético y el CLI de Protomaps lo verificó. Nginx validó HTTP Range/CORS para el archivo. MapLibre y los smoke tests integrados siguen pendientes.

2026-08-03: MapLibre validó PMTiles, COG y estados de error. WMS, WFS y OGC API - Features también pasaron, pero el endpoint MVT devolvió HTTP 400. Hito 5A continúa bloqueado hasta resolver la configuración MVT de GeoServer.

2026-08-03: el endpoint MVT se corrigió a WMS GetMap y pasó junto con WMS, WFS y OGC API - Features. Con COG, PMTiles, Nginx y MapLibre validados, Hito 5A se promovió a Hito 5B.

2026-08-03: se promovió el stack a `infra/compose.yaml`. PostGIS conserva datos en un volumen, GeoServer se reconstruye mediante REST y Nginx entrega los assets cloud-native. Se restringieron los puertos a localhost y los secretos versionados son exclusivamente ejemplos ficticios.

2026-08-03: se completó el Hito 5B con backups PostGIS verificados por SHA-256, restauración desde volumen vacío, reconfiguración REST y notebooks en modo local. La fila centinela se conservó tras la restauración destructiva.

2026-08-03: se inició el Hito 6 con un workspace TypeScript/Vite/MapLibre sin framework. El cliente carga entidades de OGC API - Features, sincroniza vista y filtro en URL, muestra tabla equivalente y verifica el estado URL con Vitest.

2026-08-03: Chromium, Firefox y WebKit ejecutaron carga, filtro y error de red mediante Playwright. WebKit es detección temprana y no reemplaza la evidencia Safari real exigida para el piloto.

2026-08-03: se inició el Hito 7. Planetiler y GDAL regeneraron los activos PMTiles y COG en `data/fixtures/cloud/`; sus manifiestos registran checksum y ambos superaron la comprobación HTTP Range/CORS de Nginx.

2026-08-03: los activos cloud-native se integraron al cliente y STAC. El benchmark HTTP ejecutó cinco repeticiones vectoriales y ráster, pero su resultado se limita explícitamente al transporte local y no sustituye la medición de renderizado en navegador.

2026-08-03: el usuario confirmó que el software libre compatible puede sugerirse para uso personal sin autorizaciones ni licenciamiento adicional. Se registró la política, manteniendo la revisión obligatoria para recursos de terceros que no son herramientas.
