---
layout: default
title: Unidad 2. Datos y calidad
permalink: /unidades/02-datos-calidad/
---

# Unidad 2. Datos y calidad

GeoJSON intercambia entidades simples en la web. GeoPackage permite transportar
capas vectoriales con esquema y sistema de referencia en un solo archivo.
TopoJSON puede reducir duplicación topológica, pero no sustituye la validación
de geometría ni el manifiesto de procedencia.

Cada dataset publicado registra fuente, propietario, versión, checksum,
licencia, CRS, esquema y sensibilidad. El fixture de este curso es sintético,
usa EPSG:4326 y no contiene datos personales. El orden de una coordenada GeoJSON
es longitud, latitud.

## Diagnóstico

Ejecuta `uv run python scripts/generate_fixtures.py` dos veces y compara los
checksums impresos. Si cambian, el pipeline no es reproducible.
