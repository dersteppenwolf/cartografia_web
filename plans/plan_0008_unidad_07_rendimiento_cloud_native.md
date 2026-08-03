# plan_0008 - Hacer autonoma la Unidad 7 de rendimiento y cloud-native

**Fecha**: 2026-08-03
**Ambito**: `docs/unidades/07_rendimiento_cloud_native.md`, activos cloud, STAC, scripts de build, Range y benchmark
**Estado**: propuesto
**Prioridad**: alta; requisito tecnico de Entrega 3

Este ExecPlan es un documento vivo. Debe mantenerse conforme a `PLANS.md`, `AGENTS.md`, `UPGRADE_PLAN.md` y `DESIGN.md`.

## Proposito / Panorama general

Al terminar, una persona podra elegir y justificar PMTiles para vector o COG para raster, explicar MVT, niveles de zoom, simplificacion, bloques, overviews, compresion, HTTP Range, CORS, cache y STAC. Podra generar los activos sinteticos, validarlos y medir transporte y carga de navegador sin confundir formato, servidor o catalogo.

## Progress

- [x] (2026-08-03) Se identifico que la unidad actual solo define PMTiles, COG y Range; no explica decisiones de produccion, cache, STAC aplicado ni interpretacion de benchmarks.
- [ ] Reescribir teoria, comparaciones y actividades de la ruta vectorial y raster.
- [ ] Documentar lectura de resultados y criterio curricular de rendimiento.
- [ ] Validar builds, Range, STAC, cliente y benchmarks.

## Surprises & Discoveries

- Observacion: los assets aprobados y sus validadores ya existen, pero el benchmark HTTP y el de navegador miden cosas distintas.
  Evidencia: `scripts/benchmark/run_benchmark.py` y `examples/maplibre/app/scripts/benchmark.mjs`.

- Observacion: GitHub Pages entrega Range y CORS para los activos publicados, pero esa capacidad debe comprobarse por proveedor y no asumirse.
  Evidencia: validacion de `206 Partial Content` sobre la URL publicada.

## Decision Log

- Decision: todo el grupo consume PMTiles y COG, pero cada proyecto genera y optimiza una sola ruta.
  Justificacion: mantiene comparacion comun sin exceder las cinco horas autonomas de la unidad.
  Fecha/Autor: 2026-08-03 / OpenCode.

## Outcomes & Retrospective

El resultado sera una unidad que enseña una cadena completa desde dato a entrega optimizada y una interpretacion responsable de mediciones.

## Contexto y orientacion

MVT es una codificacion compacta de entidades por tesela. Una tesela divide el espacio en cuadros por nivel de zoom. PMTiles empaqueta muchas teselas en un archivo y necesita leer rangos de bytes. Un COG es un GeoTIFF organizado para leer bloques y overviews remotos sin descargar el archivo completo. HTTP Range solicita una porcion de bytes y responde 206. CORS autoriza una pagina de un origen a leer recursos de otro. STAC describe activos mediante documentos JSON enlazados. Cache evita solicitudes repetidas, pero no justifica precargar mas datos de los que una persona esta viendo.

## Plan de trabajo

Reescribir la unidad con una comparacion conceptual de GeoJSON, MVT, PMTiles, GeoTIFF convencional, COG y WMS. Explicar donde se simplifica vector, por que los niveles de zoom y atributos afectan peso, como overviews y bloques ayudan al raster, y por que una capa base no sustituye datos tematicos.

Describir la cadena vectorial `GeoJSON -> Planetiler -> PMTiles -> Nginx/Pages -> protocolo MapLibre` y la raster `GeoTIFF -> GDAL COG -> Nginx/Pages -> protocolo COG`. Explicar que STAC cataloga assets, pero no los sirve. Desarrollar Range, cabeceras 206, `Accept-Ranges`, `Content-Range`, CORS, atribucion y cache.

Agregar una practica comun de generacion y validacion de ambos activos y una practica electiva por ruta para que cada estudiante justifique la seleccion. Explicar benchmark frio/caliente, mediana, bytes, solicitudes, tiempo hasta fuente disponible y limites de las mediciones locales. Incluir errores frecuentes y relacion con Entrega 3.

## Pasos concretos

Con el stack local iniciado, ejecutar desde la raiz:

    npm run data:build:pmtiles
    npm run data:build:cog
    npm run validate:cloud
    npm run benchmark:browser
    npm run benchmark -- --route vector --runs 5
    npm run benchmark -- --route raster --runs 5

El resultado esperado incluye archivos bajo `data/fixtures/cloud/`, STAC valido, respuestas HTTP 206 y reportes en `.reports/`. El documento debe indicar que la aceptacion curricular de rendimiento requiere una decision del instructor basada en esas mediciones.

## Validacion y aceptacion

La unidad se acepta cuando una persona puede decidir que ruta corresponde a vector o raster, explicar por que Range evita descargar un archivo entero, ubicar STAC en la arquitectura y leer una mediana sin afirmar causalidad no medida. Debe incluir dos recorridos comunes, una ruta electiva, autoevaluacion y criterios de Entrega 3.

`npm run validate:cloud`, ambos benchmarks, `npm run --workspace examples/maplibre/app test:e2e -- --project=chromium`, `npm run lint:markdown` y `git diff --check` deben pasar.

## Idempotencia y recuperacion

Los builders sobrescriben solo activos sinteticos derivados. Si cambia un checksum, revisar fuente, imagen fijada y manifiesto antes de aceptar el resultado. No usar servicios de teselas OSM para precarga, benchmark masivo u offline.

## Artefactos y notas

El material debe enlazar `data/fixtures/stac/`, `data/manifests/datasets.yml`, `scripts/build_vector_tiles.py`, `scripts/build_cog.py`, `scripts/validate_range.py`, los benchmarks y el cliente MapLibre. Debe separar claramente medicion de transporte HTTP y medicion de navegador.

## Interfaces y dependencias

Mantener Planetiler, PMTiles CLI, GDAL, Nginx, `pmtiles` y protocolo COG con digests o lockfiles fijados. No introducir Tippecanoe u otro servidor como requisito sin una decision y prueba de compatibilidad separada.

## Revision

2026-08-03: creado para ampliar Unidad 7 con fundamentos de rendimiento y rutas cloud-native reproducibles.
