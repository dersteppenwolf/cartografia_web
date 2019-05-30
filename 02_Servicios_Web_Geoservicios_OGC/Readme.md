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
  - [Otros](#otros)
    - [Qgis2threejs](#qgis2threejs)
    - [Tecnologías web](#tecnolog%C3%ADas-web)
  - [Otros ejemplos](#otros-ejemplos)

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


## Otros

### Qgis2threejs

* [Qgis2threejs plugin documentation](https://qgis2threejs.readthedocs.io/en/docs/)     
* [Tutorial](https://qgis2threejs.readthedocs.io/en/docs/Tutorial.html)    
 

> Qgis2threejs plugin is a QGIS plugin, which visualizes DEM data and vector data in 3D on web browsers. You can build various kinds of 3D objects with simple settings panels, view them in web view of exporter and generate files to publish them to web in simple procedure. In addition, you can save the 3D model in glTF format for 3DCG or 3D printing.


### Tecnologías web

* HTML5 Tutorial https://www.w3schools.com/html/
* JavaScript Tutorial https://www.w3schools.com/js/default.asp
* CSS Tutorial https://www.w3schools.com/css/default.asp



## Otros ejemplos

* Utilizando WMS desde leaflet http://bl.ocks.org/hpfast/2155366c06f4ae0fae59df216fc3f7ec
* Anaconda https://www.anaconda.com/
