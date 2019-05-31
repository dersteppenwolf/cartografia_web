# Servicios web, geoservicios y OGC

- [Servicios web, geoservicios y OGC](#servicios-web-geoservicios-y-ogc)
  - [Presentación](#presentaci%C3%B3n)
  - [Ejercicio 1 : Creando mapas con qgis2web y github pages](#ejercicio-1--creando-mapas-con-qgis2web-y-github-pages)
    - [Documentación](#documentaci%C3%B3n)
      - [Ejemplo](#ejemplo)
    - [GitHub Pages](#github-pages)
  - [Ejercicio 2 : Publicando mapas utilizando herramientas disponibles en la nube](#ejercicio-2--publicando-mapas-utilizando-herramientas-disponibles-en-la-nube)
  - [Ejercicio 3: Using Python to Analyze Spatial Data](#ejercicio-3-using-python-to-analyze-spatial-data)
  - [Ejercicio 4: Ejemplos Python / Arcpy](#ejercicio-4-ejemplos-python--arcpy)
  - [Ejercicio 5: Leaflet y WMS](#ejercicio-5-leaflet-y-wms)
  - [Otros](#otros)
    - [Qgis2threejs](#qgis2threejs)
    - [Tecnologías web](#tecnolog%C3%ADas-web)
  - [Notas adicionales](#notas-adicionales)
    - [Geopackage](#geopackage)
    - [QGIS](#qgis)
    - [Mapbox y geojson](#mapbox-y-geojson)

## Presentación

Enlace https://github.com/dersteppenwolf/cartografia_web/blob/master/02_Servicios_Web_Geoservicios_OGC/02_%20Servicios_web_geoservicios_OGC.pdf

## Ejercicio 1 : Creando mapas con qgis2web y github pages

### Documentación

* Web Mapping with QGIS2Web https://www.qgistutorials.com/en/docs/web_mapping_with_qgis2web.html
* Publica tus mapas en la web con qgis2web https://mappinggis.com/2016/03/crea-aplicaciones-webmapping-con-qgis/
* qgis2web wiki https://github.com/tomchadwin/qgis2web/wiki
  
> qgis2web es una herramienta que exporta los proyectos de QGIS en mapas web de OpenLayers o Leaflet (crea automáticamente los archivos HTML, Javascript y CSS).
> 
> qgis2web crea un mapa web basado en OpenLayers o Leaflet de todas las capas  existentes en un proyecto de QGIS. La herramienta convierte las capas vectoriales en GeoJSON y crea una estructura de carpetas con un archivo index.html que contiene el mapa web.
>
>Además el plugin es capaz de exportar la simbología definida en QGIS tanto de puntos, líneas y polígonos e incluir un control de visibilidad de capas y varios controles más.

#### Ejemplo

![qgis2web](qgis2web.png "qgis2web")

* Página web: https://sigfedepanela.github.io/PreciosSemanales/
* Repositorio en github: https://github.com/sigfedepanela/PreciosSemanales
* Geojson generado por la herramienta: https://raw.githubusercontent.com/sigfedepanela/PreciosSemanales/gh-pages/layers/PreciosporDepartamento_2.js




### GitHub Pages

* Getting Started with GitHub Pages https://guides.github.com/features/pages/

![qgis2web](pages.png "pages")



* Url  Página principal https://dersteppenwolf.github.io/cartografia_web/
* Mapa de ejemplo https://dersteppenwolf.github.io/cartografia_web/02_Servicios_Web_Geoservicios_OGC/ejemplo_qgis2web
* Código fuente generado https://github.com/dersteppenwolf/cartografia_web/tree/master/02_Servicios_Web_Geoservicios_OGC/ejemplo_qgis2web
  


## Ejercicio 2 :  Publicando mapas utilizando herramientas disponibles en la nube

Ver https://github.com/dersteppenwolf/taller_gis_cloud

## Ejercicio 3: Using Python to Analyze Spatial Data

Ver https://github.com/dersteppenwolf/pycon

## Ejercicio 4: Ejemplos Python / Arcpy

* Python variables y operaciones: https://gist.github.com/dersteppenwolf/fca39c1971fd0fd7c3ce
* Describir feature https://gist.github.com/dersteppenwolf/6dc546ef359ffbb85947
* Buffer https://gist.github.com/dersteppenwolf/82d65df9544933289bab
* Clip https://gist.github.com/dersteppenwolf/6dae5bfd9521db50e567


## Ejercicio 5: Leaflet y WMS

* Utilizando WMS desde leaflet http://bl.ocks.org/hpfast/2155366c06f4ae0fae59df216fc3f7ec

## Otros

### Qgis2threejs

* [Qgis2threejs plugin documentation](https://qgis2threejs.readthedocs.io/en/docs/)     
* [Tutorial](https://qgis2threejs.readthedocs.io/en/docs/Tutorial.html)    
 

> Qgis2threejs plugin is a QGIS plugin, which visualizes DEM data and vector data in 3D on web browsers. You can build various kinds of 3D objects with simple settings panels, view them in web view of exporter and generate files to publish them to web in simple procedure. In addition, you can save the 3D model in glTF format for 3DCG or 3D printing.


### Tecnologías web

* HTML5 Tutorial https://www.w3schools.com/html/
* JavaScript Tutorial https://www.w3schools.com/js/default.asp
* CSS Tutorial https://www.w3schools.com/css/default.asp


## Notas adicionales

### Geopackage

* Switch from shapefile https://es.slideshare.net/jachym/switch-from-shapefile
* GeoPackage, OWS Context and the OGC Interoperability Program https://es.slideshare.net/rajrsingh/geopackage-ows-context-and-the-ogc-interoperability-program
* Introduction to SQLite: The Most Popular Database in the World https://es.slideshare.net/jkreibich/introduction-to-sqlite-the-most-popular-database-in-the-world
* GeoPackage para novatos: ventajas y uso en ArcGIS, QGIS, GeoServer y Leaflet https://mappinggis.com/2017/06/geopackage-para-novatos-uso-en-arcgis-qgis-publicacion-en-geoserver/
* GeoPackage extensions https://www.geopackage.org/extensions.html

### QGIS

* Se encuentra disponible tanto para 32 como 64 bits https://qgis.org/es/site/forusers/download.html
* 64 bits vs. 32 bits: ¿en qué se diferencian? https://computerhoy.com/noticias/software/64-bits-vs-32-bits-que-diferencian-57224 
* ~~"Sistemas operativos de 32 bits vs 64 bits"~~ https://es.slideshare.net/WALDANA81/sistemas-operativos-de-32-bits-vs-64-bits


### Mapbox y geojson

Error de geojson exportado desde qgis:

> _Input failed. old-style crs member is not recommended, this object is equivalent to the default and should be removed on line 1._


Causa del problema "crs":

![qgis2web](geojson1.png "qgis2web")

Solución:

![qgis2web](geojson2.png "qgis2web")


Sistema de referencia: https://tools.ietf.org/html/rfc7946

> _geographic coordinate reference system, using the World Geodetic System 1984 (WGS 84) [WGS84] datum, with longitude and latitude units of decimal degrees_.