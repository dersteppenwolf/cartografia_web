---
layout: default
title: Estado de la modernizacion
permalink: /status/
---

# Estado de la modernizacion

La modernización técnica y editorial del núcleo está implementada. El sitio
publica ocho unidades mantenidas, ejemplos Leaflet y MapLibre, datos sintéticos,
notebooks, guías operativas y un artefacto estático ensamblado. El contenido
histórico permanece fuera de la navegación pública mientras se revisan licencia,
accesibilidad, seguridad, privacidad y compatibilidad.

## Disponible

- Unidades 1 a 8 con resultados de aprendizaje, práctica, errores frecuentes y
  autoevaluación.
- Mapa Leaflet accesible con datos sintéticos, atribución, estado y tabla
  equivalente.
- Presentación estática de la Unidad 1, enlazada desde su guía y construida con
  sus diagramas propios y referencias científicas verificables.
- Cliente TypeScript/Vite/MapLibre con filtro, estado URL, fuentes OGC API,
  PMTiles y COG, diálogo con foco y pruebas E2E.
- Stack local PostGIS, GeoServer y Nginx con WMS, WFS, OGC API - Features, MVT,
  HTTP Range, CORS, backup y restauración.
- Activos PMTiles y COG descritos por STAC estático y publicados mediante el
  artefacto de GitHub Pages.
- Validaciones editoriales, datos, licencias, seguridad, build, enlaces y
  controles de CI de referencia.

## Límites pendientes

El plan principal no está cerrado todavía. Faltan evidencias que no se deben
simular:

- Revisión manual WCAG 2.2 AA, incluido teclado, foco, contraste, reflow y
  lector de pantalla.
- Pruebas en Safari real sobre macOS.
- Decisión curricular del instructor sobre la meta de rendimiento o una
  excepción justificada.
- Piloto con participantes, horas, soporte, entregas e incidencias reales.

El
[plan de ejecución](https://github.com/dersteppenwolf/cartografia_web/blob/master/plans/plan_0001_modernizacion_integral.md)
conserva el estado detallado. La
[guía técnica](https://github.com/dersteppenwolf/cartografia_web/blob/master/Dev.md)
explica cómo reproducir las validaciones locales y preparar la evidencia
pendiente.
