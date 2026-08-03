---
layout: default
title: Unidad 5. Servicios e infraestructura reproducible
permalink: /unidades/05-servicios-infraestructura/
---

# Unidad 5. Servicios e infraestructura reproducible

**Tiempo:** cuatro horas presenciales y seis horas autónomas. **Producto:** un
stack local que se reconstruye desde archivos versionados, publica la colección
`referencia` mediante interfaces OGC y recupera una fila centinela desde un
backup verificado. No requiere un servidor de cohorte, una interfaz remota ni
credenciales reales.

## Resultados de aprendizaje

Al finalizar podrás:

- Dibujar el recorrido desde una tabla PostGIS hasta un cliente web.
- Explicar tabla, geometría, CRS, índice GiST, datastore, capa, estilo SLD y
  grupo de capas.
- Diferenciar WMS, WFS, OGC API - Features, MVT, PMTiles y COG según su salida.
- Iniciar, comprobar, observar logs y detener un stack Docker Compose local.
- Crear un backup con checksum, restaurarlo desde volúmenes vacíos y verificar
  el resultado.

## Arquitectura de extremo a extremo

El stack de referencia tiene tres servicios locales. **PostGIS** conserva la
tabla y sus geometrías. **GeoServer** conecta esa tabla como datastore, publica
una capa y responde interfaces OGC. **Nginx** entrega archivos estáticos, como
PMTiles y COG, con HTTP Range y CORS para el cliente MapLibre.

```text
GeoJSON sintético ──> PostGIS referencia ──> GeoServer ──> WMS / WFS / Features / MVT
                                             │
Cliente MapLibre <── Nginx <── PMTiles y COG ┘
```

La misma colección puede tener varias salidas porque cada interfaz responde una
necesidad distinta. WMS entrega una imagen renderizada; WFS y OGC API - Features
entregan entidades; MVT entrega una tesela vectorial; PMTiles empaqueta teselas
en todos los casos.

Los puertos administrativos se enlazan a `localhost`. Así, el navegador de la
misma máquina puede consultar GeoServer, pero una red externa no puede abrir su
interfaz por accidente. Los archivos en `infra/secrets/*.example` son valores
ficticios de desarrollo; un secreto real nunca se confirma en Git ni se
reutiliza en una captura o notebook.

## PostGIS: tabla, geometría e índice

PostGIS añade geometrías y funciones espaciales a PostgreSQL. La tabla
`referencia` contiene `id`, `nombre`, `valor` y `geom`. `geom` es un punto en
`EPSG:4326`; `id` es la llave primaria que evita duplicados. La inicialización
usa `INSERT ... ON CONFLICT DO UPDATE`, por lo que aplicar los datos de práctica
otra vez no crea filas nuevas sin control.

```sql
SELECT id, nombre, valor, ST_AsText(geom)
FROM referencia
ORDER BY valor;
```

Una consulta atributiva filtra columnas comunes:

```sql
SELECT id, nombre, valor
FROM referencia
WHERE valor >= 20;
```

Una consulta espacial usa la geometría. Por ejemplo, `ST_DWithin` pregunta qué
entidades están a una distancia de un punto. Para conjuntos grandes, un índice
**GiST** reduce el número de geometrías que deben compararse. En el fixture,
`referencia_geom_gist` es ese índice. El índice acelera búsquedas; no corrige
CRS ni transforma una geometría inválida en dato confiable.

```sql
SELECT id, nombre
FROM referencia
WHERE ST_DWithin(
  geom::geography,
  ST_SetSRID(ST_MakePoint(-74.07, 4.72), 4326)::geography,
  5000
);
```

La conversión a `geography` hace que los 5000 se interpreten como metros. Antes

## GeoServer: del datastore a la capa

GeoServer no adivina qué tabla publicar. `scripts/configure_geoserver.py` aplica
la configuración mediante REST y puede ejecutarse repetidamente:

1. Crea el workspace `curso`.
2. Registra el datastore `curso_postgis` que conecta a PostGIS.
3. Publica el feature type `referencia` como capa `curso:referencia`.
4. Carga o actualiza el estilo `referencia.sld`.
5. Asigna el estilo a la capa y crea el grupo de capas.

Un **workspace** evita colisiones de nombres. Un **datastore** describe cómo
llegar a los datos. Un **feature type** describe una tabla espacial publicable.
Una **capa** es la representación servida. Un **SLD** es XML que declara cómo
dibujarla: símbolo, color, tamaño, etiqueta o regla. El SLD versionado permite
reconstruir la apariencia sin clics manuales.

La configuración declarada por REST es distinta de guardar un data directory
completo. Un volumen persistente puede conservar estado, pero no demuestra que
otra persona pueda reconstruirlo. El script, SQL y SLD versionados sí lo hacen.

## Compose, salud y observabilidad mínima

Docker Compose describe los servicios, imágenes por digest, red, secretos,
volúmenes y healthchecks en `infra/compose.yaml`. Un **healthcheck** es una
prueba corta dentro del contenedor que declara cuándo un servicio está listo.
`depends_on` espera el healthcheck de PostGIS antes de iniciar GeoServer.

```powershell
docker compose -f infra/compose.yaml config --quiet
docker compose -f infra/compose.yaml up -d --build --wait
docker compose -f infra/compose.yaml ps
```

La salida de `ps` debe marcar los tres servicios como `healthy`. Si algo falla,
revisa primero el servicio afectado:

```powershell
docker compose -f infra/compose.yaml logs geoserver --tail 100
docker compose -f infra/compose.yaml logs postgis --tail 100
docker compose -f infra/compose.yaml logs static --tail 100
```

Los logs son evidencia operativa, no un sustituto de una prueba. El smoke test
consulta capacidades WMS y WFS, landing/collections/items de OGC API, un MVT y
los rangos HTTP de PMTiles/COG. Si el smoke test pasa, demuestra que las rutas
esenciales responden; no demuestra que toda consulta imaginable sea correcta.

## Interfaces de la misma colección

| Interfaz           | Recurso                              | Salida             | Uso inicial                          |
| ------------------ | ------------------------------------ | ------------------ | ------------------------------------ |
| WMS                | `GetMap`                             | Imagen             | Contexto cartográfico renderizado    |
| WFS                | `GetFeature`                         | Entidades          | Compatibilidad OGC clásica           |
| OGC API - Features | `collections` e `items`              | JSON/GeoJSON       | Cliente web y descubrimiento moderno |
| MVT                | WMS `GetMap` con formato vector tile | Tesela vectorial   | Ruta vectorial dinámica              |
| PMTiles            | Nginx con Range                      | Archivo de teselas | Ruta vectorial estática              |
| COG                | Nginx con Range                      | Bloques GeoTIFF    | Ruta raster estática                 |

La presencia de MVT en GeoServer no hace innecesario PMTiles: el primero es una
respuesta de servicio y el segundo es un archivo empaquetado. STAC describe los
activos PMTiles/COG; Nginx entrega sus bytes; MapLibre los visualiza.

## Recorrido local

Desde la raíz del repositorio, inicia el stack y configura GeoServer sin pasos
manuales:

```powershell
docker compose -f infra/compose.yaml up -d --build --wait
uv run python scripts/configure_geoserver.py
npm run validate:stack
```

La validación comprueba WMS, WFS, OGC API - Features, MVT, STAC, HTTP Range y
CORS. Después, ejecuta los notebooks en modo local para comprobar que WFS y OGC
API describen la misma colección:

```powershell
uv run python scripts/run_notebooks.py --mode local
```

## Backup y recuperación

Un backup útil contiene datos y evidencia de integridad.
`scripts/backup_stack.py` crea un dump PostgreSQL y `manifest.json` con SHA-256,
fecha y versión. No copia el data directory de GeoServer porque su configuración
se reconstruye desde REST y el SLD versionado.

La prueba de recuperación usa una fila centinela con identificador conocido:

```powershell
uv run python scripts/test_restore.py --compose-file infra/compose.yaml --backup-dir .backups
```

El script inserta la fila, genera backup, destruye solo los volúmenes de
práctica, inicia un stack vacío, verifica el checksum, restaura PostGIS,
configura GeoServer, consulta la fila y repite el smoke test. Si falla, conserva
`.backups/` para diagnóstico. No intentes restaurar sobre un volumen de estado

Para detener el entorno y eliminar únicamente los datos de práctica:

```powershell
docker compose -f infra/compose.yaml down --volumes
```

## Práctica guiada

1. Lee `infra/postgis/init/10-referencia.sql`. Identifica llave primaria,
   geometría, CRS, inserción idempotente e índice GiST.
2. Ejecuta una consulta atributiva y una espacial dentro del contenedor PostGIS.
   Explica qué atributo o geometría filtra cada una.
3. Lee `scripts/configure_geoserver.py` e identifica workspace, datastore,
   feature type, capa, estilo y grupo.
4. Inicia el stack, ejecuta `npm run validate:stack` y relaciona cada respuesta
   con la tabla de interfaces de esta unidad.
5. Detén un servicio, revisa sus logs y explica qué evidencia distingue un
   healthcheck fallido de una respuesta HTTP fallida.
6. Ejecuta `scripts/test_restore.py` y conserva el mensaje que confirma la fila
   centinela recuperada.

## Errores frecuentes

- Tratar un volumen persistente como configuración reproducible.
- Publicar un puerto administrativo en todas las interfaces de red.
- Usar una contraseña real en un ejemplo o en un comando de notebook.
- Confundir datastore, tabla, feature type, capa y estilo.
- Aplicar un SLD manualmente y no versionar la regla.
- Restaurar un dump sin verificar checksum.
- Suponer que un healthcheck verde valida los datos, estilos o todas las rutas.

## Autoevaluación

1. ¿Qué diferencia hay entre un índice GiST y una geometría?
2. ¿Qué crea GeoServer antes de publicar `curso:referencia`?
3. ¿Qué interfaz usarías para imagen, entidades y tesela vectorial?
4. ¿Por qué el SLD y el script REST son parte del backup lógico?
5. ¿Qué comprueba la fila centinela durante una restauración?

Esta unidad prepara la infraestructura reproducible de la [Entrega
2]({{ '/evaluacion/entrega-2/' | relative_url }}) y las rutas locales de las
unidades posteriores.

## Diagnóstico

Explica qué interfaz es adecuada para dibujar una imagen de mapa, descargar
entidades, descubrir una colección HTTP moderna, leer una tesela vectorial y
leer solo una parte de un archivo grande. Después, identifica el servicio que
responde por cada caso en el smoke test y explica qué parte del recorrido
restaura la prueba de la fila centinela.
