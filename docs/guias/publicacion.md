---
layout: default
title: Publicación estática
permalink: /guias/publicacion/
---

# Publicación estática

Publica únicamente el sitio ensamblado, no la raíz histórica del repositorio.
Construye Jekyll y el cliente MapLibre, después ensambla los ejemplos y activos
aprobados. Antes de configurar un hosting, comprueba que ofrece HTTP Range y
CORS para PMTiles y COG; si no lo hace, conserva esos activos en el Nginx local
de referencia.

La publicación no incluye PostGIS, GeoServer, contraseñas personales ni datos en
cuarentena. Los despliegues deben proceder de una rama o entorno aprobado.

## GitHub Pages de referencia

El workflow `.github/workflows/pages.yml` publica solo el artefacto ensamblado
`_site/` cuando `master` recibe un cambio o se ejecuta manualmente. En la
configuración del repositorio de GitHub, selecciona **Pages > Build and
deployment > Source > GitHub Actions** antes del primer despliegue. El job
`build` fija sus acciones por SHA, construye Jekyll y Vite, incorpora Leaflet,
MapLibre, PMTiles y COG, y `deploy` publica el artefacto.

Después del primer despliegue, valida desde la URL publicada que los activos
cloud-native responden los requisitos de la ruta elegida. Si el hosting no
ofrece HTTP Range para PMTiles o COG, conserva esos activos en el Nginx local de
referencia y no los declares como publicados.
