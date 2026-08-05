# plan_0012 - Cerrar vacíos de la Unidad 1

**Fecha**: 2026-08-05

**Ámbito**: `docs/slides/unidad01/`, `docs/unidades/01_web_git_publicacion.md`,
`docs/unidades/02_datos_calidad.md`,
`docs/unidades/04_apis_interoperabilidad.md`, `examples/leaflet/`,
`tests/a11y/leaflet.spec.mjs` y `package.json`.

**Estado**: cerrado técnicamente; el build completo del sitio queda bloqueado
por el daemon Docker local, ajeno a este cambio.

**Prioridad**: alta; la Unidad 1 debe permitir construir una página mínima antes
de inspeccionar el mapa, demostrar módulos ES y no publicar recursos históricos
con licencia pendiente.

Este ExecPlan es un documento vivo. Debe mantenerse conforme a `PLANS.md`,
`AGENTS.md`, `UPGRADE_PLAN.md` y `DESIGN.md`.

## Propósito / Panorama general

Después de este cambio, una persona podrá construir y servir una página web
mínima accesible, comprobar que un módulo ES actualiza una región de estado y
después continuar hacia el mapa Leaflet. La presentación hará visible esa
progresión, la actividad Markdown y el destino de los contenidos históricos sin
reintroducir catálogos de productos ni ampliar las cuatro horas presenciales.

Además, los diagramas propios de Slidev se servirán desde un directorio público
separado. Las imágenes extraídas del PDF histórico permanecerán disponibles para
la migración en el árbol de trabajo, pero no podrán aparecer en una
previsualización ni en un build de la presentación. El resultado se comprobará
construyendo un sitio Slidev aislado y verificando las rutas de un diagrama
propio y de una captura histórica.

## Progress

- [x] (2026-08-05 20:25Z) Se compararon las 78 páginas históricas con las 36
      diapositivas actuales, la guía de Unidad 1 y el programa vigente.
- [x] (2026-08-05 20:25Z) Se identificaron los vacíos que requieren cambio:
      página mínima construible, módulos ES demostrables, Markdown visible,
      hipertexto y arquitectura, destinos de formatos históricos y aislamiento
      de assets históricos.
- [x] (2026-08-05 20:25Z) Se creó este ExecPlan con decisiones, validación y
      recuperación definidas antes de editar los materiales.
- [x] (2026-08-05 20:29Z) Se implementó la página mínima, se convirtió el
      ejemplo Leaflet en módulo ES y se amplió la prueba de accesibilidad.
- [x] (2026-08-05 20:29Z) Se reescribieron las diapositivas y guías para mostrar
      la progresión práctica y los destinos curriculares de compatibilidad.
- [x] (2026-08-05 20:42Z) Se separaron los assets públicos de Slidev. Un build
      aislado contiene el SVG propio y no contiene la captura histórica.
- [x] (2026-08-05 20:45Z) Pasaron formato, lint, currículo, inventario,
      accesibilidad, revisión visual individual, build Slidev y
      `git diff     --check`.
- [x] (2026-08-05 20:45Z) Se intentó `npm run build`; MapLibre construyó
      correctamente, pero Docker no está disponible para la preparación
      posterior de activos. El bloqueo se documenta como limitación del entorno.

## Surprises & Discoveries

- Observación: la guía de Unidad 1 ya conserva Markdown y un panorama de
  XML/GML/KML/RPC/SOAP, pero la presentación no los hace visibles en su práctica
  ni precisa el destino de ESRI JSON. Evidencia:
  `docs/unidades/01_web_git_publicacion.md:221-253` frente a
  `docs/slides/unidad01/slides.md:662-704`.

- Observación: el deck afirma usar JavaScript modular, mientras
  `examples/leaflet/mapa_basico/index.html` carga `main.js` sin `type="module"`
  y `main.js` no tiene dependencias explícitas. Evidencia:
  `docs/slides/unidad01/slides.md:159-164`,
  `examples/leaflet/mapa_basico/index.html:66-67` y
  `examples/leaflet/mapa_basico/main.js:1-65`.

- Observación: Slidev publica por convención el contenido de su directorio
  `public/`. Las capturas históricas con licencia pendiente están bajo
  `docs/slides/unidad01/public/assets/`, aunque el deck no las referencia.
  Evidencia: `docs/slides/unidad01/public/assets/README.md:3-20` y la
  documentación de Slidev 52 sobre `public/` y `publicDir`.

- Observación: el ejemplo Leaflet conserva su comportamiento al cargarse como
  módulo ES y la página mínima puede probar una importación local sin servidor
  ni dependencia adicional. Evidencia: `npm run test:a11y` terminó con tres
  pruebas aprobadas el 2026-08-05; las solicitudes de `main.js` y `status.js`
  devolvieron HTTP 200.

- Observación: Vite advierte sobre una configuración TypeScript cargada como
  CommonJS cuando el archivo se llama `vite.config.ts`. El mismo contenido en
  `vite.config.mts` elimina esa advertencia. Evidencia: el primer build emitió
  la advertencia de `configLoader: 'native'`; `slidev build` posterior con
  `vite.config.mts` terminó sin ella.

- Observación: `npm run build` completa el build de la aplicación MapLibre y
  luego falla al invocar Docker para preparar activos COG. Evidencia:
  `docker: error during connect ... docker_engine ... The system cannot find the file specified`
  el 2026-08-05.

## Decision Log

- Decisión: sustituir la diapositiva de actividad digital por minuto por una
  página mínima construible, en lugar de aumentar el número de diapositivas.
  Justificación: la conectividad global ya aporta el contexto necesario; la
  actividad digital no inicia una acción verificable y compite con una unidad de
  cuatro horas. Fecha/Autor: 2026-08-05 / OpenCode.

- Decisión: crear `examples/leaflet/pagina_minima/` y usar `type="module"` con
  una importación local explícita en ese ejemplo y en el mapa Leaflet.
  Justificación: un módulo ES es un archivo JavaScript cargado como módulo cuyas
  dependencias se declaran con `import`. Una página mínima reduce la distancia
  entre concepto y mapa; importar una función de estado demuestra el contrato
  sin añadir frameworks ni dependencias. Fecha/Autor: 2026-08-05 / OpenCode.

- Decisión: aclarar GML, KML, ESRI JSON, RPC y SOAP en las guías de Unidades 2 y
  4 como compatibilidad o panorama, no como práctica obligatoria de Unidad 1.
  Justificación: el programa asigna formatos, contratos y APIs a unidades
  posteriores; nombrar el destino evita un traslado implícito inexistente sin
  ensanchar el núcleo. Fecha/Autor: 2026-08-05 / OpenCode.

- Decisión: conservar los assets históricos donde están y configurar
  `public-generated/` como único directorio público de Slidev. Los diagramas
  propios se moverán allí sin modificar sus URLs públicas `/assets/generated/`.
  Justificación: borrar o mover masivamente recursos de migración requiere una
  decisión separada. `publicDir` evita su exposición tanto durante desarrollo
  como en builds estáticos y mantiene una recuperación simple. Fecha/Autor:
  2026-08-05 / OpenCode.

- Decisión: mantener `actividad_digital_2025.svg` como diagrama propio en el
  directorio público aislado aunque la diapositiva de actividad se sustituya.
  Justificación: no es un recurso histórico ni sensible; conservarlo evita
  borrar un artefacto con procedencia documentada y permite reutilizarlo solo si
  una cohorte futura le asigna una actividad verificable. Fecha/Autor:
  2026-08-05 / OpenCode.

- Decisión: usar `vite.config.mts` en vez de `vite.config.ts`. Justificación: el
  repositorio no declara módulos ESM en el `package.json` más cercano. La
  extensión `.mts` mantiene `defineConfig` y `publicDir` sin la advertencia de
  compatibilidad futura de Vite. Fecha/Autor: 2026-08-05 / OpenCode.

## Outcomes & Retrospective

La Unidad 1 ahora empieza con `examples/leaflet/pagina_minima/`, una página
semántica que actualiza una región de estado mediante una importación ES. El
mapa Leaflet conserva su comportamiento, pero ahora también carga `main.js` como
módulo e importa el mismo contrato de estado. Tres pruebas Playwright confirman
el mapa, su error de red y la página mínima sin violaciones Axe.

La presentación reemplazó una cifra digital decorativa por la práctica
construible, añadió hipertexto, distinguió responsabilidades de servidores e
incluyó Markdown y las transferencias de compatibilidad en su guion. Las guías
de Unidades 2 y 4 nombran GML, KML, ESRI JSON, RPC y SOAP sin ampliar el núcleo
obligatorio. El inventario registra los cuatro archivos nuevos de la página
mínima.

`public-generated/` es el único directorio público de Slidev. El build aislado
de
`C:\Users\juanm\AppData\Local\Temp\opencode\slides-unidad01-final-gaps-20260805`
contiene `assets/generated/connectividad_2025.svg` y no contiene
`assets/slide-001-image-000.jpg`. Las capturas históricas continúan en el árbol
de migración y no se eliminaron.

Pasaron `npm run format:check`, `npm run lint`, `npm run test:a11y`,
`npm run validate:curriculum`, `uv run python scripts/validate_resources.py`,
`npx stylelint "docs/slides/unidad01/style.css"`, `slidev build` y
`git diff --check`. `npm run build` permanece bloqueado por un daemon Docker
apagado tras completar el build de MapLibre; no se inició Docker ni se cambió la
infraestructura para evitar una operación ajena al alcance.

## Contexto y orientación

`01_Fundamentos/01_Fundamentos_Internet.pdf` y la versión histórica de
`docs/slides/unidad01/slides.md` contienen 78 páginas. Son fuentes históricas,
no material público mantenido: incluyen capturas, cuentas, enlaces HTTP y
tecnologías sin licencia, seguridad o actualidad confirmadas. La presentación
actual `docs/slides/unidad01/slides.md` usa 36 diapositivas Slidev y diagramas
propios. Su finalidad es que el alumnado termine con un mapa Leaflet local.

Una página mínima es un pequeño sitio con HTML semántico, CSS y JavaScript
separados. El HTML describe la estructura, CSS controla la presentación y
JavaScript responde a una acción. Una región de estado es un elemento con
`role="status"` que comunica cambios a tecnologías de asistencia. La nueva
página mínima debe cargarse por HTTP desde la raíz del repositorio, igual que el
mapa, y no mediante `file://`.

Un módulo ES es un archivo JavaScript cargado mediante `type="module"`. Puede
declarar dependencias con `import` y publicar una función con `export`. El mapa
usará un módulo de estado pequeño para que la persona estudiante vea una
dependencia real sin introducir un empaquetador.

Slidev trata el directorio configurado como `publicDir` como archivos estáticos:
los sirve durante desarrollo y los copia a cada build. El directorio histórico
`docs/slides/unidad01/public/` no puede continuar como `publicDir` porque sus
capturas tienen licencia pendiente. `docs/slides/unidad01/public-generated/`
contendrá únicamente SVG propios y será el único origen público del deck.

## Plan de trabajo

Primero se añadirá `examples/leaflet/pagina_minima/` con `index.html`,
`styles.css`, `main.js` y `status.js`. La página tendrá idioma, viewport,
encabezado, contenido principal, botón con etiqueta y región de estado. Su
`main.js` importará `setStatus` desde `status.js`; al activar el botón cambiará
el mensaje visible. Se actualizarán los patrones de formato, HTML y CSS de
`package.json` para cubrir ambos ejemplos Leaflet, y
`tests/a11y/leaflet.spec.mjs` verificará el cambio de estado y ausencia de
violaciones Axe en la página mínima.

Después, `examples/leaflet/mapa_basico/index.html` cargará `main.js` con
`type="module"`. Un nuevo módulo local de estado exportará la actualización de
la región de estado; `main.js` lo importará y conservará el filtro, el mapa, la
tabla y los mensajes existentes. No se cambiarán las URLs de datos, teselas,
atribución ni la estructura de errores del mapa.

La presentación sustituirá la diapositiva de actividad digital por la práctica
de página mínima. La ruta de aprendizaje y la práctica guiada pasarán por este
ejemplo antes del mapa y harán visible la nota Markdown local. La explicación de
Internet y Web definirá hipertexto sin añadir una diapositiva. La diapositiva de
servidores distinguirá servidor estático, aplicación y servidor geoespacial en
una frase por responsabilidad. La guía de Unidad 1 reflejará los comandos y
rutas exactas de ambas prácticas.

Las guías de Unidades 2 y 4 nombrarán expresamente GML, KML y ESRI JSON como
compatibilidad de formatos, y RPC/SOAP como panorama de contratos históricos. No
se añadirán ejercicios, cuentas ni dependencias para estos temas.

Finalmente, se añadirá `docs/slides/unidad01/vite.config.mts` con
`publicDir: 'public-generated'`. Los SVG y el README de
`public/assets/generated/` se moverán a `public-generated/assets/generated/`. El
README de los assets históricos declarará que `public/` ya no es un directorio
servido por Slidev. Las URLs de las imágenes en `slides.md` no cambiarán porque
el nuevo directorio conserva la estructura `assets/generated/`.

## Pasos concretos

Desde `C:\opt\work\personal\cartografia_web`, ejecutar durante la
implementación:

    npm run format:check
    npm run lint
    npm run test:a11y
    npx prettier --check "docs/slides/unidad01/**/*.{md,css,mts,svg}"
    npx stylelint "docs/slides/unidad01/style.css"
    uv run python scripts/validate_resources.py
    git diff --check

Desde `C:\opt\work\personal\cartografia_web\docs\slides\unidad01`, construir en
un directorio temporal nuevo para que no contenga archivos de builds previos:

    slidev build slides.md --out C:\Users\juanm\AppData\Local\Temp\opencode\slides-unidad01-isolated

El build debe terminar con `built in ...` y contener
`assets/generated/connectividad_2025.svg`. La ruta
`assets/slide-001-image-000.jpg` no debe existir en ese directorio.

Para comprobar las dos prácticas desde la raíz del repositorio, iniciar:

    python -m http.server 8000

Abrir `http://localhost:8000/examples/leaflet/pagina_minima/`, activar el botón
y comprobar que cambia la región de estado. Abrir
`http://localhost:8000/examples/leaflet/mapa_basico/`, seleccionar el filtro y
confirmar que estado, tabla y mapa siguen concordando. Las herramientas de
desarrollo deben mostrar `main.js` y `status.js` como módulos solicitados.

## Validación y aceptación

La implementación se acepta cuando una persona puede completar esta secuencia
desde un clon con las dependencias instaladas:

- Servir `examples/leaflet/pagina_minima/` por HTTP, pulsar su botón y recibir
  un mensaje de estado actualizado sin errores de consola.
- Inspeccionar `index.html` y encontrar `type="module"`; inspeccionar `main.js`
  y encontrar una importación local; inspeccionar `status.js` y encontrar la
  exportación correspondiente.
- Abrir el mapa Leaflet, filtrar zonas y recibir el mismo estado y tabla que
  antes del cambio.
- Seguir las diapositivas desde una página mínima hasta la nota Markdown y el
  mapa sin encontrar una cuenta SaaS, URL HTTP externa ni token.
- Leer en las guías de Unidades 2 y 4 el destino explícito de compatibilidad de
  GML, KML, ESRI JSON, RPC y SOAP.
- Construir Slidev y comprobar que un SVG propio está disponible bajo
  `/assets/generated/`, mientras una captura `slide-001-image-000.jpg` no se
  entrega desde el build aislado.

`npm run format:check`, `npm run lint`, `npm run test:a11y`,
`uv run python scripts/validate_resources.py` y `git diff --check` deben
terminar sin errores. Si la instalación local no contiene Chromium para
Playwright, se documentará el bloqueo y se hará una captura manual con Chrome;
no se instalarán dependencias nuevas de forma implícita.

## Idempotencia y recuperación

Las ediciones son aditivas y los comandos de validación no cambian fuentes. Los
tests y las páginas pueden ejecutarse repetidamente. El build aislado usa un
directorio temporal exclusivo; si existe una salida previa, se elegirá una ruta
temporal nueva en vez de borrar archivos.

Si `publicDir` impidiera cargar un SVG propio, restaurar de forma segura el
directorio `public-generated/assets/generated/` a la estructura indicada por
`vite.config.mts`, sin reactivar `public/` como origen público. Si el nuevo
módulo afecta el mapa, revertir únicamente la importación y el script
`type="module"` después de comprobar que el módulo `status.js` está presente; no
cambiar datos, atribución ni estilos del mapa. Las capturas históricas no se
borran ni se modifican durante este plan.

## Artefactos y notas

La evidencia mínima esperada del build aislado es:

    Test-Path ...\slides-unidad01-isolated\assets\generated\connectividad_2025.svg
    True

    Test-Path ...\slides-unidad01-isolated\assets\slide-001-image-000.jpg
    False

La evidencia de módulo debe ser visible en las fuentes:

    <script type="module" src="main.js"></script>
    import { setStatus } from './status.js';
    export function setStatus(element, message) { ... }

## Interfaces y dependencias

No se agregarán bibliotecas, frameworks, cuentas ni servicios externos. El
ejemplo conserva Leaflet vendorizado y las teselas HTTPS existentes. El nuevo
módulo `status.js` expondrá exactamente `setStatus(element, message)`, donde
`element` es la región de estado y `message` es texto visible. El módulo no
usará HTML no confiable: actualizará `textContent`.

`vite.config.mts` usará `defineConfig` de `vite` y declarará
`publicDir: 'public-generated'`. Los SVG continuarán siendo accesibles con las
URLs absolutas `/assets/generated/<archivo>.svg` ya usadas por `slides.md`.

## Revisión

2026-08-05: plan creado tras comparar el deck histórico de 78 páginas, la
presentación modernizada, guías, ejemplo Leaflet y configuración de Slidev. La
revisión resuelve los vacíos sin restaurar contenido inseguro, no licenciado o
fuera del núcleo obligatorio.

2026-08-05: se añadió la evidencia del primer hito. La página mínima y el mapa
Leaflet usan módulos ES reales y las tres pruebas de accesibilidad pasan sin
agregar dependencias.

2026-08-05: la presentación, Unidad 1 y las guías de compatibilidad se
reescribieron; los SVG propios se trasladaron al nuevo directorio público de
Slidev. Falta validar el build aislado y revisar visualmente las diapositivas
modificadas.

2026-08-05: plan cerrado. El build aislado confirmó el aislamiento de assets y
la revisión individual confirmó composición y contraste. Se registró el bloqueo
de Docker de `npm run build` sin modificar infraestructura ajena.
