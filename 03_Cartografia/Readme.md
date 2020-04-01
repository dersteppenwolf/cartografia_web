# 3 -  Cartografía
- [3 - Cartografía](#3---cartograf%C3%ADa)
  - [Presentación](#presentaci%C3%B3n)
  - [Recursos](#recursos)
    - [Tutoriales cartografía con SIG Desktop](#tutoriales-cartograf%C3%ADa-con-sig-desktop)
  - [Ejercicio 1 : Publicando mapas en la nube con Qgis Cloud](#ejercicio-1--publicando-mapas-en-la-nube-con-qgis-cloud)
  - [Ejercicio 2 : Visualizando datos con Kepler.gl](#ejercicio-2--visualizando-datos-con-keplergl)

## Presentación

Enlace: https://github.com/dersteppenwolf/cartografia_web/blob/master/03_Cartografia/03_Cartografia.pdf


## Recursos

Cartografía Temática:

- Introduction to cartography https://www.slideshare.net/GavinMalavolta/introduction-to-cartography-geography1-14174414
- So You Want To Make A Map? https://medium.com/data-visualization-society/so-you-want-to-make-a-map-58c7f55f6b20
- Lab Thematic Web Map Design  https://github.com/dersteppenwolf/geog371/blob/master/labs/lab03/readme.md
- Intro to thematic mapping with carto https://www.slideshare.net/KristenVincent/maptime-madison-december-7th-2016?qid=09ec7af3-f23f-4dae-afc0-20aac79202c6&v=&b=&from_search=8
- Making Great Maps https://www.e-education.psu.edu/maps/l5_p2.html
- Layout and Symbolization https://www.e-education.psu.edu/maps/l5_p3.html


Vuestros mapas son feos y no sabéis por qué
-   https://geoinquietosvlc.github.io/tus_mapas_son_feos/
-   https://github.com/geoinquietosvlc/tus_mapas_son_feos
-   https://tus-mapas-son-feos.readthedocs.io/es/develop/

Colores:

- Choosing Colors, Match Colors To Your Data https://www.e-education.psu.edu/maps/l5_p5.html
- ColorBrewer: Color Advice for Maps http://colorbrewer2.org/
- d3-scale-chromatic : Sequential, diverging and categorical color scales. https://github.com/d3/d3-scale-chromatic

Métodos de clasificación:

- Data Classification https://www.e-education.psu.edu/maps/l5_p6.html 
- Geospatial Analysis : Classification and clustering http://www.spatialanalysisonline.com/HTML/index.html?classification_and_clustering.htm
- Data classification methods https://pro.arcgis.com/en/pro-app/help/mapping/layer-properties/data-classification-methods.htm


Normalización de datos:

- Normalization, Mapping Rates, Not Totals https://www.e-education.psu.edu/maps/l4_p5.html
- CV-05 - Statistical Mapping (Enumeration, Normalization, Classification) https://gistbok.ucgis.org/bok-topics/statistical-mapping-enumeration-normalization-classification
- Mapping with Aggregated Statistics http://www.pbcgis.com/normalize/


Otros:
- Recomendaciones cartografía símbolos proporcionales https://twitter.com/ramiroaznar/status/1245323283756613632?s=03
- Visualize 2015 Urban Populations with Proportional Symbols https://carto.com/blog/proportional-symbol-maps/
- Recomendaciones mapas coropletas https://twitter.com/ramiroaznar/status/1242693988680859650

### Tutoriales cartografía con SIG Desktop

- Thematic Maps using arcgis http://what-when-how.com/gis-and-spatial-analysis-for-the-social-sciences/thematic-maps-gis-and-spatial-analysis-part-1/
- Elements of a map https://www.gislounge.com/whats-in-a-map/
- Cartographic Tips For Creating Beautiful Maps With ArcMap https://alexurquhart.com/post/cartography-tips-arcmap/


## Ejercicio 1 : Publicando mapas en la nube con Qgis Cloud

QGIS Cloud  es un servicio en la nube Web-GIS que permite publicar mapas, datos y servicios en Internet desde Qgis Desktop.

Realizar lo siguiente: 

- Cree una cuenta gratuita en Qgis Cloud https://qgiscloud.com/
- Instale el plugin de Qgis Cloud https://plugins.qgis.org/plugins/qgiscloud/
- Publique mapas en Qgis Cloud desde Qgis 
  - Quickstart https://qgiscloud.com/pages/quickstart
  - Cómo publicar mapas online con QGIS Cloud https://mappinggis.com/2019/01/como-publicar-mapas-con-qgis/



## Ejercicio 2 : Visualizando datos con Kepler.gl

**Kepler.gl**  https://kepler.gl/ __Kepler.gl is a powerful open source geospatial analysis tool for large-scale data sets.__

Kepler.gl is a data-agnostic, high-performance web-based application for visual exploration of large-scale geolocation data sets. Built on top of **Mapbox GL** and **deck.gl**, kepler.gl can render millions of points representing thousands of trips and perform spatial aggregations on the fly.

**Enlaces:**

- **Mapbox GL JS** is a JavaScript library that uses WebGL to render interactive maps from vector tiles and Mapbox styles.  https://docs.mapbox.com/mapbox-gl-js/api/
- **WebGL**	It is the JavaScript binding for OpenGL. OpenGL (Open Graphics Library) is a cross-language, cross-platform API for 2D and 3D graphics. https://www.tutorialspoint.com/webgl/webgl_introduction.htm
  - It is a JavaScript API that can be used with HTML5. WebGL code is written within the <canvas> tag of HTML5. It is a specification that allows Internet browsers access to Graphic Processing Units (GPUs) on those computers where they were used.
- **deck.gl** is a WebGL-powered framework for visual exploratory data analysis of large datasets. https://deck.gl/#/
- From Beautiful Maps to Actionable Insights: **Introducing kepler.gl**, Uber’s Open Source Geospatial Toolbox https://eng.uber.com/keplergl/
- User guide: https://github.com/keplergl/kepler.gl/blob/master/docs/user-guides/j-get-started.md
- Código en Github https://github.com/keplergl/kepler.gl
- **How to create a map in 3 minutes:** Animating 40 years of California Earthquakes https://medium.com/vis-gl/animating-40-years-of-california-earthquakes-e4ffcdd4a289
- **Making a choropleth map:** Visualizing Unemployment for U.S. Counties with kepler.gl https://medium.com/vis-gl/visualizing-u-s-county-unemployment-with-kepler-gl-c5f2ed31c71
-  Uber Movement and kepler.gl : Using kepler.gl and Movement data to Visualize Traffic Effects of a Rainstorm https://medium.com/vis-gl/movement-in-kepler-d00e843f464d



**Datos Tweets Georreferenciados:**

 - Formato Csv https://github.com/dersteppenwolf/cartografia_web/blob/master/03_Cartografia/example/geotweets.csv

|id                 |source      |user.screen_name|pin.location.lat|pin.location.lon|lang|creation_date      |user.followers_count|entities.hashtags.text                   |
|-------------------|------------|----------------|----------------|----------------|----|-------------------|--------------------|-----------------------------------------|
|1201026267883065344|instagram   |alitos25        |3.47645398      |-76.52784348    |es  |2019-12-01T01:32:30|696                 |Chipichape,Mom,Diciembre,ILoveYou        |
|1201026433306357767|instagram   |GuillermoLVP80  |3.89502747      |-76.29474677    |es  |2019-12-01T01:33:10|15                  |nuevostalentos,guadalajaradebuga         |
|1201026492236533760|instagram   |COMBOESTRELLAS  |4.83553936      |-75.66899716    |es  |2019-12-01T01:33:24|727                 |elcombodelasestrellas,marlonmuriel,envivo|
|1201027339578007552|world cities|MedellinCO      |6.24            |-75.59          |en  |2019-12-01T01:36:46|133                 |                                         |


 - Formato geojson https://github.com/dersteppenwolf/cartografia_web/blob/master/03_Cartografia/example/geotweets.geojson

```json
{
"type": "FeatureCollection",
"name": "geotweets",
"crs": { "type": "name", "properties": { "name": "urn:ogc:def:crs:OGC:1.3:CRS84" } },
"features": [
{ "type": "Feature", "properties": { "id": "1201026267883065344", "source": "instagram", "user.screen_name": "alitos25", "pin.location.lat": "3.47645398", "pin.location.lon": "-76.52784348", "lang": "es", "creation_date": "2019-12-01T01:32:30", "user.followers_count": "696", "entities.hashtags.text": "Chipichape,Mom,Diciembre,ILoveYou" }, "geometry": { "type": "Point", "coordinates": [ -76.52784348, 3.47645398 ] } },
{ "type": "Feature", "properties": { "id": "1201026433306357767", "source": "instagram", "user.screen_name": "GuillermoLVP80", "pin.location.lat": "3.89502747", "pin.location.lon": "-76.29474677", "lang": "es", "creation_date": "2019-12-01T01:33:10", "user.followers_count": "15", "entities.hashtags.text": "nuevostalentos,guadalajaradebuga" }, "geometry": { "type": "Point", "coordinates": [ -76.29474677, 3.89502747 ] } },
{ "type": "Feature", "properties": { "id": "1201026492236533760", "source": "instagram", "user.screen_name": "COMBOESTRELLAS", "pin.location.lat": "4.83553936", "pin.location.lon": "-75.66899716", "lang": "es", "creation_date": "2019-12-01T01:33:24", "user.followers_count": "727", "entities.hashtags.text": "elcombodelasestrellas,marlonmuriel,envivo" }, "geometry": { "type": "Point", "coordinates": [ -75.66899716, 4.83553936 ] } },

```

Archivo Html Generado por kepler.gl 
- vista web https://dersteppenwolf.github.io/cartografia_web/03_Cartografia/example/kepler.gl.html
- código https://github.com/dersteppenwolf/cartografia_web/blob/master/03_Cartografia/example/kepler.gl.html
