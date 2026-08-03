# Guia para agentes

## Proposito del repositorio

Este repositorio contiene el curso **Publicacion de cartografia via web**. El
material actual se consolido alrededor de 2020 y esta en proceso de
modernizacion curricular, tecnica, editorial y operativa.

El objetivo no es convertir el repositorio en una unica aplicacion. Debe seguir
siendo un curso que combine documentacion, ejemplos ejecutables, datos de
practica, notebooks e infraestructura reproducible.

## Fuentes de verdad

Consultar estos archivos antes de proponer o implementar cambios:

1. `UPGRADE_PLAN.md`: alcance, fases, arquitectura objetivo y criterios de
   aceptacion de la modernizacion.
2. `PLANS.md`: requisitos no negociables para redactar y mantener planes de
   ejecucion (ExecPlans).
3. `DESIGN.md`: referencia visual para el sitio y los ejemplos mantenidos. Se
   aplica sin sacrificar accesibilidad, semantica ni funcionalidad cartografica.
4. `Programa.md`: duracion, competencias, evaluacion y tareas vigentes. Su
   contenido historico debe migrarse siguiendo el plan, no copiarse sin
   revision.
5. `README.md`: indice publico del curso.
6. Los `Readme.md` de cada unidad: instrucciones y ejercicios existentes.
7. `Geoserver.md` y `Herramientas.md`: material complementario, parte del cual
   es historico.

Cuando estos archivos entren en conflicto, seguir `UPGRADE_PLAN.md` para el
trabajo de modernizacion y documentar cualquier decision curricular que cambie
su alcance.

## Estructura actual

- `00_Intro/`: introduccion y prerrequisitos.
- `01_Fundamentos/`: Internet, Git, GitHub Pages, HTML, CSS, JavaScript y
  Leaflet.
- `02_Conceptos/`: SIG web, QGIS, GeoJSON, TopoJSON y exportaciones QGIS2Web.
- `03_Cartografia/`: cartografia tematica, color, clasificacion y ejemplos de
  visualizacion.
- `04_Servicios_Web_Geoservicios_OGC/`: WMS, WFS, OWSLib y notebooks.
- `05_Servidores_Mapas/`: PostGIS, GeoServer, DBeaver y servicios OGC.
- `06_Simbologia/`: SLD, CSS, YSLD, MBStyle, SQL y vector tiles.
- `07_Servicios_Cloud/`: plataformas SaaS y datos de ejercicios.
- `08_Arquitectura_SIG/`: arquitectura, GeoNode, Kepler.gl y storytelling.
- `img/`: recursos compartidos.
- `_config.yml`: configuracion actual de GitHub Pages/Jekyll.
- `package.json`: tooling Markdown historico; no representa una aplicacion de
  runtime.

La estructura objetivo propuesta en `UPGRADE_PLAN.md` separa documentacion,
ejemplos mantenidos, infraestructura, fixtures y material historico. No mover
directorios de forma masiva antes de aprobar y documentar la matriz de
migracion.

## Prioridad de trabajo

Implementar la modernizacion en este orden:

1. Inventario, privacidad, licencias y secretos.
2. Saneamiento editorial, estructura y controles minimos de CI.
3. Programa, horas, competencias, rubricas y prerrequisitos.
4. Fundamentos web, datos, cartografia y accesibilidad.
5. OGC clasico, OGC API Common/Features y STAC estatico.
6. PostGIS, GeoServer y servidor estatico reproducibles.
7. Cliente TypeScript/Vite/MapLibre.
8. MVT/PMTiles o COG, rendimiento e integracion.
9. Seguridad, publicacion, restauracion y piloto.

No iniciar una fase que dependa de decisiones pendientes de una fase anterior.
En particular, no convertir una tecnologia en requisito estudiantil hasta que
el ejemplo docente funcione desde un clon limpio.

## Planes de ejecucion

`UPGRADE_PLAN.md` define la hoja de ruta curricular y tecnica general. No
sustituye los planes de ejecucion detallados para cambios complejos. Antes de
planificar o implementar uno de esos cambios, leer `PLANS.md` completo y
seguirlo al pie de la letra.

Crear un ExecPlan cuando se cumpla al menos una condicion:

- El cambio toca mas de dos modulos o capas, por ejemplo frontend, servicios,
  pruebas y scripts.
- El cambio modifica un contrato publico de herramientas o una estructura de
  errores.
- El cambio requiere migracion, despliegue gradual o mitigacion explicita de
  riesgo.

Guardar cada ExecPlan en `plans/` con el nombre
`plan_<nnnn>_<objetivo>.md`, donde `<nnnn>` es un consecutivo de cuatro digitos
y `<objetivo>` usa minusculas separadas por guiones bajos. No reutilizar numeros
ni crear planes fuera de `plans/`.

Todo ExecPlan debe:

- Ser autocontenido y comprensible para una persona sin conocimiento previo del
  repositorio.
- Explicar primero el proposito y el comportamiento observable que habilitara.
- Definir en lenguaje sencillo cada termino especializado.
- Nombrar rutas relativas al repositorio, modulos, interfaces y comandos
  exactos, incluido el directorio de trabajo.
- Producir comportamiento funcional demostrable, no limitarse a cambios que
  compilan o satisfacen una lista interna.
- Incluir validacion de punta a punta, resultados esperados, idempotencia,
  recuperacion y alternativas seguras para operaciones riesgosas.
- Resolver las decisiones de implementacion dentro del plan y registrar su
  justificacion, en vez de trasladarlas a quien lo ejecute.
- Incluir hitos narrativos e independientes que produzcan incrementos
  verificables.
- Usar prototipos o pruebas de concepto cuando una dependencia, formato o
  arquitectura tenga riesgos o incognitas importantes.
- Mantener obligatoriamente las secciones `Progress`,
  `Surprises & Discoveries`, `Decision Log` y `Outcomes & Retrospective`.
- Seguir el esqueleto de `PLANS.md` e incluir tambien contexto y orientacion,
  plan de trabajo, pasos concretos, validacion y aceptacion, idempotencia y
  recuperacion, artefactos, interfaces y dependencias.
- Terminar con una nota que describa cada revision relevante y su motivo.

En un archivo `.md` cuyo unico contenido sea el ExecPlan, escribir Markdown
directamente, sin envolver todo el documento en una cerca de codigo. Preferir
prosa clara; evitar tablas, enumeraciones largas y listas de verificacion fuera
de `Progress`. Usar dos saltos de linea despues de cada encabezado, segun
`PLANS.md`.

Si el ExecPlan se presenta dentro de otro documento o mensaje, envolverlo en un
unico bloque cercado `md` y no anidar otras cercas. Esta envoltura se omite en
los archivos de plan guardados en `plans/`.

Durante la implementacion, tratar el ExecPlan como documento vivo:

- Actualizar `Progress` en cada punto de pausa con marcas de tiempo y estado
  real.
- Registrar hallazgos con evidencia en `Surprises & Discoveries`.
- Registrar cambios de rumbo y su razon en `Decision Log`.
- Resumir resultados, pendientes y lecciones en `Outcomes & Retrospective` al
  cerrar un hito o el plan.
- Continuar con el siguiente hito sin pedir al usuario que defina "siguientes
  pasos", salvo que exista un bloqueo que requiera una decision externa.
- Mantener los pasos idempotentes y las pruebas pasando durante migraciones o
  implementaciones paralelas.
- Al revisar el plan, reflejar cada cambio en todas las secciones afectadas para
  que el documento siga siendo autocontenido.

Los commits frecuentes mencionados en `PLANS.md` solo se realizan cuando el
usuario haya autorizado explicitamente crear commits para esa ejecucion. Sin
esa autorizacion, mantener cambios verificables sin confirmar y actualizar el
ExecPlan con el estado real.

## Alcance curricular

- El curso dispone de 32 horas presenciales y propone 40 horas de trabajo
  autonomo.
- El nucleo obligatorio debe caber en esos limites.
- OGC API Common y OGC API - Features son obligatorios.
- WMS y WFS se conservan como compatibilidad institucional.
- STAC estatico es obligatorio; STAC API es electiva hasta disponer de una
  implementacion local fijada.
- Cada proyecto elige una ruta de entrega: MVT/PMTiles para vector o COG para
  raster.
- Records, Processes, EDR, Coverages, Zarr, GeoParquet, OpenLayers avanzado y
  3D son contenidos panoramicos o electivos.
- GitHub Pages, GitHub Actions y otros SaaS son implementaciones de referencia,
  no requisitos exclusivos.

No ampliar el nucleo obligatorio sin ajustar horas, rubricas y criterios del
piloto.

## Seguridad, privacidad y licencias

Estas reglas son bloqueantes:

- No agregar secretos, contrasenas, tokens activos ni credenciales reales.
- No reutilizar tokens Mapbox presentes en ejemplos historicos. Deben revocarse
  o reemplazarse por configuracion ficticia/restringida durante la fase
  correspondiente.
- No depender de IPs o servidores de cohortes anteriores.
- No publicar endpoints HTTP inseguros, salvo `localhost` para desarrollo.
- Tratar los datos sociales geolocalizados existentes como material en
  cuarentena. No copiarlos, transformarlos ni volverlos a publicar hasta que se
  resuelvan licencia, base de uso y riesgo de reidentificacion.
- Antes de agregar un dataset, registrar fuente, propietario, fecha o version,
  checksum, licencia, CRS, esquema y clasificacion de sensibilidad.
- No asumir que la licencia MIT cubre PDFs, imagenes, fuentes, datos o codigo de
  terceros. Registrar sus licencias por separado.
- Excluir del sitio publico cualquier material historico que no cumpla las
  politicas de seguridad, privacidad y licencia.

Si una tarea requiere reescribir el historial Git para retirar datos o secretos,
detenerse y solicitar aprobacion explicita. No ejecutar una reescritura de
historial como parte de un cambio ordinario.

## Convenciones de edicion

- Escribir el material docente en espanol claro y consistente.
- Preservar los nombres de rutas existentes hasta que su migracion este
  aprobada.
- Preferir cambios pequenos y verificables. No modernizar archivos no
  relacionados con la tarea actual.
- Usar enlaces relativos para recursos internos.
- Usar HTTPS para recursos externos siempre que sea posible.
- No editar binarios, PDFs o ZIP como si fueran sus fuentes. Localizar la fuente
  editable o reemplazarlos mediante una decision documentada.
- Considerar los arboles QGIS2Web como codigo generado. No hacer correcciones
  manuales extensas dentro de ellos; actualizar la fuente o archivarlos.
- Mantener `package-lock.json` sincronizado cuando se cambien dependencias npm.
- Fijar versiones en lockfiles, imagenes, extensiones y herramientas
  ejecutables. Evitar fijar versiones innecesarias en explicaciones
  conceptuales.
- No agregar un framework frontend al nucleo. La plantilla base usa TypeScript,
  Vite y MapLibre sin requerir React, Vue o Svelte.

## Diseno visual

Usar `DESIGN.md` como referencia visual para el sitio publico y los ejemplos
mantenidos. Adaptar su lenguaje de portafolio al contenido docente: mapas,
datos, ejercicios y explicaciones siguen siendo el contenido principal. No
copiar literalmente nombres, textos o componentes de la marca de referencia.

La direccion visual es una galeria editorial clara y contenida:

- Tema claro, superficies planas y composicion principalmente monocromatica.
- `#ffffff` para el lienzo y `#000000` para texto principal y controles de alto
  contraste.
- `#e5e5e5` y `#d4d4d4` para bandas de seccion; `#0a0a0a` y `#171717` para
  bloques oscuros con texto blanco.
- `#737373` y `#525252` solo para texto secundario cuando la combinacion supera
  WCAG 2.2 AA. No usar `#a3a3a3` como texto sobre blanco.
- Definir los valores como propiedades CSS con los nombres de `DESIGN.md`, en
  vez de repetir colores y espacios de forma literal en cada componente.
- Usar una sola familia sans serif. ABC Oracle solo se puede incorporar si su
  licencia y archivos estan documentados; de lo contrario usar Inter o la pila
  de fuentes del sistema indicada en `DESIGN.md`.
- Mantener 14px como apariencia base mediante unidades relativas, por ejemplo
  `0.875rem`, y pesos 400/500. Conservar encabezados HTML semanticos aunque su
  jerarquia visual use peso y espacio en vez de aumentar el tamano.
- Usar interlineado 1.43 para prosa. No usar interlineado 1.0 en texto de varias
  lineas.
- Basar el espaciado en 6px y preferir los valores 6, 8, 12 y 48px, con
  separaciones de seccion entre 48 y 96px.
- Mantener radio de borde 0, sin sombras, degradados, brillos ni elevacion.
- Alinear el texto a la izquierda y usar espacio en blanco para crear jerarquia.
  No centrar bloques editoriales ni superponer texto sobre imagenes.
- Usar imagenes grandes, sin bordes ni recortes decorativos, solo cuando tengan
  licencia, procedencia y texto alternativo. No introducir fotografias de
  relleno para imitar el portafolio de referencia.
- Evitar iconos decorativos y ornamentos. Los iconos funcionales deben tener
  nombre accesible y no sustituir etiquetas necesarias.

Los ejemplos cartograficos pueden apartarse de la composicion de portafolio
cuando la funcion lo exija. Mapas, leyendas, atribuciones, controles, tablas y
mensajes de estado no deben eliminarse para obtener una pagina mas minimalista.
Evitar controles sobre el mapa cuando puedan situarse fuera; se permiten los
controles y atribuciones superpuestos que requiera la biblioteca, siempre que
sean legibles y operables.

La referencia visual no prevalece sobre accesibilidad:

- Todos los controles interactivos deben tener estados de foco visibles. La
  indicacion de `DESIGN.md` de no usar estados hover no elimina los estados de
  foco, activo, seleccionado, carga o error.
- Los enlaces dentro de prosa deben distinguirse sin depender solo del color,
  por ejemplo mediante subrayado.
- Respetar zoom, preferencias de fuente y reflow; no bloquear el escalado para
  conservar una medida visual exacta.
- Verificar contraste sobre cada banda clara u oscura y en controles de mapa.
- No usar las bandas grises puramente decorativas si agregan ruido, desplazan
  contenido esencial o dificultan la navegacion.
- Mantener alternativas textuales o tabulares para visualizaciones, aunque no
  formen parte de la composicion descrita en `DESIGN.md`.

No agregar Tailwind solo porque `DESIGN.md` incluya un ejemplo de tema. Preferir
CSS nativo y propiedades personalizadas en el cliente base. Adoptar Tailwind u
otra dependencia requiere una necesidad concreta, justificacion y, si el
cambio cumple los criterios, un ExecPlan.

## Accesibilidad

El objetivo es WCAG 2.2 nivel AA para el sitio, ejemplos y entregas.

- Todos los controles deben funcionar con teclado y mostrar foco visible.
- No depender unicamente de color, posicion, hover o gestos de arrastre.
- Proporcionar leyenda, atribucion y mensajes de carga/error comprensibles.
- Acompanar los mapas con tabla, resumen o descarga equivalente de los datos o
  hallazgos principales.
- Proporcionar texto alternativo util para contenido no textual.
- Los videos deben incluir subtitulos o transcripcion.
- Las comprobaciones automaticas no sustituyen la revision manual.
- Una excepcion solo procede como conformidad parcial para contenido de terceros
  fuera de control y debe incluir una alternativa accesible.

## Infraestructura objetivo

El stack obligatorio debe poder reconstruirse localmente mediante Docker
Compose e incluye:

- PostgreSQL/PostGIS.
- GeoServer 3.x con modulos compatibles de OGC API - Features y Vector Tiles.
- Un servidor estatico con soporte de HTTP Range y CORS para PMTiles/COG.
- Configuracion de GeoServer versionada mediante un data directory saneado o
  scripts REST idempotentes.
- Healthchecks y smoke tests para PostGIS, WMS/WFS y OGC API - Features.

Usar secretos por archivo cuando las imagenes lo permitan. Las interfaces
administrativas deben enlazarse solo a `localhost` en desarrollo. No asumir que
un volumen persistente equivale a configuracion reproducible.

El cliente MapLibre debe fijar y probar:

- El paquete `pmtiles` para la ruta vectorial.
- `@geomatico/maplibre-cog-protocol` para la ruta raster.
- La cadena completa desde HTTP Range hasta visualizacion.

## Validacion

Actualmente no existe una suite de pruebas del proyecto. El unico script npm es
`npm run precommit`, que ejecuta Prettier con `--write` y `git add`. No usarlo
como comprobacion de solo lectura porque modifica archivos y el indice Git.

Comprobaciones seguras disponibles:

```powershell
git status --short
git diff --check
npx prettier --check "**/*.md"
```

Usar `npx prettier --check` solo cuando las dependencias locales ya esten
instaladas; evitar descargas implicitas durante una revision offline.

Para probar HTML y cargas de archivos locales, servir el repositorio por HTTP:

```powershell
python -m http.server 8000
```

No evaluar ejemplos que usan `fetch` o AJAX mediante `file://`.

Cuando se implemente el plan, cada comprobacion de CI debe tener un comando
local equivalente. La validacion objetivo incluye:

- Markdown, enlaces internos, HTML y CSS.
- GeoJSON semantico y geometria valida.
- XML/SLD, OpenAPI y STAC.
- COG, PMTiles, MVT, MapLibre Style y HTTP Range.
- Compose, healthchecks y consultas de integracion.
- Lint, pruebas, build y accesibilidad del frontend.
- Ejecucion completa de notebooks obligatorios.
- Secretos, licencias y vulnerabilidades.

## Git y alcance de cambios

- Revisar `git status`, `git diff` y el historial reciente antes de confirmar
  cambios.
- Incluir en cada commit solo los archivos relacionados con la tarea.
- No modificar, revertir ni eliminar cambios ajenos.
- No usar comandos destructivos ni reescribir historial sin solicitud
  explicita.
- No crear commits, tags, releases o pushes salvo solicitud del usuario.
- Mantener mensajes de commit breves y coherentes con el historial en espanol.

## Criterio de finalizacion

Un cambio esta terminado cuando:

- Cumple el alcance solicitado y la fase correspondiente de `UPGRADE_PLAN.md`.
- No introduce cuentas SaaS, secretos o infraestructura externa obligatoria.
- Incluye documentacion, atribucion y licencia cuando agrega datos o recursos.
- Aplica `DESIGN.md` en interfaces nuevas o modificadas sin degradar la
  semantica, la funcionalidad cartografica ni la accesibilidad.
- Mantiene o mejora WCAG 2.2 AA en el alcance afectado.
- Puede ejecutarse o verificarse desde un clon limpio con instrucciones
  documentadas.
- Ejecuta las comprobaciones disponibles y reporta las que no pudieron
  realizarse.
- `git diff --check` no reporta errores.
