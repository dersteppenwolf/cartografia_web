# Servicios web, geoservicios y OGC

- [Servicios web, geoservicios y OGC](#servicios-web-geoservicios-y-ogc)
  - [Presentación](#presentaci%C3%B3n)
  - [Notas adicionales](#notas-adicionales)
    - [Geopackage](#geopackage)
    - [QGIS](#qgis)
    - [Mapbox y geojson](#mapbox-y-geojson)
    - [Vector Tiles](#vector-tiles)

## Presentación

Enlace https://github.com/dersteppenwolf/cartografia_web/blob/master/02_Servicios_Web_Geoservicios_OGC/02_%20Servicios_web_geoservicios_OGC.pdf

## Notas adicionales

### Geopackage

- Switch from shapefile https://es.slideshare.net/jachym/switch-from-shapefile
- GeoPackage, OWS Context and the OGC Interoperability Program https://es.slideshare.net/rajrsingh/geopackage-ows-context-and-the-ogc-interoperability-program
- Introduction to SQLite: The Most Popular Database in the World https://es.slideshare.net/jkreibich/introduction-to-sqlite-the-most-popular-database-in-the-world
- GeoPackage para novatos: ventajas y uso en ArcGIS, QGIS, GeoServer y Leaflet https://mappinggis.com/2017/06/geopackage-para-novatos-uso-en-arcgis-qgis-publicacion-en-geoserver/
- GeoPackage extensions https://www.geopackage.org/extensions.html

### QGIS

- Se encuentra disponible tanto para 32 como 64 bits https://qgis.org/es/site/forusers/download.html
- 64 bits vs. 32 bits: ¿en qué se diferencian? https://computerhoy.com/noticias/software/64-bits-vs-32-bits-que-diferencian-57224
- "Sistemas operativos de 32 bits vs 64 bits" https://es.slideshare.net/WALDANA81/sistemas-operativos-de-32-bits-vs-64-bits

### Mapbox y geojson

Error de geojson exportado desde qgis:

> _Input failed. old-style crs member is not recommended, this object is equivalent to the default and should be removed on line 1._

Causa del problema "crs":

![qgis2web](geojson1.png "qgis2web")

Solución:

![qgis2web](geojson2.png "qgis2web")

Sistema de referencia: https://tools.ietf.org/html/rfc7946

> _geographic coordinate reference system, using the World Geodetic System 1984 (WGS 84) [WGS84] datum, with longitude and latitude units of decimal degrees_.

### Vector Tiles

- Crear vector tiles con arcgis pro https://pro.arcgis.com/en/pro-app/help/mapping/map-authoring/author-a-map-for-vector-tile-creation.htm
