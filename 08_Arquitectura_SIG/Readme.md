# Arquitectura de aplicaciones Web para SIG

- [Arquitectura de aplicaciones Web para SIG](#arquitectura-de-aplicaciones-web-para-sig)
  - [Presentación](#presentaci%C3%B3n)
  - [Bases de datos](#bases-de-datos)
  - [Arquitectura de aplicaciones SIG : Lecturas](#arquitectura-de-aplicaciones-sig--lecturas)
  - [Artículos de interés](#art%C3%ADculos-de-inter%C3%A9s)
  - [Taller](#taller)
    - [Creando un tablero de control con Carto](#creando-un-tablero-de-control-con-carto)
    - [Geonode](#geonode)
      - [Servidor Geonode para pruebas en clase](#servidor-geonode-para-pruebas-en-clase)
      - [Introducción](#introducci%C3%B3n)
      - [Arquitectura](#arquitectura)
      - [Tutoriales](#tutoriales)
      - [Documentación adicional](#documentaci%C3%B3n-adicional)

## Presentación

Enlace https://github.com/dersteppenwolf/cartografia_web/blob/master/08_Arquitectura_SIG/08_Arquitectura_aplicaciones_Web_SIG.pdf

## Bases de datos 

- AWS: Enter the purpose-built database era: Finding the right database for the right job https://pages.awscloud.com/rs/112-TZM-766/images/Enter_the_Purpose-Built-Database-Era.pdf
- AWS - Ingrese a la era de las bases de datos personalizadas: Encuentre la base de datos adecuada para el trabajo adecuado https://es.slideshare.net/dersteppenwolf/aws-ngrese-a-la-era-de-las-bases-de-datos-personalizadas-encuentre-la-base-de-datos-adecuada-para-el-trabajo-adecuado


## Arquitectura de aplicaciones SIG : Lecturas

- Architecting the ArcGIS Platform: Best Practices https://assets.esri.com/content/dam/esrisites/en-us/media/pdf/architecting-the-arcgis-platform.pdf

## Artículos de interés

- Design and implementation of spatial database and geo-processing models for a road geo-hazard information management and risk assessment system WeiDong Wang, Jie Wu, LiGang Fang, Ke Zeng, XinSheng Chang

- Creating a Data Portal for Small Rivers in Rostock
  Sebastian Hübner, Ferdinand Vettermann, Christian Seip and Ralf Bill
  https://link.springer.com/chapter/10.1007/978-3-319-44711-7_24

- Service Oriented Architecture Based SDI Model for Education Sector in India
  Rabindra K. Barik1 and Arun B. Samaddar2
  https://link.springer.com/chapter/10.1007/978-3-319-02931-3_63

- Automated Web-Based Geoprocessing of Rental Prices
  Harald Schernthanner1, Sebastian Steppan, Christian Kuntzsch, Erik Borg and Hartmut Asche
  https://link.springer.com/chapter/10.1007/978-3-319-62401-3_37

- Geospatial Big Data: Challenges and Opportunities. Jae-Gil Lee, Minseo Kang

## Taller 

### Creando un tablero de control con Carto

**Videotutorial**

<a href="https://www.youtube.com/watch?v=9UaAdF2ZkOM&feature=youtu.be" target="_blank" >
<img src="images/video2.png"  >
</a>

**Datos:**

data/world_agriculture_2016.zip

**Modelo de datos:**

![](images/model.png)

**Atributos principales:**

* geom: Geometría tipo polígono
* incomegroup: Categórica.  Nivel de ingreso.
* world_region: Categórica. Región del mundo
* year_2016: Secuencial.  % de área cultivable


**Mockup:** 

![](images/mockup.png)


**Dashboard Resultado**

<a href="https://gkudos.carto.com/u/kudosg/builder/501b7abf-3809-41e7-a71b-39223fb3dbbf/embed" target="_blank" >
<img src="images/dashboard.png"  >
</a>


### Geonode

Geonode http://geonode.org/

    Open Source Geospatial Content Management System
    GeoNode is a web-based application and platform for developing 
    geospatial information systems (GIS) and for 
    deploying spatial data infrastructures (SDI).

    It is designed to be extended and modified, 
    and can be integrated into existing platforms.

SDI

    A spatial data infrastructure (SDI) is a data 
    infrastructure implementing a framework of geographic 
    data, metadata, users and tools that are interactively 
    connected in order to use spatial data in an 
    efficient and flexible way. 

#### Servidor Geonode para pruebas en clase


* Url Geonode http://34.83.176.208
* Url WMS Geonode http://34.83.176.208/geoserver/wms?version=1.3.0&request=GetCapabilities 
* Url WFS Geonode http://34.83.176.208/geoserver/wfs?version=2.0.0&request=GetCapabilities 
* Url CSW Geonode http://34.83.176.208/catalogue/csw
  * Consultando el catálogo de geonode con QGIS https://docs.qgis.org/3.10/en/docs/user_manual/plugins/core_plugins/plugins_metasearch.html?highlight=csw

#### Introducción 

+ Introducción a Geonode https://es.slideshare.net/geosolutions/introduction-to-geonode-89583201

#### Arquitectura 

  Imagen tomada de "GeoNode Integration with GIS
  and Data Processing workflows" http://siteresources.worldbank.org/INTLACREGTOPURBDEV/Images/840342-1264721236030/GeoNodeDM_2_IntegrationWithGISandDataProcessing.pdf  

![](images/geonode.png)

#### Tutoriales

+ Videotutorial: Introducción a Geonode


+ Video - Seminario Taller web: Manejo básico de GeoNode   https://www.youtube.com/watch?v=N1OqQb8b3pI&feature=youtu.be
  + Nota: El tutorial para la carga de datos empieza en el minuto 9:44 https://youtu.be/N1OqQb8b3pI?t=584

<a href="https://youtu.be/N1OqQb8b3pI?t=584" target="_blank" >
<img src="images/video_geonode.png"  >
</a>




#### Documentación adicional

+ Geonode User Features http://geonode.org/user_features/
+ Publicando datos y mapas: GeoNode Quickstart  https://live.osgeo.org/es/quickstart/geonode_quickstart.html
+ Bringing GEOSS services into Practice for Beginners: GeoNode Tutorial https://es.slideshare.net/dersteppenwolf/bringing-geoss-services-into-practice-for-beginners-geonode-tutorial
+ Spatial Data Infrastructure Best Practices with GeoNode https://es.slideshare.net/SebastianBenthall/spatial-data-infrastructure-best-practices-with-geonode?

