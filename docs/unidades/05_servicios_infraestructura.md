---
layout: default
title: Unidad 5. Servicios e infraestructura reproducible
permalink: /unidades/05-servicios-infraestructura/
---

# Unidad 5. Servicios e infraestructura reproducible

El stack de referencia ejecuta PostGIS, GeoServer y un servidor estático local.
PostGIS conserva la colección `referencia`; GeoServer publica la misma colección
mediante WMS, WFS y OGC API - Features, y también genera MVT por WMS. El servidor
estático entrega PMTiles y COG con HTTP Range y CORS para el cliente MapLibre.

No se publica ninguna interfaz administrativa fuera de `localhost`. Las
credenciales de los ejemplos son ficticias, se entregan por archivo y no deben
reutilizarse en otros entornos.

## Recorrido local

Desde la raíz del repositorio, inicia el stack y configura GeoServer sin pasos
manuales:

```powershell
docker compose -f infra/compose.yaml up -d --build --wait
uv run python scripts/configure_geoserver.py
uv run python infra/smoke/smoke_stack.py
```

El último comando comprueba WMS, WFS, OGC API - Features, MVT, HTTP Range y CORS.
Para detener el entorno y eliminar sus datos de práctica, ejecuta:

```powershell
docker compose -f infra/compose.yaml down --volumes
```

## Diagnóstico

Explica qué interfaz es adecuada para: dibujar una imagen de mapa, descargar
entidades, descubrir una colección HTTP moderna y leer solo una parte de un
archivo grande. Después, identifica el servicio que responde por cada caso en el
smoke test.
