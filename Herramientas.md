# Herramientas

Enlaces a herramientas comentadas durante el curso.

- [Herramientas](#herramientas)
  - [Software libre para SIG](#software-libre-para-sig)
  - [Bases de datos espaciales](#bases-de-datos-espaciales)
  - [Migración de Datos / ETL](#migraci%C3%B3n-de-datos--etl)
  - [Herramientas GIS en la Nube](#herramientas-gis-en-la-nube)
  - [Recopilación de datos con dispositivos móviles](#recopilaci%C3%B3n-de-datos-con-dispositivos-m%C3%B3viles)
  - [Entornos interactivos para programación (notebooks)](#entornos-interactivos-para-programaci%C3%B3n-notebooks)
  - [Varios](#varios)

## Software libre para SIG

- OSGeoLive: http://live.osgeo.org/en/index.html OSGeoLive is a self-contained bootable DVD, USB thumb drive or Virtual Machine based on Lubuntu, that allows you to try a wide variety of open source geospatial software without installing anything. It is composed entirely of free software, allowing it to be freely distributed, duplicated and passed around.

## Bases de datos espaciales

- Postgis https://postgis.net/
- Spatialite https://www.gaia-gis.it/fossil/libspatialite/index
- Spatialite y Geopackage https://acolita.com/introduccion-al-uso-de-spatialite-y-geopackage-en-qgis-3/

## Migración de Datos / ETL

- GDAL: A translator library for raster and vector geospatial data formats https://gdal.org/

ogr2ogr -f "Geojson" mydata.geojson PG:"host=localhost user=user dbname=yourdb password=yourpwd" -sql "SELECT \* FROM my_table " -progress

- fgdb2postgis: Python library providing functionality for converting ESRI file geodatabase to PostGIS https://github.com/dersteppenwolf/fgdb2postgis
- FME https://www.safe.com/
- GeoKettle https://live.osgeo.org/archive/10.5/ko/overview/geokettle_overview.html

## Database Tools

- registrant: Python package used for generating HTML reports about the contents of Esri geodatabases. https://github.com/dersteppenwolf/registrant
- Enterprise architect https://sparxsystems.com/arcgis/

## Herramientas GIS en la Nube

- Mapbox https://www.mapbox.com/
- Qgis Cloud https://qgiscloud.com/
  - Quickstart https://qgiscloud.com/en/pages/quickstart
- Carto https://carto.com/
  - Versión para estudiantes disponible en "Github Education pack" https://education.github.com/pack
  - How can I get a student account in CARTO? https://carto.com/help/getting-started/student-accounts/
- Mango Maps https://mangomap.com/
- Gis Cloud https://www.giscloud.com/
- Arcgis online http://www.arcgis.com/home/index.html

## Servidores GIS

Open Source:

- Geoserver http://geoserver.org/
- Mapserver https://mapserver.org/
- Geonode http://geonode.org/ Open Source Geospatial Content Management System
  - Documentation http://docs.geonode.org/en/2.10.x/index.html
  - Docker install http://docs.geonode.org/en/2.10.x/install/core/index.html#deploy-a-vanilla-geonode-2-10-with-docker

Comerciales:

- Argis server https://enterprise.arcgis.com/es/server/latest/get-started/windows/what-is-arcgis-for-server-.htm
- Hexagon https://www.hexagongeospatial.com/
- Bluespatial https://www.bluespatial.com/

## Recopilación de datos con dispositivos móviles

- Open data kit https://opendatakit.org/
- Geographical Open Data Kit http://geoodk.com/
- Fulcrum https://www.fulcrumapp.com/

## Entornos interactivos para programación (notebooks)

- Anaconda / Jupyter ( https://medium.com/saturdays-ai/empezando-a-usar-jupyter-notebook-para-python-parte-1-instalaci%C3%B3n-94e97b4c5f37 ) para las prácticas interactivas con python
- Observable https://observablehq.com/
- Google Colab https://medium.com/better-programming/one-stop-guide-to-google-colab-d67c94d30516
- Intro a Google colab https://colab.research.google.com/notebooks/welcome.ipynb?hl=es
- Google Colab: Tips para principiantes https://medium.com/marvik/google-colab-tips-para-principiantes-e39d6e7051d4

## Varios

- GitHub userscripts : Userscripts to add functionality to GitHub. https://github.com/Mottie/GitHub-userscripts
- GitHub static time: A userscript that replaces relative times with a static time formatted as you like it https://github.com/Mottie/GitHub-userscripts/wiki/GitHub-static-time
- Formatting Markdown and Codeblocks With Prettier and Hugo https://www.christopherbiscardi.com/post/formatting-markdown-and-codeblocks-with-prettier-and-hugo/
- Using Prettier with a Pre-commit Hook https://www.brianhan.co/prettier-with-a-pre-commit-hook

