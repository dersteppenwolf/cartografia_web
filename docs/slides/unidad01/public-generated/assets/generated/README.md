# Diagramas propios de la Unidad 1

Los SVG de este directorio son diagramas creados para la presentación
modernizada. No reutilizan imágenes, logotipos, capturas ni composición visual
del PDF histórico. Se consideran material del proyecto, sujeto a la licencia del
repositorio.

`vite.config.mts` declara `public-generated/` como el único directorio público
de Slidev. Por eso estos diagramas se pueden usar con rutas
`/assets/generated/<archivo>.svg` sin exponer los recursos históricos de
`public/assets/`.

Cada archivo contiene `title` y `desc` para identificación básica. `slides.md`
proporciona texto alternativo útil y comentarios con la fuente de los datos.

## Fuentes de datos

- `connectividad_2025.svg` resume la nota de prensa de ITU: seis mil millones de
  personas usan Internet, 2.2 mil millones permanecen desconectadas y 5G cubre
  al 55 % de la población mundial en 2025.
- `actividad_digital_2025.svg` reproduce, como valores textuales y sin
  reutilizar la infografía, tres indicadores por minuto publicados por Domo en
  su _Data Never Sleeps: AI Edition 2025_. Son indicadores de esa publicación,
  no una medida de toda la actividad de Internet. La diapositiva también cita el
  artículo de Cloudflare Radar 2025, que reporta un promedio de más de 81
  millones de solicitudes HTTP por segundo en su red global.

Las fuentes deben revisarse antes de cada cohorte. Los demás diagramas describen
procesos y estados del ejemplo local `examples/leaflet/mapa_basico/`.
