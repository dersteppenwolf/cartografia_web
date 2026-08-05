# Recursos extraídos para migración

Los archivos de este directorio se extrajeron de
`01_Fundamentos/01_Fundamentos_Internet.pdf` para reconstruir la presentación
Slidev de la Unidad 1. Cada nombre sigue el patrón
`slide-<página>-image-<índice>.jpg` y conserva su relación con la página de
origen.

Las seis imágenes que usan transparencia incluyen una máscara asociada en
formato PPM. Se retienen junto al JPEG original para conservar la extracción sin
añadir dependencias de composición durante la migración.

Estos recursos se usan únicamente durante la migración y quedan excluidos del
build público de Jekyll mediante `docs/_config.yml`. La licencia y procedencia
de cada imagen embebida deben revisarse antes de incluirla en material público o
reutilizarla fuera de esta presentación.

Para previsualizar la presentación y sus assets, ejecute `slidev slides.md`
desde `docs/slides/unidad01/`.
