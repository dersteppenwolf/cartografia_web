---
layout: default
title: Inventario de migracion
permalink: /gobierno/inventario-migracion/
---

# Inventario de migracion

La fuente procesable de este inventario es
`docs/governance/resource-inventory.yml`. La siguiente síntesis evita mover
contenido antes de que haya una ruta aprobada y una licencia resuelta.

| Ruta actual                                               | Decision  | Destino o condicion                                         |
| --------------------------------------------------------- | --------- | ----------------------------------------------------------- |
| `00_Intro/` y `01_Fundamentos/`                           | Sustituir | Unidades 1 a 3 y ejemplos mantenidos                        |
| `02_Conceptos/`                                           | Sustituir | Unidad 2; QGIS2Web queda como salida generada histórica     |
| `03_Cartografia/example/geotweets.*` y `kepler.gl.html`   | Bloquear  | Cuarentena; no se publica ni transforma                     |
| `04_Servicios_Web_Geoservicios_OGC/`                      | Sustituir | Unidad 4 y notebooks deterministas                          |
| `05_Servidores_Mapas/`, `Geoserver.md` y `06_Simbologia/` | Sustituir | Unidad 5 e infraestructura reproducible                     |
| `07_Servicios_Cloud/`                                     | Archivar  | Solo comparativas con licencia aprobada                     |
| `08_Arquitectura_SIG/`                                    | Sustituir | Unidad 8 y operación                                        |
| PDF, ZIP, fuentes e imágenes                              | Bloquear  | Revisar procedencia, licencia, texto alternativo y utilidad |

No se elimina ni mueve masivamente ningún directorio histórico durante esta
fase. El artefacto público solo incluye `docs/` y ejemplos que hayan superado la
revisión de gobierno.
