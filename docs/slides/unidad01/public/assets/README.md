# Recursos extraídos para migración

Los archivos de este directorio se extrajeron de
`01_Fundamentos/01_Fundamentos_Internet.pdf` para reconstruir la presentación
histórica durante la migración de la Unidad 1. La presentación modernizada en
`docs/slides/unidad01/slides.md` no referencia estos archivos. Cada nombre sigue
el patrón `slide-<página>-image-<índice>.jpg` y conserva su relación con la
página de origen.

Las seis imágenes que usan transparencia incluyen una máscara asociada en
formato PPM. Se retienen junto al JPEG original para conservar la extracción sin
añadir dependencias de composición durante la migración.

Estos recursos se usan únicamente durante la migración. `vite.config.mts` usa
`public-generated/` como directorio público de Slidev, por lo que este
directorio no se sirve ni se copia a sus builds. También quedan excluidos del
build público de Jekyll mediante `docs/_config.yml`.

La licencia y procedencia de cada imagen embebida deben revisarse antes de
incluirla en material público o reutilizarla fuera de esta presentación. Para
previsualizar la presentación, ejecute `slidev slides.md` desde
`docs/slides/unidad01/`; los únicos assets públicos serán los diagramas propios
de `public-generated/assets/generated/`.
