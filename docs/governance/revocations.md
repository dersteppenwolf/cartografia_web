# Estado de revocaciones

Los valores de tokens no se registran en este documento. Los hallazgos se
identifican solo por ruta y por un identificador no sensible cuando exista.

| Recurso                  | Rutas conocidas                                                                                                                                                                                                               | Estado            | Evidencia requerida                                         |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- | ----------------------------------------------------------- |
| Tokens Mapbox historicos | `01_Fundamentos/ejemplo_leaflet.html`, `02_Conceptos/html/leaflet_geojson_simple.html`, `03_Cartografia/example/kepler.gl.html`, `04_Servicios_Web_Geoservicios_OGC/html/leaflet_wms_2.html`, `05_Servidores_Mapas/Readme.md` | revoked-confirmed | Mapbox, 2026-08-03, instructor del curso, baja de la cuenta |

El usuario confirmó el 2026-08-03 que se dio de baja la cuenta Mapbox. Como la
cuenta que emitía los tokens dejó de existir y los valores se retiraron del
árbol actual, se registra la revocación como `revoked-confirmed`. El historial
Git no se reescribe sin una autorización explícita separada.

La auditoría histórica de Gitleaks del 2026-08-03 encontró además tres
ocurrencias de token en `01_Fundamentos/ejemplo_leaflet.html`,
`02_Conceptos/html/leaflet_geojson_simple.html` y
`04_Servicios_Web_Geoservicios_OGC/html/leaflet_wms_2.html`. Sus valores fueron
retirados del árbol actual mediante `scripts/redact_historical_tokens.py`; los
commits históricos no se reescribieron.
