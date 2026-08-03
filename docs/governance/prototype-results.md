# Resultados de prototipos

## GeoServer oficial 3.0.0

Fecha: 2026-08-03.

PostGIS 17-3.5 y GeoServer 3.0.0 iniciaron correctamente con secretos por
archivo, `SKIP_DEMO_DATA=true`, ejecución no privilegiada y la extensión
`vectortiles`. El healthcheck de ambos contenedores fue correcto y el log de
GeoWebCache registró el tipo MVT.

La ruta `http://localhost:18080/geoserver/ogc/features/v1` devolvió HTTP 404.
Por tanto, la imagen oficial con la extensión vectorial no satisface todavía el
requisito obligatorio de OGC API - Features. El prototipo se detuvo y eliminó
volúmenes con `docker compose down --volumes`.

Decisión: no promover esta configuración. El siguiente intento debe usar el
Dockerfile alternativo del Hito 5A con el WAR GeoServer 3.0.0 y el módulo OGC
API - Features compatible, verificando sus SHA-256 antes del build.

## GeoServer 3.0.0 con módulo OGC API - Features

Fecha: 2026-08-03.

El Dockerfile alternativo descargó `geoserver-3.0.0-ogcapi-features-plugin.zip`,
verificó el SHA-256
`1d338a1b89ca7a02cde8aae47ede387a1b28ffa51388e104aa1b1f75c3e41296` e instaló sus
JAR bajo `/opt/additional_libs`. El mismo Compose inició saludable y
`http://localhost:18080/geoserver/ogc/features/v1` devolvió HTTP 200.

Decisión provisional: promover esta imagen a la siguiente prueba del Hito 5A.
Antes de aprobar Hito 5A aún debe configurarse una colección PostGIS mediante
REST y comprobar WMS, WFS, OGC API - Features y MVT sobre la misma capa.

## Smoke test de servicios

Fecha: 2026-08-03.

Con la capa `curso:referencia` configurada por REST, WMS, WFS y OGC API -
Features respondieron HTTP 200. La solicitud MVT mediante GeoWebCache respondió
HTTP 400:
`application/vnd.mapbox-vector-tile is not a supported format for curso:referencia`.
La extensión vectorial necesita una configuración o endpoint adicional antes de
promover el prototipo.

La solicitud WMS `GetMap` con `format=application/vnd.mapbox-vector-tile`
respondió HTTP 200 y el tipo de contenido MVT esperado. Con ese endpoint, WMS,
WFS, OGC API - Features y MVT pasaron el smoke test sobre `curso:referencia`.

Decisión: promover las imágenes, Dockerfile, configuración REST, Nginx, COG,
PMTiles y los protocolos MapLibre al Hito 5B.

## COG sintético

Fecha: 2026-08-03.

La imagen GDAL fijada generó `referencia.cog.tif` con layout COG, compresión
DEFLATE, EPSG:4326 y bloque 256x256. Su SHA-256 es
`c226f051dd093075daf40e5ad38fc30f17f8bf1d972673ccb160c68b9a034831`. Nginx lo
sirvió con HTTP 206, `Accept-Ranges: bytes`, `Content-Range` y CORS restringido
a `http://localhost:4173`.

## PMTiles sintético

Fecha: 2026-08-03.

Planetiler generó `referencia.pmtiles` desde el GeoJSON sintético y el CLI
oficial PMTiles lo verificó correctamente. Nginx sirvió el archivo con HTTP 206,
`Accept-Ranges: bytes`, `Content-Range` y el mismo CORS restringido.
