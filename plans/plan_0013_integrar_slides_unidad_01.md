# plan_0013 - Integrar la presentación de la Unidad 1 al sitio publicado

**Fecha**: 2026-08-06

**Ámbito**: `package.json`, `package-lock.json`, `docs/slides/unidad01/`,
`docs/slides/Readme.md`, `docs/unidades/01_web_git_publicacion.md`,
`docs/status.md`, `Dev.md`, `docs/governance/third-party.yml`,
`THIRD_PARTY_NOTICES.md`, `scripts/build_slides.py`,
`scripts/validate_slides.py`, `scripts/build_site.py`,
`scripts/assemble_site.py`, `playwright.slides.config.mjs`, `tests/slides/`,
`tests/validation/test_build_slides.py` y `.github/workflows/validate.yml`.

**Estado**: propuesto; no se ha iniciado la implementación.

**Prioridad**: alta. La presentación de la Unidad 1 está revisada localmente,
pero no forma parte del artefacto de GitHub Pages ni tiene una ruta pública
desde la guía docente.

Este ExecPlan es un documento vivo. Debe mantenerse conforme a `PLANS.md`,
`AGENTS.md`, `UPGRADE_PLAN.md` y `DESIGN.md`. `PLANS.md` está versionado en la
raíz del repositorio y define la estructura, actualización y evidencia exigidas
para este documento.

## Propósito / Panorama general

Después de este cambio, una persona podrá abrir la guía publicada de la Unidad 1
en `/unidades/01-web-git-publicacion/`, seguir un enlace textual llamado “Abrir
presentación de la Unidad 1” y llegar a una presentación Slidev servida en
`/presentaciones/unidad-01/`. La presentación mostrará sus diagramas propios,
las citas visibles y la bibliografía final tanto en una vista local como bajo el
prefijo de GitHub Pages, por ejemplo
`/cartografia_web/presentaciones/unidad-01/#/11`.

El cambio conserva la separación editorial actual: Jekyll seguirá generando la
documentación Markdown y Slidev seguirá generando la presentación. Jekyll no
leerá la fuente de Slidev; el ensamblador copiará únicamente el artefacto
estático construido. Así se evita publicar el directorio histórico de recursos y
se hace que el deck sea reproducible desde `npm ci`, sin depender del ejecutable
Slidev instalado globalmente en una máquina.

Una persona podrá demostrar el resultado con `npm run build`, comprobando que
`_site/presentaciones/unidad-01/index.html` existe, y con
`npm run test:slides:unidad01`, que abrirá el artículo y las diapositivas 11,
28, 29 y final bajo una ruta simulada de GitHub Pages. Las pruebas comprobarán
el enlace desde la guía, las citas visibles, los SVG propios y la ausencia de
errores de carga de recursos del deck.

## Progress

- [x] (2026-08-06 00:31Z) Se confirmó que `docs/_config.yml` excluye la fuente
      `docs/slides/` del build Jekyll y que `scripts/assemble_site.py` todavía
      no acepta ni copia artefactos de Slidev.
- [x] (2026-08-06 00:31Z) Se confirmó que
      `docs/unidades/01_web_git_publicacion.md` no enlaza la presentación y que
      el build local usa `slidev` instalado globalmente, sin `package.json` ni
      lockfile de Slidev versionados.
- [x] (2026-08-06 00:31Z) Se creó este ExecPlan con una ruta pública,
      dependencia fijada, interfaz de ensamblado, pruebas de prefijo y criterios
      de aceptación definidos.
- [x] (2026-08-06 00:36Z) Se creó el workspace privado de Slidev, se añadió la
      CLI 52.19.0 al lockfile y `npm ci` terminó correctamente después de
      detener el preview local que bloqueaba un binario de Rolldown.
- [x] (2026-08-06 00:36Z) El primer build del workspace falló al tratar rutas
      `./assets/generated/` como importaciones relativas al Markdown; se
      conservaron las URLs públicas `/assets/generated/` y el build con `--base`
      confirmó que Vite las prefija correctamente.
- [x] (2026-08-06 00:42Z) El build con rutas públicas y
      `--base /cartografia_web/presentaciones/unidad-01/` generó el SVG propio,
      excluyó la captura histórica y escribió las rutas publicadas en los
      módulos de Slidev.
- [x] (2026-08-06 00:49Z) La prueba Python de Slidev se ajustó para decodificar
      salida UTF-8 en Windows y pasó junto con la prueba del ensamblador.
- [x] (2026-08-06 00:55Z) Se integró el deck bajo `/presentaciones/unidad-01/`,
      se enlazó desde la Unidad 1 y se añadieron las cinco referencias
      científicas al artículo docente.
- [x] (2026-08-06 00:55Z) Pasaron el build final, los enlaces internos y las dos
      pruebas Playwright bajo `/cartografia_web`.
- [ ] Revisión manual pendiente: teclado, foco, reflow a 320 CSS px, zoom 200 %,
      lector de pantalla y Safari real sobre la presentación publicada.
- [x] (2026-08-06 01:00Z) Se creó el commit `a920a84` y se empujó `master` a
      `origin/master`; el repositorio local quedó sincronizado con el remoto.
- [ ] Confirmar desde GitHub Actions y GitHub Pages la ejecución remota y la
      ruta publicada. El entorno local no incluye `gh`, por lo que esta
      evidencia no se puede consultar desde la terminal actual.

## Surprises & Discoveries

- Observación: `docs/_config.yml` excluye `slides`, por lo que la fuente del
  deck no se publica accidentalmente con Jekyll. Esta exclusión es necesaria por
  la separación de recursos históricos, pero impide que el deck llegue al sitio
  sin una fase de ensamblado adicional. Evidencia: `docs/_config.yml:5-6`.

- Observación: el flujo de Pages construye Jekyll y copia Leaflet, MapLibre y
  activos cloud, pero no ejecuta `slidev build` ni tiene una entrada para un
  directorio de diapositivas ya construido. Evidencia:
  `.github/workflows/pages.yml:35-46` y `scripts/assemble_site.py:35-42`.

- Observación: la presentación se construye actualmente con un ejecutable global
  Slidev 52.19.0. La carpeta de la Unidad 1 contiene `node_modules/` ignorado,
  pero no contiene manifiesto ni lockfile; por tanto, un clon limpio no puede
  reproducir el build con una versión declarada. Evidencia:
  `docs/slides/unidad01/`, `package.json:5-8` y `slidev --version` devuelven
  52.19.0 desde una instalación global.

- Observación: `slidev build --help` admite `--base` y `--router-mode hash`.
  Estas opciones permiten alojar un deck en un subdirectorio, porque la ruta de
  la diapositiva queda después de `#` y no exige que el servidor conozca rutas
  como `/11`. Evidencia: salida local de `slidev build --help` el 2026-08-06.

- Observación: los SVG propios están versionados bajo
  `docs/slides/unidad01/public-generated/assets/generated/`; los recursos
  históricos no se sirven ni se copian al build actual. Evidencia:
  `docs/slides/unidad01/vite.config.mts` y
  `docs/slides/unidad01/public/assets/README.md`.

- Observación: en Slidev 52, una URL de imagen que comienza con `./` dentro del
  Markdown se convierte en una importación relativa al módulo virtual de la
  diapositiva. Ese módulo no está junto a `public-generated/`, por lo que 13 SVG
  propios fallaron con `UNRESOLVED_IMPORT`. Evidencia:
  `npm run validate:slides:unidad01` falló el 2026-08-06 al resolver
  `./assets/generated/cliente_servidor_mapa.svg` y otros 12 SVG.

- Observación: `npm ci` no pudo reemplazar inicialmente
  `rolldown-binding.win32-x64-msvc.node` porque el preview Slidev local lo tenía
  abierto. Tras detener el proceso del preview, instaló 873 paquetes y terminó
  correctamente. Evidencia: error `EPERM unlink` seguido de `added 873 packages`
  el 2026-08-06.

- Observación: el test Python que capturaba salida de Slidev falló en Windows
  aunque el proceso terminó correctamente, porque `subprocess` usó CP1252 para
  bytes UTF-8 producidos por la CLI. Evidencia: `UnicodeDecodeError` y
  `result.stdout is None` durante
  `uv run pytest tests/validation/test_build_slides.py` el 2026-08-06.

- Observación: Docker inicialmente no tenía daemon local, lo que bloqueó el
  build Jekyll y el recorrido Playwright del artefacto final. El daemon se
  inició después y las validaciones bloqueadas se repitieron correctamente.
  Evidencia: `docker version` devolvió primero que no existe la tubería
  `//./pipe/docker_engine` y luego informó versión 25.0.3 el 2026-08-06.

- Observación: después de iniciar Docker Desktop, `npm test`, el build Jekyll,
  el ensamblado, Linkinator y la prueba de integración publicada terminaron
  correctamente. El primer uso descargó la imagen Ruby fijada. Evidencia: Docker
  25.0.3 respondió y `npm test` informó 9 pruebas aprobadas;
  `npm run test:slides:unidad01` informó 2 pruebas aprobadas y
  `npm run links:internal` verificó 73 enlaces el 2026-08-06.

- Observación: la primera prueba Playwright publicada encontró correctamente el
  deck y sus SVG, pero no encontró la etiqueta esperada del enlace de la guía.
  Se corrigió el texto de enlace a “Abrir presentación de la Unidad 1”; la
  segunda ejecución aprobó ambas pruebas. Evidencia: el primer recorrido tuvo 1
  fallo por nombre accesible y el segundo informó `2 passed` el 2026-08-06.

- Observación: el servidor temporal `python -m http.server` registró algunos
  `ConnectionAbortedError` de Windows mientras Playwright cancelaba solicitudes
  concurrentes de módulos. Las respuestas requeridas fueron HTTP 200 y las
  pruebas no fallaron. Evidencia: logs del servidor durante
  `npm run test:slides:unidad01` y resultado final de 2 pruebas aprobadas el
  2026-08-06.

- Observación: el commit de integración se empujó correctamente, pero la CLI
  oficial `gh` no está instalada en este entorno para consultar estados de
  Actions o la URL de Pages. Evidencia: `git rev-parse HEAD` y
  `git rev-parse origin/master` devolvieron ambos
  `a920a84adc127ad757d6f5b49a212965a64bc19a`; `gh run list` devolvió que el
  comando no se reconoce el 2026-08-06.

## Decision Log

- Decisión: conservar `exclude: slides` en `docs/_config.yml` y publicar solo el
  resultado de Slidev en `/presentaciones/unidad-01/` mediante
  `scripts/assemble_site.py`. Justificación: la fuente de Slidev incluye
  directorios auxiliares de migración que no deben entrar al sitio Jekyll.
  Copiar una salida estática ya validada mantiene separadas las fuentes docentes
  y el artefacto público. Fecha/Autor: 2026-08-06 / OpenCode.

- Decisión: crear el workspace privado npm `@cartografia-web/slides-unidad01` en
  `docs/slides/unidad01/package.json` y fijar exactamente `@slidev/cli` en la
  versión `52.19.0`. Justificación: el repositorio ya utiliza un lockfile npm
  único y workspaces. Esta opción elimina la dependencia de la instalación
  global observada y hace que `npm ci` instale la misma CLI en CI y en un clon
  limpio. La versión se fija sin prefijos de rango para que el significado del
  build no cambie dentro de una cohorte. Fecha/Autor: 2026-08-06 / OpenCode.

- Decisión: publicar el deck con `routerMode: hash` y construirlo con el valor
  de `--base` calculado como `<baseurl>/presentaciones/unidad-01/`.
  Justificación: GitHub Pages puede servir el curso bajo un prefijo como
  `/cartografia_web`. El modo hash mantiene la navegación interna en el cliente;
  `--base` hace que scripts, estilos y archivos de Slidev se soliciten dentro de
  la ruta publicada y no desde la raíz del dominio. Fecha/Autor: 2026-08-06 /
  OpenCode.

- Decisión: conservar en `docs/slides/unidad01/slides.md` las URLs públicas
  `/assets/generated/<archivo>.svg` y comprobar que `slidev build --base` las
  reescribe bajo la ruta publicada. Justificación: Slidev 52 trata
  `./assets/...` como una importación relativa al módulo virtual de cada
  diapositiva y no puede resolverla desde `public-generated/`. Los assets
  declarados en `publicDir` deben conservar una URL pública; `--base` es el
  mecanismo de Vite que debe prefijarla al construir el artefacto. Fecha/Autor:
  2026-08-06 / OpenCode.

- Decisión: enlazar la presentación desde
  `docs/unidades/01_web_git_publicacion.md` usando
  `{{ '/presentaciones/unidad-01/' | relative_url }}` y mantener el enlace fuera
  de la navegación global. Justificación: la presentación complementa la guía y
  no reemplaza el artículo, la práctica ni los ejemplos. `relative_url` añade
  automáticamente el prefijo configurado; ubicar el enlace en la Unidad 1
  mantiene una ruta de aprendizaje clara sin añadir un destino desconectado en
  la portada. Fecha/Autor: 2026-08-06 / OpenCode.

- Decisión: repetir en el artículo las cinco referencias científicas ya visibles
  en el deck, con la misma lista de DOI y una breve explicación de su uso.
  Justificación: el artículo debe poder sostener por sí mismo las afirmaciones
  sobre conectividad, accesibilidad de mapas y geoprivacidad. La lista no cambia
  actividades, horas ni requisitos de la Unidad 1; documenta la procedencia de
  contenido ya incorporado. Fecha/Autor: 2026-08-06 / OpenCode.

- Decisión: añadir validación automatizada del artefacto bajo el prefijo
  `/cartografia_web`, además de la revisión manual de teclado, reflow y lector
  de pantalla. Justificación: un build que funciona en la raíz puede fallar en
  Pages por una ruta absoluta. Playwright verificará las rutas, citas y enlace
  reales; la revisión humana conservará la evidencia que Axe o una comprobación
  de carga no pueden probar. Fecha/Autor: 2026-08-06 / OpenCode.

- Decisión: dejar `.github/workflows/pages.yml` invocando solo
  `scripts/build_site.py` para construir y ensamblar el sitio. Justificación:
  `build_site.py` ya genera Jekyll, MapLibre, Slidev y llama a
  `assemble_site.py`; una segunda invocación del ensamblador duplicaba trabajo y
  podía ocultar qué interfaz produce el artefacto `_site`. Fecha/Autor:
  2026-08-06 / OpenCode.

## Outcomes & Retrospective

La integración técnica está completa y funciona en el artefacto estático local.
`@slidev/cli` 52.19.0 queda fijado en el workspace `docs/slides/unidad01/`,
instalado por `npm ci` y ejecutado por scripts Python, sin depender de la
instalación global. `scripts/build_slides.py` construye el deck con base
configurable y modo hash; verifica que exista un SVG propio y que no se publique
una captura histórica. `scripts/build_site.py` incorpora esa salida y
`scripts/assemble_site.py` la publica en `presentaciones/unidad-01/`.

La guía `docs/unidades/01_web_git_publicacion.md` enlaza el deck y replica las
cinco referencias científicas que sustentan conectividad, accesibilidad de mapas
29 y 37 bajo `/cartografia_web`; verifican citas, DOI y solicitudes de recursos
sin respuestas 4xx. La vista manual a 1280 por 720 confirmó composición sin
recortes para la guía, esas diapositivas y la bibliografía final.

Pasaron `npm run validate`, `npm test` con 9 pruebas, `npm run test:a11y` con 3
pruebas, `npm run test:slides:unidad01` con 2 pruebas, `npm run build`,
`npm run links:internal`, `uv run python scripts/validate_resources.py` y
`npm audit --omit=dev --audit-level=high`. La advertencia de chunk MapLibre por
encima de 500 kB permanece preexistente y no bloquea su build.

Este plan no puede declararse completamente cerrado: las tareas manuales de
accesibilidad y Safari real siguen pendientes en
`docs/governance/manual-accessibility-review.md`, y falta revisar la ejecución
real de GitHub Actions/Pages después del push. Se creó y empujó el commit
`a920a84`; no se crearon tags, releases ni despliegues manuales.

## Contexto y orientación

La raíz del repositorio es `C:\opt\work\personal\cartografia_web`. Todas las
rutas y comandos de este plan son relativos a esa raíz salvo que se indique otro
directorio. El curso usa Jekyll para convertir Markdown de `docs/` en páginas
HTML y usa `scripts/assemble_site.py` para copiar ejemplos aprobados a un único
árbol estático final. Ese árbol se llama artefacto estático: es el conjunto de
archivos que un servidor web puede entregar sin ejecutar una aplicación en el
servidor.

Slidev convierte `docs/slides/unidad01/slides.md` en una aplicación estática de
presentación. `docs/slides/unidad01/public-generated/` es su directorio público:
sus SVG propios se copian al build. `docs/slides/unidad01/public/` es material
histórico de migración y no debe reactivarse como directorio público. La
configuración `docs/slides/unidad01/vite.config.mts` ya selecciona
`public-generated/`.

Un workspace npm es un subproyecto declarado en el `package.json` raíz que
comparte el mismo `package-lock.json` y se instala con `npm ci`. Se creará un
workspace privado para el deck; privado significa que npm no podrá publicarlo
como paquete. Un lockfile registra las versiones exactas de todas las
dependencias resueltas.

`baseurl` es el prefijo donde se aloja el sitio. En producción de GitHub Pages,
el workflow recibe ese valor de `actions/configure-pages`; en la prueba local se
usará `/cartografia_web`. El argumento `--base` de Slidev debe recibir la ruta
completa del deck, por ejemplo `/cartografia_web/presentaciones/unidad-01/`. Una
URL de recurso público comienza con `/assets/`; Slidev la resuelve desde su
directorio público y Vite la reescribe con `--base` durante el build. El modo de
navegación hash representa una diapositiva como `#/11`, de modo que el servidor
siempre entrega `index.html` sin configurar rutas dinámicas.

El artículo docente mantenido es `docs/unidades/01_web_git_publicacion.md`.
Explica el producto de la unidad, HTML, CSS, módulos ES, HTTP, GeoJSON,
accesibilidad, Git y publicación. La presentación debe enlazarse como apoyo
visual inmediatamente después de los resultados de aprendizaje y conservar una
sección de fuentes que explique que sus cinco artículos científicos amplían,
pero no cambian, las prácticas obligatorias.

Los módulos actuales son los siguientes. `scripts/build_site.py` ejecuta el
build Jekyll y llama al ensamblador. `scripts/assemble_site.py` copia árboles
aprobados a la salida final. `.github/workflows/pages.yml` invoca
`scripts/build_site.py` para generar el artefacto de Pages.
`.github/workflows/validate.yml` ejecuta las comprobaciones locales equivalentes
en cada cambio. La configuración existente de Playwright,
`playwright.config.mjs`, sirve ejemplos Leaflet desde la raíz; la presentación
necesita una configuración separada porque debe probarse desde el artefacto
ensamblado bajo `/cartografia_web`.

## Plan de trabajo

### Hito 1: fijar Slidev y demostrar el build bajo un prefijo

Crear `docs/slides/unidad01/package.json` con el nombre privado
`@cartografia-web/slides-unidad01`, versión `0.1.0`, scripts `dev` y `build`, y
la dependencia de desarrollo exacta `@slidev/cli` versión `52.19.0`. El script
`dev` ejecutará `slidev slides.md`; el script `build` ejecutará
`slidev build slides.md`. No codificará directorio de salida ni prefijo: ambos
serán argumentos que la capa de Python suministrará para evitar que un build
local sobrescriba el artefacto de publicación.

Actualizar `package.json` raíz para incluir `docs/slides/unidad01` en
`workspaces`. Añadir scripts `build:slides:unidad01`, `validate:slides:unidad01`
y `test:slides:unidad01`; los dos primeros invocarán scripts Python nuevos y el
tercero construirá una vista previa con prefijo antes de ejecutar Playwright.
Regenerar `package-lock.json` con npm, sin editarlo a mano. `npm ci` debe
instalar la CLI sin requerir que exista `node_modules/` bajo la presentación.

Crear `scripts/build_slides.py`. El script recibirá `--baseurl` y `--output`.
Normalizará un `baseurl` vacío o iniciado por `/`, rechazará URLs completas,
consultas y fragmentos, y construirá la base final como
`<baseurl>/presentaciones/unidad-01/`. El script borrará solo el directorio
`--output` indicado, invocará desde la raíz:

    npm run --workspace @cartografia-web/slides-unidad01 build -- --out <salida> --base <base-final> --router-mode hash

Después comprobará que existen `<salida>/index.html` y
`<salida>/assets/generated/internet_web.svg`, y que no existe
`<salida>/assets/slide-001-image-000.jpg`. Si una condición falla, terminará con
código distinto de cero y un mensaje que nombre la ruta faltante o prohibida.

Crear `scripts/validate_slides.py`. Usará un directorio temporal del sistema,
invocará `build_slides.py` con `--baseurl /cartografia_web`, comprobará que el
HTML contiene la base publicada esperada y eliminará el directorio temporal aun
si falla la verificación. Esta validación no modificará archivos fuente ni
dejará artefactos persistentes.

En `docs/slides/unidad01/slides.md`, añadir `routerMode: hash` al front matter y
conservar cada `src="/assets/generated/<archivo>.svg"` como URL pública de
Slidev. Mantener los textos alternativos, los SVG propios y las citas
existentes. Construir primero una salida temporal con `/cartografia_web` y
servirla por HTTP para demostrar que las rutas de los SVG y la navegación a
`#/11` funcionan antes de integrar el deck al sitio completo.

Registrar Slidev CLI en `docs/governance/third-party.yml` con versión 52.19.0,
fuente en el manifiesto y lockfile de la Unidad 1, licencia MIT, tipo “generador
de presentación estática” y uso “compilar la presentación pública de la Unidad
1”. Añadir un aviso equivalente y conciso a `THIRD_PARTY_NOTICES.md`. No añadir
recursos de terceros ni capturas históricas a `public-generated/`.

Este hito se acepta cuando `npm ci` seguido de
`npm run validate:slides:unidad01` funciona sin CLI global, y una solicitud a
`http://localhost:8011/cartografia_web/presentaciones/unidad-01/#/11` devuelve
la diapositiva con `connectividad_2025.svg` sin solicitudes 404. Si `--base` no
produce la ruta correcta durante el prototipo, el único ajuste permitido será
añadir `base: process.env.SLIDEV_BASE` a `docs/slides/unidad01/vite.config.mts`
y hacer que `build_slides.py` defina esa variable al invocar npm; no se
habilitará `public/` ni se convertirán los SVG en importaciones relativas.

### Hito 2: ensamblar el deck en el artefacto estático de Pages

Ampliar `scripts/assemble_site.py` con el argumento opcional `--slides-dir`.
Cuando reciba un directorio existente de Slidev, copiará su contenido a
`<output>/presentaciones/unidad-01/`. Rechazará un argumento que no sea
directorio y conservará el comportamiento actual cuando se omita. La ruta de
destino será fija porque representa el contrato público enlazado desde la Unidad
1; no añadir una opción que permita publicarlo accidentalmente en otra ruta.

Modificar `scripts/build_site.py` para invocar `scripts/build_slides.py` después
del build Jekyll y antes del ensamblado. Usará
`<directorio-padre-de-output>/_site_slides` como salida intermedia, pasará el
mismo `--baseurl` recibido por Jekyll y añadirá
`--slides-dir <salida-intermedia>` a la llamada de `assemble_site.py`. El patrón
`_site_*` ya está ignorado por Git. El script conservará las salidas actuales de
Jekyll, Leaflet, MapLibre y activos cloud; no cambiará sus rutas públicas.

Mantener `docs/_config.yml` con `exclude: slides`. Actualizar
`docs/slides/Readme.md` para explicar que esa exclusión aplica a la fuente, no
al artefacto generado: `npm run build:slides:unidad01` producirá una salida
local ignorada y `npm run build` la copiará a la ruta pública mediante el
ensamblador. Retirar de esa guía la instrucción de ejecutar `npm init -y` o
instalar Slidev de forma aislada, y sustituirla por `npm ci` desde la raíz y los
scripts del workspace.

Este hito se acepta cuando `npm run build` crea
`_site/presentaciones/unidad-01/index.html`, conserva los SVG en
`_site/presentaciones/unidad-01/assets/generated/` y no crea
`_site/presentaciones/unidad-01/assets/slide-001-image-000.jpg`. La misma
comprobación con `--baseurl /cartografia_web` debe crear
`.preview/cartografia_web/presentaciones/unidad-01/index.html` y cargar
correctamente `#/11`, `#/31`, `#/32` y `#/37` al servirse por HTTP.

### Hito 3: enlazar el artículo y mantener las fuentes científicas

En `docs/unidades/01_web_git_publicacion.md`, insertar después de “Resultados de
aprendizaje” la sección “Presentación de apoyo”. Debe contener un enlace textual
`Abrir presentación de la Unidad 1` hacia
`{{ '/presentaciones/unidad-01/' | relative_url }}` y una frase que indique que
la presentación resume visualmente la misma ruta de HTML, HTTP, GeoJSON,
accesibilidad, privacidad y publicación; no reemplaza la práctica guiada ni el
mapa Leaflet.

Añadir una sección breve llamada “Evidencia científica para decisiones de
diseño” cerca de “Arquitectura de una publicación cartográfica”. Explicará que
la conectividad no equivale solo a cobertura, que WCAG necesita alternativas
específicas para mapas y que la minimización espacial puede afectar patrones
locales. No añadirá ejercicios de rendimiento, geomasking ni cartografía
temática avanzada a la Unidad 1; remitirán a unidades posteriores cuando sea
necesario.

Al final de la guía, antes de “Errores frecuentes”, añadir “Referencias
científicas de apoyo” con exactamente estas cinco referencias completas y DOI,
en el mismo orden que la diapositiva final:

1. Gozzi, N., Comini, N., y Perra, N. (2024). _Bridging the Digital Divide:
   Mapping Internet Connectivity Evolution, Inequalities, and Resilience in Six
   Brazilian Cities_. _EPJ Data Science_, 13.
   [https://doi.org/10.1140/epjds/s13688-024-00508-8](https://doi.org/10.1140/epjds/s13688-024-00508-8)
2. Li, H., Huang, J., y Kwan, M.-P. (2025). _Challenges in Geoprivacy
   Protection: Methodological Issues, Cultural and Regulatory Contexts, and
   Public Attitudes_. _Transactions in GIS_, 29(4), e70075.
   [https://doi.org/10.1111/tgis.70075](https://doi.org/10.1111/tgis.70075)
3. Manu, S. D., Burghardt, D., y Hauthal, E. (2025). _Enhancing Accessibility of
   Thematic Web Maps for Visually Impaired Users_. _KN - Journal of Cartography
   and Geographic Information_, 75(2), 107-121.
   [https://doi.org/10.1007/s42489-025-00189-x](https://doi.org/10.1007/s42489-025-00189-x)
4. Raihan, M. M. H. et al. (2024). _Dimensions and Barriers for Digital
   (In)equity and Digital Divide: A Systematic Integrative Review_. _Digital
   Transformation and Society_, 4(2), 111-127.
   [https://doi.org/10.1108/DTS-04-2024-0054](https://doi.org/10.1108/DTS-04-2024-0054)
5. Tiwari, A. et al. (2023). _Exploring Geomasking Methods for Geoprivacy: A
   Pilot Study in an Environment with Built Features_. _Geospatial Health_,
   18(2).
   [https://doi.org/10.4081/gh.2023.1205](https://doi.org/10.4081/gh.2023.1205)

Actualizar `docs/status.md` para señalar que la presentación de la Unidad 1 se
publica como artefacto estático complementario. No declarará conformidad WCAG
completa; conservará las limitaciones de revisión manual y Safari ya
registradas.

Actualizar `Dev.md` para documentar `npm run build:slides:unidad01`,
`npm run validate:slides:unidad01` y `npm run test:slides:unidad01`, incluido
que la última prueba requiere Docker disponible porque construye Jekyll bajo un
prefijo simulado antes de ejecutar Playwright.

Este hito se acepta cuando el artículo publicado contiene el enlace y las cinco
referencias, el enlace se resuelve bajo ambos `baseurl`, y ninguna referencia
externa se convierte en dependencia de ejecución de la práctica.

### Hito 4: automatizar la integración, revisar la accesibilidad y publicar

Crear `playwright.slides.config.mjs` con `testDir: 'tests/slides'`, servidor
local en el puerto 8011 para `.preview/` y `baseURL`
`http://127.0.0.1:8011/cartografia_web`. Crear `tests/slides/unidad01.spec.mjs`.
Antes de Playwright, el script `test:slides:unidad01` construirá
`_site_preview_jekyll` con `scripts/build_site.py --baseurl /cartografia_web`;
el servidor de Playwright entregará `.preview/` sin reconstruir fuentes.

La prueba debe comprobar que la guía en
`/cartografia_web/unidades/01-web-git-publicacion/` contiene el enlace con la
ruta publicada. Debe abrir el deck en `#/11`, `#/31`, `#/32` y `#/37`, confirmar
los encabezados y las citas autor-fecha visibles, comprobar que la diapositiva
final muestra los cinco DOI y registrar cualquier respuesta 404 de rutas bajo
`/cartografia_web/presentaciones/unidad-01/` como fallo. También comprobará que
el `src` resuelto de un diagrama propio empieza por
`/cartografia_web/presentaciones/unidad-01/assets/generated/`, no por
`/assets/generated/`.

Crear `tests/validation/test_build_slides.py` para ejecutar
`scripts/validate_slides.py` desde un directorio temporal y esperar código cero.
La prueba cubre que la CLI fijada construye, que el prefijo está presente en el
HTML, que se entrega un SVG propio y que una captura histórica no se entrega.

Ampliar `.github/workflows/validate.yml`: después de instalar Chromium, ejecutar
`npm run test:slides:unidad01`; el paso debe quedar antes de “Build approved
static site” porque ya construye y prueba la variante con prefijo. Mantener los
permisos de solo lectura, las acciones fijadas por SHA y la separación actual
entre validación y despliegue. No cambiar `.github/workflows/pages.yml` salvo
que el nuevo `scripts/build_site.py` requiera argumentos adicionales; el
workflow actual debe publicar el deck automáticamente al usar el script
actualizado.

Ampliar `docs/governance/manual-accessibility-review.md` con una sección para la
presentación. La revisión manual pendiente debe incluir abrir el enlace desde la
Unidad 1, avanzar y retroceder con teclado, comprobar foco visible, reflow a 320
CSS px, zoom de navegador al 200 %, lectura de las citas y bibliografía, y
anunciar cualquier limitación de Slidev con lector de pantalla. No marcar esas
casillas como completadas sin fecha, navegador, evidencia y persona responsable.

Este hito se acepta cuando el workflow de validación ejecuta la prueba del deck,
el workflow de Pages produce la ruta pública, Linkinator no informa enlaces
internos rotos después de `npm run build`, y la revisión manual conserva un
estado honesto de lo que aún necesita evidencia.

## Pasos concretos

Desde `C:\opt\work\personal\cartografia_web`, antes de editar, comprobar que el
estado de Git no contiene cambios ajenos sin entender:

    git status --short
    git diff --check

Crear el manifiesto del workspace, añadirlo al arreglo `workspaces` de
`package.json`, fijar la dependencia y regenerar el lockfile:

    npm install --workspace @cartografia-web/slides-unidad01 --save-dev @slidev/cli@52.19.0
    npm ci
    npm run --workspace @cartografia-web/slides-unidad01 build -- --out C:\Users\<usuario>\AppData\Local\Temp\cartografia-web-slides --base /cartografia_web/presentaciones/unidad-01/ --router-mode hash

La última orden debe terminar con `built in ...`. La salida debe contener
`index.html` y `assets/generated/internet_web.svg`. No debe contener una ruta
`assets/slide-001-image-000.jpg`.

Durante el Hito 2, ejecutar desde la raíz:

    uv run python scripts/build_slides.py --baseurl /cartografia_web --output _site_slides
    uv run python scripts/build_site.py --baseurl /cartografia_web --output _site_preview_jekyll
    Test-Path .preview\cartografia_web\presentaciones\unidad-01\index.html

La última orden debe imprimir `True`. Para inspección manual, iniciar un
servidor desde la raíz:

    python -m http.server 8011 --directory .preview

Abrir `http://localhost:8011/cartografia_web/unidades/01-web-git-publicacion/`,
activar el enlace “Abrir presentación de la Unidad 1” y confirmar que abre
`http://localhost:8011/cartografia_web/presentaciones/unidad-01/#/`. Navegar a
`#/11`, `#/31`, `#/32` y `#/37`; comprobar los diagramas, citas y referencias.
Detener el servidor con Ctrl+C.

Después de implementar todos los hitos, ejecutar desde la raíz:

    npm run format:check
    npm run lint
    npm run validate:slides:unidad01
    npm test
    npm run test:a11y
    npm run test:slides:unidad01
    npm run build
    npm run links:internal
    uv run python scripts/validate_resources.py
    git diff --check

`npm run test:slides:unidad01` requiere Docker disponible para Jekyll y Chromium
instalado para Playwright. Si Docker no está activo, no se declarará la
integración completa: se podrá ejecutar `npm run validate:slides:unidad01` y se
registrará el bloqueo exacto antes de reintentar. En CI, el runner Ubuntu debe
ejecutar el recorrido completo.

## Validación y aceptación

La implementación se acepta cuando una persona con un clon limpio puede ejecutar
`npm ci` y `uv sync --frozen`, sin instalar Slidev globalmente, y observa todos
estos comportamientos:

- `npm run validate:slides:unidad01` termina correctamente y elimina su salida
  temporal.
- `npm run build` crea el archivo `_site/presentaciones/unidad-01/index.html`
  junto con los SVG bajo `_site/presentaciones/unidad-01/assets/generated/`.
- Una versión con `--baseurl /cartografia_web` entrega la guía en
  `/cartografia_web/unidades/01-web-git-publicacion/` y el deck en
  `/cartografia_web/presentaciones/unidad-01/#/` sin recursos 404.
- La guía contiene un enlace textual hacia el deck y las cinco referencias
  científicas; el deck muestra citas autor-fecha en las diapositivas 11, 28 y 29
  y la lista completa de DOI al final.
- `npm run test:slides:unidad01` termina con todas las pruebas de
  `tests/slides/unidad01.spec.mjs` aprobadas. Cada prueba debe fallar antes de
  la integración por falta de ruta, enlace o cita visible, y pasar después.
- `npm run links:internal` no informa enlaces internos rotos en el artefacto que
  incluye la presentación.
- La revisión manual de la presentación queda documentada con resultado real;
  una casilla pendiente sigue pendiente si no se realizó la prueba en el
  navegador, dispositivo o lector de pantalla indicado.

## Idempotencia y recuperación

`scripts/build_slides.py` puede ejecutarse repetidamente porque borra solo el
directorio entregado por `--output` antes de reconstruirlo. El directorio debe
ser una ruta de salida ignorada, como `_site_slides`, o una ruta temporal; nunca
debe apuntar a `docs/slides/unidad01/public-generated/`, `docs/` ni `examples/`.
`scripts/validate_slides.py` usa un directorio temporal y lo limpia al terminar.
`scripts/assemble_site.py` ya reconstruye su salida completa, por lo que volver
a ejecutar `npm run build` no acumula versiones antiguas del deck.

Si el prototipo bajo `/cartografia_web` encuentra recursos 404, no publicar el
deck. Confirmar primero que los `src` de SVG conservan la URL pública
`/assets/generated/` y que `build_slides.py` pasa
`--base /cartografia_web/presentaciones/unidad-01/`. Si la CLI no aplica
`--base`, activar la alternativa limitada definida en el Hito 1 mediante
`SLIDEV_BASE` en `vite.config.mts`; volver a ejecutar el prototipo antes de
tocar el ensamblador.

Si `npm ci` no instala el workspace, comprobar que la ruta
`docs/slides/unidad01` figura tanto en `package.json` como en
`package-lock.json`. Regenerar el lockfile con la versión exacta de Slidev,
revisar el diff y no copiar `node_modules/` al repositorio. Si la prueba de
integración falla por Docker apagado, iniciar Docker o ejecutar el mismo comando
en CI; no simular un build Jekyll ni declarar el deck publicado sin el artefacto
real.

Si se necesita revertir la publicación antes del despliegue, retirar el enlace
de la guía y el argumento `--slides-dir` del ensamblador en un commit separado,
conservar la fuente del deck excluida por Jekyll y ejecutar `npm run build` más
`npm run links:internal`. No eliminar los SVG propios ni restaurar capturas
históricas como parte de la reversión.

## Artefactos y notas

La interfaz observable del build de la presentación debe ser equivalente a esta
transcripción:

    > uv run python scripts/build_slides.py --baseurl /cartografia_web --output _site_slides
    Built slides to ...\_site_slides
    Verified index.html and assets/generated/internet_web.svg

La estructura final esperada del artefacto de Pages es:

    _site/
      unidades/
        01-web-git-publicacion/
          index.html
      presentaciones/
        unidad-01/
          index.html
          assets/
            generated/
              internet_web.svg

La siguiente solicitud debe devolver HTTP 200 y una página con el título de la
diapositiva de conectividad, no una página 404 del servidor estático:

    GET /cartografia_web/presentaciones/unidad-01/#/11

El fragmento `#/11` no llega al servidor; el navegador solicita
`/cartografia_web/presentaciones/unidad-01/` y Slidev selecciona la
diapositiva 11. Esta distinción explica por qué el modo hash es apropiado para
hosting estático sin reglas de reescritura de rutas.

## Interfaces y dependencias

`docs/slides/unidad01/package.json` debe exponer los scripts `dev` y `build` y
declarar la dependencia de desarrollo exacta `@slidev/cli: 52.19.0`.
`package.json` raíz debe declarar el workspace y exponer
`build:slides:unidad01`, `validate:slides:unidad01` y `test:slides:unidad01`.
Los scripts no deben usar rutas de perfil de usuario ni el ejecutable global
`slidev`.

`scripts/build_slides.py` debe aceptar:

    --baseurl <cadena vacía o prefijo que comienza por />
    --output <directorio de salida>

Debe devolver cero solo si Slidev termina correctamente, `index.html` existe, un
SVG propio requerido existe y una captura histórica prohibida no existe.
`scripts/validate_slides.py` no recibe argumentos obligatorios y debe devolver
cero solo si el build temporal bajo `/cartografia_web` cumple las mismas
condiciones y contiene la base esperada.

`scripts/assemble_site.py` debe aceptar `--slides-dir <directorio>` como
argumento opcional. Su contrato público es copiar ese directorio exactamente a
`presentaciones/unidad-01/` dentro de `--output`. `scripts/build_site.py` debe
construir y pasar ese directorio automáticamente. `playwright.slides.config.mjs`
debe servir `.preview/` en el puerto 8011 y `tests/slides/unidad01.spec.mjs`
debe usar el prefijo `/cartografia_web`.

La única nueva dependencia es Slidev CLI. Debe constar en
`docs/governance/third-party.yml` y `THIRD_PARTY_NOTICES.md` con versión,
licencia, origen y uso. No se agregan cuentas SaaS, secretos, tokens, recursos
históricos ni servicios remotos obligatorios.

## Revisión

2026-08-06: plan creado después de comprobar que la presentación de la Unidad 1
funciona y fue revisada localmente, pero está excluida de Jekyll, no tiene
manifiesto npm reproducible, no se ensambla en Pages y no se enlaza desde la
guía docente. La revisión decide publicar un artefacto Slidev separado bajo
`/presentaciones/unidad-01/`, mantener la fuente excluida, usar un workspace npm
con versión exacta, verificar el prefijo de Pages y mantener la evidencia
científica sincronizada entre la guía y las diapositivas.

2026-08-06: se implementó y validó la integración técnica. Un intento inicial de
usar URLs relativas para SVG falló por la resolución de módulos virtuales de
Slidev; se conservaron las URLs públicas y `--base` las prefijó correctamente.
Se corrigieron la decodificación UTF-8 de la prueba Python y la etiqueta del
enlace docente. El artefacto, los enlaces y las pruebas publicadas pasan; quedan
pendientes la revisión manual, Safari real y el despliegue de Pages tras un push
autorizado.

2026-08-06: con autorización explícita, se creó y empujó `a920a84` a
`origin/master`. La evidencia de CI y Pages continúa pendiente porque `gh` no
está disponible en el entorno local; el estado remoto debe revisarse desde
GitHub Actions o una terminal con esa CLI.
