# plan_0011 - Enriquecer fundamentos web desde el material histórico

**Fecha**: 2026-08-03

**Ámbito**: `docs/unidades/01_web_git_publicacion.md`,
`examples/leaflet/mapa_basico/`, `docs/evaluacion/entrega_1.md` y trazabilidad
curricular.

**Estado**: cerrado técnicamente; revisión manual transversal pendiente en
`plan_0001`

**Prioridad**: alta; mejora la autonomía conceptual de la Unidad 1 sin ampliar
sus cuatro horas presenciales.

Este ExecPlan es un documento vivo. Debe mantenerse conforme a `PLANS.md`,
`AGENTS.md`, `UPGRADE_PLAN.md` y `DESIGN.md`.

## Propósito / Panorama general

Después de implementar este plan, una persona podrá explicar cómo una URL lleva
una solicitud desde un navegador a un servidor y cómo la respuesta carga HTML,
CSS, JavaScript, datos y un mapa. Podrá observar ese recorrido en las
herramientas de desarrollo del navegador, identificar un código HTTP, distinguir
Internet de Web y explicar por qué una página publicada necesita HTTPS, rutas
correctas y un servidor HTTP.

La Unidad 1 conservará su producto actual, el mapa Leaflet accesible servido
localmente, pero lo usará como evidencia del modelo cliente-servidor. No
dependerá de cuentas GitHub, servicios institucionales, recursos HTTP inseguros,
estadísticas históricas ni imágenes del PDF de 2020.

## Progress

- [x] (2026-08-03) Se analizaron las 78 páginas de
      `01_Fundamentos/01_Fundamentos_Internet.pdf` y `01_Fundamentos/Readme.md`
      para separar conceptos vigentes de instrucciones históricas.
- [x] (2026-08-03) Se clasificaron los conceptos útiles del PDF y se excluyeron
      capturas, estadísticas, cuentas, HTTP inseguro y tecnologías históricas
      del núcleo mantenido.
- [x] (2026-08-03) Se reescribió `docs/unidades/01_web_git_publicacion.md` con
      Internet, Web, URL, navegador, cliente-servidor, HTTP, HTTPS, origen y
      caché.
- [x] (2026-08-03) Se añadieron diagramas textuales, práctica de inspección de
      red, Markdown local, panorama posterior y autoevaluación ampliada.
- [x] (2026-08-03) Se mantuvo la trazabilidad existente porque las nuevas
      actividades usan los mismos artefactos y validaciones de Unidad 1.
- [x] (2026-08-03) Pasaron Markdownlint, las dos pruebas Leaflet, build y 41
       enlaces internos. La inspección manual de red y accesibilidad permanece
       como evidencia transversal del piloto en `plan_0001`.

## Surprises & Discoveries

- Observación: el PDF histórico contiene conceptos de red, cliente-servidor,
  URL, navegador, HTTP, HTTPS, caché y tecnologías web que siguen siendo
  didácticamente útiles. Evidencia: páginas 9 a 36, 41 a 46 y 68 a 77 de
  `01_Fundamentos/01_Fundamentos_Internet.pdf`.

- Observación: el PDF mezcla contenido vigente con ejemplos incompatibles con el
  núcleo actual, como HTTP inseguro, Flash/Flex, HTML con atributos de
  presentación, JavaScript inline, capturas de interfaces antiguas y
  estadísticas de 2017. Evidencia: páginas 12, 25, 32 a 36, 72 a 74 y capturas
  de servicios de la cohorte histórica.

- Observación: XML, GML, KML, REST y APIs aparecen en el PDF, pero su
  explicación detallada pertenece a las Unidades 2 y 4. Evidencia: páginas 49 a
  67 del PDF y `Programa.md` líneas 60 a 78.

## Decision Log

- Decisión: mantener el alcance presencial de la Unidad 1 en cuatro horas y
  trasladar profundizaciones de formatos geográficos, APIs y servicios a las
  unidades ya asignadas. Justificación: `Programa.md` distribuye explícitamente
  el núcleo en ocho unidades de cuatro horas; enriquecer no significa ampliar
  silenciosamente el currículo. Fecha/Autor: 2026-08-03 / OpenCode.

- Decisión: conservar el PDF como fuente histórica de ideas, no como material
  público obligatorio. Justificación: sus imágenes, capturas y fuentes requieren
  evaluación de licencia, accesibilidad y actualidad. El material docente
  mantenido se redacta directamente en Markdown accesible. Fecha/Autor:
  2026-08-03 / OpenCode.

- Decisión: usar el ejemplo Leaflet y las herramientas de desarrollo del
  navegador como demostración de solicitud-respuesta. Justificación: el ejemplo
  es local, token-free, accesible y ya tiene pruebas; evita depender de sitios
  externos para explicar HTTP. Fecha/Autor: 2026-08-03 / OpenCode.

## Outcomes & Retrospective

La Unidad 1 ya explica HTML, CSS, JavaScript, `fetch`, Git y publicación
estática. Este plan incorporó el modelo de red y navegador, URL, HTTPS, caché y
arquitectura inicial sin duplicar contenidos de datos, APIs, infraestructura o
rendimiento. El PDF histórico permanece como fuente de ideas no publicada; sus
capturas, estadísticas, cuentas obligatorias y tecnologías retiradas no se
migraron.

## Contexto y orientación

`01_Fundamentos/01_Fundamentos_Internet.pdf` es una presentación histórica de 78
páginas. Su contenido no se debe editar ni publicar de nuevo como fuente docente
mantenida. `01_Fundamentos/Readme.md` añade ejercicios asociados, pero exige
cuentas personales, repositorios públicos individuales, issues del curso y
GitHub Pages. Esos requisitos no se migran porque el curso moderno funciona
localmente y no exige SaaS.

`docs/unidades/01_web_git_publicacion.md` es la unidad mantenida y se publica en
`/unidades/01-web-git-publicacion/`. `examples/leaflet/mapa_basico/` es su
ejemplo ejecutable. La página carga `data/referencia.geojson` mediante `fetch`,
equivalente.

Internet es una red de redes que intercambian información mediante protocolos.
La Web es un sistema que usa Internet para enlazar recursos mediante URLs e
hipertexto. HTTP define una solicitud y una respuesta; HTTPS protege esa
comunicación mediante TLS. Una URL identifica un recurso y contiene, según el
caso, esquema, host, puerto, ruta, parámetros de consulta y fragmento. Un
navegador solicita recursos, interpreta HTML/CSS/JavaScript y muestra los
resultados. Un servidor estático entrega archivos ya construidos; un servidor de
aplicación puede ejecutar lógica y un servidor geoespacial puede entregar
imágenes, entidades o teselas.

La caché conserva temporalmente recursos para evitar solicitudes repetidas.
Puede existir en navegador, proxy o servidor. No debe confundirse con una copia
autorizada para descarga offline ni con un mecanismo para precargar teselas de
un proveedor público.

## Plan de trabajo

Reescribir la apertura de `docs/unidades/01_web_git_publicacion.md` para incluir
una sección "Internet, Web y publicación". Debe definir Internet, Web,
protocolo, recurso, URL, navegador, servidor y cliente con lenguaje claro.
Añadir una tabla breve que distinga Internet, Web, servidor estático, API,
servidor de mapas y cliente web, sin desarrollar todavía contratos OGC.

Añadir una sección "Anatomía de una URL" con una URL ficticia y segura, por
ejemplo:

    https://curso.example.org:443/unidades/01?tema=http#practica

Explicar cada componente. La URL no incluirá credenciales ni ejemplos de
`userinfo`, porque las contraseñas no deben viajar en URLs ni aparecer en
material docente.

Añadir una sección "Del navegador al mapa" con un diagrama textual accesible:

    Navegador
      -> GET /examples/leaflet/mapa_basico/
      <- HTML, CSS y JavaScript
      -> GET /examples/leaflet/mapa_basico/data/referencia.geojson
      <- GeoJSON con HTTP 200
      -> Renderiza la capa, la leyenda, el estado y la tabla

Explicar que `file://` no ofrece el mismo recorrido y que la práctica debe
servirse por HTTP. Mostrar los códigos 200, 404 y 500 sin trasladar el análisis
completo de HTTP a la Unidad 4.

Añadir una sección "HTTPS, origen y caché" que enseñe por qué la publicación usa
HTTPS, cómo un origen se forma por esquema/host/puerto y cómo la caché puede
explicar una respuesta rápida o un recurso antiguo. Mencionar que CORS,
cabeceras, APIs, XML, JSON, GML, KML, REST y servicios OGC se profundizan en las
Unidades 2, 4 y 7.

Añadir una sección "Arquitectura de una publicación cartográfica" que conecte el
ejemplo actual con los componentes que aparecerán después:

    Datos y manifiesto -> cliente Leaflet/MapLibre -> servidor estático
    Datos y servicios locales -> PostGIS/GeoServer -> cliente MapLibre
    PMTiles/COG -> servidor Range -> protocolo MapLibre

Debe ser una introducción, no una guía de Docker, OGC API o COG.

Actualizar la práctica guiada. Después de servir el repositorio, la persona
abrirá las herramientas de desarrollo, seleccionará la solicitud GeoJSON y
registrará URL, método, estado, tipo de contenido, tamaño y si la respuesta vino
de caché. También probará una URL inexistente en una copia temporal para
observar 404 y restaurará el archivo antes de terminar.

Añadir una actividad de Markdown que cree una nota de proyecto local sin datos
personales, con encabezado, lista, enlace relativo y bloque de código. La
actividad se evaluará mediante Markdownlint, no mediante una cuenta GitHub o
issue remoto.

Añadir una subsección "Panorama posterior" para nombrar XML/GML/KML, RPC/SOAP,
APIs REST, frameworks, clientes de escritorio, móviles y servidores de
aplicación. Cada término tendrá una frase de orientación y un enlace a la unidad
posterior correspondiente. Flash/Flex se nombrará únicamente como tecnología
histórica retirada, sin ejercicio.

Actualizar `docs/governance/curriculum-traceability.yml` solo si la nueva
actividad de inspección de red o Markdown requiere una validación adicional.
Mantener la misma rúbrica `docs/evaluacion/entrega_1.md`.

## Pasos concretos

Desde `C:\opt\work\personal\cartografia_web`, ejecutar durante la
implementación:

    npm run lint:markdown
    npm run test:a11y
    npm run build
    npm run links:internal
    git diff --check

Para comprobar el recorrido HTTP, servir el artefacto:

    python -m http.server 8000 --directory _site

Abrir:

    http://localhost:8000/examples/leaflet/mapa_basico/

En las herramientas de desarrollo del navegador, abrir la pestaña Network,
recargar la página y seleccionar `referencia.geojson`. El resultado esperado es
un `GET` con HTTP 200 y contenido GeoJSON. En una copia temporal del ejemplo,
cambiar la ruta del archivo para provocar un 404; el estado visible debe
comunicar que no fue posible cargar los datos.

## Validación y aceptación

La ampliación se acepta cuando una persona puede:

- Diferenciar Internet, Web, navegador, cliente, servidor, protocolo y URL.
- Identificar esquema, host, puerto, ruta, query y fragmento de una URL segura.
- Explicar la secuencia que carga HTML, CSS, JavaScript y GeoJSON.
- Explicar por qué `file://` no sustituye un servidor HTTP.
- Identificar 200, 404 y 500 en el contexto del ejemplo.
- Explicar qué aporta HTTPS y qué puede hacer la caché.
- Distinguir el núcleo de Unidad 1 de los temas que se profundizan después.
- Completar la práctica Leaflet y la nota Markdown local sin cuenta externa.

Deben pasar `npm run lint:markdown`, `npm run test:a11y`, `npm run build`,
`npm run links:internal` y `git diff --check`. La revisión manual confirma foco,
comprensibles sin imagen.

## Idempotencia y recuperación

Las validaciones no modifican fuentes. La actividad de error se realiza en una
copia temporal o restaurando inmediatamente la ruta original. Si la caché impide
observar una solicitud, usar una ventana privada o desactivar caché en
herramientas de desarrollo; no cambiar el fixture. No agregar cuentas, tokens,
servidores externos ni secretos para completar las actividades.

## Artefactos y notas

El PDF histórico permanece en `01_Fundamentos/01_Fundamentos_Internet.pdf` y no
se publica desde el sitio mantenido. La unidad final puede citar el PDF en
`docs/migration-inventory.md` como fuente histórica revisada, pero no copia sus
imágenes, estadísticas ni capturas. Los conceptos reutilizados se redactan y
verifican en Markdown.

## Interfaces y dependencias

No agregar frameworks, bibliotecas ni dependencias. Usar HTML semántico, CSS
nativo, JavaScript modular, Leaflet vendorizado, OpenStreetMap con atribución
visible, Python HTTP server y herramientas de desarrollo del navegador. GitHub
Pages sigue siendo un adaptador de publicación, no un requisito de estudiantes.

## Revisión

2026-08-03: plan propuesto tras analizar las 78 páginas del PDF histórico y
`01_Fundamentos/Readme.md`. Conserva fundamentos de red, Web, URL, navegador,
cliente-servidor, HTTP, HTTPS, caché y tecnologías web; actualiza HTML/CSS/JS y
excluye instrucciones de cuentas, issues, capturas, HTTP inseguro, Flash/Flex,
estadísticas históricas y material sin licencia resuelta.

2026-08-03: cerrado técnicamente tras ampliar la unidad y validar Markdown,
Leaflet, build y enlaces. La revisión manual de red, foco, reflow y contraste se
mantiene como evidencia transversal del plan principal.
