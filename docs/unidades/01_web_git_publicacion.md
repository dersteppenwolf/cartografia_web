---
layout: default
title: Unidad 1. Web, Git y publicación
permalink: /unidades/01-web-git-publicacion/
---

# Unidad 1. Web, Git y publicación

El navegador interpreta HTML para estructura, CSS para presentación y JavaScript
para interacción. Git registra cambios locales; un hosting estático publica
archivos sin ejecutar un servidor de aplicación. La práctica no requiere cuentas
ni tokens.

El ejemplo [mapa Leaflet básico]({{ '/examples/leaflet/mapa_basico/' |
relative_url }}) se sirve por HTTP local. Su JavaScript usa módulos del
navegador, `fetch`, `async`/`await`, el mapa base OpenStreetMap con atribución
visible y un mensaje de error cuando el archivo no está disponible.

## Diagnóstico

Explica la diferencia entre abrir un HTML mediante `file://` y servirlo con
`python -m http.server 8000`. Demuestra la respuesta observando el estado de
carga del ejemplo.
