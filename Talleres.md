# Talleres y Tareas

- [Talleres y Tareas](#talleres-y-tareas)
  - [Taller 2: Introducción a Qgis](#taller-2-introducci%C3%B3n-a-qgis)
    - [Objetivos](#objetivos)
    - [Ejercicio 1](#ejercicio-1)
      - [Docs: Tutoriales cartografía con SIG Desktop](#docs-tutoriales-cartograf%C3%ADa-con-sig-desktop)
      - [Fuentes de datos sugeridas](#fuentes-de-datos-sugeridas)
    - [Ejercicio 2: Creando mapas con Qgis2web](#ejercicio-2-creando-mapas-con-qgis2web)
      - [Docs: QGIS2Web](#docs-qgis2web)
      - [Docs: Qgis2threejs](#docs-qgis2threejs)
  - [Taller 3: Geojson](#taller-3-geojson)
  - [Taller 4: Consumiendo servicios WMS](#taller-4-consumiendo-servicios-wms)
  - [Taller 5: Consumiendo servicios WMTS](#taller-5-consumiendo-servicios-wmts)
  - [Taller 6: Consumiendo servicios WFS](#taller-6-consumiendo-servicios-wfs)
  - [Taller 7: Consumiendo servicios WCS](#taller-7-consumiendo-servicios-wcs)
  - [Taller 8: Cargando datos en Postgis Utilizando QGIS](#taller-8-cargando-datos-en-postgis-utilizando-qgis)
  - [Taller 9: Publicando servicios WMS, WMTS y WFS en Geoserver](#taller-9-publicando-servicios-wms-wmts-y-wfs-en-geoserver)
  - [Taller 11: Publicando datos en Geonode](#taller-11-publicando-datos-en-geonode)
  - [Taller 12: Publicando mapas utilizando herramientas disponibles en la nube](#taller-12-publicando-mapas-utilizando-herramientas-disponibles-en-la-nube)
  - [Taller 13: Ejemplos Python / Arcpy](#taller-13-ejemplos-python--arcpy)
  - [Taller 14: Servicios OGC y Python](#taller-14-servicios-ogc-y-python)
  - [Taller 15: Using Python to Analyze Spatial Data](#taller-15-using-python-to-analyze-spatial-data)
  - [Taller 16: Desarrollo web con Leaflet y WMS](#taller-16-desarrollo-web-con-leaflet-y-wms)









## Taller 2: Introducción a Qgis

### Objetivos

- Conocer el funcionamiento básico de QGIS
- Publicar mapas en la web con la ayuda de QGIS.

### Ejercicio 1

Conocer el funcionamiento básico de QGIS

#### Docs: Tutoriales cartografía con SIG Desktop

- QGIS Tutorials http://www.qgistutorials.com/en/index.html
- Thematic Maps using arcgis http://what-when-how.com/gis-and-spatial-analysis-for-the-social-sciences/thematic-maps-gis-and-spatial-analysis-part-1/
- A quick tour of displaying layers (Arcgis)
- Elements of a map https://www.gislounge.com/whats-in-a-map/
- Cartographic Tips For Creating Beautiful Maps With ArcMap https://alexurquhart.com/post/cartography-tips-arcmap/

#### Fuentes de datos sugeridas

- Natural Earth (Large scale data, 1:10m) http://www.naturalearthdata.com/downloads/
- Marco Geográfico Nacional (MGN) Dane 2017 - Colombia https://geoportal.dane.gov.co/
- World Borders http://thematicmapping.org/downloads/world_borders.php
- World Bank https://data.worldbank.org/
- World Bank Explorer http://data.un.org/Explorer.aspx
- Portal de datos abiertos de Colombia: datos.gov.co
- Portal de datos abiertos del IGAC: datos.igac.gov.co
- Openstreetmap (geofabrik) http://download.geofabrik.de/
- IDECA https://www.ideca.gov.co/datos-de-referencia
- Datos abiertos Bogotá http://datosabiertos.bogota.gov.co/

### Ejercicio 2: Creando mapas con Qgis2web 

Qgis2web es una herramienta que exporta los proyectos de QGIS en mapas web de OpenLayers https://openlayers.org/ o Leaflet https://leafletjs.com/ (crea automáticamente los archivos HTML, Javascript y CSS).

La herramienta convierte las capas vectoriales en GeoJSON https://geojson.org/ y crea una estructura de carpetas con un archivo **index.html** que contiene el mapa web.

Además el plugin es capaz de exportar la simbología definida en QGIS tanto de puntos, líneas y polígonos e incluir un control de visibilidad de capas y varios controles más.

**Ejemplo**

![qgis2web](images/qgis2web.png "qgis2web")

- Página web: https://sigfedepanela.github.io/PreciosSemanales/
- Repositorio en github: https://github.com/sigfedepanela/PreciosSemanales
- Geojson generado por la herramienta: https://raw.githubusercontent.com/sigfedepanela/PreciosSemanales/gh-pages/layers/PreciosporDepartamento_2.js



#### Docs: QGIS2Web

- Web Mapping with QGIS2Web https://www.qgistutorials.com/en/docs/web_mapping_with_qgis2web.html
- Publica tus mapas en la web con qgis2web https://mappinggis.com/2016/03/crea-aplicaciones-webmapping-con-qgis/
- Qgis2web wiki https://github.com/tomchadwin/qgis2web/wiki



#### Docs: Qgis2threejs

- [Qgis2threejs plugin documentation](https://qgis2threejs.readthedocs.io/en/docs/)
- [Tutorial](https://qgis2threejs.readthedocs.io/en/docs/Tutorial.html)

> Qgis2threejs plugin is a QGIS plugin, which visualizes DEM data and vector data in 3D on web browsers. You can build various kinds of 3D objects with simple settings panels, view them in web view of exporter and generate files to publish them to web in simple procedure. In addition, you can save the 3D model in glTF format for 3DCG or 3D printing.


## Taller 3: Geojson

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

Ejercicio 3: Clientes ligeros

- Visualizando geojson usando mapbox gl https://www.mapbox.com/mapbox-gl-js/example/geojson-polygon/
- Visualizando geojson usando leaflet http://leafletjs.com/examples/geojson/
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

## Taller 4: Consumiendo servicios WMS

Ejemplos de WMS:

- IGAC https://geoportal.igac.gov.co/contenido/datos-abiertos-cartografia-y-geografia
- Datos Abiertos Bogotá https://datosabiertos.bogota.gov.co/dataset?res_format=WMS

Ejercicio 1: Visualizar con clientes ligeros

- Visor WMS Esri Js https://developers.arcgis.com/javascript/3/samples/layers_wms/
- Mapbox Gl https://www.mapbox.com/mapbox-gl-js/example/wms/
- Carto https://carto.com/learn/guides/styling/inserting-external-basemaps/

Ejercicio 2: Visualizar con clientes pesados

- Qgis Working with WMS Data http://www.qgistutorials.com/en/docs/working_with_wms.html
- Arcgis Desktop Adding WMS services http://desktop.arcgis.com/en/arcmap/latest/map/web-maps-and-services/adding-wms-services.htm

## Taller 5: Consumiendo servicios WMTS

Ejercicios

- Cree una cuenta en mapbox https://www.mapbox.com/
- Modifique / publique un mapa base
- Consuma el mapa como WMTS con diferentes clientes

Referencias:

- Mapa base con Cartogram https://apps.mapbox.com/cartogram/#13.01/40.7251/-74.0051
- Mapbox Create a custom style https://docs.mapbox.com/help/tutorials/create-a-custom-style/
- Add Mapbox maps as layers in ArcGIS and QGIS with WMTS https://docs.mapbox.com/help/tutorials/mapbox-arcgis-qgis/
- Is it possible to use WMTS in QGIS? https://gis.stackexchange.com/questions/52346/is-it-possible-to-use-wmts-in-qgis

## Taller 6: Consumiendo servicios WFS

Ejemplos de WFS:

- Datos Abiertos Bogotá https://datosabiertos.bogota.gov.co/dataset?res_format=WFS&_res_format_limit=0
- Servidor Geoserver Clase http://34.83.176.208:18080/geoserver/ows?service=wfs&version=2.0.0&request=GetCapabilities

Ejercicio 1:

- Cargue datos vectoriales en QGIS y Arcgis desde servicios WFS
- QGIS : Using WFS https://docs.qgis.org/testing/en/docs/training_manual/online_resources/wfs.html
- Arcgis : Adding a WFS connection https://desktop.arcgis.com/en/arcmap/latest/extensions/production-mapping/adding-a-wfs-connection.htm

## Taller 7: Consumiendo servicios WCS

Ejemplos de WCS:

- Servidor Geoserver Clase http://34.83.176.208:18080/geoserver/ows?service=WCS&version=2.0.1&request=GetCapabilities

Ejercicio 1:

- Cargue datos provenientes de servicios WCS en QGIS https://docs.qgis.org/3.4/en/docs/user_manual/working_with_ogc/ogc_client_support.html#wcs-client

## Taller 8: Cargando datos en Postgis Utilizando QGIS

Ejercicio:

- Cargar datos geográficos en postgresql / postgis utilizando qgis.
- Utilice el servidor de base de datos en la nube asignado en la clase.
- Loading data into PostgreSQL from QGIS https://astuntech.atlassian.net/wiki/spaces/ISHAREHELP/pages/137390054/Loading+data+into+PostgreSQL+from+QGIS
- Nota: Al nombre de la capa asígnele su prefijo asignado según la lista de clase. Ejemplo: u1_departamentos

## Taller 9: Publicando servicios WMS, WMTS y WFS en Geoserver

Ejercicio:

- Publicar servicios WMS y WFS en geoserver a partir de los datos cargados en el taller 8.
- Utilice el servidor geoserver en la nube asignado en la clase.
- Publishing a PostGIS table https://docs.geoserver.org/stable/en/user/gettingstarted/postgis-quickstart/index.html
- Nota: Al nombre de la capa publicada asígnele su prefijo asignado según la lista de clase. Ejemplo: u1_departamentos_layer

## Taller 11: Publicando datos en Geonode

Ejercicio:

- Publicar datos en Geonode .
- Utilice el servidor Geonode en la nube asignado en la clase.
- Geonode Quick start https://live.osgeo.org/es/quickstart/geonode_quickstart.html
- Nota: Al nombre de la capa publicada asígnele su prefijo asignado según la lista de clase. Ejemplo: u1_departamentos_layer

## Taller 12: Publicando mapas utilizando herramientas disponibles en la nube

- Ver https://github.com/dersteppenwolf/taller_gis_cloud

## Taller 13: Ejemplos Python / Arcpy

- Python variables y operaciones: https://gist.github.com/dersteppenwolf/fca39c1971fd0fd7c3ce
- Describir feature https://gist.github.com/dersteppenwolf/6dc546ef359ffbb85947
- Buffer https://gist.github.com/dersteppenwolf/82d65df9544933289bab
- Clip https://gist.github.com/dersteppenwolf/6dae5bfd9521db50e567

## Taller 14: Servicios OGC y Python

Ejercicio: Introducción a Python

- Python for beginners https://data-flair.training/blogs/start-learning-python-with-infographic/ https://d2h0cx97tjks2p.cloudfront.net/blogs/wp-content/uploads/sites/2/2019/02/Python-Infographic-for-beginners-to-learn-Python-Quickly.jpg
- Python Hello world https://www.learnpython.org/en/Hello,_World!
- Primeros pasos con Jupyter Notebook https://www.adictosaltrabajo.com/2018/01/18/primeros-pasos-con-jupyter-notebook/
- [Ejemplo Python y Jupyter : "Hola Mundo" ](02_Servicios_Web_Geoservicios_OGC/ejemplo_python.ipynb)
- Google Colab: Python y Machine Learning en la nube https://www.adictosaltrabajo.com/2019/06/04/google-colab-python-y-machine-learning-en-la-nube/
  - “Colaboratory es un entorno gratuito de Jupyter Notebook que no requiere configuración y que se ejecuta completamente en la nube.”
- Ejemplo de servicios OGC con Python OWSLib https://colab.research.google.com/drive/1S1UygmFjZIFswq8gtMxuYoX571vdI2KR

## Taller 15: Using Python to Analyze Spatial Data

Ver https://github.com/dersteppenwolf/pycon

## Taller 16: Desarrollo web con Leaflet y WMS

- Utilizando WMS desde leaflet http://bl.ocks.org/hpfast/2155366c06f4ae0fae59df216fc3f7ec


