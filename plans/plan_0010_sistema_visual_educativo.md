# plan_0010 - Aplicar un sistema visual educativo en color

**Fecha**: 2026-08-03
**Ámbito**: `DESIGN.md`, tokens y estilos de `docs/`, layout Jekyll y cliente
MapLibre
**Estado**: cerrado técnicamente; revisión manual de contraste pendiente en
`plan_0001`
**Prioridad**: alta; mejora la orientación del material docente mantenido

Este ExecPlan es un documento vivo. Debe mantenerse conforme a `PLANS.md`,
`AGENTS.md`, `UPGRADE_PLAN.md` y `DESIGN.md`.

## Propósito / Panorama general

Después del cambio, el curso tendrá una identidad educativa más clara: cabecera
índigo para orientar, superficies azuladas claras para organizar contenido,
bloques de evidencia. El color no sustituirá texto, iconos funcionales,
atribuciones ni estados accesibles. Una persona podrá comprobar el resultado en
la portada, una unidad y el cliente MapLibre sin perder contraste, navegación de
teclado o reflow.

La paleta toma como referencia el contraste azul/amarillo/coral de las imágenes
aportadas por la persona usuaria y los principios de rutas claras, práctica y
progreso legible observados en Memorisely y Uxcel. No se copia su marca,
fotografía, componentes, gamificación ni contenido.

## Progress

- [x] (2026-08-03) Se revisaron `DESIGN.md`, `docs/assets/css/`, el layout
      Jekyll y los estilos MapLibre actuales.
- [x] (2026-08-03) Se actualizó la guía visual y los tokens canónicos con una
      paleta educativa índigo, azul claro, amarillo y coral.
- [x] (2026-08-03) Se aplicaron los tokens al sitio Jekyll, navegación, cliente
      MapLibre y ejemplo Leaflet.
- [x] (2026-08-03) Se sincronizaron los tokens y pasaron formato, lint CSS,
      pruebas Leaflet, pruebas MapLibre Chromium, build, enlaces e inventario.
- [ ] Registrar la revisión manual de contraste en los fondos y controles nuevos.

## Surprises & Discoveries

- Observación: los estilos actuales aplican una composición monocromática mínima
  pero no expresan la estructura de ruta, práctica y evidencia que requieren las
  unidades ampliadas. Evidencia: `docs/assets/css/site.css` y
  `docs/_layouts/default.html`.

- Observación: `scripts/sync_design_tokens.py` puede mantener idénticos los
  tokens del sitio y el cliente sin introducir una dependencia CSS adicional.
  Evidencia: `scripts/sync_design_tokens.py`.

## Decision Log

- Decisión: usar índigo como color de orientación y acciones primarias, amarillo
  para foco y acciones secundarias de alto contraste, coral solo para énfasis no
  crítico y azul noche para superficies oscuras. Justificación: conserva una
  señal visual educativa clara y evita usar color como único canal de estado o
  progreso. Fecha/Autor: 2026-08-03 / OpenCode.

- Decisión: mantener borde recto, una familia sans serif, base de 14 px, CSS
  nativo y ausencia de sombras o gradientes. Justificación: moderniza el color
  sin sacrificar el lenguaje editorial, rendimiento ni accesibilidad del curso.
  Fecha/Autor: 2026-08-03 / OpenCode.

## Outcomes & Retrospective

La guía, sitio y cliente comparten ahora tokens de un sistema educativo índigo,
azul claro, amarillo y coral. Pasaron sincronización, formato, lint, pruebas,
build, enlaces e inventario. La revisión manual de contraste sobre las nuevas
superficies y focos sigue pendiente como evidencia transversal del plan principal.

## Contexto y orientación

`DESIGN.md` define las decisiones de interfaz. `docs/assets/css/tokens.css` es
la fuente canónica de propiedades CSS. `docs/assets/css/site.css` implementa la
documentación Jekyll y `docs/_layouts/default.html` contiene cabecera,
navegación, contenido y pie. `examples/maplibre/app/src/styles/tokens.css` es
una copia generada para el cliente; `scripts/sync_design_tokens.py` la
sincroniza.

El contraste es la diferencia de luminancia entre texto y fondo. WCAG 2.2 AA
exige normalmente al menos 4.5:1 para texto normal. El foco visible muestra qué
control recibe el teclado. Una superficie es un fondo que agrupa contenido, no
un reemplazo de jerarquía semántica.

## Plan de trabajo

Actualizar `DESIGN.md` con la paleta, usos permitidos y prohibidos, arquitectura
de páginas educativas, estados, componentes docentes y criterios de revisión.
Definir tokens índigo, azul noche, amarillo, coral y azul claro en
`docs/assets/css/tokens.css`, conservando nombres existentes cuando eviten
ruptura y agregando nombres semánticos para los colores nuevos.

Modificar `docs/_layouts/default.html` para incluir navegación textual hacia
inicio, programa, ruta de unidades y ejemplos. Aplicar en `site.css` cabecera
índigo, navegación legible, superficie de contenido clara, bloques de código,
tablas, enlaces, foco amarillo con contorno índigo y pie azul noche. No usar
sombras, radios ni imágenes decorativas.

Actualizar `examples/maplibre/app/src/styles.css` con los mismos tokens para
controles, tabla, estado y mapa. Sincronizar la copia de tokens. No modificar el
contrato de fuentes/capas durante este plan salvo los colores de presentación.

## Pasos concretos

Desde `C:\opt\work\personal\cartografia_web`, ejecutar:

    uv run python scripts/sync_design_tokens.py
    uv run python scripts/sync_design_tokens.py --check
    npm run lint:css
    npm run --workspace examples/maplibre/app lint
    npm run --workspace examples/maplibre/app test:e2e -- --project=chromium
    npm run build
    npm run links:internal

Abrir `_site/` por HTTP y comprobar portada, una unidad, tabla y controles del
ejemplo MapLibre a 320 CSS px y al 200 % de zoom.

## Validación y aceptación

El cambio se acepta cuando el sitio muestra identidad índigo/azul claro sin
reducir contraste; los enlaces, foco y estados siguen legibles; la navegación es
textual y operable; los mapas conservan atribución, leyenda y alternativas; los
tokens de docs y MapLibre son idénticos; y todos los comandos de validación
pasan.

La revisión manual documenta contraste de texto blanco sobre índigo/azul noche,
texto índigo/negro sobre azul claro y foco amarillo sobre fondos claros y
oscuros. No se declara WCAG completa solo por las pruebas automatizadas.

## Idempotencia y recuperación

`sync_design_tokens.py` puede ejecutarse varias veces y solo copia la fuente
canónica. Si una combinación no supera contraste o rompe una prueba, ajustar el
token canónico, sincronizar y repetir build; no añadir excepciones de color por
componente.

## Artefactos y notas

El resultado incluye `DESIGN.md`, tokens, layout, estilos y las pruebas
existentes del cliente. El sitio publicado por Pages se actualiza después de un
push a `master`; la revisión remota comprueba que el artefacto conserva los
recursos.

## Interfaces y dependencias

Usar CSS nativo y propiedades personalizadas. No agregar Tailwind, librerías de
componentes, fuentes sin licencia, iconos decorativos ni proveedores SaaS. OSM
mantiene su atribución visible y sigue siendo contexto opcional de mejor
esfuerzo.

## Revisión

2026-08-03: creado para implementar una paleta educativa contrastada inspirada
en las referencias aportadas, sin copiar sus identidades comerciales.
