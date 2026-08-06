# Generación de presentaciones Slidev

Este directorio conserva presentaciones Slidev creadas durante la migración de
los PDF docentes. Los PDF históricos son fuentes de consulta y reconstrucción;
las presentaciones mantenidas pueden condensar su contenido y deben declarar qué
material histórico se conserva, reemplaza o excluye.

Las capturas extraídas de PDF solo se usan temporalmente durante una revisión de
migración. No se versionan en el repositorio ni se publican hasta resolver su
procedencia, licencia, texto alternativo y utilidad pedagógica.

## Alcance y publicación

`docs/_config.yml` excluye `slides/` del build Jekyll. En la Unidad 1,
`vite.config.mts` sirve solo `public-generated/`; las capturas históricas no se
copian a la previsualización ni al build de Slidev. El ensamblador del sitio
copia únicamente la salida validada de Slidev a `/presentaciones/unidad-01/`. No
elimine esas exclusiones ni publique recursos extraídos hasta revisar su
procedencia, licencia y texto alternativo.

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
       public-generated/
         assets/
           generated/
             internet_web.svg
```

`slides.md` usa el tema `default` de Slidev. Una reconstrucción histórica puede
usar comentarios `<!-- PDF página: N -->`; una presentación mantenida documenta
sus revisiones con comentarios que no impliquen una correspondencia uno a uno
con el PDF. En la Unidad 1, los diagramas propios se sirven desde
`public-generated/assets/generated/`, por ejemplo:

```html
<img
  src="/assets/generated/internet_web.svg"
  alt="Diagrama que diferencia Internet de la Web."
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

Slidev es un workspace npm fijado en `docs/slides/unidad01/`. Desde la raíz,
instale todas las dependencias con:

```powershell
npm ci
```

El `package-lock.json` de la raíz registra esa dependencia. No use una CLI
Slidev instalada globalmente para validar o publicar la presentación.

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

Antes de extraer, cree un directorio temporal fuera del repositorio y confirme
que es el destino correcto:

```powershell
$assets = Join-Path $env:TEMP "cartografia-web-unidad01-assets"
New-Item -ItemType Directory -Force -Path $assets
Test-Path -LiteralPath $assets -PathType Container
```

Use `pdfimages` por página para que el nombre de salida preserve la página de
origen. El siguiente comando genera archivos como `slide-004-image-000.jpg`:

```powershell
$source = "01_Fundamentos/01_Fundamentos_Internet.pdf"
$assets = Join-Path $env:TEMP "cartografia-web-unidad01-assets"

foreach ($page in 1..78) {
  $prefix = Join-Path $assets ("slide-{0:D3}-image" -f $page)
  pdfimages -f $page -l $page -j $source $prefix
  if ($LASTEXITCODE -ne 0) {
    throw "pdfimages falló en la página $page."
  }
}
```

`pdfimages -j` conserva los JPEG embebidos. Algunas imágenes transparentes
generan además una máscara PPM. Mantenga la máscara junto al JPEG solo durante
la revisión necesaria para decidir si se requiere un derivado aprobado. Elimine
la extracción temporal al terminar y no publique imágenes ni derivados sin la
revisión de licencia correspondiente.

Después de extraer, no enlace directamente la captura temporal. Solo un recurso
con procedencia, licencia, texto alternativo y utilidad pedagógica documentados
puede convertirse en un asset mantenido. Compruebe sus referencias antes de
publicar:

```powershell
$references = @(
  rg --only-matching 'src="/assets/generated/[^"]+"' docs/slides/unidad01/slides.md |
    ForEach-Object { $_ -replace '^src="/assets/generated/', '' -replace '"$', '' }
)

$references | ForEach-Object {
  $path = Join-Path "docs/slides/unidad01/public-generated/assets/generated" $_
  if (-not (Test-Path -LiteralPath $path)) {
    throw "Asset ausente: $_"
  }
}
```

## Previsualización y build

Para previsualizar el deck desde el directorio de la unidad, ejecute el script
del workspace. En la Unidad 1, `vite.config.mts` configura `public-generated/`
como directorio público:

```powershell
npm run --workspace @cartografia-web/slides-unidad01 dev
```

Para construir la versión estática:

```powershell
npm run build:slides:unidad01
```

`_site_slides/` es un artefacto generado e ignorado por Git y no sustituye la
revisión de licencias. `npm run build` construye la misma salida y la integra al
artefacto público bajo `/presentaciones/unidad-01/`, mientras la fuente de
`slides/` permanece excluida de Jekyll.

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

Registre en el `README.md` de assets de cada unidad el PDF de origen, la
decisión de conservar o eliminar las extracciones temporales y las restricciones
de reutilización.
