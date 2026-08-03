---
layout: default
title: Unidad 7. Rendimiento y formatos cloud-native
permalink: /unidades/07-rendimiento-cloud-native/
---

# Unidad 7. Rendimiento y formatos cloud-native

PMTiles agrupa teselas vectoriales MVT en un archivo único. Un COG organiza un
GeoTIFF para que el cliente solicite solo los bloques necesarios. Ambos dependen
de HTTP Range: una respuesta correcta devuelve `206 Partial Content`,
`Accept-Ranges` y `Content-Range`.

El curso genera los dos activos desde fixtures sintéticos con herramientas en
contenedores fijados. No descarga datos ni exige una instalación geoespacial
nativa:

```powershell
npm run data:build:pmtiles
npm run data:build:cog
npm run test:range
```

Un proyecto elige PMTiles para vector o COG para ráster. Todo el grupo debe
comprender y visualizar ambas rutas, sin confundir el formato, el servidor
estático y el catálogo STAC que describe el activo.
