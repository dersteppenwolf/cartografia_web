---
layout: default
title: Seguridad local
permalink: /guias/seguridad/
---

# Seguridad local

Usa HTTPS al publicar y limita el desarrollo a `localhost`. GeoServer se enlaza
en `127.0.0.1:18080` y el servidor de activos en `127.0.0.1:18081`; PostGIS no
publica un puerto del host.

Los archivos versionados bajo `infra/secrets/` son ejemplos ficticios. Los
secretos de un entorno institucional se entregan por archivos no versionados, se
rotan ante una exposición y nunca se incluyen en registros, notebooks o
capturas.

Antes de integrar cambios ejecuta
`uv run python scripts/security_scan.py --scope worktree` y revisa las
excepciones y revocaciones versionadas.
