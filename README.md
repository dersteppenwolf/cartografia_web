# Publicación de cartografía vía web

Curso de 32 horas presenciales para diseñar, publicar y evaluar cartografía web
comprensible, accesible, interoperable y reproducible.

**Sitio publicado:**
[cartografia_web en GitHub Pages](https://dersteppenwolf.github.io/cartografia_web/)

## Empieza aquí

- [Programa del curso](Programa.md)
- [Material docente publicado](https://dersteppenwolf.github.io/cartografia_web/)
- [Estado de la modernización](docs/status.md)
- [Guía técnica de desarrollo y validación](Dev.md)
- [Plan de modernización](UPGRADE_PLAN.md)
- [Plan de ejecución principal](plans/plan_0001_modernizacion_integral.md)

## Ruta de aprendizaje

| Unidad | Tema                        | Producto verificable                     |
| ------ | --------------------------- | ---------------------------------------- |
| 1      | Web, Git y publicación      | Mapa Leaflet servido por HTTP            |
| 2      | Datos y calidad             | Pipeline reproducible con manifiesto     |
| 3      | Cartografía accesible       | Mapa temático con alternativa tabular    |
| 4      | APIs e interoperabilidad    | Consulta WFS y OGC API - Features        |
| 5      | Servicios e infraestructura | Stack local reconstruible                |
| 6      | Cliente web moderno         | Cliente TypeScript con MapLibre          |
| 7      | Rendimiento y cloud-native  | Ruta PMTiles o COG justificada           |
| 8      | Operación y publicación     | Artefacto estático y backend documentado |

## Ejemplos mantenidos

- [Mapa básico con Leaflet](https://dersteppenwolf.github.io/cartografia_web/examples/leaflet/mapa_basico/)
- [Cliente MapLibre](https://dersteppenwolf.github.io/cartografia_web/examples/maplibre/)
- [PMTiles de referencia](https://dersteppenwolf.github.io/cartografia_web/assets/data/referencia.pmtiles)
- [COG de referencia](https://dersteppenwolf.github.io/cartografia_web/assets/data/referencia.cog.tif)

## Principios del curso

- No se requieren cuentas SaaS, tokens activos, IPs históricas ni servicios de
  pago para completar las entregas obligatorias.
- Los datos de práctica son sintéticos, tienen manifiesto y no incluyen datos
  sociales geolocalizados en cuarentena.
- WMS y WFS se conservan para compatibilidad; OGC API - Features y STAC estático
  son parte del núcleo moderno.
- Cada visualización incluye atribución, estado comprensible y alternativa de
  datos accesible.

## Para contribuir

Consulta [Dev.md](Dev.md) antes de cambiar material, ejemplos, infraestructura o
dependencias. La guía incluye el entorno local, validaciones, build, seguridad,
publicación, recuperación y el proceso para cerrar el plan de modernización.

## Programa y autor

- [Programa vigente en revisión](Programa.md)
- Juan Carlos Méndez
- juan[~~at~~]gkudos.com

## Material histórico

Las unidades, guías, exportaciones y datos anteriores se mantienen versionados
para inventario y revisión. No se enlazan desde la navegación mantenida ni deben
tratarse como requisitos vigentes hasta que superen las revisiones de licencia,
accesibilidad, seguridad, privacidad y compatibilidad.
