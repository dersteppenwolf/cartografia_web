---
layout: default
title: Unidad 7. Rendimiento y formatos cloud-native
permalink: /unidades/07-rendimiento-cloud-native/
---

# Unidad 7. Rendimiento y formatos cloud-native

**Tiempo:** cuatro horas presenciales y cinco horas autónomas. **Producto:** una
ruta de entrega optimizada, PMTiles para vector o COG para ráster, documentada
con STAC, HTTP Range y mediciones reproducibles. Todo el grupo consume ambos
formatos; cada proyecto genera y justifica una sola ruta.

## Resultados de aprendizaje

Al finalizar podrás:

- Distinguir GeoJSON, MVT, PMTiles, GeoTIFF convencional, COG y WMS.
- Explicar cómo niveles de zoom, simplificación y atributos afectan una ruta
  vectorial.
- Explicar cómo bloques, overviews y compresión afectan una ruta ráster.
- Verificar HTTP Range, CORS y las relaciones entre Catalog, Collection, Item y
  assets STAC.
- Ejecutar y leer benchmarks de transporte HTTP y de navegador sin atribuir a un
  formato una causa que no fue medida.

## Por qué no basta con un archivo pequeño

El rendimiento de un mapa depende de bytes, solicitudes, caché, tamaño de
ventana, zoom, estilo, CPU/GPU, red y estrategia de entrega. Un archivo reducido
puede seguir siendo lento si el navegador descarga más de lo que necesita; un
archivo grande puede resultar útil si se lee por partes y usa niveles de
detalle. Por eso esta unidad compara una cadena completa, no solo tamaños en
disco.

**GeoJSON** entrega entidades completas en un documento JSON. Es fácil de
inspeccionar y útil para colecciones pequeñas, pero un cliente descarga todo el
archivo antes de filtrar o dibujar. **MVT** codifica entidades vectoriales por
tesela. Una **tesela** divide el espacio en cuadros para cada nivel de zoom; el
cliente pide solo los cuadros que cubren su vista. **PMTiles** empaqueta muchas
teselas MVT en un solo archivo y usa un índice interno para ubicar los bytes de
cada tesela.

Un **GeoTIFF** convencional puede contener un ráster completo en un orden poco
útil para la web. Un **COG** organiza bloques internos y overviews, versiones de
menor resolución, para que el cliente lea primero una aproximación y solicite
detalle solo al acercarse. WMS sigue siendo una alternativa de compatibilidad:
el servidor renderiza una imagen por solicitud, mientras COG entrega bytes de un
activo y el cliente lo interpreta.

| Ruta    | Entrega                 | Quién simboliza      | Primer uso                                |
| ------- | ----------------------- | -------------------- | ----------------------------------------- |
| GeoJSON | Documento completo      | Cliente              | Colección pequeña, inspección y enseñanza |
| MVT     | Tesela vectorial        | Cliente              | Mapa vectorial por vista y zoom           |
| PMTiles | Archivo de teselas      | Cliente              | Vector estático con Range                 |
| WMS     | Imagen renderizada      | Servidor             | Compatibilidad y mapa de servidor         |
| GeoTIFF | Archivo ráster completo | Cliente o escritorio | Intercambio y análisis base               |
| COG     | Bloques y overviews     | Cliente              | Ráster remoto con Range                   |

## Ruta vectorial: GeoJSON, MVT y PMTiles

La ruta vectorial del curso es:

```text
GeoJSON sintético -> Planetiler -> PMTiles -> Nginx o Pages -> protocolo PMTiles -> MapLibre
```

Planetiler recibe `data/fixtures/vector/referencia.geojson` y el esquema
`scripts/planetiler-referencia.yml`. El esquema define zoom mínimo, zoom máximo,
capa y atributos que se conservan. Cada atributo adicional ocupa bytes en cada
tesela; no copies columnas que el mapa no usa. La **simplificación** reduce
vértices según zoom para que una geometría distante no cargue el mismo detalle
que una geometría cercana. Una simplificación excesiva deforma límites; una nula
puede transferir detalle invisible.

Los niveles de zoom deben responder a una pregunta de uso: a baja escala importa
la forma general y a alta escala pueden aparecer detalles o etiquetas. Un punto
no requiere la misma generalización que un polígono complejo. El fixture es
pequeño, pero el esquema documenta la decisión que se mediría con un dataset
mayor.

```powershell
npm run data:build:pmtiles
```

El script ejecuta Planetiler y luego el CLI PMTiles fijado por digest para
verificar el archivo. El resultado aprobado queda en
`data/fixtures/cloud/referencia.pmtiles`.

## Ruta ráster: GeoTIFF y COG

La ruta ráster del curso es:

```text
GeoTIFF sintético -> GDAL COG -> Nginx o Pages -> protocolo COG -> MapLibre
```

Un **bloque** es una porción interna del ráster. Un **overview** es una versión
reducida que permite responder rápidamente cuando la vista cubre un área grande.
La compresión reduce bytes almacenados y transferidos, pero puede aumentar
tiempo de CPU o afectar valores según el método. El builder del curso usa
bloques de 256 y compresión DEFLATE, decisiones explícitas y reproducibles, no
una receta universal.

```powershell
npm run data:build:cog
```

El script usa GDAL fijado por digest, ejecuta `gdal_translate -of COG` e
inspecciona la salida con `gdalinfo`. El activo resultante queda en
`data/fixtures/cloud/referencia.cog.tif`. Para un ráster real, también debes
documentar NoData, bandas, resolución, fecha, CRS y el efecto de reamostrar.

## HTTP Range, CORS y caché

PMTiles y COG necesitan pedir rangos de bytes. Una solicitud correcta envía una
cabecera como `Range: bytes=0-15`. El servidor debe responder
`206 Partial Content`, `Accept-Ranges: bytes` y un `Content-Range` que indique
qué fragmento entregó. Si devuelve 200 con el archivo completo, el cliente puede
perder la ventaja de formato cloud-native.

CORS autoriza que una página en un origen solicite recursos en otro. El Nginx
local permite `http://localhost:4173` y expone cabeceras Range necesarias.
GitHub Pages entrega sus propios activos con una política distinta; cada hosting
debe probarse después de desplegar, no asumirse por haber funcionado localmente.

La caché reduce solicitudes repetidas. No es permiso para precargar una ciudad,
todos los zooms o datos offline desde un proveedor público de teselas. Respeta
las cabeceras de caché y las políticas del proveedor. OSM es contexto visual de
mejor esfuerzo; no se usa para benchmarks masivos ni para la ruta de entrega del
proyecto.

```powershell
npm run test:range
```

Este comando valida PMTiles y COG contra Nginx con `206`, Range y CORS. Si
falla, revisa servidor, origen, cabeceras y ruta antes de culpar al formato.

## STAC: catálogo, no servidor

STAC describe activos mediante documentos JSON enlazados. El **Catalog** del
curso enlaza la **Collection** `referencia`; el **Item** describe extensión,
fecha y assets. `data/fixtures/stac/item-referencia.json` enlaza el COG y
PMTiles generados. STAC responde “qué activo existe y dónde se describe”; Nginx
o Pages entrega los bytes; MapLibre los visualiza. Ninguno de esos tres roles es
intercambiable.

```powershell
npm run validate:stac
```

El validador comprueba Catalog, Collection, Item y que los enlaces de assets
locales existan. Si un builder reemplaza un archivo, revisa su checksum y el
manifiesto antes de actualizar STAC.

## Medir sin prometer más de lo observado

El benchmark HTTP ejecuta al menos cinco solicitudes por ruta y escribe mediana,
bytes y estado. Para vector compara GeoJSON y PMTiles; para ráster compara WMS y
COG. La medición indica transporte local, no tiempo total de renderizado ni
experiencia de una red móvil.

```powershell
npm run benchmark -- --route vector --runs 5
npm run benchmark -- --route raster --runs 5
```

El benchmark de navegador abre Chromium cinco veces para OGC API, PMTiles y COG.
Mide hasta que MapLibre registra la fuente y guarda recursos observados por la
Performance API. Incluye carga de script, WebGL, red y ejecución del navegador;
no representa Safari real ni todas las condiciones de hardware.

```powershell
npm run benchmark:browser
```

Los reportes viven en `.reports/` y no se versionan. Registra checksum, equipo,
navegador, fecha, caché fría o caliente, número de solicitudes, bytes, mediana y
limitaciones. El objetivo curricular de reducción del 30 % requiere una decisión
comando imprimió una mediana.

## Práctica común y ruta elegida

Todo el grupo debe generar, validar y visualizar ambos activos:

```powershell
npm run data:build:pmtiles
npm run data:build:cog
npm run validate:cloud
npm run test:range
```

Después, cada proyecto elige una ruta:

- **Vector PMTiles:** documenta zooms, simplificación, atributos incluidos,
  tamaño, fuente y estilo cliente.
- **Ráster COG:** documenta bandas, NoData, compresión, bloques, overviews, CRS,
  resolución y visualización.

Abre el [cliente MapLibre mantenido]({{ '/examples/maplibre/' | relative_url }})
referencia textual de las entidades; un ráster requiere además resumen, leyenda
o

## Errores frecuentes

- Confundir MVT, PMTiles, COG, STAC y Nginx como si fueran el mismo formato.
- Descargar un archivo completo y afirmar que se usó Range porque el servidor
  tenía esa cabecera.
- Conservar todos los atributos o todos los vértices sin justificar su uso.
- Usar una tesela de un proveedor público para precargar o hacer benchmark
  masivo.
- Comparar una sola ejecución caliente y atribuir el resultado al formato.
- Cambiar un asset generado sin actualizar manifest, checksum o STAC.
- Exigir que cada estudiante produzca PMTiles y COG completos cuando la entrega
  solo requiere optimizar una ruta.

## Autoevaluación

1. ¿Qué diferencia hay entre una tesela MVT y un archivo PMTiles?
2. ¿Qué hace un overview y por qué ayuda a un COG?
3. ¿Qué cabeceras demuestran una respuesta Range correcta?
4. ¿Qué describe STAC y qué componente entrega los bytes?
5. ¿Qué diferencia hay entre benchmark HTTP y benchmark de navegador?
6. ¿Qué información justificarías para elegir la ruta vectorial o ráster?

Esta unidad prepara la ruta optimizada de la [Entrega
3]({{ '/evaluacion/entrega-3/' | relative_url }}).

## Diagnóstico

Explica qué bytes solicita un cliente PMTiles o COG antes de dibujar una vista,
qué cabecera confirma esa solicitud y qué medición usarías para diferenciar
transporte HTTP de disponibilidad de una fuente en MapLibre. Justifica la ruta
de tu proyecto con una limitación explícita.
