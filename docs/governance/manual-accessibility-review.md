---
layout: default
title: Evidencia manual de accesibilidad
permalink: /gobierno/evidencia-accesibilidad/
---

# Evidencia manual de accesibilidad

Esta hoja separa evidencia automatizada de revisión humana. La conformidad
objetivo es WCAG 2.2 AA; una prueba automatizada sin hallazgos no demuestra por
sí sola esa conformidad.

## Evidencia automatizada

- [x] Axe no reporta violaciones en la carga, filtro, PMTiles y COG del cliente
      MapLibre mediante `examples/maplibre/app/tests/app.spec.ts`.
- [x] Playwright ejecuta los flujos de carga, filtro, error de red, PMTiles y
      COG en Chromium, Firefox y WebKit.
- [x] El cliente anuncia carga y errores con `role="status"`, mantiene una tabla
      equivalente y devuelve el foco al mapa al cerrar el diálogo de consulta.

## Revisión manual pendiente

- [ ] Con teclado solamente, recorrer controles, aplicar filtro, consultar una
      entidad y cerrar el diálogo; confirmar orden lógico y foco visible.
- [ ] Con zoom del navegador al 200% y ancho de 320 CSS px, confirmar reflow sin
      pérdida de controles, tabla o mensajes de estado.
- [ ] Revisar contraste de texto, bordes, foco, botón y bandas sobre todas las
      superficies del sitio y del cliente.
- [ ] Revisar el anuncio de carga, vacío y error con un lector de pantalla.
- [ ] Confirmar en Safari real sobre macOS los flujos de carga, filtro, consulta
      y error. Playwright WebKit solo es detección temprana.

La persona responsable de web y accesibilidad debe completar fecha, navegador,
asistencia técnica, resultado y cualquier excepción institucional en los
resultados del piloto. No marcar una casilla pendiente sin evidencia observable.
