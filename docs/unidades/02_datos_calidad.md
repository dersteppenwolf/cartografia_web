---
layout: default
title: Unidad 2. Datos y calidad
permalink: /unidades/02-datos-calidad/
---

# Unidad 2. Datos y calidad

**Tiempo:** cuatro horas presenciales y cinco horas autónomas. **Producto:** un
pipeline reproducible que genera, valida y documenta datos sintéticos para
publicación. La unidad no reutiliza datos sociales, descargas no documentadas ni
archivos con licencia o sensibilidad sin resolver.

## Resultados de aprendizaje

Al finalizar podrás:

- Distinguir entidad, atributo, geometría, esquema y sistema de referencia.
- Elegir entre GeoJSON, GeoPackage y TopoJSON según la tarea.
- Interpretar coordenadas GeoJSON como longitud, latitud y detectar un orden
  invertido.
- Evaluar precisión, geometría, licencia, procedencia y sensibilidad antes de
  publicar.
- Reproducir un fixture y comprobar su checksum y manifiesto.

## Modelo de datos geográficos

Una **entidad** representa algo del territorio, por ejemplo una zona, una vía o
una estación. Sus **atributos** describen propiedades como nombre, fecha o
valor. La **geometría** indica dónde está o qué extensión ocupa: punto, línea o
polígono. El **esquema** declara qué campos existen, qué tipo de valores admiten
y qué significan. Una geometría sin contexto, atributos sin unidades o una capa
sin sistema de referencia no son suficientes para una publicación responsable.

El **CRS** o sistema de referencia de coordenadas permite convertir números en
ubicaciones. El fixture vectorial del curso usa `EPSG:4326`, que expresa
longitud y latitud en grados. GeoJSON escribe posiciones en este orden:

```json
"coordinates": [-74.07, 4.72]
```

El primer valor es longitud, oeste o este; el segundo es latitud, sur o norte.
Invertirlos puede situar un dato en otro continente o producir una geometría que
parece válida pero no representa el lugar esperado.

## Formatos y decisiones

**GeoJSON** es texto JSON que representa entidades simples y funciona bien en la
web. Es fácil de inspeccionar con un editor, pero no conserva todas las
capacidades de una base de datos ni resulta eficiente para colecciones grandes.

**GeoPackage** es un archivo SQLite que puede contener capas, atributos,
clientes de escritorio. En este curso se genera desde el GeoJSON aprobado para
demostrar una conversión reproducible, no para reemplazar el archivo fuente.

**TopoJSON** comparte arcos entre geometrías vecinas y puede disminuir la
duplicación en límites administrativos. Es una comparación útil de tamaño y
topología, pero no corrige geometrías inválidas, atributos ambiguos ni una
licencia ausente. Un formato compacto no demuestra calidad.

**GML** y **KML** son formatos XML de compatibilidad que se sitúan en la Unidad
4: GML puede aparecer como representación de WFS y KML se orienta a
visualización. **ESRI JSON** es una representación específica de un proveedor.
Si se recibe alguno de estos formatos, documenta fuente, versión, CRS, esquema y
conversión antes de usarlo; no son formatos iniciales ni entregables de esta
unidad.

| Necesidad                                  | Decisión inicial | Razón                                    |
| ------------------------------------------ | ---------------- | ---------------------------------------- |
| Inspeccionar entidades en una página web   | GeoJSON          | El navegador lo puede leer directamente. |
| Intercambiar una capa con esquema y CRS    | GeoPackage       | Conserva estructura en un solo archivo.  |
| Comparar compresión de límites compartidos | TopoJSON         | Reduce arcos repetidos en algunos casos. |

## Calidad antes de publicar

La precisión no es solo el número de decimales. Siete decimales en una columna
no prueban que una posición sea exacta a centímetros; pueden ser redondeo de una
medición menos precisa. Conserva la precisión justificada por la fuente y evita
publicar coordenadas individuales cuando el riesgo de reidentificación supera el
valor pedagógico.

Una geometría válida respeta las reglas del tipo que representa. Un polígono no
debe cruzarse a sí mismo; una línea no debe tener segmentos imposibles por un
error de conversión; un punto debe estar dentro de un rango de coordenadas
coherente. La validez geométrica no demuestra que el dato sea correcto: también
hay que revisar cobertura, fecha, unidades, atributos faltantes y coherencia con
el problema territorial.

Antes de incorporar un dataset, responde:

1. ¿Quién lo produjo y bajo qué licencia?
2. ¿Qué fecha, versión y cobertura territorial tiene?
3. ¿Cuál es el CRS y qué unidad tienen sus atributos?
4. ¿Qué significa cada campo y qué valores faltantes existen?
5. ¿Puede identificar personas, hogares, rutas sensibles u otra información
   restringida?
6. ¿Qué transformación se aplicó y cómo se puede repetir?

## Manifiesto y trazabilidad

`data/manifests/datasets.yml` es la fuente de verdad del curso para los datos
redistribuidos. Cada entrada declara identificador, título, fuente, propietario,
versión, fecha, checksum, licencia, CRS, esquema, sensibilidad y archivo. Un
**checksum** es una huella calculada desde los bytes del archivo. Si el archivo
cambia, el checksum cambia; esa diferencia obliga a revisar el origen y no a
actualizar el manifiesto sin explicación.

El fixture `referencia-sintetica-vector` usa datos creados localmente, licencia
CC0-1.0, `EPSG:4326` y sensibilidad pública. Esa combinación permite practicar
sin trasladar datos personales o de cohortes anteriores al material mantenido.

## QGIS como inspección local

Abre `data/fixtures/vector/referencia.gpkg` en QGIS LTR. Observa el nombre de la
capa, la tabla de atributos, el CRS y las geometrías. Cambia la simbología para
inspeccionar los valores, pero no confundas una representación temporal con una
transformación de datos. Comprueba que los identificadores, nombres y valores
coinciden con el GeoJSON fuente.

QGIS es una herramienta local recomendada, no una fuente de datos ni un servicio
de publicación obligatorio. QGIS2Web se conserva como salida generada histórica:
puede ayudar a explorar un prototipo, pero no reemplaza una aplicación con
datos, estado, accesibilidad y pruebas mantenibles.

## Pipeline reproducible

Los fixtures se generan con un script versionado. Ejecuta desde la raíz:

```powershell
uv run python scripts/generate_fixtures.py
uv run pytest tests/data
uv run python scripts/prepare_vector_data.py --input data/fixtures/vector/referencia.geojson --output data/fixtures/vector/referencia.gpkg
uv run python scripts/validate_resources.py
```

`generate_fixtures.py` crea GeoJSON, CSV y GeoTIFF sintéticos. La conversión usa
GDAL en un contenedor con digest fijado, valida geometrías y escribe un
GeoPackage en `EPSG:4326`. La prueba repite el proceso y comprueba que los
resultados son deterministas. Si un checksum cambia, identifica primero qué
entrada, herramienta o metadato cambió antes de aceptar la nueva salida.

## Práctica guiada

1. Lee la entrada vectorial de `data/manifests/datasets.yml` y anota sus campos
   obligatorios.
2. Abre el GeoJSON y localiza una coordenada. Indica cuál valor es longitud y
   cuál es latitud.
3. Carga el GeoPackage en QGIS y compara atributos, número de entidades y CRS
   con el GeoJSON.
4. Ejecuta el generador dos veces. Explica qué evidenciaría un checksum
   distinto.
5. Propón un campo adicional para una publicación territorial e indica unidad,
   tipo, valores faltantes y riesgo de sensibilidad.

## Errores frecuentes

- Declarar `EPSG:4326` sin comprobar el orden longitud, latitud.
- Confundir más decimales con mayor exactitud.
- Publicar un archivo porque “funciona en QGIS” sin verificar licencia o
  sensibilidad.
- Transformar un dato y perder la fuente o versión original.
- Usar TopoJSON como argumento para omitir validación geométrica.
- Actualizar un checksum sin explicar por qué cambió el archivo.

## Autoevaluación

1. ¿Qué diferencia a GeoJSON de GeoPackage en este curso?
2. ¿Qué información permite interpretar `[-74.07, 4.72]` correctamente?
3. ¿Por qué una geometría válida no garantiza que el dato sea publicable?
4. ¿Qué debe suceder si falta licencia o la sensibilidad no está resuelta?
5. ¿Qué demuestra una segunda generación con el mismo checksum?

Esta unidad prepara el procesamiento documentado de la [Entrega
1]({{ '/evaluacion/entrega-1/' | relative_url }}).

## Diagnóstico

Ejecuta `uv run python scripts/generate_fixtures.py` dos veces y compara los
checksums impresos. Si cambian, el pipeline no es reproducible: identifica el
archivo, el metadato o la herramienta que produjo la diferencia antes de
continuar.
