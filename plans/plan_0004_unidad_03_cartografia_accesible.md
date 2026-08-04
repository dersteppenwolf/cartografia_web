# plan_0004 - Hacer autonoma la Unidad 3 de cartografia accesible

**Fecha**: 2026-08-03
**Ambito**: `docs/unidades/03_cartografia_accesible.md`, ejemplo Leaflet,
rubricas y guia de accesibilidad
**Estado**: cerrado técnicamente; revisión manual WCAG y Safari real pendientes
en `plan_0001`
**Prioridad**: alta; requisito de Entrega 1 y de toda visualizacion posterior

Este ExecPlan es un documento vivo. Debe mantenerse conforme a `PLANS.md`,
`AGENTS.md`, `UPGRADE_PLAN.md` y `DESIGN.md`.

## Proposito / Panorama general

Al terminar, una persona podra justificar una clasificacion y una simbologia
tematica, distinguir conteos de tasas, comunicar incertidumbre y ofrecer una
lectura equivalente sin depender de color, raton o canvas. Podra evaluar el
ejemplo Leaflet con teclado, foco, reflow, leyenda, atribucion, estado y tabla.

## Progress

- [x] (2026-08-03) Se detecto una frase incompleta en la unidad actual y
      ausencia de explicacion sobre normalizacion, clasificacion, escala,
      incertidumbre y simbolizacion.
- [x] (2026-08-03) Se reparo la frase truncada y se reescribio la leccion con
      normalizacion, clasificacion, simbolos, paletas, leyenda, incertidumbre y
      limites de interpretacion.
- [x] (2026-08-03) Se agregaron practica guiada, revision por pares, errores
      frecuentes, autoevaluacion y enlaces a Entrega 1 y accesibilidad.
- [x] (2026-08-03) Pasaron Markdownlint, las dos pruebas Axe/Leaflet, build y
      enlaces internos. La evidencia manual permanece pendiente en
      `docs/governance/manual-accessibility-review.md`.

## Surprises & Discoveries

- Observacion: `03_Cartografia/Readme.md` reune referencias utiles de color y
  clasificacion, pero sus ejercicios obligatorios dependen de QGIS Cloud y
  Flourish. Evidencia: `03_Cartografia/Readme.md` lineas 15 a 122.

- Observacion: el ejemplo Leaflet ya ofrece leyenda, tabla, filtro, foco y
  mensaje de estado, pero necesita una explicacion de las decisiones que
  demuestra. Evidencia: `examples/leaflet/mapa_basico/` y
  `docs/evaluacion/entrega_1.md`.

## Decision Log

- Decision: convertir OSM en contexto visual atribuible y no en fuente de datos
  ni requisito de conectividad para aprobar. Justificacion: el aprendizaje
  cartografico debe seguir disponible con la tabla y los fixtures locales si el
  mapa base falla. Fecha/Autor: 2026-08-03 / OpenCode.

## Outcomes & Retrospective

La Unidad 3 quedó convertida en una lección de normalización, clasificación,
Leaflet demuestra tabla equivalente, estado, foco, leyenda y atribución; Axe y
Playwright pasan. La conformidad manual WCAG y Safari real permanecen como
evidencia de piloto, sin declararse aprobadas por este cierre técnico.

## Contexto y orientacion

Clasificacion agrupa valores numericos en clases; normalizacion transforma un
conteo en una medida comparable, por ejemplo por poblacion o superficie. Una
paleta secuencial representa magnitud ordenada; una divergente resalta
separacion respecto a un punto medio. Incertidumbre comunica limites de
cobertura, fecha, precision, metodo o comparabilidad. Reflow es la capacidad de
reorganizar contenido sin perdida al ampliar texto o reducir ancho. Una
alternativa equivalente permite entender el hallazgo sin operar el mapa.

## Plan de trabajo

Reescribir la unidad con resultados de aprendizaje, vocabulario y una narrativa
que parta de una pregunta territorial. Explicar seleccion de variable, tipo de
dato, conteo frente a tasa, clasificacion, simbolos proporcionales, coropletas,
paletas, contraste, leyenda, escala, atribucion e incertidumbre. Incluir
ejemplos de decisiones incorrectas y su consecuencia interpretativa.

Explicar WCAG aplicada a mapas: nombre accesible, teclado, foco visible,
controles fuera del canvas, estados de carga/error, no depender solo de color,
reflow y tabla equivalente. Usar el ejemplo Leaflet para que cada requisito se
observe en una interfaz real. Agregar una actividad de rediseño de una leyenda y
una actividad de revision por pares con criterios de Entrega 1.

## Pasos concretos

Desde la raiz ejecutar:

    python -m http.server 8000
    npm run test:a11y
    npm run lint:markdown

Abrir `http://localhost:8000/examples/leaflet/mapa_basico/`, navegar con Tab y
Shift+Tab, aplicar filtros, verificar tabla y ampliar al 200 por ciento. La
unidad debe documentar este recorrido y explicar que Axe es apoyo, no sustituto
de revision humana.

## Validacion y aceptacion

La unidad se acepta cuando una persona puede justificar una clasificacion,
identificar por que un total no siempre es comparable, proponer una alternativa
al color y completar una lista de teclado, foco, reflow, leyenda, atribucion,
estado y tabla. Debe corregir la frase truncada actual y enlazar Entrega 1 y la
guia de accesibilidad.

`npm run test:a11y`, `npm run lint:markdown` y `git diff --check` deben pasar.
La evidencia manual se registra en
`docs/governance/manual-accessibility-review.md`, sin declarar Safari real si no
se probo.

## Idempotencia y recuperacion

Las actividades no cambian el fixture ni publican datos. Si una prueba manual
revela un problema, registrar el hallazgo antes de modificar estilos o
semantica; repetir las pruebas de navegador despues de la correccion.

## Artefactos y notas

La unidad final debe contener una lista breve de errores frecuentes: coropleta
con totales no normalizados, paleta sin contraste, leyenda ambigua, escala
ausente, popup inaccesible y mapa sin alternativa.

## Interfaces y dependencias

Mantener CSS nativo, Leaflet, tabla HTML y OSM con atribucion. No agregar
herramientas SaaS ni datos sociales. Reutilizar `docs/guias/accesibilidad.md`,
`docs/governance/manual-accessibility-review.md` y
`docs/evaluacion/entrega_1.md`.

## Revision

2026-08-03: creado para reparar y expandir Unidad 3 como material de cartografia
y accesibilidad autonomo.
