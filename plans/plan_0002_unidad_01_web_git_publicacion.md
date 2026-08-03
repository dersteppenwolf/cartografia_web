# plan_0002 - Hacer autonoma la Unidad 1 de web, Git y publicacion

**Fecha**: 2026-08-03
**Ambito**: `docs/unidades/01_web_git_publicacion.md`, `examples/leaflet/mapa_basico/`, guias y validacion editorial
**Estado**: propuesto
**Prioridad**: alta; prerrequisito didactico de las Unidades 2 a 8

Este ExecPlan es un documento vivo. Debe mantenerse conforme a `PLANS.md`, `AGENTS.md`, `UPGRADE_PLAN.md` y `DESIGN.md`.

## Proposito / Panorama general

Al terminar, una persona sin experiencia previa podra crear una pagina HTML semantica, aplicar CSS responsive, cargar un GeoJSON local por HTTP con JavaScript modular y explicar el ciclo basico de Git sin necesitar una cuenta externa. Podra verificar el resultado abriendo el ejemplo Leaflet, desconectando temporalmente el archivo de datos y observando un estado de error comprensible.

La unidad mantenida debe sustituir las instrucciones historicas que exigen cuentas personales, issues, repositorios publicos individuales o GitHub Pages como requisito. GitHub Pages seguira apareciendo solo como implementacion de referencia de la publicacion estatica.

## Progress

- [x] (2026-08-03) Se identifico que `docs/unidades/01_web_git_publicacion.md` tiene 23 lineas y no cubre HTML semantico, CSS responsive, modulos ES, HTTP, errores ni flujo Git suficiente para cuatro horas.
- [ ] Reescribir el documento como leccion autonoma y enlazar el ejemplo aprobado.
- [ ] Crear o ampliar ejercicios, autoevaluacion y comprobaciones docentes.
- [ ] Validar contenido, enlaces, ejemplo y accesibilidad afectada.

## Surprises & Discoveries

- Observacion: `01_Fundamentos/Readme.md` explica Git y Pages con detalle, pero exige crear cuentas, repositorios personales e issues del curso historico.
  Evidencia: `01_Fundamentos/Readme.md` lineas 62 a 157.

- Observacion: el ejemplo mantenido Leaflet ya usa `fetch`, estados y una tabla equivalente; es una demostracion ejecutable adecuada para la unidad.
  Evidencia: `examples/leaflet/mapa_basico/main.js` e `examples/leaflet/mapa_basico/index.html`.

## Decision Log

- Decision: explicar Git mediante un repositorio local y comandos no destructivos; presentar remotos, push y Pages como adaptadores opcionales.
  Justificacion: el nucleo no puede requerir una cuenta SaaS ni un repositorio de una persona docente.
  Fecha/Autor: 2026-08-03 / OpenCode.

- Decision: usar el ejemplo Leaflet mantenido y su GeoJSON sintetico como caso de principio a fin.
  Justificacion: evita introducir datos externos, tokens o un segundo ejemplo sin pruebas.
  Fecha/Autor: 2026-08-03 / OpenCode.

## Outcomes & Retrospective

El resultado inicial es una ficha breve. Al cerrar este plan, la Unidad 1 sera una leccion autocontenida con teoria, practica, errores comunes y criterios de verificacion que preparan las unidades posteriores.

## Contexto y orientacion

La ruta docente objetivo es `docs/unidades/01_web_git_publicacion.md`. Jekyll la convierte en la ruta publica `/unidades/01-web-git-publicacion/`. El ejemplo es `examples/leaflet/mapa_basico/`; su pagina se publica en `/examples/leaflet/mapa_basico/` y carga `data/referencia.geojson` por HTTP.

HTML semantico significa elegir elementos por su funcion, por ejemplo `main`, `nav`, `button`, `label`, `table` y encabezados, en lugar de usar contenedores genericos para todo. CSS responsive significa que la disposicion se adapta a pantallas pequenas sin ocultar informacion. Un modulo ES es un archivo JavaScript que declara dependencias con `import` o se carga como modulo. HTTP es el protocolo que usa el navegador para solicitar recursos; un codigo 200 indica exito y un codigo 404 indica que el recurso no existe. Git es un historial local de cambios; un commit es una instantanea identificada del trabajo preparado.

## Plan de trabajo

Reescribir `docs/unidades/01_web_git_publicacion.md` con una apertura que indique sus cuatro horas presenciales y cuatro autonomas, prerrequisitos y producto observable. Explicar primero el recorrido navegador-servidor-archivo y por que `file://` no equivale a servir archivos con HTTP. Incluir ejemplos pequenos de estructura HTML, etiquetas y formularios accesibles, reglas CSS de reflow y un modulo JavaScript que usa `fetch`, `await`, comprobacion de `response.ok` y mensaje de error.

Explicar Git como un ciclo local: inspeccionar estado, preparar cambios, confirmar una unidad coherente y revisar el historial. Diferenciar repositorio local, remoto y hosting estatico; no pedir crear cuenta ni publicar informacion personal. Describir GitHub Pages como una opcion institucional que publica el artefacto ensamblado, no como el mecanismo obligatorio de entrega.

Convertir el ejemplo Leaflet en el hilo conductor: identificar HTML, CSS, JavaScript, GeoJSON, mapa base OSM, leyenda, atribucion, estado y tabla. Incluir una actividad guiada que cambie el filtro y una actividad de error que renombre temporalmente el GeoJSON durante una sesion local, sin confirmar esa modificacion. Anadir secciones de errores frecuentes, autoevaluacion y relacion con Entrega 1.

## Pasos concretos

Desde `C:\opt\work\personal\cartografia_web`, editar la unidad y comprobar el ejemplo con:

    python -m http.server 8000
    npm run test:a11y -- --project=leaflet
    npm run lint:markdown
    npm run links:internal

En otra terminal, abrir `http://localhost:8000/examples/leaflet/mapa_basico/`. El resultado esperado es un mapa con datos sinteticos, mapa base atribuido, filtro, leyenda, tabla y mensaje de estado. Al simular la ausencia del GeoJSON, el estado debe explicar el error y la pagina no debe quedar vacia.

## Validacion y aceptacion

La unidad se acepta cuando una persona puede leerla sin consultar el arbol historico y responder que es HTML semantico, por que se sirve por HTTP, que hace `response.ok`, como se registra un cambio Git y por que Pages es opcional. Debe contener resultados de aprendizaje, vocabulario definido, recorrido guiado, ejercicio, errores frecuentes, autoevaluacion y enlace a Entrega 1.

`npm run lint:markdown`, `npm run test:a11y -- --project=leaflet`, `npm run links:internal` y `git diff --check` deben terminar con codigo cero. La revision manual confirma teclado, foco, reflow y atribucion de OSM.

## Idempotencia y recuperacion

Los comandos de validacion no deben modificar fuentes. La actividad de error usa una copia temporal o revierte el nombre del GeoJSON antes de terminar. Si un navegador conserva el recurso en cache, abrir una ventana privada o recargar con el cache desactivado; no cambiar el fixture versionado.

## Artefactos y notas

El producto de la unidad es un mapa Leaflet publicable localmente, no una cuenta remota. El texto docente debe enlazar rutas internas con `relative_url`, y cada enlace externo debe usar HTTPS y aportar valor pedagogico concreto.

## Interfaces y dependencias

No agregar frameworks. Mantener Leaflet vendorizado, APIs nativas del navegador y OSM como contexto visual opcional atribuido. Usar `examples/leaflet/mapa_basico/main.js` como referencia de `fetch` y estado; no copiar codigo QGIS2Web ni ejemplos historicos con jQuery o tokens.

## Revision

2026-08-03: creado para transformar la ficha inicial de Unidad 1 en material docente autonomo sin requerir SaaS.
