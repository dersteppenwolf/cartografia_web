---
layout: default
title: Unidad 4. APIs e interoperabilidad
permalink: /unidades/04-apis-interoperabilidad/
---

# Unidad 4. APIs e interoperabilidad

**Tiempo:** cuatro horas presenciales y cinco horas autónomas. **Producto:** una
consulta reproducible que compara la colección `referencia` mediante WFS y OGC
API - Features, y un catálogo STAC que describe sus activos cloud-native. El
recorrido obligatorio usa fixtures locales; el stack local amplía la práctica
sin depender de servicios institucionales externos.

## Resultados de aprendizaje

Al finalizar podrás:

- Leer una solicitud HTTP y distinguir URL, método, cabeceras, parámetros,
  cuerpo, respuesta y código de estado.
- Elegir WMS, WFS u OGC API - Features según se necesite una imagen, entidades o
  un contrato web moderno.
- Descubrir una colección desde una landing page, sus declaraciones de
  conformidad, sus metadatos y sus entidades.
- Interpretar una descripción OpenAPI y un filtro básico por propiedad, espacio
  o tiempo.
- Explicar cómo Catalog, Collection e Item de STAC describen activos, sin
  confundir un catálogo con un servicio de entidades.

## HTTP: el contrato antes del mapa

HTTP es el protocolo que permite a un cliente pedir un recurso y a un servidor
responder. Una solicitud contiene una **URL**, un **método**, cabeceras y,
cuando corresponde, un cuerpo. La URL puede tener una ruta y un _query string_
de parámetros. La respuesta contiene un código de estado, cabeceras y un cuerpo
que puede ser imagen, XML, JSON o GeoJSON.

| Código | Significado en esta unidad         | Qué hacer                                 |
| ------ | ---------------------------------- | ----------------------------------------- |
| 200    | La solicitud se completó           | Leer y validar el tipo de respuesta       |
| 400    | La solicitud no cumple el contrato | Revisar parámetro, formato o filtro       |
| 404    | La ruta o colección no existe      | Descubrir enlaces desde la landing page   |
| 500    | El servicio falló internamente     | Mostrar error comprensible y revisar logs |

Un HTTP 200 no demuestra que el contenido responda la pregunta territorial: una
imagen puede estar vacía o una colección puede no tener entidades. Del mismo
modo, una colección vacía no es automáticamente un error. La interfaz debe
distinguir resultado vacío, respuesta inválida y fallo de red.

## Servicios para necesidades distintas

WMS, WFS y OGC API - Features pueden describir la misma colección, pero no
entregan el mismo producto ni se descubren del mismo modo.

| Interfaz           | Solicitud principal              | Respuesta habitual           | Úsala cuando                                          |
| ------------------ | -------------------------------- | ---------------------------- | ----------------------------------------------------- |
| WMS                | `GetMap` o `GetCapabilities`     | Imagen o XML de capacidades  | Necesitas una representación cartográfica renderizada |
| WFS                | `GetFeature` o `GetCapabilities` | Entidades GML, GeoJSON o XML | Necesitas entidades mediante el contrato OGC clásico  |
| OGC API - Features | landing, `collections`, `items`  | JSON, GeoJSON y enlaces      | Necesitas descubrimiento HTTP moderno y entidades web |
| STAC estático      | Catalog, Collection, Item        | JSON enlazado                | Necesitas describir activos espaciotemporales         |

WMS entrega una imagen: el estilo se aplica en el servidor y el cliente no
recibe necesariamente cada entidad. WFS y OGC API - Features entregan entidades
y sus atributos, por lo que el cliente puede filtrarlas, tabularlas o
simbolizarlas. STAC no reemplaza ninguno de esos servicios: describe dónde están
activos como un COG o PMTiles, junto con fecha, extensión y enlaces.

## Descubrir OGC API - Features

No construyas rutas a ciegas ni copies URLs de una cohorte anterior. Una landing
page es el punto de entrada que enlaza los recursos que el servidor declara. El
fixture `data/fixtures/responses/ogc-api-features/landing.json` contiene dos
enlaces: `conformance` y `data`.

El recorrido es:

1. **Landing page:** identifica el servicio y sus enlaces principales.
2. **Conformance:** declara las especificaciones que el servidor afirma cumplir.
3. **Collections:** enumera colecciones, título, extensión espacial y temporal.
4. **Collection:** describe una colección concreta.
5. **Items:** entrega entidades de esa colección, normalmente como GeoJSON.

En los fixtures, la colección se llama `referencia`; en el stack GeoServer puede
aparecer como `curso:referencia` porque el nombre incluye el workspace. La
comparación debe reconocer esa diferencia de prefijo y comprobar que las
entidades, atributos y geometrías corresponden al mismo origen.

Una colección grande puede paginar resultados mediante enlaces `next` o
parámetros de límite. El cliente no debe asumir que la primera respuesta
contiene

## OpenAPI y filtros

OpenAPI es un documento procesable que describe rutas, parámetros, respuestas y
tipos esperados. `data/fixtures/openapi/features.json` declara, entre otras,
`/collections` y `/collections/referencia/items`. Leer este contrato antes de
programar evita inventar rutas o interpretar una respuesta de forma ambigua.

Un filtro restringe entidades según una condición. Los filtros básicos del curso
se expresan como propiedad, espacio o tiempo: valor mayor que un umbral, entidad
dentro de un área o entidad en un intervalo de fechas. CQL2 es un lenguaje OGC
para expresar filtros más completos; aquí se presenta como vocabulario y se
practica la lógica de filtro sin exigir que cada servidor admita todas sus
extensiones.

Antes de aceptar un filtro, declara qué campo usa, qué unidad tiene, qué ocurre
con valores faltantes y qué código HTTP esperas si la expresión es inválida. Un
filtro correcto técnicamente puede producir una interpretación engañosa si el
atributo no está documentado.

## STAC estático

STAC organiza descripciones JSON enlazadas. El **Catalog** es la entrada; una
**Collection** agrupa activos con una extensión y periodo comunes; un **Item**
`curso-cartografia-web` y enlaza una Collection `referencia`. El Item enlaza los
activos COG y PMTiles aprobados.

STAC responde “qué activo existe, dónde está y cuándo/cómo se describe”. No
responde por sí mismo una consulta de entidades ni renderiza un mapa. El cliente
puede usar el Item para encontrar un COG; un servidor estático con HTTP Range
entrega los bytes; MapLibre y el protocolo COG lo visualizan. Son
responsabilidades

## Notebooks reproducibles

Los notebooks obligatorios no instalan paquetes ni consultan Internet en su
recorrido principal:

- `notebooks/ogc_clasico.ipynb` lee WFS local o fixture XML.
- `notebooks/ogc_api_features.ipynb` recorre landing, conformidad, colecciones e
  items.
- `notebooks/stac_estatico.ipynb` verifica Catalog, Collection, Item y activo.

El modo `fixtures` permite aprender el contrato sin levantar servicios. El modo
`local` consulta el stack de la Unidad 5 usando `notebooks/config.local.json`,
conclusión sobre la colección de referencia.

## Práctica guiada

1. Ejecuta los notebooks en modo `fixtures` y anota el identificador de la
   colección, una entidad y la extensión espacial.
2. Abre `landing.json`. Sigue los enlaces `conformance` y `data` sin escribir
   una ruta nueva.
3. Abre `features.json` y señala la ruta que entrega colecciones y la que
   entrega entidades.
4. Compara el nombre WFS `curso:referencia` con el identificador de Features.
   Explica por qué un workspace puede aparecer en un contrato y no en otro.
5. Abre `data/fixtures/stac/catalog.json`, sigue el enlace a la Collection y
   localiza los assets del Item. Indica qué parte de la arquitectura sirve el
   archivo y cuál solo lo describe.
6. Con el stack local iniciado, repite los notebooks en modo `local` y compara
   los resultados.

## Errores frecuentes

- Usar WMS para descargar atributos cuando se necesitan entidades.
- Construir una URL manual sin consultar landing, OpenAPI o capabilities.
- Interpretar cualquier 200 como resultado útil.
- Confundir una Collection STAC con una colección de entidades OGC API.
- Suponer que todos los servidores implementan todos los filtros CQL2.
- Usar un endpoint HTTP externo o `verify=False` para que un notebook “pase”.
- Comparar solo nombres y no atributos, geometría, CRS o alcance de una
  colección.

## Autoevaluación

1. ¿Qué interfaz elegirías para obtener una imagen estilizada y cuál para una
   tabla de entidades?
2. ¿Qué recurso visitas primero en una OGC API - Features y por qué?
3. ¿Qué diferencia existe entre un código 400 y un 404?
4. ¿Qué información agrega OpenAPI antes de escribir código cliente?
5. ¿Qué describe STAC y qué componente entrega los bytes de un COG?

Esta unidad prepara la comparación de servicios de la [Entrega
2]({{ '/evaluacion/entrega-2/' | relative_url }}).

## Diagnóstico

Ejecuta los notebooks en modo `fixtures`. Identifica la colección `referencia`,
su extensión espacial y una entidad. Luego compara el nombre de la colección en
la respuesta WFS y en `collections.json`, e indica qué enlace de la landing page
usaste para llegar a la colección.
