---
layout: default
title: Restauración local
permalink: /guias/restauracion/
---

# Restauración local

El backup contiene un volcado PostGIS y un manifiesto SHA-256. GeoServer se
reconstruye mediante `scripts/configure_geoserver.py`; caches y data directories
son regenerables y no se respaldan.

```powershell
uv run python scripts/test_restore.py --compose-file infra/compose.yaml --backup-dir .backups
```

La prueba inserta una fila centinela, crea el backup, elimina los volúmenes,
restaura el volcado, vuelve a configurar GeoServer y repite los smoke tests. No
modifica el backup si la recuperación falla.
