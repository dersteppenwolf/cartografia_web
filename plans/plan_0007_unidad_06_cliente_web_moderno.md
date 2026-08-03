# plan_0007 - Hacer autonoma la Unidad 6 de cliente web moderno

**Fecha**: 2026-08-03 **Ambito**: `docs/unidades/06_cliente_web.md`,
`examples/maplibre/app/`, pruebas Vitest y Playwright **Estado**: propuesto
**Prioridad**: alta; base de Entrega 3

Este ExecPlan es un documento vivo. Debe mantenerse conforme a `PLANS.md`,
`AGENTS.md`, `UPGRADE_PLAN.md` y `DESIGN.md`.

## Proposito / Panorama general

Al terminar, una persona podra recorrer y modificar un cliente
TypeScript/Vite/MapLibre sin framework, distinguir configuracion local de
recursos publicados, explicar fuentes, capas, eventos y estado URL, y comprobar
carga, filtro, consulta y error con pruebas. Podra abrir el cliente publicado y
el local sin confundir el GeoServer de desarrollo con los assets estaticos.

## Progress

- [x] (2026-08-03) Se identifico que la unidad actual describe el resultado y
      comandos, pero no explica TypeScript, Vite, modulos, ciclo de carga,
      capas, configuracion ni pruebas.
- [x] (2026-08-03) Se reescribió la teoría y el recorrido de módulos, fuentes,
      capas, estado URL, configuración local/publicada y accesibilidad.
- [x] (2026-08-03) Se incorporaron actividades de configuración, filtros,
      consulta, fuente, error, tabla equivalente y autoevaluación.
- [x] (2026-08-03) Pasaron Vitest, tipos, 15 pruebas E2E en Chromium/Firefox/
      WebKit, build y enlaces internos.

## Surprises & Discoveries

- Observacion: el cliente necesita diferenciar recursos `localhost` de assets
  publicados para no intentar conectar al computador de cada visitante.
  Evidencia: `examples/maplibre/app/src/config.ts` define rutas segun el host
  actual.

- Observacion: el cliente ya mantiene tabla equivalente, dialogo con foco y
  pruebas en Chromium, Firefox y WebKit. Evidencia:
  `examples/maplibre/app/src/main.ts`, `tests/app.spec.ts` y
  `playwright.config.ts`.

## Decision Log

- Decision: explicar el cliente por modulos existentes y no crear un segundo
  tutorial paralelo. Justificacion: el material docente debe conducir a una
  aplicacion mantenible y probada, no a codigo de demostracion desechable.
  Fecha/Autor: 2026-08-03 / OpenCode.

## Outcomes & Retrospective

El resultado sera una leccion de arquitectura de frontend geoespacial que
permite leer, modificar y verificar el cliente mantenido.

## Contexto y orientacion

TypeScript agrega tipos a JavaScript para detectar errores antes de ejecutar.
Vite sirve modulos durante desarrollo y produce archivos estaticos para
publicar. MapLibre representa un mapa mediante fuentes, que describen datos, y
capas, que describen como dibujarlos. Un estado URL guarda valores en la
direccion para compartir una vista. Una fuente GeoJSON entrega entidades
completas; una fuente vectorial entrega teselas; una raster entrega imagenes. Un
E2E es una prueba que abre un navegador y recorre la interfaz como una persona
usuaria.

## Plan de trabajo

Reescribir la unidad con un mapa de modulos de `examples/maplibre/app/src/`:
`config.ts`, `state.ts`, `map.ts`, `status.ts` y `main.ts`. Explicar
`AppConfig`, lectura y escritura de URL, inicializacion de MapLibre,
fuente/capa, filtro por atributo, tabla equivalente, dialogo de consulta, foco y
mensajes de error.

Describir la diferencia entre desarrollo local, donde se consulta OGC API local,
y sitio publicado, donde se consumen GeoJSON y assets estaticos del mismo
artefacto. Explicar el mapa base OSM como contexto atribuido y opcional, sin
ocultar que es una dependencia externa de mejor esfuerzo. Introducir pruebas
puras con Vitest, pruebas de navegador con Playwright y Axe como apoyo.

Agregar actividades que cambien un umbral, inspeccionen la URL, provoquen un
error de red mediante Playwright y comparen la tabla con el popup. Cerrar con
errores frecuentes: usar URL absoluta de localhost en Pages, eliminar la
atribucion, poner controles esenciales sobre canvas, no gestionar foco o usar
estado global no compartible.

## Pasos concretos

Desde la raiz, con el stack local iniciado para la ruta API:

    npm run --workspace examples/maplibre/app dev
    npm run --workspace examples/maplibre/app lint
    npm run --workspace examples/maplibre/app test
    npm run --workspace examples/maplibre/app test:e2e -- --project=chromium
    npm run --workspace examples/maplibre/app build

Abrir la URL de Vite, cambiar el filtro, copiar la URL y abrirla de nuevo. El
resultado esperado conserva vista y filtro, muestra tabla equivalente y anuncia
errores de red. Para el sitio publicado, abrir `/examples/maplibre/` y confirmar
que usa assets estaticos, no el localhost del visitante.

## Validacion y aceptacion

La unidad se acepta cuando una persona puede explicar cada modulo, diferenciar
fuente y capa, describir estado URL, justificar tabla equivalente y ejecutar una
prueba de error. Debe incluir un ejercicio guiado, autoevaluacion, errores
frecuentes, relacion con Entrega 3 y enlace al cliente publicado.

Los comandos indicados, `npm run lint:markdown` y `git diff --check` deben
pasar. Las pruebas E2E deben verificar carga, filtro, PMTiles, COG, error y
ausencia de violaciones Axe automatizadas.

## Idempotencia y recuperacion

Vite y las pruebas no modifican fuentes. Si el E2E falla por servicios locales
detenidos, iniciar Compose y ejecutar `scripts/configure_geoserver.py`; no
cambiar la configuracion a un endpoint externo. Los assets generados `dist/`
siguen ignorados.

## Artefactos y notas

El documento debe enlazar el ejemplo publicado con `relative_url`, la Unidad 5
para infraestructura y la Unidad 7 para PMTiles/COG. Debe explicar que la
revision manual WCAG y Safari real se registran fuera de las pruebas
automatizadas.

## Interfaces y dependencias

Mantener TypeScript, Vite, MapLibre, `pmtiles` y
`@geomatico/maplibre-cog-protocol` fijados por lockfile. No agregar React, Vue,
Svelte, Tailwind ni un proveedor de mapas con token.

## Revision

2026-08-03: creado para convertir Unidad 6 en una guia autonoma del cliente
probado.
