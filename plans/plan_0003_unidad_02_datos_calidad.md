# plan_0003 - Hacer autonoma la Unidad 2 de datos y calidad

**Fecha**: 2026-08-03 **Ambito**: `docs/unidades/02_datos_calidad.md`, fixtures,
manifiestos, `scripts/generate_fixtures.py` y `scripts/prepare_vector_data.py`
**Estado**: propuesto **Prioridad**: alta; base de cartografia, servicios y
cliente

Este ExecPlan es un documento vivo. Debe mantenerse conforme a `PLANS.md`,
`AGENTS.md`, `UPGRADE_PLAN.md` y `DESIGN.md`.

## Proposito / Panorama general

Al terminar, una persona podra distinguir GeoJSON, GeoPackage y TopoJSON,
inspeccionar CRS, orden de coordenadas, precision, atributos y geometria, y
producir datos de practica reproducibles con manifiesto. Podra demostrarlo
regenerando fixtures con checksum estable y convirtiendo el GeoJSON aprobado a
GeoPackage sin descargar datos externos.

## Progress

- [x] (2026-08-03) Se identifico que la unidad actual solo define formatos y
      manifiestos en 22 lineas; no explica QGIS, CRS, validacion, precision ni
      el pipeline completo.
- [x] (2026-08-03) Se reescribio el documento con modelo de datos, CRS,
      formatos, precision, validez, manifiestos, QGIS local, pipeline, practica,
      errores y autoevaluacion.
- [x] (2026-08-03) Se conecto el texto con fixtures, manifiesto y conversion
      GeoPackage aprobados.
- [x] (2026-08-03) Pasaron pruebas de datos, validacion de recursos, build y
      enlaces internos.

## Surprises & Discoveries

- Observacion: `02_Conceptos/Readme.md` tiene ejercicios de QGIS y GeoJSON, pero
  depende de descargas externas, ArcGIS, QGIS2Web y recursos HTTP historicos.
  Evidencia: `02_Conceptos/Readme.md` lineas 27 a 195.

- Observacion: los fixtures mantenidos ya tienen CRS, licencia, checksum y
  sensibilidad registrados. Evidencia: `data/manifests/datasets.yml` y pruebas
  en `tests/data/`.

## Decision Log

- Decision: usar los fixtures sinteticos como unica fuente obligatoria y tratar
  QGIS como herramienta local de inspeccion, no como proveedor de datos.
  Justificacion: protege privacidad, elimina dependencia de red y permite
  repetir la practica desde un clon limpio. Fecha/Autor: 2026-08-03 / OpenCode.

## Outcomes & Retrospective

La unidad pasara de un glosario a un recorrido que conecta calidad conceptual,
metadatos y un pipeline verificable. El producto sera el insumo documentado para
Entrega 1.

## Contexto y orientacion

La unidad dura cuatro horas presenciales y cinco autonomas.
`data/fixtures/vector/referencia.geojson` es una coleccion de entidades
sinteticas en EPSG:4326. `data/fixtures/vector/referencia.gpkg` es su
equivalente GeoPackage. `data/manifests/datasets.yml` declara fuente,
propietario, version, checksum, licencia, CRS, esquema y sensibilidad. Un CRS es
la convencion que permite interpretar coordenadas; EPSG:4326 usa grados. GeoJSON
escribe posiciones como longitud, latitud. Precision es el numero de decimales
retenidos; no debe inventar exactitud que los datos no poseen. Una geometria
valida cumple reglas topologicas del tipo punto, linea o poligono.

## Plan de trabajo

Reescribir la unidad con resultados de aprendizaje y una secuencia: problema
territorial, modelo de entidad-atributo-geometria, formatos, CRS, coordenadas,
precision, validacion, metadatos, licencia y sensibilidad. Explicar por que
GeoPackage conserva varias capas y esquema, por que GeoJSON es util en web y por
que TopoJSON es una comparacion de compresion, no una sustitucion de calidad.

Incluir una practica QGIS sin cuenta: abrir el GeoPackage, inspeccionar tabla de
atributos, CRS y geometria, cambiar simbologia solo para inspeccion y no
exportar datos externos. Describir el pipeline `generate_fixtures.py` y
`prepare_vector_data.py`, con entradas, salidas, checksum e idempotencia.
Explicar que un manifiesto no es texto decorativo: habilita atribucion,
auditoria y una decision sobre si un dato puede publicarse.

Agregar ejercicios de deteccion de orden invertido, CRS faltante, atributo
ambiguo, licencia desconocida y precision excesiva. Cerrar con autoevaluacion y
conexion directa con Entrega 1.

## Pasos concretos

Desde la raiz ejecutar:

    uv run python scripts/generate_fixtures.py
    uv run pytest tests/data
    uv run python scripts/prepare_vector_data.py --input data/fixtures/vector/referencia.geojson --output data/fixtures/vector/referencia.gpkg
    uv run python scripts/validate_resources.py
    npm run lint:markdown

La segunda generacion debe conservar los checksums registrados. Si
`prepare_vector_data.py` recibe otro nombre de argumentos, actualizar la
documentacion con la interfaz real en vez de inventar comandos.

## Validacion y aceptacion

La leccion se acepta cuando define cada formato y termino, permite distinguir
longitud de latitud, explica un CRS, muestra como leer un manifiesto y propone
una respuesta para datos sin licencia o con sensibilidad no resuelta. Debe
contener una actividad QGIS local, una actividad de pipeline, errores
frecuentes, autoevaluacion y criterios de Entrega 1.

`uv run pytest tests/data`, `uv run python scripts/validate_resources.py`,
`npm run lint:markdown` y `git diff --check` deben pasar. Una prueba didactica
debe comparar dos ejecuciones y explicar por que un checksum distinto bloquea la
publicacion.

## Idempotencia y recuperacion

Los scripts no descargan datos. Si una conversion cambia el GeoPackage, ejecutar
de nuevo el generador de fixtures y comprobar el manifiesto antes de confirmar
cambios. Nunca reemplazar los fixtures por datos sociales, geolocalizados o de
licencia pendiente.

## Artefactos y notas

El documento final debe enlazar `data/manifests/datasets.yml` y los scripts
relevantes, con explicacion legible de sus campos. Los resultados de QGIS se
describen en texto y tabla; una captura no es evidencia suficiente.

## Interfaces y dependencias

Usar QGIS LTR como visor local recomendado, GDAL/Rasterio solo mediante los
scripts fijados y los fixtures existentes. No reintroducir geojson.io, ArcGIS o
QGIS2Web como requisito. Mantener el contrato de `data/manifests/datasets.yml` y
`scripts/validate_resources.py`.

## Revision

2026-08-03: creado para ampliar la Unidad 2 sin migrar fuentes externas o datos
no aprobados.
