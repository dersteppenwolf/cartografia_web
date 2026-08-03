---
layout: default
title: Unidad 4. APIs e interoperabilidad
permalink: /unidades/04-apis-interoperabilidad/
---

# Unidad 4. APIs e interoperabilidad

WMS entrega una imagen de mapa y WFS entrega entidades geográficas mediante el
modelo OGC Web Services clásico. OGC API - Features expone colecciones y
entidades con rutas HTTP, documentos OpenAPI y declaraciones de conformidad. Las
dos interfaces pueden describir la misma colección, pero sus contratos y formas
de descubrimiento son distintos.

La landing page de una OGC API conduce a `conformance`, `collections` e `items`.
OpenAPI describe rutas, parámetros y respuestas. CQL2 expresa filtros; en este
núcleo se presenta como concepto y se trabaja el filtro básico por propiedades,
espacio y tiempo.

STAC describe activos espaciotemporales con Catalog, Collection e Item. No es un
mapa ni un reemplazo general de WMS o WFS. WCS, CSW, WPS, Records, Processes,
EDR y Coverages se conservan como panorama; Coverages es una especificación
candidata.

## Diagnóstico

Ejecuta los notebooks en modo `fixtures`. Identifica la colección `referencia`,
su extensión espacial y una entidad. Luego compara el nombre de la colección en
la respuesta WFS y en `collections.json`.
