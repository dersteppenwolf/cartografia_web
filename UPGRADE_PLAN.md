# Plan de modernizacion del curso de cartografia web

**Fecha de referencia:** 2026-08-03  
**Estado:** Propuesto  
**Alcance:** Modernizacion curricular, tecnica, editorial y operativa del repositorio `cartografia_web`.

## 1. Objetivo

Actualizar el curso, originalmente estructurado en 2020, para que ensene publicacion de cartografia web con practicas reproducibles, interoperables, seguras y actuales. La actualizacion debe conservar los fundamentos valiosos de SIG, cartografia, PostGIS, GeoServer y servicios OGC clasicos, a la vez que incorpora APIs geoespaciales modernas, datos cloud-native, clientes web actuales, automatizacion y operacion.

El resultado sera un curso que permita a cada estudiante construir, documentar y probar una aplicacion geoespacial web; publicar su frontend o producir un artefacto estatico desplegable; y reproducir localmente los servicios con estado. Ninguna actividad obligatoria dependera de infraestructura temporal, cuentas personales del docente ni de un unico proveedor SaaS.

Este plan asume las 32 horas presenciales registradas en `Programa.md` y propone 40 horas de trabajo autonomo. Si la institucion no aprueba ese componente autonomo, la profundizacion profesional definida en la seccion 4 se trasladara a un curso o modulo posterior.

## 2. Principios de ejecucion

1. Conservar los conceptos antes que los productos: cartografia, interoperabilidad, SQL espacial y arquitectura no dependen de una plataforma SaaS.
2. Mantener compatibilidad didactica con servicios OGC Web Services clasicos, pero ensenar OGC API Common y OGC API - Features como base para implementaciones nuevas.
3. Preferir herramientas abiertas, formatos abiertos y entornos reproducibles para las practicas obligatorias.
4. Separar herramientas obligatorias de alternativas comerciales u optativas.
5. No incluir credenciales, tokens activos, IPs de infraestructura docente ni dependencias HTTP inseguras en ejemplos publicados.
6. Validar cada modulo de extremo a extremo en una instalacion limpia antes de declararlo listo.
7. Mantener el material conceptual independiente de versiones cuando sea posible, pero fijar versiones exactas, extensiones y digests en lockfiles, contenedores y demas artefactos ejecutables.
8. Introducir seguridad, accesibilidad, licencias y calidad desde la primera fase; no tratarlas como controles agregados al final.
9. Distinguir estandares aprobados, especificaciones candidatas y tecnologias experimentales.

## 3. Alcance y resultado esperado

### Incluido

- Actualizacion de las unidades, ejercicios, tareas y criterios de evaluacion.
- Reemplazo o modernizacion de ejemplos HTML, JavaScript, notebooks y guias de infraestructura.
- Creacion de un stack local reproducible con Docker Compose para PostGIS, GeoServer y archivos estaticos con soporte de HTTP Range.
- Adicion obligatoria de OGC API Common, OGC API - Features y STAC estatico; practica guiada de MVT/PMTiles y COG, con una de las dos rutas como requisito del proyecto.
- Presentacion electiva de OGC API - Records, Processes, EDR, Coverages, STAC API, Zarr, GeoParquet, 3D Tiles y nubes de puntos.
- Introduccion de TypeScript, Vite, MapLibre GL JS y JavaScript moderno.
- Automatizacion mediante scripts locales, con GitHub Actions como implementacion de referencia y no como requisito exclusivo.
- Seguridad basica, accesibilidad, rendimiento, documentacion y operacion como criterios de entrega.
- Inventario y saneamiento de enlaces, recursos externos, tokens, licencias, datos personales y contenidos historicos.

### Excluido de la primera iteracion

- Migrar o reescribir cada exportacion generada por QGIS2Web.
- Construir una plataforma institucional completa de aprendizaje o una infraestructura productiva de alta disponibilidad.
- Obligar el uso de un framework frontend especifico.
- Eliminar WMS, WFS, WMTS, SLD o GeoServer: permanecen como contenidos de interoperabilidad y compatibilidad.
- Exigir que cada estudiante publique PostGIS o GeoServer en Internet.
- Garantizar funcionamiento completamente offline; se garantizara independencia de la infraestructura historica y se documentaran las descargas necesarias.

## 4. Arquitectura didactica objetivo

El curso tendra un nucleo comun obligatorio y una profundizacion profesional electiva. No se presentaran como dos rutas equivalentes: el nucleo define lo que todos deben aprobar y los electivos amplian el alcance sin bloquear la finalizacion del curso.

| Nivel | Objetivo | Herramientas principales |
| --- | --- | --- |
| Nucleo obligatorio | Publicar un mapa claro, accesible y documentado; consumir WMS/WFS y OGC API - Features; y reproducir un stack local preparado | QGIS LTR, GeoPackage, GeoJSON, Leaflet, PostGIS, GeoServer 3.x, Docker Compose |
| Proyecto integrador obligatorio | Optimizar y publicar un frontend estatico que consuma datos o servicios reproducibles | TypeScript, Vite, MapLibre GL JS, MVT/PMTiles o COG, scripts locales de calidad |
| Profundizacion electiva | Ampliar interoperabilidad, analitica, catalogos o visualizacion avanzada | OGC API - Records/Processes/EDR, STAC API, Zarr, OpenLayers avanzado, GeoParquet, Cesium/3D Tiles |

Las soluciones comerciales o SaaS, como ArcGIS Online, Mapbox, CARTO, Flourish, QGIS Cloud, GitHub Pages y Kepler.gl, se mantendran como implementaciones de referencia o alternativas optativas. Ninguna tarea obligatoria requerira una cuenta, token o servicio SaaS de terceros, gratuito o de pago. Los comandos de build, prueba y validacion deberan poder ejecutarse localmente aunque el repositorio use GitHub Actions como CI de referencia.

### 4.1 Distribucion de tiempo

| Unidad | Horas presenciales | Trabajo autonomo estimado | Alcance obligatorio |
| --- | ---: | ---: | --- |
| 1. Web, Git y publicacion | 4 | 4 | HTML semantico, Git, JavaScript moderno y primer mapa Leaflet |
| 2. Datos y calidad | 4 | 5 | QGIS, GeoPackage/GeoJSON, CRS, metadatos, licencia y mapa tematico |
| 3. Cartografia accesible y UX | 4 | 4 | WCAG 2.2 AA aplicable, movil, teclado, leyenda y alternativa de datos |
| 4. APIs e interoperabilidad | 4 | 5 | HTTP, OGC clasico, OGC API Common/Features y comparacion WFS/Features |
| 5. Servicios e infraestructura | 4 | 6 | PostGIS, GeoServer, Docker Compose, SQL e indices |
| 6. Cliente web moderno | 4 | 6 | Plantilla TypeScript/Vite/MapLibre, filtros y manejo de errores |
| 7. Rendimiento y cloud-native | 4 | 5 | MVT/PMTiles para vector o COG para raster, STAC estatico y HTTP Range |
| 8. Operacion y publicacion | 4 | 5 | Pruebas, CI, secretos, artefacto desplegable y documentacion |
| **Total** | **32** | **40** | **Un proyecto vertical acumulativo** |

Los contenidos electivos no consumiran horas del nucleo salvo que una cohorte sustituya explicitamente otro tema. La carga se volvera a medir durante el piloto.

En la Unidad 7 todo el alumnado consumira y validara artefactos PMTiles y COG ya preparados. Cada estudiante elegira una sola ruta para generar, integrar y medir en su proyecto: vectorial con MVT/PMTiles o raster con COG. Las cinco horas autonomas se distribuiran en una hora de comparacion comun y cuatro horas para la ruta seleccionada.

### 4.2 Arquitectura tecnica de referencia

| Capacidad | Implementacion base | Condicion |
| --- | --- | --- |
| Datos y SQL espacial | PostgreSQL/PostGIS en imagen fijada | Obligatoria |
| WMS y WFS | GeoServer 3.x | Obligatoria |
| WMTS | GeoServer/GeoWebCache | Demostrativa; electiva en el proyecto |
| WCS, CSW y WPS | Modulos compatibles de GeoServer o servicio de referencia | Panorama/electivas |
| OGC API - Features | Modulo compatible de GeoServer, instalado y fijado junto con la imagen | Obligatoria |
| Estilos | SLD en GeoServer | Obligatoria; CSS/YSLD/MBStyle son comparativos |
| Teselas vectoriales | Extension Vector Tiles de GeoServer | Obligatoria para la demostracion y ruta vectorial |
| MVT/PMTiles | Tippecanoe y PMTiles CLI en herramientas o contenedores fijados | Obligatoria para la ruta vectorial |
| COG | GDAL o rio-cogeo fijado | Obligatoria para la ruta raster |
| Cliente PMTiles | Paquete `pmtiles` y protocolo registrado en MapLibre | Obligatoria para la ruta vectorial |
| Cliente COG | `@geomatico/maplibre-cog-protocol` registrado en MapLibre | Obligatoria para la ruta raster |
| Archivos con HTTP Range | Servidor estatico local configurado para Range y CORS | Obligatoria para PMTiles/COG |
| STAC | Catalogo, Collection e Items pequenos versionados y validados | Obligatoria sin requerir una STAC API |
| OGC API - Processes/STAC API | pygeoapi o implementacion seleccionada por cohorte | Electiva |
| Hosting | Build estatico local; Pages u hosting institucional como adaptador | Publicacion remota opcional |

OGC API - Coverages se presentara como especificacion candidata mientras no sea un estandar aprobado. OGC API - Records, Processes y EDR se explicaran como panorama o electivos. WPS se conservara para comparar su modelo con OGC API - Processes.

### 4.3 Versiones y compatibilidad

Antes de cada cohorte se publicara una matriz legible por personas y maquinas con versiones exactas, fecha de fin de soporte y compatibilidad. Para la primera implementacion se validaran como candidatos QGIS 3.44 LTR, Node.js 24 LTS, GeoServer 3.0.x y Java 17 o 21. La combinacion PostgreSQL/PostGIS se elegira despues de probar la imagen y extensiones seleccionadas.

Los manifiestos ejecutables fijaran versiones y, cuando sea viable, digests. No se actualizaran versiones mayores durante una cohorte; los parches de seguridad se probaran y aplicaran mediante una entrega controlada.

## 5. Fases de trabajo

### Fase 0. Gobierno, inventario y decisiones base

**Objetivo:** establecer el alcance definitivo y evitar que el nuevo material herede dependencias inseguras o no reproducibles.

**Actividades**

1. Designar responsables de contenido SIG/cartografico, desarrollo web, infraestructura y revision pedagogica.
2. Crear un inventario de todos los enlaces, endpoints, recursos CDN, datasets, videos, capturas, tokens y cuentas externas usados por el repositorio.
3. Clasificar cada recurso como: conservar, actualizar, reemplazar, archivar como historico o eliminar.
4. Poner en cuarentena los archivos de redes sociales geolocalizados hasta verificar base legal, licencia y necesidad pedagogica; reemplazarlos por datos sinteticos o agregados si no se autoriza su redistribucion.
5. Revisar el historial Git para detectar tokens, credenciales y datos personales. Revocar credenciales activas; eliminar del arbol actual los valores reales y evaluar reescritura del historial solo mediante una decision separada y coordinada.
6. Crear una matriz de licencias por artefacto que separe codigo, material docente, presentaciones, imagenes, fuentes, datos y dependencias de terceros. Resolver el alcance de MIT frente a materiales con otras licencias y crear `THIRD_PARTY_NOTICES.md` o `LICENSES/`.
7. Confirmar la politica institucional para cuentas cloud, limites de coste, datos personales, licencias, accesibilidad y publicacion estudiantil.
8. Definir versiones de referencia de la primera cohorte modernizada:
   - QGIS LTR vigente.
   - PostgreSQL/PostGIS vigentes y soportados.
   - GeoServer 3.x y Java 17 o 21, segun compatibilidad validada.
   - Node.js LTS vigente.
   - Python vigente y entorno virtual o `uv`/`pip-tools` definido.
9. Elegir un proveedor o entorno para demos institucionales, si se requiere uno; el curso debe seguir funcionando localmente sin dicho proveedor.
10. Establecer una politica para actualizar dependencias, datasets y enlaces antes de cada cohorte.

**Entregables**

- Inventario versionado de recursos externos y su estado.
- Matriz de decisiones tecnicas y de herramientas.
- Matriz de licencias y politica de secretos, atribucion, privacidad y publicacion de datos.
- Decision documentada sobre cada dataset social geolocalizado y, si aplica, reemplazo anonimizado o sintetico.
- Calendario de actualizacion semestral/anual.

**Criterios de aceptacion**

- Ningun requisito obligatorio depende de una IP, cuenta, token o servicio SaaS de terceros, nuevo o existente.
- Se conocen propietario, licencia, disponibilidad y clasificacion de sensibilidad de cada dataset redistribuido, obligatorio u optativo.
- No se publica informacion personal o geolocalizacion individual sin una base documentada, minimizacion y revision de riesgo.
- Las credenciales encontradas se han revocado y el arbol actual supera un escaneo de secretos.
- Existe una lista aprobada de versiones y una estrategia para revisarlas.

### Fase 1. Estabilizacion, estructura y controles base

**Objetivo:** corregir fallos evidentes y proteger los cambios posteriores con una estructura y controles minimos.

**Actividades**

1. Corregir el enlace de Unidad 8 en `README.md`, que actualmente apunta a `05_Arquitectura_SIG` en vez de `08_Arquitectura_SIG`.
2. Eliminar fechas de 2020, referencias a la modalidad de emergencia y el tema obligatorio de COVID-19 de `Programa.md`.
3. Reemplazar instrucciones ligadas a issues y repositorios personales del docente por un mecanismo institucional configurable.
4. Revisar enlaces `http://` y migrarlos a HTTPS cuando el servicio lo soporte; eliminar enlaces inseguros que no tengan alternativa.
5. Revocar o rotar tokens de Mapbox presentes en ejemplos, confirmar sus restricciones de origen y sustituirlos por marcadores de configuracion o tokens demostrativos restringidos.
6. Corregir recursos locales faltantes, incluido el marcador referenciado por ejemplos Leaflet, o retirar la referencia.
7. Etiquetar contenidos que se conservaran exclusivamente como contexto historico: Mapbox.js, ArcMap, Cartogram, CARTO Builder/CartoCSS y guias antiguas de GeoNode.
8. Actualizar metadatos del repositorio, tabla de contenidos, navegacion y enlaces de bibliografia.
9. Separar codigo generado por QGIS2Web de los ejemplos mantenidos manualmente; documentar que es una salida generada y no un patron de desarrollo moderno.
10. Definir la estructura objetivo y la convivencia entre documentacion Jekyll y aplicaciones Vite. Como referencia:
    - `docs/` para material docente mantenido.
    - `examples/leaflet/` y `examples/maplibre/` para ejemplos mantenidos.
    - `infra/` para Compose, configuracion y scripts idempotentes.
    - `data/fixtures/` para datos pequenos, versionados y con checksum.
    - `archive/` para material historico excluido del build publico.
11. Configurar controles locales y CI minimo: formato Markdown, enlaces internos, sintaxis JSON/YAML/XML, validacion HTML, escaneo de secretos y comprobacion de licencias conocidas.
12. Hacer que cada comprobacion de CI tenga un comando local equivalente. GitHub Actions sera el adaptador de referencia, no la unica forma de validacion.
13. Decidir por ruta si cada PDF se rehace en Markdown/HTML accesible, se sustituye, se conserva con fuente editable o se archiva fuera del build.

**Entregables**

- Indice de curso navegable y sin enlaces internos rotos.
- Politica documentada de tokens, secretos y configuracion local.
- Directorio o seccion de material historico claramente rotulado.
- Estructura de repositorio aprobada y estrategia Jekyll/Vite documentada.
- CI minimo y comandos locales equivalentes.
- Matriz ruta actual -> accion -> ruta destino, incluidos PDF, ZIP, notebooks, imagenes, QGIS2Web, Jekyll y archivos vendorizados.

**Criterios de aceptacion**

- Los enlaces internos, imagenes locales y ejemplos basicos se resuelven desde un servidor web local.
- No hay credenciales funcionales ni tokens sin restringir en archivos versionados.
- Ninguna actividad obligatoria contiene fechas o infraestructura de la cohorte de 2020.
- Un cambio con Markdown, HTML o JSON invalido falla localmente y en CI.
- El material historico no se incluye en el sitio publico salvo que cumpla las politicas de seguridad, licencia y privacidad.

### Fase 2. Redisenar el programa y la evaluacion

**Objetivo:** convertir el temario en una secuencia actual, acumulativa y evaluable por resultados observables.

**Actividades**

1. Reescribir objetivos generales y competencias de `Programa.md` para incluir reproducibilidad, accesibilidad, seguridad, rendimiento, etica y operacion.
2. Reorganizar el curso en las ocho unidades definidas en la seccion 6 de este documento.
3. Reemplazar la dependencia de productos concretos por capacidades: publicar, consultar, estilizar, optimizar, desplegar y operar.
4. Actualizar las tres tareas integradoras con requisitos funcionales, tecnicos y de documentacion independientes del proveedor.
5. Crear rubricas con criterios publicos para cartografia, datos, accesibilidad, interoperabilidad, rendimiento, seguridad, reproducibilidad y comunicacion.
6. Aplicar la distribucion de 32 horas presenciales y 40 autonomas; rotular cada contenido como obligatorio, electivo o historico.
7. Establecer uno o dos datasets de referencia pequenos, con licencia clara, manifiesto y variantes opcionales de mayor escala.
8. Incluir actividades de diagnostico inicial y ejercicios cortos verificables para cada unidad.
9. Definir una politica de uso responsable de IA generativa: declaracion de uso, trazabilidad de fuentes, verificacion tecnica y prohibicion de exponer datos sensibles.
10. Actualizar los prerrequisitos tecnicos: RAM, CPU, espacio, virtualizacion, sistemas operativos, navegadores, WebGL, puertos y conocimientos previos. Publicar un equipo de referencia inicial de al menos 4 nucleos de CPU, 16 GB de RAM, SSD con 20 GB libres y virtualizacion habilitada, sujeto a validacion en el piloto.

**Entregables**

- `Programa.md` actualizado.
- Rubricas de evaluacion y plantillas de entrega.
- Catalogo de datasets de referencia y fichas de metadatos.
- Guia para docencia, soporte y recuperacion ante fallos de servicios externos.
- Tabla de horas, contenidos obligatorios/electivos y prerrequisitos por unidad.

**Criterios de aceptacion**

- Cada competencia tiene al menos una actividad y un criterio de evaluacion asociado.
- Las tareas se pueden completar con software abierto y servicios locales.
- La evaluacion mide calidad y justificacion tecnica, no solo la presencia de capturas o URLs.
- La suma de actividades presenciales no excede 32 horas y el piloto mide separadamente el trabajo autonomo.

### Fase 3. Modernizar las unidades 1 a 3: fundamentos, datos y cartografia

**Objetivo:** actualizar la base del curso sin aumentar innecesariamente la barrera de entrada.

**Actividades**

1. Actualizar la Unidad 1 para incluir Git actual, hosting estatico con GitHub Pages como referencia opcional, HTML semantico, CSS responsive, JavaScript moderno, modulos ES, `fetch`, `async/await` y gestion de errores.
2. Reemplazar ejemplos Leaflet 1.6 y jQuery por una version vigente de Leaflet y APIs nativas del navegador.
3. Actualizar la Unidad 2 con GeoPackage, GeoJSON, validacion de geometria, CRS, precision, orden de coordenadas, calidad y procedencia de datos.
4. Convertir QGIS2Web en una actividad de prototipado o comparacion; no presentarlo como sustituto de una aplicacion mantenible.
5. Adoptar WCAG 2.2 nivel AA como objetivo para sitio, ejemplos y entregas. Solo se admitira una declaracion de conformidad parcial para contenido de terceros fuera de control, documentando el criterio afectado y una alternativa accesible.
6. Actualizar la Unidad 3 con contraste, paletas no dependientes solo del color, diseno para movil, foco visible, controles operables por teclado, alternativas a gestos de arrastre, mensajes de estado y manejo de incertidumbre.
7. Exigir una tabla, resumen o descarga accesible equivalente para los hallazgos principales del mapa, ademas de texto alternativo para contenido no textual.
8. Incluir subtitulos o transcripcion en videos y una estrategia para sustituir o archivar PDF no accesibles.
9. Incorporar atribucion obligatoria, licencias de datos y privacidad geoespacial en las practicas.
10. Crear un pipeline reproducible inicial con GDAL/OGR; el componente SQL se incorporara despues de introducir PostGIS en la Fase 5.

**Entregables**

- Ejemplos HTML modernos y autocontenidos.
- Guia WCAG 2.2 AA y lista de comprobacion cartografica, con pruebas automaticas y manuales.
- Ejercicio de preparacion de datos con script y metadatos.

**Criterios de aceptacion**

- Un estudiante puede crear un mapa responsive sin usar jQuery ni tokens incrustados.
- El mapa satisface todos los criterios WCAG 2.2 AA aplicables incluidos en la lista de comprobacion. El analisis automatico no presenta incidencias serias o criticas y la revision manual confirma teclado, foco, zoom/reflow, controles etiquetados y alternativa de datos.
- Los datos de practica pueden regenerarse desde sus fuentes y scripts documentados.

### Fase 4. Modernizar interoperabilidad y servicios geoespaciales

**Objetivo:** mantener el conocimiento de OGC clasico y ensenar el modelo API actual.

**Actividades**

1. Mantener WMS, WFS, WMTS, WCS, CSW y WPS como OGC Web Services clasicos y de compatibilidad institucional; no calificarlos genericamente como obsoletos.
2. Mantener SLD como estandar de estilos, separado de los servicios OGC.
3. Ensenar OGC API Common y OGC API - Features como nucleo obligatorio.
4. Introducir HTTP, REST, OpenAPI, recursos, colecciones, enlaces de descubrimiento, declaraciones de conformidad, paginacion, CQL2 basico, filtros espaciales/temporales, formatos y codigos HTTP.
5. Comparar WFS con OGC API - Features en una practica obligatoria.
6. Presentar OGC API - Tiles o Maps mediante una demostracion; dejar Records, Processes y EDR como panorama/electivos y Coverages como especificacion candidata.
7. Conservar WPS para la comparacion conceptual con OGC API - Processes.
8. Incluir STAC Catalog, Collection e Item mediante un fixture estatico local. STAC API y busqueda espacial-temporal contra servicios remotos seran electivas o informativas hasta incorporar un servidor local fijado.
9. Actualizar los notebooks de OWSLib y Python; eliminar salidas antiguas, fijar kernel/dependencias y ejecutar las celdas obligatorias desde un entorno limpio.
10. Proporcionar fixtures o respuestas grabadas para pruebas deterministas sin red y separar las celdas que dependen de endpoints externos.
11. Agregar validacion de disponibilidad, CORS, conformidad y respuesta de endpoints en los ejercicios.

**Entregables**

- Notebooks renovados y ejecutables de OGC API, WMS/WFS y STAC.
- Archivo de dependencias Python reproducible.
- Guia de migracion conceptual entre servicios OGC clasicos y OGC API.
- Fixture STAC local pequeno y validado.

**Criterios de aceptacion**

- Los notebooks se ejecutan de principio a fin en un entorno limpio.
- Cada API usada tiene documentados endpoint, parametros, respuesta esperada, licencia y estrategia ante indisponibilidad.
- El estudiante puede explicar cuando usar una interfaz clasica y cuando una OGC API.
- Las pruebas obligatorias no fallan por indisponibilidad de un endpoint de terceros.

### Fase 5. Infraestructura local reproducible

**Objetivo:** reemplazar la infraestructura manual y efimera por un entorno que cualquier estudiante pueda levantar localmente.

**Actividades**

1. Sustituir la guia de Java 8, Tomcat 9 y WAR de GeoServer por Docker Compose.
2. Crear servicios fijados para PostGIS, GeoServer 3.x y un servidor estatico con HTTP Range. Instalar explicitamente los modulos OGC API - Features y Vector Tiles compatibles con la version de GeoServer.
3. Documentar instalacion previa, arranque, parada, reinicializacion, carga de datos, copias de seguridad y solucion de problemas.
4. Crear roles de Postgres con privilegios minimos y credenciales de desarrollo no reutilizables fuera del entorno local. Usar secretos por archivo en vez de exponer contrasenas directamente en variables de entorno cuando la imagen lo permita.
5. Incluir scripts SQL para esquema, indices GiST, carga, analisis y limpieza de datos de ejemplo.
6. Versionar un data directory minimo saneado o scripts idempotentes contra la REST API para reconstruir workspaces, stores, capas, estilos y grupos desde un clon limpio.
7. Documentar publicacion en GeoServer, SLD, teselas vectoriales y cache. CSS/YSLD/MBStyle se mantendran como comparacion si sus extensiones se instalan y validan.
8. Configurar CORS de forma explicita para desarrollo y documentar la configuracion segura para despliegue.
9. Enlazar interfaces administrativas solo a localhost en desarrollo, ejecutar contenedores sin privilegios cuando sea compatible y omitir datos demo innecesarios.
10. Agregar healthchecks y smoke tests para base de datos, WMS/WFS y OGC API - Features.
11. Evaluar GeoNode moderno como opcion de catalogo/IDE, separado del stack obligatorio, tras validar su instalacion y operacion.

**Entregables**

- `compose.yaml`, `.env.example`, secretos de ejemplo no sensibles y documentacion de ejecucion local.
- Scripts de inicializacion PostGIS y datos de muestra con licencia conocida.
- Guia de GeoServer actualizada para Java LTS y version soportada.
- Configuracion idempotente de GeoServer y smoke tests.

**Criterios de aceptacion**

- Una persona con los prerrequisitos documentados puede levantar el stack con un comando y completar la preparacion inicial en menos de 60 minutos en el equipo de referencia publicado, sin contar la descarga inicial de imagenes.
- La carga de datos, publicacion de una capa y consulta desde un cliente se completan sin una IP de clase.
- La infraestructura no expone credenciales por defecto en una configuracion de despliegue.
- Destruir volumenes y reconstruir el stack reproduce workspaces, capas, estilos y endpoints sin pasos manuales no documentados.
- Los healthchecks y consultas de humo pasan desde una instalacion limpia.

### Fase 6. Cliente web moderno

**Objetivo:** disponer del cliente mantenible que se usara para aprender optimizacion y completar el proyecto integrador.

**Actividades**

1. Crear una plantilla de aplicacion con Vite, TypeScript, ESLint, formatter y scripts de desarrollo, prueba, accesibilidad y compilacion.
2. Adoptar MapLibre GL JS como cliente principal para vector tiles, estilos y WebGL.
3. Mantener Leaflet para la introduccion. OpenLayers y capacidades 3D quedaran como electivos.
4. Documentar una arquitectura minima de aplicacion: fuentes, capas, controles, estado, URL compartible, errores, carga y atribuciones. Incluir los protocolos fijados `pmtiles` y `@geomatico/maplibre-cog-protocol` para las rutas cloud-native.
5. Implementar filtros, popup accesible, control de capas, consulta de atributos, deep linking y estados de carga/error.
6. Incluir pruebas unitarias para transformaciones y pruebas end-to-end para carga, filtro, consulta y error de red.
7. Crear una ruta electiva para React, Vue o Svelte; no hacerla prerrequisito del proyecto base.
8. Actualizar o archivar el ejemplo antiguo de Kepler.gl y eliminar dependencias heredadas de React 16, Redux 3 y Mapbox GL 1 del material publicado.

**Entregables**

- Plantilla TypeScript/Vite para actividades.
- Ejemplo MapLibre que consuma GeoJSON y OGC API - Features antes de introducir formatos optimizados.
- Guia de pruebas, errores y accesibilidad de aplicaciones.

**Criterios de aceptacion**

- El frontend compila reproduciblemente con la version LTS de Node.js fijada para la cohorte.
- El visor funciona en las dos ultimas versiones estables de Chromium, Firefox y Safari, con excepciones documentadas para WebGL.
- Las pruebas end-to-end cubren carga correcta, filtro, consulta y fallo de red.
- La lista de criterios WCAG 2.2 AA aplicables queda completamente satisfecha; una herramienta automatica se usa solo como apoyo y no como declaracion de conformidad.

### Fase 7. Datos cloud-native, rendimiento e integracion

**Objetivo:** optimizar la entrega del mismo proyecto y ensenar las diferencias entre formato, codificacion, empaquetado, catalogo y servicio.

**Actividades**

1. Organizar el contenido por funcion:
   - Intercambio y edicion: GeoJSON y GeoPackage.
   - Almacenamiento y consulta: PostGIS.
   - Codificacion de entrega vectorial: MVT.
   - Empaquetado y distribucion: PMTiles.
   - Entrega raster: COG.
   - Catalogo y descubrimiento: STAC.
   - API o servicio: WMS/WFS/WMTS y OGC API.
2. Consumir en MapLibre los artefactos de referencia PMTiles y COG mediante los protocolos fijados, y probar la cadena completa desde HTTP Range hasta visualizacion.
3. Elegir una ruta de proyecto: generar MVT/PMTiles con generalizacion y estilo, o generar un COG con overviews y validacion estructural.
4. Servir los artefactos desde el servidor estatico local y comprobar `Accept-Ranges`, respuestas `206 Partial Content` y CORS.
5. Crear y validar un catalogo STAC estatico para los activos del ejercicio. La busqueda contra una STAC API publica sera una comparacion no bloqueante.
6. Explicar cache, almacenamiento de objetos, CDN, TileJSON, limites de zoom, simplificacion y carga diferida.
7. Ejecutar un benchmark reproducible segun la ruta seleccionada. La ruta vectorial comparara el mismo dataset como GeoJSON, MVT servido y MVT en PMTiles; la ruta raster comparara GeoTIFF convencional, COG y WMS sin tratarlos como equivalentes vectoriales.
8. Incluir Zarr, GeoParquet, COPC, 3D Tiles, Cesium o terreno 3D como electivos.

**Entregables**

- Ejemplos de MVT/PMTiles, COG y STAC estatico.
- Guia de decision por funcion, tamano, edicion, latencia, coste y conectividad.
- Protocolo e informe de benchmark reproducible.

**Criterios de aceptacion**

- El benchmark fija dataset, checksum, numero de entidades, equipo, navegador, perfil de red, cache fria/caliente, repeticiones y metricas.
- Se reportan como minimo bytes transferidos, numero de solicitudes, tiempo hasta mapa utilizable y memoria aproximada; cada medicion usa al menos cinco repeticiones y su mediana.
- La entrega optimizada reduce al menos 30% los bytes iniciales frente a la linea base de su ruta. Una excepcion requiere evidencia reproducible, explicacion tecnica y aprobacion del responsable de la rubrica antes de aceptar la entrega.
- Una prueba automatizada confirma HTTP Range para PMTiles y COG.
- Una prueba end-to-end confirma que MapLibre visualiza PMTiles con el paquete `pmtiles` y COG con `@geomatico/maplibre-cog-protocol`.
- El estudiante distingue correctamente MVT de PMTiles, COG de formatos vectoriales y STAC de un servicio de mapas.

### Fase 8. Seguridad, automatizacion y despliegue

**Objetivo:** completar los controles introducidos en la Fase 1 y producir artefactos publicables sin exigir un backend individual en Internet.

**Actividades**

1. Actualizar `package.json`, regenerar el lockfile y eliminar Husky 3, lint-staged 9 y Prettier 1; adoptar herramientas vigentes y scripts que no modifiquen ni indexen cambios inesperadamente.
2. Ampliar los scripts locales y GitHub Actions para ejecutar validacion de Markdown, enlaces, datos, estilos, notebooks, lint, pruebas, accesibilidad y build.
3. Crear comprobaciones que no dependan de un servicio externo para aprobar cambios; las pruebas de endpoints remotos deben poder marcarse como informativas o ejecutarse programadamente.
4. Ejecutar checks de pull request sin secretos y con permisos de solo lectura. Fijar acciones de terceros por SHA, evitar `pull_request_target` con checkout de codigo no confiable y no usar runners institucionales compartidos para pull requests publicos.
5. Definir gestion de secretos mediante archivos locales ignorados, secretos del proveedor de CI y, para despliegue, credenciales efimeras/OIDC cuando exista soporte. No usar secretos en frontend; las claves publicas deben estar restringidas por origen y alcance.
6. Documentar HTTPS, CORS, CSP, cabeceras de seguridad, limites de peticiones, autenticacion y autorizacion por capa/rol.
7. Generar siempre un `dist/` verificable. La publicacion estatica en Pages u otro hosting sera opcional; los servicios con estado permaneceran locales salvo que exista un entorno institucional aprobado.
8. Separar validacion y despliegue. Los previews solo se crearan desde ramas o entornos aprobados y sin acceso a secretos de produccion.
9. Incorporar observabilidad minima al stack: healthchecks, logs, estado y registro de errores. Metricas, alertas y monitoreo continuo seran electivos si no existe backend institucional.
10. Crear un runbook con propietario, alcance de backup, elementos regenerables, retencion y objetivos didacticos iniciales de RPO de 24 horas y RTO de 4 horas para un entorno institucional. Para el entorno local se exigira reconstruccion desde cero y restauracion de datos/configuracion.
11. Documentar costes y limites del hosting elegido sin convertirlo en requisito de una cuenta personal.

**Entregables**

- Workflows de GitHub Actions.
- Politica de seguridad y guia de despliegue.
- Lista de comprobacion para revision de proyectos estudiantiles.
- Artefacto `dist/`, runbook y evidencia de reconstruccion/restauracion.

**Criterios de aceptacion**

- Un pull request muestra el resultado de validacion, pruebas y compilacion antes de integrarse.
- No se publican secretos ni se requieren tokens personales para ejecutar ejemplos basicos.
- Los workflows de pull request tienen permisos de solo lectura, no reciben secretos y no ejecutan codigo no confiable en runners privilegiados.
- El procedimiento de publicacion estatica, reconstruccion local y restauracion esta documentado y se prueba en cada version candidata del curso.
- El build estatico puede publicarse en cualquier hosting compatible; GitHub Pages no es un requisito de aprobacion.

### Fase 9. Proyecto piloto, revision y publicacion

**Objetivo:** validar que el curso se puede impartir de principio a fin antes de adoptarlo para una cohorte completa.

**Actividades**

1. Seleccionar un grupo piloto de estudiantes con distintos niveles de experiencia.
2. Ejecutar todas las practicas con equipos limpios y sistemas operativos representativos.
3. Recopilar por unidad horas presenciales, trabajo autonomo, errores, dependencia de soporte y coste de infraestructura.
4. Revisar accesibilidad con herramientas automaticas y pruebas manuales de teclado y movil.
5. Revisar cada tarea con la rubrica propuesta y calibrar carga de trabajo, dificultad y ponderacion.
6. Corregir instrucciones ambiguas, datasets fragiles y pasos no reproducibles.
7. Etiquetar una version del curso para la cohorte y publicar notas de version.

**Entregables**

- Informe de piloto con incidencias, decisiones y mejoras.
- Version etiquetada del curso y guia de actualizacion por cohorte.
- Backlog priorizado para la siguiente iteracion.

**Criterios de aceptacion**

- Al menos 80% de participantes completa el nucleo obligatorio y 70% completa el proyecto integrador sin acceso a infraestructura historica.
- La mediana de trabajo presencial no supera 32 horas y la mediana de trabajo autonomo no supera 40 horas; cualquier exceso obliga a recortar alcance antes de publicar.
- Todas las actividades obligatorias tienen instrucciones, datos y resultados esperados verificables.
- Las incidencias bloqueantes se resuelven antes de la publicacion de la cohorte.

## 6. Temario objetivo

| Unidad | Contenidos | Producto de aprendizaje |
| --- | --- | --- |
| 1. Web, Git y publicacion | Git, hosting estatico, HTML semantico, CSS responsive, JavaScript moderno, atribucion | Build local y mapa basico Leaflet |
| 2. Datos y calidad | QGIS, GeoPackage, GeoJSON, CRS, validacion, metadatos, licencias, privacidad | Pipeline reproducible de datos |
| 3. Cartografia accesible y UX | Clasificacion, simbolizacion, incertidumbre, WCAG 2.2 AA, movil y narrativa | Mapa tematico con alternativa de datos |
| 4. APIs e interoperabilidad | HTTP, OGC clasico, OGC API Common/Features, OpenAPI y STAC estatico | Comparacion reproducible WFS/Features |
| 5. Servicios e infraestructura | PostGIS, GeoServer, SQL, estilos, Docker Compose, secretos y restauracion | Stack local reconstruible |
| 6. Cliente web moderno | TypeScript, Vite, MapLibre, estado, errores y pruebas | Aplicacion interactiva mantenible |
| 7. Rendimiento y cloud-native | MVT, PMTiles, COG, HTTP Range, STAC, cache y benchmark | Entrega optimizada y comparativa reproducible |
| 8. Operacion y publicacion | CI/CD, seguridad, build estatico, runbook, coste y etica | Artefacto desplegable y backend local reproducible |

## 7. Entregas evaluables propuestas

### Entrega 1. Mapa publicable y accesible

- Problema territorial y uno o dos datasets de referencia documentados; integrar tres fuentes sera un criterio avanzado, no un requisito base.
- Procesamiento reproducible, metadatos, atribucion y licencia.
- Mapa responsive conforme al alcance WCAG 2.2 AA, accesible por teclado y con tabla, resumen o descarga equivalente para los hallazgos principales.
- Justificacion de clasificacion, colores, escala, incertidumbre y limites de interpretacion.

### Entrega 2. Servicio interoperable reproducible

- PostGIS y GeoServer ejecutados mediante Docker Compose.
- OGC API - Features y WFS sobre la misma coleccion para comparar ambos modelos.
- SQL versionado, indices espaciales, roles de lectura y datos de ejemplo.
- Estilo SLD documentado, capas agrupadas, cliente web, healthchecks y pruebas de disponibilidad.
- Reconstruccion del stack desde un clon limpio mediante scripts o configuracion versionada.

### Entrega 3. Aplicacion geoespacial desplegable

- Tema abierto, renovable por cohorte: clima, riesgo, movilidad, biodiversidad, energia, desigualdad o servicios urbanos.
- Cliente TypeScript con filtros, interaccion, narrativa y manejo de errores.
- Uso de OGC API - Features y una ruta de entrega optimizada: MVT/PMTiles para vector o COG para raster.
- Catalogo STAC estatico cuando existan activos espaciotemporales; STAC API sera electiva.
- Scripts locales y CI, documentacion de arquitectura, pruebas, analisis WCAG 2.2 AA y evaluacion de privacidad/etica.
- `dist/` desplegable en hosting estatico y backend reproducible local. El despliegue full-stack individual sera electivo o usara infraestructura institucional aprobada.

## 8. Matriz de migracion de contenidos existentes

| Contenido actual | Accion | Destino |
| --- | --- | --- |
| GitHub Pages, Markdown y Git | Conservar Pages como referencia opcional; actualizar interfaz/instrucciones | Unidad 1 |
| HTML, CSS, JavaScript basico | Reescribir con estandares actuales | Unidad 1 |
| Leaflet 1.6 y jQuery 3.1 | Actualizar; sustituir jQuery por APIs nativas | Unidad 1 |
| QGIS, GeoJSON, TopoJSON y GeoPackage | Conservar; hacer visible GeoPackage en Markdown y ejercitar calidad/CRS | Unidad 2 |
| QGIS2Web | Mantener como prototipo/actividad optativa | Unidad 2, anexo |
| Cartografia tematica | Conservar y ampliar accesibilidad/UX/incertidumbre | Unidad 3 |
| WMS, WFS, WMTS, WCS, CSW y WPS | Conservar como OGC Web Services clasicos; comparar WPS/Processes | Unidad 4 |
| OWSLib y notebooks antiguos | Actualizar, fijar dependencias y volver a ejecutar | Unidad 4 |
| PostGIS y GeoServer | Conservar y contenerizar | Unidad 5 |
| GeoServer 2.15, Java 8, Tomcat 9 | Retirar de la guia principal | Anexo historico |
| SLD, CSS, YSLD y MBStyle | Mantener SLD como base; dejar alternativas sujetas a extensiones validadas | Unidad 5 |
| Vector tiles | Ampliar con MVT, PMTiles, HTTP Range, cache y benchmarks | Unidad 7 |
| Kepler.gl y deck.gl | Mantener como exploracion avanzada | Unidad 7, optativo |
| Mapbox.js y Cartogram | Retirar de actividades obligatorias | Anexo historico |
| Mapbox, CARTO, ArcGIS Online, Flourish | Mantener como comparativa/proveedor opcional | Unidades 3 y 7 |
| GeoNode antiguo | Reevaluar una version vigente o volverlo optativo | Unidad 5, optativo |
| COVID-19 como tema obligatorio | Sustituir por retos renovables | Entrega 3 |
| Datos sociales geolocalizados | Poner en cuarentena; verificar licencia y privacidad; sustituir por datos sinteticos/agregados | Fase 0 |
| PDF docentes | Rehacer en formato accesible, sustituir o archivar fuera del build | Por unidad |
| Jekyll y `_config.yml` | Conservar para documentacion o migrar mediante decision explicita; separar de Vite | Infraestructura editorial |
| ZIP, binarios y datasets grandes | Inventariar, asignar licencia/checksum y decidir Git, LFS, release u objeto externo | `data/` o almacenamiento externo |
| Fuentes y JavaScript vendorizados | Inventariar licencia y excluir del build si solo son historicos | `archive/` |
| `00_Intro` | Actualizar prerrequisitos tecnicos, recursos minimos y diagnostico inicial | Introduccion y Unidad 1 |
| `Herramientas.md` | Clasificar cada herramienta como obligatoria, electiva, historica o eliminada | Indice de herramientas actualizado |
| `Geoserver.md` | Sustituir la guia principal por Compose; conservar la instalacion antigua solo fuera del build | Unidad 5 y `archive/` |
| `package.json` y `package-lock.json` | Definir tooling raiz, actualizar dependencias y regenerar lockfile | Infraestructura editorial/CI |
| Imagenes y capturas | Verificar licencia, utilidad y texto alternativo; reemplazar capturas obsoletas | Por unidad |

## 9. Validacion y control de calidad

### Validaciones automaticas

- Formato de Markdown y enlaces internos.
- Enlaces externos, ejecutados de manera programada o informativa para evitar bloquear contribuciones por fallos de terceros.
- HTML y CSS del sitio y los ejemplos.
- Sintaxis y semantica de JSON/GeoJSON, geometria valida, coordenadas dentro de rango y CRS esperado.
- YAML, XML y SLD mediante esquemas o herramientas especificas cuando corresponda.
- OpenAPI, declaraciones de conformidad y respuestas basicas de OGC API.
- STAC mediante un validador compatible con la version fijada.
- COG, PMTiles, MVT, MapLibre Style y HTTP Range mediante herramientas y smoke tests especificos.
- `compose.yaml`, healthchecks y una consulta de integracion contra PostGIS/GeoServer.
- Lint, pruebas y build del frontend TypeScript.
- Ejecucion completa de notebooks obligatorios desde un entorno fijado; las celdas remotas informativas se separan.
- Accesibilidad automatica, complementada siempre con revision manual.
- Analisis de secretos, licencias y dependencias vulnerables. No se aceptaran secretos detectados ni vulnerabilidades criticas conocidas en dependencias directas sin excepcion documentada.

### Validaciones manuales

- Revision cartografica por pares: simbologia, clasificacion, leyenda, escala, atribucion y limites interpretativos.
- Prueba movil, zoom/reflow, navegacion solo con teclado y lector de pantalla durante el piloto.
- Revision WCAG 2.2 AA de contraste, foco, controles, mensajes, texto alternativo, subtitulos y alternativa de datos; el contenido no dependera unicamente del color o de gestos de arrastre.
- Prueba de instalacion desde cero de Docker Compose, frontend y notebooks.
- Revision de licencias, privacidad y datos sensibles.
- Prueba de restauracion de PostGIS y configuracion de GeoServer desde una version candidata.

## 10. Riesgos y mitigaciones

| Riesgo | Mitigacion |
| --- | --- |
| Cambios de precio, interfaz o disponibilidad de SaaS | Mantener ruta obligatoria con herramientas abiertas y ejemplos locales |
| Equipos estudiantiles con recursos limitados | Publicar requisitos minimos, usar datasets pequenos, perfiles ligeros, alternativas estaticas y servicios compartidos opcionales |
| Alta complejidad de Docker/GeoServer | Guia paso a paso, imagenes fijadas, diagnostico de errores y practica previa controlada |
| Dependencias externas fragiles | Fixtures locales, datos de ejemplo versionados y pruebas externas no bloqueantes |
| Exposicion de datos sensibles | Cuarentena inicial, datos sinteticos/agregados, manifiesto de sensibilidad y revision previa de publicacion |
| Licencias incompatibles o inciertas | Matriz por artefacto, separacion de licencias y exclusion del build hasta resolverlas |
| Sobrecarga curricular | Nucleo obligatorio de 32+40 horas, modulos avanzados electivos y umbrales del piloto |
| Obsolescencia futura | Revision de versiones, enlaces y proveedores antes de cada cohorte |
| Configuracion irreproducible de GeoServer | Data directory saneado o scripts REST idempotentes probados desde volumenes vacios |
| CI sobre codigo estudiantil no confiable | Permisos minimos, sin secretos en PR, acciones fijadas y sin runners privilegiados compartidos |

## 11. Orden de implementacion recomendado

1. Ejecutar la Fase 0 antes de publicar o reutilizar datasets: inventario, cuarentena, licencias, privacidad y secretos.
2. Completar la Fase 1 para disponer de estructura, saneamiento y CI minimo antes de reescribir ejemplos.
3. Completar la Fase 2 para fijar horas, resultados, prerrequisitos y rubricas antes de escribir nuevo contenido.
4. Implementar las Fases 3 y 4: fundamentos, accesibilidad e interoperabilidad.
5. Implementar la Fase 5 y probar el stack reconstruible antes de convertirlo en requisito estudiantil.
6. Implementar las Fases 6 y 7, en ese orden, antes de pasar al endurecimiento y publicacion.
7. Completar la Fase 8 para endurecimiento, artefactos publicables y recuperacion.
8. Ejecutar la Fase 9 con una cohorte piloto y publicar una version etiquetada solo despues de resolver incidencias bloqueantes y cumplir los umbrales de tiempo/finalizacion.

## 12. Definition of done

La modernizacion se considerara completada cuando se cumplan simultaneamente estas condiciones:

- El indice, programa, unidades y tareas reflejan el temario objetivo y no contienen dependencias obligatorias de 2020.
- Todos los ejemplos obligatorios funcionan desde un clon limpio del repositorio, con prerrequisitos documentados.
- PostGIS, GeoServer y el servidor estatico se reconstruyen localmente mediante Docker Compose, configuracion versionada y smoke tests, sin infraestructura de una cohorte previa.
- El curso ensena y practica OGC API Common/Features, STAC estatico, MVT/PMTiles o COG, ademas de los servicios OGC clasicos. Las especificaciones candidatas y los electivos estan rotulados.
- El cliente principal usa TypeScript y una biblioteca actual; Leaflet queda como introduccion actualizada y sin jQuery.
- Los flujos de entrega incluyen WCAG 2.2 AA, seguridad, pruebas, automatizacion local/CI, documentacion y reproducibilidad.
- No hay secretos, tokens activos sin restringir, credenciales por defecto ni endpoints HTTP inseguros, salvo `localhost` de desarrollo, en los ejemplos publicados.
- Todos los artefactos redistribuidos tienen licencia y sensibilidad documentadas; los datos sociales originales no se publican sin autorizacion y minimizacion verificadas.
- El frontend genera un artefacto estatico independiente del proveedor y el backend obligatorio es reproducible localmente; el despliegue full-stack es institucional o electivo.
- El piloto cumple 80% de finalizacion del nucleo, 70% del proyecto y los limites de 32 horas presenciales y 40 autonomas.
- Existe una guia para actualizar versiones, enlaces, datasets y proveedores antes de cada nueva cohorte.
