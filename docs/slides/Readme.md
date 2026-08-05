# Generación de presentaciones Slidev

Este directorio conserva presentaciones Slidev creadas durante la migración de
los PDF docentes. Cada presentación debe poder reconstruirse desde el PDF de
origen, mantener una diapositiva por página y usar recursos con nombres
deterministas.

## Alcance y publicación

`docs/_config.yml` excluye `slides/` del build Jekyll. Las presentaciones y sus
recursos se usan durante la migración, no se publican con el sitio del curso. No
elimine esa exclusión ni publique recursos extraídos hasta revisar la
procedencia, la licencia y el texto alternativo de cada imagen.

Los PDF históricos son la única fuente para su conversión. Conserve idioma,
terminología, código, cifras y enlaces. No complete texto ilegible ni sustituya
capturas o diagramas por contenido inventado.

## Estructura

Cada unidad usa esta estructura:

```text
docs/slides/
  Readme.md
  unidad01/
    slides.md
    public/
      assets/
        README.md
        slide-001-image-000.jpg
```

`slides.md` usa el tema `default` de Slidev. Cada diapositiva comienza con el
comentario `<!-- PDF página: N -->` y contiene un layout compatible con Slidev.
Los archivos dentro de `public/assets/` se referencian con rutas absolutas para
el servidor de desarrollo de Slidev, por ejemplo:

```html
<img
  src="/assets/slide-004-image-000.jpg"
  alt="Infografía de población mundial y estimación de usuarios de internet."
/>
```

## Dependencias

Ejecute los comandos desde la raíz del repositorio, salvo que se indique otro
directorio.

Se necesita Node.js y npm para Slidev, y Poppler para extraer las imágenes. En
Windows, compruebe que `pdfinfo` y `pdfimages` están disponibles en `PATH`:

```powershell
node --version
npm --version
pdfinfo -v
pdfimages -v
```

Instale Slidev como dependencia local de cada presentación. Esto evita una
dependencia global y permite repetir la previsualización en otro equipo:

```powershell
Set-Location docs/slides/unidad01
npm init -y
npm install --save-dev @slidev/cli
```

El archivo `package-lock.json` generado en la unidad debe mantenerse
sincronizado con su `package.json`.

## Conversión del PDF

1. Identifique el PDF de origen y cuente sus páginas.

   ```powershell
   pdfinfo 01_Fundamentos/01_Fundamentos_Internet.pdf
   ```

2. Cree `docs/slides/unidadNN/slides.md` con un frontmatter global de Slidev.
   Debe existir exactamente una diapositiva por cada página y conservarse el
   orden. Agregue `<!-- PDF página: N -->` antes de cada una.

3. Transcriba el texto visible y seleccione el layout que mejor reproduzca la
   composición: `cover`, `section`, `center`, `default` o `two-cols`. Conserve
   bloques de código con su lenguaje cuando pueda identificarse.

4. Si una imagen todavía no puede incorporarse, use temporalmente un comentario
   como `<!-- TODO: extraer imagen principal de la página N -->`. No invente el
   contenido de la imagen.

## Extracción de imágenes

Antes de extraer, cree el directorio de assets y confirme que es el destino
correcto:

```powershell
$assets = "docs/slides/unidad01/public/assets"
New-Item -ItemType Directory -Force -Path $assets
Test-Path -LiteralPath $assets -PathType Container
```

Use `pdfimages` por página para que el nombre de salida preserve la página de
origen. El siguiente comando genera archivos como `slide-004-image-000.jpg`:

```powershell
$source = "01_Fundamentos/01_Fundamentos_Internet.pdf"
$assets = "docs/slides/unidad01/public/assets"

foreach ($page in 1..78) {
  $prefix = Join-Path $assets ("slide-{0:D3}-image" -f $page)
  pdfimages -f $page -l $page -j $source $prefix
  if ($LASTEXITCODE -ne 0) {
    throw "pdfimages falló en la página $page."
  }
}
```

`pdfimages -j` conserva los JPEG embebidos. Algunas imágenes transparentes
generan además una máscara PPM. Mantenga la máscara junto al JPEG mientras se
decide si se necesita componer un PNG derivado con una herramienta aprobada. No
elimine ni publique las imágenes ni sus derivados sin la revisión de licencia
correspondiente.

Después de extraer, reemplace los marcadores TODO por elementos `img` con texto
alternativo que describa la información visible. Compruebe que cada referencia
apunta a un archivo existente:

```powershell
$references = @(
  rg --only-matching 'src="/assets/[^"]+"' docs/slides/unidad01/slides.md |
    ForEach-Object { $_ -replace '^src="/assets/', '' -replace '"$', '' }
)

$references | ForEach-Object {
  $path = Join-Path "docs/slides/unidad01/public/assets" $_
  if (-not (Test-Path -LiteralPath $path)) {
    throw "Asset ausente: $_"
  }
}
```

## Previsualización y build

Ejecute Slidev desde el directorio de la unidad para que `public/assets/` sea el
directorio público de la presentación:

```powershell
Set-Location docs/slides/unidad01
npx slidev slides.md
```

Para construir la versión estática:

```powershell
npx slidev build slides.md
```

El directorio `dist/` es un artefacto generado y no sustituye la revisión de
licencias. No lo integre al sitio Jekyll mientras `slides/` permanezca excluido
del build público.

## Validación

Desde la raíz del repositorio, ejecute:

```powershell
npm run format:check
npm run lint:markdown
uv run python scripts/validate_resources.py
```

Verifique además que el número de comentarios de página coincide con el número
de páginas del PDF y que no falten ni se repitan números:

```powershell
$expected = 1..78
$found = @(
  rg --only-matching '^<!-- PDF página: [0-9]+ -->$' docs/slides/unidad01/slides.md |
    ForEach-Object { [int]($_ -replace '\D', '') }
)
$missing = @($expected | Where-Object { $_ -notin $found })
$duplicates = @($found | Group-Object | Where-Object Count -gt 1)

if ($found.Count -ne $expected.Count -or $missing.Count -gt 0 -or $duplicates.Count -gt 0) {
  throw "La numeración de las diapositivas no coincide con el PDF."
}
```

Registre en el `README.md` de assets de cada unidad el PDF de origen, el patrón
de nombres, las máscaras extraídas y las restricciones de reutilización.
