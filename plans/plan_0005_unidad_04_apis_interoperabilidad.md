# plan_0005 - Hacer autonoma la Unidad 4 de APIs e interoperabilidad

**Fecha**: 2026-08-03
**Ambito**: `docs/unidades/04_apis_interoperabilidad.md`, notebooks, fixtures
OGC/OpenAPI/STAC y validadores
**Estado**: cerrado técnicamente
**Prioridad**: alta; prerrequisito conceptual de servicios y cliente

Este ExecPlan es un documento vivo. Debe mantenerse conforme a `PLANS.md`,
`AGENTS.md`, `UPGRADE_PLAN.md` y `DESIGN.md`.

## Proposito / Panorama general

Al terminar, una persona podra leer una solicitud y respuesta HTTP, distinguir
WMS, WFS y OGC API - Features, descubrir una coleccion desde una landing page,
interpretar OpenAPI y explicar como STAC describe activos. Podra comparar la
misma coleccion local mediante WFS y OGC API sin depender de Internet.

## Progress

- [x] (2026-08-03) Se identifico que la unidad actual describe servicios en 29
      lineas y no desarrolla HTTP, parametros, respuestas, paginacion, OpenAPI
      ni filtros aplicados.
- [x] (2026-08-03) Se amplio la teoria de HTTP, WMS, WFS, OGC API - Features,
      OpenAPI, filtros, STAC y descubrimiento mediante fixtures locales.
- [x] (2026-08-03) Se integraron los tres notebooks en una practica guiada que
      compara modo fixtures y modo local.
- [x] (2026-08-03) Pasaron notebooks en ambos modos, validacion OpenAPI, STAC,
      build y enlaces internos.

## Surprises & Discoveries

- Observacion: el material historico usa servicios institucionales externos y
  Google Colab, que no pueden ser obligatorios. Evidencia:
  `04_Servicios_Web_Geoservicios_OGC/Readme.md` lineas 16 a 108.

- Observacion: los notebooks mantenidos ya separan modo fixtures y modo local.
  Evidencia: `notebooks/ogc_clasico.ipynb`, `notebooks/ogc_api_features.ipynb`,
  `notebooks/stac_estatico.ipynb` y `scripts/run_notebooks.py`.

## Decision Log

- Decision: usar respuestas grabadas como recorrido obligatorio y el stack local
  como extension verificable. Justificacion: permite aprobar sin red y despues
  demostrar interoperabilidad real sobre la misma coleccion. Fecha/Autor:
  2026-08-03 / OpenCode.

## Outcomes & Retrospective

La Unidad 4 quedó convertida en una guía de descubrimiento, consulta y evaluación
de contratos geoespaciales. Los notebooks demuestran WFS, OGC API - Features y
STAC con fixtures y stack local, mientras OpenAPI y los validadores hacen
observable el contrato sin red externa obligatoria.

## Contexto y orientacion

HTTP define solicitudes y respuestas entre cliente y servidor. Una URL
identifica un recurso; metodo, parametros, cabeceras y cuerpo expresan la
solicitud; el codigo de estado comunica el resultado. WMS entrega una imagen
renderizada. WFS entrega entidades mediante el modelo OGC clasico. OGC API -
Features entrega colecciones y entidades mediante rutas HTTP modernas. OpenAPI
describe rutas, parametros y respuestas en un documento procesable. STAC enlaza
Catalog, Collection e Item para describir activos espaciotemporales. Una pagina
landing es el punto inicial para descubrir enlaces, conformidad y colecciones.

## Plan de trabajo

Reescribir la unidad con una tabla conceptual en prosa que compare finalidad,
entrada, salida, descubrimiento y caso de uso de WMS, WFS, OGC API - Features y
STAC. Explicar URL, query string, JSON, XML, GeoJSON, codigos 200, 400, 404 y
500 con los fixtures existentes. Mostrar el recorrido landing, conformance,
collections e items y explicar por que no se construye una URL a ciegas.

Desarrollar OpenAPI como contrato y CQL2 como lenguaje de filtro, limitando la
practica obligatoria a propiedades, espacio y tiempo simples. Conectar cada
seccion con un notebook: OGC clasico, Features y STAC. Mantener WCS, CSW, WPS,
Records, Processes, EDR y Coverages como panorama, definidos sin convertirlos en
requisito.

## Pasos concretos

Desde la raiz ejecutar:

    uv run python scripts/run_notebooks.py --mode fixtures
    npm run validate:openapi
    npm run validate:stac
    npm run lint:markdown

Con el stack iniciado, ejecutar tambien:

    uv run python scripts/run_notebooks.py --mode local

El resultado esperado es que WFS y OGC API describan `referencia` y que STAC
valide Catalog, Collection, Item y assets locales.

## Validacion y aceptacion

La unidad se acepta cuando una persona puede explicar que servicio usar para una
imagen, entidades o catalogo; identificar una landing page; interpretar un
codigo HTTP; comparar el identificador de coleccion WFS y Features; y describir
la diferencia entre STAC y una API de entidades. Debe incluir ejercicios,
soluciones esperadas o criterios de verificacion, errores frecuentes y relacion
con Entrega 2.

Los comandos indicados y `git diff --check` deben pasar. Ningun camino
obligatorio puede acceder a un endpoint externo o usar `verify=False`.

## Idempotencia y recuperacion

El modo fixtures no modifica archivos. El modo local requiere Compose saludable;
si falla, volver al modo fixtures, ejecutar smoke tests y no sustituir el
endpoint por uno externo.

## Artefactos y notas

El material final debe enlazar los tres notebooks,
`data/fixtures/openapi/features.json` y `data/fixtures/stac/`. Las respuestas de
error deben ser ejemplos saneados, sin credenciales ni hosts historicos.

## Interfaces y dependencias

Usar Requests y OWSLib ya fijados en `uv.lock`, fixtures locales y GeoServer
local. No hacer obligatorio Colab, servicios colombianos remotos ni APIs de
terceros.

## Revision

2026-08-03: creado para convertir la Unidad 4 en una leccion autonoma basada en
contratos y fixtures reproducibles.
