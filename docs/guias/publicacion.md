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
