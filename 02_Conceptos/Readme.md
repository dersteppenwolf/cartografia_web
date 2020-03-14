# 2 - Los SIG y la Web


- [2 - Los SIG y la Web](#2---los-sig-y-la-web)
  - [Presentación](#presentaci%C3%B3n)
  - [Ejercicio 1 : Introducción a Qgis](#ejercicio-1--introducci%C3%B3n-a-qgis)
    - [Fuentes de datos sugeridas](#fuentes-de-datos-sugeridas)
  - [Ejercicio 2: Conociendo Geojson](#ejercicio-2-conociendo-geojson)
  - [Ejercicio 3: Creando mapas con Qgis2web](#ejercicio-3-creando-mapas-con-qgis2web)
    - [Documentación QGIS2Web](#documentaci%C3%B3n-qgis2web)
    - [Generación de mapas 3D: Qgis2threejs](#generaci%C3%B3n-de-mapas-3d-qgis2threejs)

## Presentación

Enlace: https://github.com/dersteppenwolf/cartografia_web/blob/master/02_Conceptos/02_Los_SIG_y_la_web.pdf




## Ejercicio 1 : Introducción a Qgis


Objetivos

- Conocer el funcionamiento básico de QGIS
- Publicar mapas en la web con la ayuda de QGIS.
- QGIS Tutorials http://www.qgistutorials.com/en/index.html


Realizar lo siguiente: 

- Instale QGIS 3.x https://www.qgis.org/es/site/ versión LTS (Long Term Support). Versión a la fecha 3.10
- Explore la interfaz de qgis
- Descargue un conjunto de datos pequeño (shapefile o geojson) desde alguna de las fuentes sugeridas.
- Adicione una capa a qgis
- Cuantos registros tiene?
- Asigne simbología a la capa
- Adicione otras capas y asigne simbología según corresponda
- Impresión de mapas: Seguir el tutorial  https://docs.qgis.org/3.4/en/docs/training_manual/map_composer/map_composer.html
- Generar pdf y subirlo a su repositorio de github
- Publique el mapa generado su repositorio git con el fin de poder visualizarlo a través de github pages (Carpeta __ejercicio_qgis2web__).
* Crear un issue en https://github.com/dersteppenwolf/cartografia_web/issues con lo siguiente:
  - Título: Ejercicio Mapa Pdf QGIS - CODIGO_ESTUDIANTE
  - Contenido: 
    - Enlace público en github al pdf generado

### Fuentes de datos sugeridas

- Portal de datos abiertos de Colombia: https://www.datos.gov.co/
- Portal de datos abiertos del IGAC: https://geoportal.igac.gov.co/
- Openstreetmap (geofabrik) http://download.geofabrik.de/
- IDECA https://www.ideca.gov.co/datos-de-referencia
- Datos abiertos Bogotá http://datosabiertos.bogota.gov.co/
- Natural Earth (Large scale data, 1:10m) http://www.naturalearthdata.com/downloads/
- Marco Geográfico Nacional (MGN) Dane 2017 - Colombia https://geoportal.dane.gov.co/
- World Borders http://thematicmapping.org/downloads/world_borders.php
- World Bank https://data.worldbank.org/
- World Bank Explorer http://data.un.org/Explorer.aspx






## Ejercicio 2: Conociendo Geojson

Conociendo y Visualizando geojson :

Ejercicio 1:

- Ingrese al portal de datos abiertos de Philadelphia y descarge el conjunto de datos “Licenses and Inspections Districts” en formato geojson https://www.opendataphilly.org/dataset/licenses-inspections-district-boundaries
- Ingrese a http://geojson.io/ y cargue el archivo
- Preguntas:
  - Qué tipo de geometría tienen los datos?
  - Qué atributos tiene?
  - Cuantos registros hay?

Ejercicio 2:

- Descargue otros conjuntos de datos desde opendataphilly y haga el mismo procedimiento https://www.opendataphilly.org/dataset?res_format=geojson
- Tipos de Geometrías:
  - Líneas
  - Puntos
- Pregunta: En qué otros formatos está disponible la información?

Ejercicio 3: Visualizando Geojson con Clientes ligeros

- Visualizando geojson usando leaflet 
- 
  - Ejemplo 1: Leaflet Simple 
    - Vista mapa  https://dersteppenwolf.github.io/cartografia_web/02_Conceptos/html/leaflet_geojson_simple.html
    - Código https://github.com/dersteppenwolf/cartografia_web/blob/master/02_Conceptos/html/leaflet_geojson_simple.html
    - Tutorial http://leafletjs.com/examples/geojson/


  - Ejemplo 2: Geojson externo
    - Vista mapa https://dersteppenwolf.github.io/cartografia_web/02_Conceptos/html/leaflet_geojson_externo.html
    - Código https://github.com/dersteppenwolf/cartografia_web/blob/master/02_Conceptos/html/leaflet_geojson_externo.html
    - Datos https://github.com/dersteppenwolf/cartografia_web/blob/master/02_Conceptos/html/datos/limite_departamental_simplificado.geojson 
    - Tutorial: Loading External GeoJSON: A(nother) Way to Do It with jQuery  https://medium.com/@maptastik/loading-external-geojson-a-nother-way-to-do-it-with-jquery-c72ae3b41c01

- Visualizando geojson usando mapbox gl https://www.mapbox.com/mapbox-gl-js/example/geojson-polygon/

- Visualizando geojson Usando openlayers http://dev.openlayers.org/examples/geojson.html
- Arcgis JS Geojson layer https://developers.arcgis.com/javascript/latest/sample-code/layers-geojson/index.html

Ejercicio 4: Clientes Pesados - Qgis

- Busque en la web archivos de tipo geojson Ejemplo: https://bit.ly/2EqUvFG
- Cargue el archivo en QGIS http://webgeodatavore.com/add-geojson-content-in-qgis-short-recipes.html
- Preguntas:
  - Tipo de geometría? Atributos? Cantidad registros?
  - Se puede editar?

Ejercicio 5: Clientes Pesados - Arcgis

- Cargue los datos geojson en Arcgis Desktop
- Edite la información y/o utilice alguna herramienta de geoprocesamiento
- Tips:
  - https://opengislab.com/blog/2018/11/8/adding-and-viewing-geojson-in-qgis-and-arcgis
  - https://www.esri.com/en-us/arcgis/products/arcgis-data-interoperability/overview






## Ejercicio 3: Creando mapas con Qgis2web 

Qgis2web es una herramienta que exporta los proyectos de QGIS en mapas web de OpenLayers https://openlayers.org/ o Leaflet https://leafletjs.com/ (crea automáticamente los archivos HTML, Javascript y CSS).

La herramienta convierte las capas vectoriales en GeoJSON https://geojson.org/ y crea una estructura de carpetas con un archivo **index.html** que contiene el mapa web.

Además el plugin es capaz de exportar la simbología definida en QGIS tanto de puntos, líneas y polígonos e incluir un control de visibilidad de capas y varios controles más.

**Ejemplo**

![qgis2web](qgis2web.png "qgis2web")

- Página web: https://sigfedepanela.github.io/PreciosSemanales/
- Repositorio en github: https://github.com/sigfedepanela/PreciosSemanales
- Geojson generado por la herramienta: https://raw.githubusercontent.com/sigfedepanela/PreciosSemanales/gh-pages/layers/PreciosporDepartamento_2.js


Realizar lo siguiente: 

* Instalar el plugin Qgis2web. (Instalación de plugins https://docs.qgis.org/3.4/en/docs/training_manual/qgis_plugins/fetching_plugins.html)
* A partir del mapa generado en el ejercicio 1, genere el mapa para la web utilizando Qgis2web
* Características del mapa generado: 
  * Exportar como leaflet
  * habilitar popups (personalizar campos a mostrar)
  * Activar Encendido / apagado de mapas
* Publique el mapa generado su repositorio git con el fin de poder visualizarlo a través de github pages (Carpeta __ejercicio_qgis2web__).
* Crear un issue en https://github.com/dersteppenwolf/cartografia_web/issues con lo siguiente:
  - Título: Ejercicio Qgis2web - CODIGO_ESTUDIANTE
  - Contenido: 
    - Enlace a la vista pública del mapa generado a través de github pages. (Ejemplo: https://dersteppenwolf.github.io/cartografia_web/02_Conceptos/ejemplo_qgis2web/ )


### Documentación QGIS2Web

- Web Mapping with QGIS2Web https://www.qgistutorials.com/en/docs/web_mapping_with_qgis2web.html
- Publica tus mapas en la web con qgis2web https://mappinggis.com/2016/03/crea-aplicaciones-webmapping-con-qgis/
- Qgis2web wiki https://github.com/tomchadwin/qgis2web/wiki


### Generación de mapas 3D:  Qgis2threejs

- [Qgis2threejs plugin documentation](https://qgis2threejs.readthedocs.io/en/docs/)
- [Tutorial](https://qgis2threejs.readthedocs.io/en/docs/Tutorial.html)

> Qgis2threejs plugin is a QGIS plugin, which visualizes DEM data and vector data in 3D on web browsers. You can build various kinds of 3D objects with simple settings panels, view them in web view of exporter and generate files to publish them to web in simple procedure. In addition, you can save the 3D model in glTF format for 3DCG or 3D printing.



