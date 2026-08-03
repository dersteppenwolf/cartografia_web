# Plan de modernizacion del curso de cartografia web

**Fecha de referencia:** 2026-08-03  
**Estado:** Propuesto  
**Alcance:** Modernizacion curricular, tecnica, editorial y operativa del repositorio `cartografia_web`.

## 1. Objetivo

Actualizar el curso, originalmente estructurado en 2020, para que ensene publicacion de cartografia web con practicas reproducibles, interoperables, seguras y actuales. La actualizacion debe conservar los fundamentos valiosos de SIG, cartografia, PostGIS, GeoServer y servicios OGC clasicos, a la vez que incorpora APIs geoespaciales modernas, datos cloud-native, clientes web actuales, automatizacion y operacion.

El resultado sera un curso que permita a cada estudiante construir, documentar, probar y desplegar una aplicacion geoespacial web sin depender de infraestructura temporal, cuentas personales del docente ni productos SaaS especificos.

## 2. Principios de ejecucion

1. Conservar los conceptos antes que los productos: cartografia, interoperabilidad, SQL espacial y arquitectura no dependen de una plataforma SaaS.
2. Mantener compatibilidad didactica con servicios OGC clasicos, pero ensenar OGC API como interfaz principal para implementaciones nuevas.
3. Preferir herramientas abiertas, formatos abiertos y entornos reproducibles para las practicas obligatorias.
4. Separar herramientas obligatorias de alternativas comerciales u optativas.
5. No incluir credenciales, tokens activos, IPs de infraestructura docente ni dependencias HTTP inseguras en ejemplos publicados.
6. Validar cada modulo de extremo a extremo en una instalacion limpia antes de declararlo listo.
7. Actualizar las referencias de versiones en cada inicio de cohorte; no fijar versiones antiguas en el material narrativo si no son necesarias.

## 3. Alcance y resultado esperado

### Incluido

- Actualizacion de las unidades, ejercicios, tareas y criterios de evaluacion.
- Reemplazo o modernizacion de ejemplos HTML, JavaScript, notebooks y guias de infraestructura.
- Creacion de un stack local reproducible con Docker Compose.
- Adicion de OGC API, STAC, vector tiles, PMTiles, COG y fundamentos de datos cloud-native.
- Introduccion de TypeScript, Vite, MapLibre GL JS y JavaScript moderno.
- Automatizacion de validaciones mediante GitHub Actions.
- Seguridad basica, accesibilidad, rendimiento, documentacion y operacion como criterios de entrega.
- Inventario y saneamiento de enlaces, recursos externos, tokens y contenidos historicos.

### Excluido de la primera iteracion

- Migrar o reescribir cada exportacion generada por QGIS2Web.
- Construir una plataforma institucional completa de aprendizaje o una infraestructura productiva de alta disponibilidad.
- Obligar el uso de un framework frontend especifico.
- Eliminar WMS, WFS, WMTS, SLD o GeoServer: permanecen como contenidos de interoperabilidad y compatibilidad.

## 4. Arquitectura didactica objetivo

El curso tendra dos rutas complementarias que confluyen en el proyecto final.

| Ruta | Objetivo | Herramientas principales |
| --- | --- | --- |
| Publicacion inicial | Publicar mapas claros, accesibles y documentados con barrera de entrada baja | QGIS LTR, GeoPackage, GeoJSON, HTML/CSS, Leaflet actualizado, GitHub Pages |
| Aplicacion profesional | Crear una aplicacion geoespacial reproducible y operable | PostGIS, GeoServer 3.x, OGC API, MVT/PMTiles, MapLibre GL JS, TypeScript, Vite, Docker Compose, GitHub Actions |

Las soluciones comerciales o SaaS, como ArcGIS Online, Mapbox, CARTO, Flourish, QGIS Cloud y Kepler.gl, se mantendran como comparativas o alternativas optativas. Ninguna tarea obligatoria debe requerir una cuenta de pago ni depender de la disponibilidad de una interfaz de terceros.

## 5. Fases de trabajo

### Fase 0. Gobierno, inventario y decisiones base

**Objetivo:** establecer el alcance definitivo y evitar que el nuevo material herede dependencias inseguras o no reproducibles.

**Actividades**

1. Designar responsables de contenido SIG/cartografico, desarrollo web, infraestructura y revision pedagogica.
2. Crear un inventario de todos los enlaces, endpoints, recursos CDN, datasets, videos, capturas, tokens y cuentas externas usados por el repositorio.
3. Clasificar cada recurso como: conservar, actualizar, reemplazar, archivar como historico o eliminar.
4. Confirmar la politica institucional para cuentas cloud, limites de coste, datos personales, licencias, accesibilidad y publicacion estudiantil.
5. Definir versiones de referencia de la primera cohorte modernizada:
   - QGIS LTR vigente.
   - PostgreSQL/PostGIS vigentes y soportados.
   - GeoServer 3.x y Java LTS compatible.
   - Node.js LTS vigente.
   - Python vigente y entorno virtual o `uv`/`pip-tools` definido.
6. Elegir un proveedor o entorno para demos institucionales, si se requiere uno; el curso debe seguir funcionando localmente sin dicho proveedor.
7. Establecer una politica para actualizar dependencias, datasets y enlaces antes de cada cohorte.

**Entregables**

- Inventario versionado de recursos externos y su estado.
- Matriz de decisiones tecnicas y de herramientas.
- Politica de secretos, licencias, atribucion y publicacion de datos.
- Calendario de actualizacion semestral/anual.

**Criterios de aceptacion**

- Ningun requisito obligatorio depende de una IP, cuenta o token personal existente.
- Se conocen el propietario, licencia y disponibilidad de cada dataset obligatorio.
- Existe una lista aprobada de versiones y una estrategia para revisarlas.

### Fase 1. Estabilizacion editorial y saneamiento del repositorio

**Objetivo:** corregir fallos evidentes y preparar el repositorio para cambios incrementales verificables.

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

**Entregables**

- Indice de curso navegable y sin enlaces internos rotos.
- Politica documentada de tokens, secretos y configuracion local.
- Directorio o seccion de material historico claramente rotulado.

**Criterios de aceptacion**

- Los enlaces internos, imagenes locales y ejemplos basicos se resuelven desde un servidor web local.
- No hay credenciales funcionales ni tokens sin restringir en archivos versionados.
- Ninguna actividad obligatoria contiene fechas o infraestructura de la cohorte de 2020.

### Fase 2. Redisenar el programa y la evaluacion

**Objetivo:** convertir el temario en una secuencia actual, acumulativa y evaluable por resultados observables.

**Actividades**

1. Reescribir objetivos generales y competencias de `Programa.md` para incluir reproducibilidad, accesibilidad, seguridad, rendimiento, etica y operacion.
2. Reorganizar el curso en las ocho unidades definidas en la seccion 6 de este documento.
3. Reemplazar la dependencia de productos concretos por capacidades: publicar, consultar, estilizar, optimizar, desplegar y operar.
4. Actualizar las tres tareas integradoras con requisitos funcionales, tecnicos y de documentacion independientes del proveedor.
5. Crear rubricas con criterios publicos para cartografia, datos, accesibilidad, interoperabilidad, rendimiento, seguridad, reproducibilidad y comunicacion.
6. Establecer datasets de referencia pequenos, con licencia clara y variantes opcionales de mayor escala.
7. Incluir actividades de diagnostico inicial y ejercicios cortos verificables para cada unidad.
8. Definir una politica de uso responsable de IA generativa: declaracion de uso, trazabilidad de fuentes, verificacion tecnica y prohibicion de exponer datos sensibles.

**Entregables**

- `Programa.md` actualizado.
- Rubricas de evaluacion y plantillas de entrega.
- Catalogo de datasets de referencia y fichas de metadatos.
- Guia para docencia, soporte y recuperacion ante fallos de servicios externos.

**Criterios de aceptacion**

- Cada competencia tiene al menos una actividad y un criterio de evaluacion asociado.
- Las tareas se pueden completar con software abierto y servicios locales.
- La evaluacion mide calidad y justificacion tecnica, no solo la presencia de capturas o URLs.

### Fase 3. Modernizar las unidades 1 a 3: fundamentos, datos y cartografia

**Objetivo:** actualizar la base del curso sin aumentar innecesariamente la barrera de entrada.

**Actividades**

1. Actualizar la Unidad 1 para incluir Git actual, GitHub Pages, HTML semantico, CSS responsive, JavaScript moderno, modulos ES, `fetch`, `async/await` y gestion de errores.
2. Reemplazar ejemplos Leaflet 1.6 y jQuery por una version vigente de Leaflet y APIs nativas del navegador.
3. Actualizar la Unidad 2 con GeoPackage, GeoJSON, validacion de geometria, CRS, precision, orden de coordenadas, calidad y procedencia de datos.
4. Convertir QGIS2Web en una actividad de prototipado o comparacion; no presentarlo como sustituto de una aplicacion mantenible.
5. Actualizar la Unidad 3 con accesibilidad WCAG, contraste, paletas no dependientes solo del color, diseno para movil, leyendas, escalas y manejo de incertidumbre.
6. Incorporar atribucion obligatoria, licencias de datos y privacidad geoespacial en las practicas.
7. Crear un pipeline reproducible de transformacion con GDAL/OGR y SQL, con entradas, salidas y validacion documentadas.

**Entregables**

- Ejemplos HTML modernos y autocontenidos.
- Guia de accesibilidad y lista de comprobacion cartografica.
- Ejercicio de preparacion de datos con script y metadatos.

**Criterios de aceptacion**

- Un estudiante puede crear un mapa responsive sin usar jQuery ni tokens incrustados.
- El mapa funciona con teclado y presenta atribucion, leyenda y alternativa textual adecuada.
- Los datos de practica pueden regenerarse desde sus fuentes y scripts documentados.

### Fase 4. Modernizar interoperabilidad y servicios geoespaciales

**Objetivo:** mantener el conocimiento de OGC clasico y ensenar el modelo API actual.

**Actividades**

1. Mantener WMS, WFS, WMTS, WCS, CSW y SLD como estandares heredados y de compatibilidad institucional.
2. Crear una nueva unidad o subseccion central para OGC API - Features, Tiles, Maps, Records, Processes, Coverages y EDR.
3. Introducir conceptos REST, OpenAPI, recursos, colecciones, enlaces de descubrimiento, paginacion, filtros espaciales y temporales, formatos y codigos HTTP.
4. Incluir STAC: Catalog, Collection, Item, STAC API, busqueda espacial-temporal y extensiones basicas de observacion de la Tierra.
5. Actualizar los notebooks de OWSLib y Python; eliminar salidas antiguas, fijar dependencias y ejecutar las celdas desde un entorno limpio.
6. Crear ejercicios que comparen WFS con OGC API - Features y WMTS con OGC API - Tiles.
7. Agregar validacion de disponibilidad, CORS y respuesta de endpoints en los ejercicios.

**Entregables**

- Notebooks renovados y ejecutables de OGC API, WMS/WFS y STAC.
- Archivo de dependencias Python reproducible.
- Guia de migracion conceptual entre servicios OGC clasicos y OGC API.

**Criterios de aceptacion**

- Los notebooks se ejecutan de principio a fin en un entorno limpio.
- Cada API usada tiene documentados endpoint, parametros, respuesta esperada, licencia y estrategia ante indisponibilidad.
- El estudiante puede explicar cuando usar una interfaz clasica y cuando una OGC API.

### Fase 5. Infraestructura local reproducible

**Objetivo:** reemplazar la infraestructura manual y efimera por un entorno que cualquier estudiante pueda levantar localmente.

**Actividades**

1. Sustituir la guia de Java 8, Tomcat 9 y WAR de GeoServer por Docker Compose.
2. Crear servicios para PostGIS y GeoServer 3.x, con volumenes persistentes, red interna, variables de entorno y datos de demostracion opcionales.
3. Documentar instalacion previa, arranque, parada, reinicializacion, carga de datos, copias de seguridad y solucion de problemas.
4. Crear roles de Postgres con privilegios minimos y credenciales de desarrollo no reutilizables fuera del entorno local.
5. Incluir scripts SQL para esquema, indices GiST, carga, analisis y limpieza de datos de ejemplo.
6. Documentar publicacion en GeoServer, estilos SLD/YSLD/MBStyle y cache de teselas.
7. Configurar CORS de forma explicita para desarrollo y documentar la configuracion segura para despliegue.
8. Evaluar GeoNode moderno como opcion de catalogo/IDE, separado del stack obligatorio, tras validar su instalacion y operacion.

**Entregables**

- `compose.yaml`, `.env.example` y documentacion de ejecucion local.
- Scripts de inicializacion PostGIS y datos de muestra con licencia conocida.
- Guia de GeoServer actualizada para Java LTS y version soportada.

**Criterios de aceptacion**

- Una persona con los prerrequisitos documentados puede levantar PostGIS y GeoServer con un comando.
- La carga de datos, publicacion de una capa y consulta desde un cliente se completan sin una IP de clase.
- La infraestructura no expone credenciales por defecto en una configuracion de despliegue.

### Fase 6. Datos cloud-native, teselas y rendimiento

**Objetivo:** preparar a los estudiantes para publicar datos mas alla de GeoJSON completo y servicios rasterizados tradicionales.

**Actividades**

1. Incorporar MVT y teselas vectoriales: generacion, generalizacion por zoom, estilos y consultas de entidades.
2. Incorporar PMTiles como opcion de distribucion estatica de gran escala.
3. Incorporar COG para raster y una introduccion a Zarr para cubos o datos multidimensionales.
4. Crear un ejercicio STAC que encuentre y consuma activos por extension espacial, fecha y propiedades.
5. Medir y comparar peso, tiempo de carga, solicitudes y experiencia de usuario entre GeoJSON, WMS, MVT y PMTiles.
6. Explicar cache, CDN, TileJSON, limites de zoom, estrategias de simplificacion y carga diferida.
7. Incluir nubes de puntos/COPC, 3D Tiles, Cesium o terreno 3D como tema electivo avanzado, no como requisito basico.

**Entregables**

- Ejemplos de MVT/PMTiles, COG y STAC.
- Guia de decisiones de formato segun tamano, edicion, latencia, coste y acceso offline.
- Informe de benchmark reproducible con datos de referencia.

**Criterios de aceptacion**

- Al menos un ejemplo demuestra una mejora medible frente a cargar un GeoJSON grande completo.
- El estudiante puede justificar la eleccion entre GeoJSON, GeoPackage, MVT, PMTiles y COG.

### Fase 7. Cliente web moderno y aplicaciones geoespaciales

**Objetivo:** crear ejemplos mantenibles de aplicaciones, no solo paginas HTML aisladas.

**Actividades**

1. Crear una plantilla de aplicacion con Vite, TypeScript, ESLint, formatter y scripts de desarrollo, prueba y compilacion.
2. Adoptar MapLibre GL JS como cliente principal para vector tiles, estilos, WebGL y capacidades 3D basicas.
3. Mantener Leaflet para introduccion y OpenLayers para interoperabilidad OGC avanzada.
4. Documentar una arquitectura minima de aplicacion: fuentes, capas, controles, estado, URL compartible, errores y carga.
5. Implementar ejemplos con filtros espaciales/temporales, popup accesible, busqueda, control de capas, consulta de atributos y deep linking.
6. Incluir pruebas unitarias para utilidades de datos y pruebas end-to-end para los flujos principales.
7. Crear una ruta electiva para React, Vue o Svelte; no hacerla prerequisito del proyecto base.
8. Actualizar o archivar el ejemplo antiguo de Kepler.gl y eliminar dependencias heredadas de React 16, Redux 3 y Mapbox GL 1.

**Entregables**

- Plantilla TypeScript/Vite para actividades.
- Ejemplo MapLibre que consuma MVT, PMTiles u OGC API.
- Ejemplo OpenLayers para interoperabilidad avanzada.
- Guia de pruebas, rendimiento y accesibilidad de aplicaciones.

**Criterios de aceptacion**

- El frontend compila reproduciblemente con una version LTS de Node.js.
- El visor se adapta a movil, muestra fallos de red de forma comprensible y no bloquea la navegacion por teclado.
- Las pruebas cubren al menos el flujo principal de carga, filtro y consulta de una capa.

### Fase 8. Seguridad, automatizacion y despliegue

**Objetivo:** convertir calidad, seguridad y operacion en parte del proceso de publicacion.

**Actividades**

1. Actualizar `package.json` y eliminar Husky 3, lint-staged 9 y Prettier 1; adoptar herramientas vigentes y scripts que no modifiquen ni indexen cambios inesperadamente.
2. Configurar GitHub Actions para ejecutar validacion de Markdown, enlaces internos/externos, JSON/GeoJSON, XML/SLD cuando corresponda, formateo, lint, pruebas y build.
3. Crear comprobaciones que no dependan de un servicio externo para aprobar cambios; las pruebas de endpoints remotos deben poder marcarse como informativas o ejecutarse programadamente.
4. Definir gestion de secretos mediante variables de entorno y secretos del proveedor de CI; no usar secretos en frontend salvo claves publicas restringidas.
5. Documentar HTTPS, CORS, CSP, cabeceras de seguridad, limites de peticiones, autenticacion y autorizacion por capa/rol.
6. Crear despliegues de vista previa para el frontend y un flujo de despliegue separado para servicios con estado.
7. Incorporar observabilidad minima: logs, estado de salud, metricas de errores y monitoreo de disponibilidad.
8. Documentar costes, limites, retencion de datos, backups y recuperacion ante incidentes.

**Entregables**

- Workflows de GitHub Actions.
- Politica de seguridad y guia de despliegue.
- Lista de comprobacion para revision de proyectos estudiantiles.

**Criterios de aceptacion**

- Un pull request muestra el resultado de validacion, pruebas y compilacion antes de integrarse.
- No se publican secretos ni se requieren tokens personales para ejecutar ejemplos basicos.
- El procedimiento de despliegue y recuperacion esta documentado y ha sido probado al menos una vez.

### Fase 9. Proyecto piloto, revision y publicacion

**Objetivo:** validar que el curso se puede impartir de principio a fin antes de adoptarlo para una cohorte completa.

**Actividades**

1. Seleccionar un grupo piloto de estudiantes con distintos niveles de experiencia.
2. Ejecutar todas las practicas con equipos limpios y sistemas operativos representativos.
3. Recopilar tiempos, errores, dependencia de soporte y coste de infraestructura.
4. Revisar accesibilidad con herramientas automaticas y pruebas manuales de teclado y movil.
5. Revisar cada tarea con la rubrica propuesta y calibrar carga de trabajo, dificultad y ponderacion.
6. Corregir instrucciones ambiguas, datasets fragiles y pasos no reproducibles.
7. Etiquetar una version del curso para la cohorte y publicar notas de version.

**Entregables**

- Informe de piloto con incidencias, decisiones y mejoras.
- Version etiquetada del curso y guia de actualizacion por cohorte.
- Backlog priorizado para la siguiente iteracion.

**Criterios de aceptacion**

- Un participante del piloto completa el proyecto final sin acceso a infraestructura historica.
- Todas las actividades obligatorias tienen instrucciones, datos y resultados esperados verificables.
- Las incidencias bloqueantes se resuelven antes de la publicacion de la cohorte.

## 6. Temario objetivo

| Unidad | Contenidos | Producto de aprendizaje |
| --- | --- | --- |
| 1. Web, Git y publicacion | Git, GitHub Pages, HTML semantico, CSS responsive, JavaScript moderno, atribucion | Sitio y mapa basico accesible |
| 2. Datos y calidad | QGIS, GeoPackage, GeoJSON, CRS, validacion, metadatos, licencias, privacidad | Pipeline reproducible de datos |
| 3. Cartografia y UX | Clasificacion, simbolizacion, incertidumbre, accesibilidad, movil, narrativa | Mapa tematico evaluado con lista de comprobacion |
| 4. APIs e interoperabilidad | WMS/WFS/WMTS/WCS, OGC API, OpenAPI, STAC, filtros | Cliente que consume servicios clasicos y modernos |
| 5. Servicios e infraestructura | PostGIS, GeoServer, SQL, estilos, Docker Compose, roles y backups | Stack local reproducible |
| 6. Rendimiento y cloud-native | MVT, PMTiles, COG, Zarr, cache, CDN, benchmarks | Visor optimizado y comparativa de formatos |
| 7. Aplicaciones geoespaciales | TypeScript, Vite, MapLibre, OpenLayers, estado, pruebas, 3D electivo | Aplicacion interactiva mantenible |
| 8. Operacion y publicacion | CI/CD, seguridad, observabilidad, coste, arquitectura y etica | Proyecto final desplegado y documentado |

## 7. Entregas evaluables propuestas

### Entrega 1. Mapa publico accesible

- Problema territorial y minimo tres fuentes de datos documentadas.
- Procesamiento reproducible, metadatos, atribucion y licencia.
- Mapa responsive, accesible por teclado y con alternativa textual para los hallazgos principales.
- Justificacion de clasificacion, colores, escala, incertidumbre y limites de interpretacion.

### Entrega 2. Servicio interoperable reproducible

- PostGIS y GeoServer ejecutados mediante Docker Compose.
- Minimo una interfaz OGC API y un servicio clasico por compatibilidad.
- SQL versionado, indices espaciales, roles de lectura y datos de ejemplo.
- Estilo documentado, capas agrupadas, cliente web y pruebas de disponibilidad.

### Entrega 3. Aplicacion geoespacial desplegable

- Tema abierto, renovable por cohorte: clima, riesgo, movilidad, biodiversidad, energia, desigualdad o servicios urbanos.
- Cliente TypeScript con filtros, interaccion, narrativa y manejo de errores.
- Uso justificado de OGC API, vector tiles, PMTiles, COG o STAC cuando aplique.
- CI/CD, documentacion de arquitectura, pruebas, analisis de accesibilidad y evaluacion de privacidad/etica.

## 8. Matriz de migracion de contenidos existentes

| Contenido actual | Accion | Destino |
| --- | --- | --- |
| GitHub Pages, Markdown y Git | Conservar y actualizar interfaz/instrucciones | Unidad 1 |
| HTML, CSS, JavaScript basico | Reescribir con estandares actuales | Unidad 1 |
| Leaflet 1.6 y jQuery 3.1 | Actualizar; sustituir jQuery por APIs nativas | Unidades 1 y 7 |
| QGIS, GeoJSON y TopoJSON | Conservar; complementar con GeoPackage, calidad y CRS | Unidad 2 |
| QGIS2Web | Mantener como prototipo/actividad optativa | Unidad 2, anexo |
| Cartografia tematica | Conservar y ampliar accesibilidad/UX/incertidumbre | Unidad 3 |
| WMS, WFS, WMTS, WCS y CSW | Conservar como compatibilidad | Unidad 4 |
| OWSLib y notebooks antiguos | Actualizar, fijar dependencias y volver a ejecutar | Unidad 4 |
| PostGIS y GeoServer | Conservar y contenerizar | Unidad 5 |
| GeoServer 2.15, Java 8, Tomcat 9 | Retirar de la guia principal | Anexo historico |
| SLD, CSS, YSLD y MBStyle | Conservar; contextualizar con estilos modernos | Unidad 5 |
| Vector tiles | Ampliar con MVT, PMTiles, cache y benchmarks | Unidad 6 |
| Kepler.gl y deck.gl | Mantener como exploracion avanzada | Unidad 7, optativo |
| Mapbox.js y Cartogram | Retirar de actividades obligatorias | Anexo historico |
| Mapbox, CARTO, ArcGIS Online, Flourish | Mantener como comparativa/proveedor opcional | Unidades 3 y 7 |
| GeoNode antiguo | Reevaluar una version vigente o volverlo optativo | Unidad 5, optativo |
| COVID-19 como tema obligatorio | Sustituir por retos renovables | Entrega 3 |

## 9. Validacion y control de calidad

### Validaciones automaticas

- Formato de Markdown y enlaces internos.
- Enlaces externos, ejecutados de manera programada o informativa para evitar bloquear contribuciones por fallos de terceros.
- Sintaxis de JSON, GeoJSON, YAML, XML y SLD cuando corresponda.
- Lint, pruebas y build del frontend TypeScript.
- Ejecucion controlada de notebooks o comprobacion de celdas desde un entorno fijado.
- Analisis de secretos y dependencias vulnerables.

### Validaciones manuales

- Revision cartografica por pares: simbologia, clasificacion, leyenda, escala, atribucion y limites interpretativos.
- Prueba movil y navegacion solo con teclado.
- Revision de contraste, texto alternativo y contenido no dependiente unicamente del color.
- Prueba de instalacion desde cero de Docker Compose, frontend y notebooks.
- Revision de licencias, privacidad y datos sensibles.
- Prueba de restauracion basica de PostGIS y configuracion de servicios.

## 10. Riesgos y mitigaciones

| Riesgo | Mitigacion |
| --- | --- |
| Cambios de precio, interfaz o disponibilidad de SaaS | Mantener ruta obligatoria con herramientas abiertas y ejemplos locales |
| Equipos estudiantiles con recursos limitados | Datasets pequenos, perfiles ligeros, alternativas estaticas y servicios compartidos opcionales |
| Alta complejidad de Docker/GeoServer | Guia paso a paso, imagenes fijadas, diagnostico de errores y practica previa controlada |
| Dependencias externas fragiles | Fixtures locales, datos de ejemplo versionados y pruebas externas no bloqueantes |
| Exposicion de datos sensibles | Politica de privacidad, datasets anonimizados y revision previa de publicacion |
| Sobrecarga curricular | Ruta base obligatoria y modulos avanzados electivos; validacion con piloto |
| Obsolescencia futura | Revision de versiones, enlaces y proveedores antes de cada cohorte |

## 11. Orden de implementacion recomendado

1. Ejecutar Fases 0 y 1 antes de modificar ejercicios: inventario, saneamiento, seguridad y correcciones editoriales.
2. Completar Fase 2 para fijar resultados de aprendizaje y rubricas antes de escribir nuevo codigo.
3. Implementar Fases 3, 4 y 5 para tener una ruta formativa completa desde datos hasta servicios reproducibles.
4. Implementar Fases 6 y 7 para el proyecto final moderno y el contenido avanzado.
5. Completar Fase 8 antes de la adopcion oficial para que las validaciones y despliegues protejan el material.
6. Ejecutar Fase 9 con una cohorte piloto y publicar una version etiquetada solo despues de resolver incidencias bloqueantes.

## 12. Definition of done

La modernizacion se considerara completada cuando se cumplan simultaneamente estas condiciones:

- El indice, programa, unidades y tareas reflejan el temario objetivo y no contienen dependencias obligatorias de 2020.
- Todos los ejemplos obligatorios funcionan desde un clon limpio del repositorio, con prerrequisitos documentados.
- PostGIS y GeoServer se ejecutan localmente mediante Docker Compose y no requieren infraestructura de una cohorte previa.
- El curso ensena y practica OGC API, STAC, formatos cloud-native y vector tiles ademas de los servicios OGC clasicos.
- El cliente principal usa TypeScript y una biblioteca actual; Leaflet queda como introduccion actualizada y sin jQuery.
- Los flujos de entrega incluyen accesibilidad, seguridad, pruebas, automatizacion, documentacion y reproducibilidad.
- No hay secretos, tokens activos sin restringir, credenciales por defecto ni endpoints HTTP inseguros en los ejemplos publicados.
- Un piloto completa las tres entregas con la documentacion disponible y sus incidencias se incorporan al backlog.
- Existe una guia para actualizar versiones, enlaces, datasets y proveedores antes de cada nueva cohorte.
