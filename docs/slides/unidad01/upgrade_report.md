# Análisis de modernización — Publicación de cartografía para la web

<!-- markdownlint-disable MD024 -->

## 1. Resumen ejecutivo

- **Fecha de corte:** 5 de agosto de 2026.
- **Audiencia identificada:** estudiantes hispanohablantes de Especialización en
  Geomática que inician el curso de publicación de cartografía web.
- **Propósito identificado:** capacitar.
- **Ámbito geográfico o jurisdicción:** global, con contexto académico
  colombiano.
- **Profundidad identificada:** académica y técnica introductoria.
- **Diapositivas analizadas:** 78.
- **Diapositivas con hallazgos:** 69. Los hallazgos se agrupan cuando varias
  diapositivas deben sustituirse o trasladarse como una misma decisión
  editorial.
- **Nivel general de desactualización:** alto.
- **Principales riesgos:** cifras sin fecha que presentan 2015/2017 como
  actualidad; ejemplos con HTTP inseguro, enlaces de cohortes anteriores y SaaS
  como requisito; tecnologías retiradas o sin soporte; explicación demasiado
  simplificada de HTTP, API, REST y JSON; y capturas sin licencia resuelta ni
  alternativa textual suficiente.
- **Actualizaciones prioritarias:** sustituir las cifras de conectividad,
  reescribir los ejemplos HTML/JavaScript y HTTP, retirar Flash/Xamarin como
  opciones vigentes, eliminar dependencias de GitHub Pages y trasladar formatos,
  APIs, servidores y rendimiento a las unidades que los cubren en el programa
  actual.
- **Limitaciones del análisis:** no se verificó la vigencia del correo de la
  portada ni la autorización de cada captura histórica. La fuente oficial de
  Adobe para la fecha de fin de Flash no respondió durante la revisión; por ello
  no se incorpora una fecha de fin de soporte sin marcarla como pendiente. Las
  licencias de las imágenes extraídas siguen pendientes de revisión conforme a
  la política del repositorio.

## 2. Hallazgos por diapositiva

### Diapositiva 1 — Publicación de cartografía para la web

- **Prioridad:** media.
- **Categoría:** referencia.
- **Confianza:** media.
- **Contenido original:** “`juan@gkudos.com`” y un icono de licencia Creative
  Commons sin texto legible.
- **Problema detectado:** el correo público no está verificado y la licencia de
  la presentación y sus capturas no queda expresada en texto. Una imagen de
  licencia no resuelve por sí sola el alcance de reutilización de recursos de
  terceros.
- **Evidencia verificable:** la política del repositorio aclara que MIT no cubre
  automáticamente PDF, capturas ni imágenes, y prohíbe que recursos sin licencia
  resuelta entren al sitio público.
- **Estado de la evidencia:** verificado.
- **Fecha del dato:** 3 de agosto de 2026.
- **Fuente:**
  [Repositorio, Política de Licencias Inicial, 3 de agosto de 2026](../../governance/licenses.md).
- **Recomendación:** sustituir el correo por un canal institucional configurable
  y añadir una atribución de autoría y licencia en texto, tras comprobar ambas.
- **Impacto narrativo:** evita que la portada publique un contacto o una
  licencia no confirmados.

#### Contenido propuesto

```md
---
layout: cover
---

# Publicación de cartografía para la web

Unidad 1. Web, Git y publicación

Especialización en Geomática

<!-- REQUIERE VERIFICACIÓN: confirmar el canal institucional de contacto y la
licencia aplicable a la presentación y a cada recurso visual antes de publicar. -->
```

### Diapositiva 3 — Objetivo

- **Prioridad:** alta.
- **Categoría:** estructura.
- **Confianza:** alta.
- **Contenido original:** “Conocer los conceptos y tecnologías básicas
  utilizadas para la publicación de contenido y servicios en internet”.
- **Problema detectado:** el objetivo no es observable y omite HTML semántico,
  CSS responsive, JavaScript moderno, Git, publicación estática, accesibilidad y
  el producto verificable definidos para la Unidad 1 vigente.
- **Evidencia verificable:** el programa actual fija como producto un mapa
  Leaflet básico construido localmente y define esos contenidos para la
  Unidad 1.
- **Estado de la evidencia:** verificado.
- **Fecha del dato:** 3 de agosto de 2026.
- **Fuente:**
  [Programa del curso, Unidad 1. Web, Git y publicación, 3 de agosto de 2026](../../../Programa.md).
- **Recomendación:** reemplazar el objetivo por resultados observables alineados
  con el mapa servido por HTTP local.
- **Impacto narrativo:** convierte la introducción en una ruta que cabe en las
  cuatro horas presenciales de la unidad.

#### Contenido propuesto

```md
---
layout: default
---

# Resultado de la unidad

Al finalizar podrás explicar cómo el navegador solicita recursos a un servidor
estático y publicar un mapa Leaflet básico que:

- usa HTML semántico, CSS responsive y JavaScript modular;
- carga datos mediante `fetch` y comunica errores HTTP;
- conserva leyenda, atribución y una tabla equivalente; y
- se ejecuta localmente sin cuenta SaaS, token ni IP histórica.

<!--
Fuentes:
- Programa del curso, Unidad 1. Web, Git y publicación, 2026-08-03:
  ../../../Programa.md
-->
```

### Diapositivas 4–5 — Infografías de conectividad y “Data Never Sleeps”

- **Prioridad:** crítica.
- **Categoría:** estadística.
- **Confianza:** alta.
- **Contenido original:** “World Population 7.3 Billion”, “Estimated number of
  internet users 3.010 Billion” y una infografía de 2017 sin cita ni fecha
  visible en la diapositiva.
- **Problema detectado:** la primera cifra corresponde a un contexto histórico
  no rotulado y la segunda infografía no aporta una conclusión curricular
  verificable. Ambas pueden interpretarse como datos actuales.
- **Evidencia verificable:** el último dato disponible antes de la fecha de
  corte indica que, en 2025, casi tres cuartas partes de la población mundial
  estaban conectadas y 2.2 mil millones de personas seguían desconectadas.
- **Estado de la evidencia:** último dato disponible.
- **Fecha del dato:** 2025; publicación de la ITU en noviembre de 2025.
- **Fuente:**
  [International Telecommunication Union, _Measuring digital development: Facts and Figures 2025_, 2025](https://www.itu.int/itu-d/reports/statistics/facts-figures-2025/).
- **Recomendación:** reemplazar ambas imágenes por una sola diapositiva textual
  con fecha, fuente y una pregunta sobre brecha de conectividad. No reutilizar
  la infografía de terceros sin licencia documentada.
- **Impacto narrativo:** actualiza el contexto sin convertir una cifra global en
  un dato decorativo.

#### Contenido propuesto

```md
---
layout: default
---

# Conectividad global: contexto, no garantía de acceso

**Último dato disponible: 2025.** Casi tres cuartas partes de la población
mundial estaban en línea, pero **2.2 mil millones de personas** seguían sin
conexión.

La disponibilidad, la calidad y el costo de la conectividad condicionan cómo se
publican y usan mapas web. Diseñar para una conexión limitada sigue siendo parte
del problema técnico.

<!--
Fuentes:
- International Telecommunication Union, Measuring digital development: Facts
  and Figures 2025, 2025:
  https://www.itu.int/itu-d/reports/statistics/facts-figures-2025/
-->
```

### Diapositivas 7–8 — Mapa de Facebook y captura de _The IT Crowd_

- **Prioridad:** alta.
- **Categoría:** estructura.
- **Confianza:** alta.
- **Contenido original:** un mapa de “Facebook” y una captura con el texto “THIS
  JEN, IS THE INTERNET.”
- **Problema detectado:** ambas imágenes son referencias históricas de terceros
  sin atribución, licencia ni relación verificable con el resultado de
  aprendizaje. La segunda no añade contenido técnico.
- **Evidencia verificable:** los recursos visuales sin licencia resuelta no
  pueden entrar al sitio público ni a fixtures de curso.
- **Estado de la evidencia:** verificado.
- **Fecha del dato:** 3 de agosto de 2026.
- **Fuente:**
  [Repositorio, Política de Licencias Inicial, 3 de agosto de 2026](../../governance/licenses.md).
- **Recomendación:** retirar ambas imágenes. Conservar, si se necesita una
  transición, una pregunta textual sobre qué redes y protocolos intervienen al
  cargar el mapa local de la práctica.
- **Impacto narrativo:** reduce distracción, riesgo de licencia y tiempo de
  exposición.

#### Contenido propuesto

```md
---
layout: center
---

# Antes de abrir un mapa web

¿Qué recursos solicita el navegador y qué sistema responde cada uno?

En esta unidad observaremos HTML, CSS, JavaScript y GeoJSON desde las
herramientas de desarrollo del navegador.
```

### Diapositiva 9 — Qué es Internet?

- **Prioridad:** baja.
- **Categoría:** terminología.
- **Confianza:** alta.
- **Contenido original:** “Es un esfuerzo cooperativo regido por un estándares.”
- **Problema detectado:** contiene un error de concordancia y no identifica que
  los protocolos y estándares permiten interoperabilidad; la afirmación sobre
  propiedad es correcta pero insuficiente para el objetivo didáctico.
- **Evidencia verificable:** HTTP se define como un protocolo de aplicación con
  semántica común, independiente de la implementación de recursos y servicios.
- **Estado de la evidencia:** verificado.
- **Fecha del dato:** junio de 2022.
- **Fuente:**
  [IETF, RFC 9110: HTTP Semantics, junio de 2022](https://www.rfc-editor.org/rfc/rfc9110.html).
- **Recomendación:** corregir el texto y enlazar el concepto de red con la idea
  de protocolos interoperables, sin intentar explicar la gobernanza completa de
  Internet.
- **Impacto narrativo:** prepara la diferencia posterior entre Internet, Web y
  HTTP.

#### Contenido propuesto

```md
---
layout: default
---

# Qué es Internet?

- Es una red de redes que conecta sistemas independientes.
- Ninguna organización posee Internet en su conjunto.
- La interoperabilidad depende de protocolos y estándares compartidos.
- Su función es transportar información entre sistemas; la Web es uno de los
  sistemas que usa esa infraestructura.

<!--
Fuentes:
- IETF, RFC 9110: HTTP Semantics, 2022-06:
  https://www.rfc-editor.org/rfc/rfc9110.html
-->
```

### Diapositivas 12–15 — HTTP, URL, hipertexto y HTTPS

- **Prioridad:** crítica.
- **Categoría:** tecnología.
- **Confianza:** alta.
- **Contenido original:** un enlace `http://www.elespectador.com/`, una URL con
  `john.doe:password@`, una definición de hipertexto y “HTTPS: Extensión de
  Http”.
- **Problema detectado:** enseña una URL HTTP externa insegura, muestra una
  contraseña dentro de una URL y simplifica HTTPS de forma imprecisa. El uso de
  información de usuario en URI HTTP(S) está desaconsejado y los ejemplos del
  curso deben reservar HTTP para `localhost`.
- **Evidencia verificable:** RFC 9110 define los esquemas `http` y `https` y
  desaconseja `userinfo` en URI HTTP(S); el estándar URL define las partes y las
  consideraciones de seguridad de una URL. OGC API - Features espera que la
  mayoría de servidores use HTTPS.
- **Estado de la evidencia:** verificado.
- **Fecha del dato:** junio de 2022; julio de 2026; mayo de 2022.
- **Fuente:**
  [IETF, RFC 9110: HTTP Semantics, junio de 2022](https://www.rfc-editor.org/rfc/rfc9110.html);
  [WHATWG, URL Standard, 6 de julio de 2026](https://url.spec.whatwg.org/);
  [OGC, OGC API - Features Part 1: Core corrigendum, 11 de mayo de 2022](https://docs.ogc.org/is/17-069r4/17-069r4.html).
- **Recomendación:** condensar las cuatro diapositivas en dos: una para URL y
  otra para HTTP/HTTPS. Usar un host ficticio HTTPS, eliminar credenciales del
  diagrama e indicar que el fragmento no se envía al servidor.
- **Impacto narrativo:** elimina un patrón inseguro que puede reproducirse en
  entregas estudiantiles.

#### Contenido propuesto

````md
---
layout: two-cols
---

# URL, HTTP y HTTPS

::left::

Una URL identifica un recurso web:

```text
https://curso.example.org:443/mapas?tema=http#practica
```

- `https`: esquema seguro.
- `curso.example.org`: host.
- `443`: puerto habitual de HTTPS.
- Ruta, consulta y fragmento localizan o describen el recurso.

::right::

HTTP define cómo un cliente solicita una representación y cómo un servidor
responde. HTTPS usa HTTP sobre una conexión protegida por TLS.

No incluya contraseñas, tokens ni datos personales en una URL. El fragmento
`#practica` lo usa el navegador y no se envía al servidor.

<!--
Fuentes:
- IETF, RFC 9110: HTTP Semantics, 2022-06:
  https://www.rfc-editor.org/rfc/rfc9110.html
- WHATWG, URL Standard, 2026-07-06: https://url.spec.whatwg.org/
-->
````

### Diapositiva 17 — Herramientas de desarrollo del navegador

- **Prioridad:** media.
- **Categoría:** caso de estudio.
- **Confianza:** alta.
- **Contenido original:** captura de un sitio periodístico y una pestaña Network
  de navegador.
- **Problema detectado:** la captura no ofrece un procedimiento reproducible y
  depende de un sitio externo que puede cambiar. No conecta la observación con
  el GeoJSON y el mapa de la práctica vigente.
- **Evidencia verificable:** la Unidad 1 actual solicita observar URL, método,
  código de estado, tipo de contenido, tamaño y procedencia de caché para el
  recurso local `referencia.geojson`.
- **Estado de la evidencia:** verificado.
- **Fecha del dato:** 3 de agosto de 2026.
- **Fuente:**
  [Unidad 1. Web, Git y publicación, Del navegador al mapa, 3 de agosto de 2026](../../unidades/01_web_git_publicacion.md).
- **Recomendación:** crear una captura propia del ejemplo mantenido o convertir
  la diapositiva en una instrucción de observación textual.
- **Impacto narrativo:** transforma una imagen pasiva en evidencia de la
  práctica.

#### Contenido propuesto

```md
---
layout: default
---

# Observa una solicitud real

1. Abre las herramientas de desarrollo y la pestaña **Network**.
2. Recarga el mapa local.
3. Busca `data/referencia.geojson`.
4. Registra URL, método, código HTTP, tipo de contenido, tamaño y si la
   respuesta vino de caché.

La evidencia observada vale más que asumir que un recurso cargó porque el mapa
parece visible.

<!--
Fuentes:
- Unidad 1. Web, Git y publicación, 2026-08-03:
  ../../unidades/01_web_git_publicacion.md
-->
```

### Diapositivas 18–23 — Modelo cliente-servidor, IDE, arquitectura y clientes

- **Prioridad:** alta.
- **Categoría:** estructura.
- **Confianza:** alta.
- **Contenido original:** cuatro diagramas históricos y listas que mezclan
  entrega de datos, imágenes, filtros, procesamiento y clientes “ligeros” o
  “pesados”.
- **Problema detectado:** seis diapositivas repiten una arquitectura genérica y
  no distinguen con claridad datos, representaciones, cliente, servidor estático
  y servicios geoespaciales. Las imágenes externas requieren licencia y su texto
  no es una alternativa suficiente.
- **Evidencia verificable:** el curso actual usa una secuencia explícita entre
  datos/manifiesto, cliente Leaflet o MapLibre, servidor estático, PostGIS,
  GeoServer y activos PMTiles/COG.
- **Estado de la evidencia:** verificado.
- **Fecha del dato:** 3 de agosto de 2026.
- **Fuente:**
  [Unidad 1. Web, Git y publicación, Arquitectura de una publicación cartográfica, 3 de agosto de 2026](../../unidades/01_web_git_publicacion.md).
- **Recomendación:** sustituir el bloque por un único diagrama de texto propio y
  trasladar el procesamiento y los servidores de mapas a las Unidades 4 y 5.
- **Impacto narrativo:** libera tiempo para la práctica de publicación y elimina
  capturas no licenciadas.

#### Contenido propuesto

````md
---
layout: default
---

# Arquitectura mínima de una publicación cartográfica

```text
Datos y manifiesto -> cliente Leaflet o MapLibre -> servidor estático
Datos y servicios locales -> PostGIS y GeoServer -> cliente MapLibre
PMTiles o COG -> servidor con HTTP Range -> protocolo MapLibre
```

- El cliente solicita recursos y presenta una interfaz.
- Un servidor estático entrega archivos ya construidos.
- Un servicio geoespacial publica datos o representaciones con un contrato.

<!--
Fuentes:
- Unidad 1. Web, Git y publicación, 2026-08-03:
  ../../unidades/01_web_git_publicacion.md
-->
````

### Diapositiva 25 — Página Html Simple

- **Prioridad:** crítica.
- **Categoría:** tecnología.
- **Confianza:** alta.
- **Contenido original:** `<body bgcolor="white" text="red">` y una página sin
  `<!doctype html>`, idioma, codificación, viewport ni estructura semántica.
- **Problema detectado:** presenta atributos de estilo heredados como ejemplo de
  HTML inicial y no enseña la separación entre estructura, estilos y
  comportamiento que exige el curso.
- **Evidencia verificable:** el estándar HTML vigente se mantiene como _Living
  Standard_ y documenta requisitos de autoría, elementos semánticos, metadatos y
  características obsoletas.
- **Estado de la evidencia:** verificado.
- **Fecha del dato:** 20 de julio de 2026.
- **Fuente:**
  [WHATWG, HTML Living Standard, 20 de julio de 2026](https://html.spec.whatwg.org/multipage/).
- **Recomendación:** reemplazar el ejemplo por HTML semántico mínimo, con
  `lang`, `charset`, `viewport` y una región `main`. Enseñar color desde CSS, no
  desde atributos presentacionales.
- **Impacto narrativo:** impide que la primera práctica establezca patrones
  obsoletos.

#### Contenido propuesto

````md
---
layout: two-cols
---

# Una página HTML mínima y semántica

::left::

```html
<!doctype html>
<html lang="es">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Mi primera página</title>
  </head>
  <body>
    <main>
      <h1>Mi primera página</h1>
      <p>Esta es mi primera página web.</p>
    </main>
  </body>
</html>
```

::right::

HTML comunica estructura y significado. CSS controla la presentación y
JavaScript añade comportamiento cuando hace falta.

<!--
Fuentes:
- WHATWG, HTML Living Standard, 2026-07-20:
  https://html.spec.whatwg.org/multipage/
-->
````

### Diapositivas 26–28 — Ejercicio y publicación de `hello.html`

- **Prioridad:** alta.
- **Categoría:** tecnología.
- **Confianza:** alta.
- **Contenido original:** crear `hello.html`, abrirlo en el navegador y
  publicarlo mediante un enlace de GitHub Pages de una cuenta histórica.
- **Problema detectado:** abrir directamente un archivo no comprueba solicitudes
  HTTP ni `fetch`; el enlace depende de una cuenta y una ruta histórica; y
  GitHub Pages queda implícitamente como requisito.
- **Evidencia verificable:** GitHub Pages es un servicio de hosting estático que
  publica archivos desde un repositorio. El programa vigente lo conserva como
  referencia opcional y exige una ruta local sin SaaS.
- **Estado de la evidencia:** verificado.
- **Fecha del dato:** documentación sin fecha de publicación; consultada antes
  de la fecha de corte.
- **Fuente:**
  [GitHub, What is GitHub Pages?, sin fecha](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages);
  [Programa del curso, 3 de agosto de 2026](../../../Programa.md).
- **Recomendación:** servir el archivo con HTTP local, indicar el resultado
  esperado y presentar Pages como una implementación de referencia, no como el
  servidor obligatorio.
- **Impacto narrativo:** hace reproducible la práctica y evita dependencia de
  cuentas personales.

#### Contenido propuesto

```md
---
layout: default
---

# De un archivo a una publicación local

1. Crea `hello.html` con la estructura semántica de la diapositiva anterior.
2. Desde la raíz del repositorio, ejecuta `python -m http.server 8000`.
3. Abre `http://localhost:8000/hello.html`.
4. Observa la solicitud en **Network** y comprueba que responde con HTTP.

Un hosting estático entrega los mismos archivos mediante HTTPS. GitHub Pages es
una opción de referencia, no un requisito de esta actividad.

<!--
Fuentes:
- GitHub, What is GitHub Pages?, sin fecha:
  https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages
- Programa del curso, 2026-08-03: ../../../Programa.md
-->
```

### Diapositivas 29–35 — HTML, CSS y JavaScript

- **Prioridad:** alta.
- **Categoría:** tecnología.
- **Confianza:** alta.
- **Contenido original:** “Html 5 / Javascript / CSS”, “HTML5”, “CSS” y un
  ejemplo JavaScript que usa un controlador `onclick` en línea.
- **Problema detectado:** trata HTML como una versión cerrada, CSS como “CSS3” y
  JavaScript como cambios visuales aislados. El ejemplo mezcla contenido y
  comportamiento con un atributo en línea y no enseña módulos, `fetch`, manejo
  de errores ni responsive, que son resultados de la Unidad 1.
- **Evidencia verificable:** HTML y URL son estándares vivos; CSS se publica por
  módulos y el W3C mantiene snapshots de las partes implementables. La Unidad 1
  actual exige HTML semántico, CSS responsive, módulos ES, `fetch` y errores.
- **Estado de la evidencia:** verificado.
- **Fecha del dato:** 20, 6 y 29 de julio de 2026; 3 de agosto de 2026.
- **Fuente:**
  [WHATWG, HTML Living Standard, 20 de julio de 2026](https://html.spec.whatwg.org/multipage/);
  [W3C, Cascading Style Sheets, 29 de julio de 2026](https://www.w3.org/Style/CSS/Overview.en.html);
  [Unidad
  1. Web, Git y publicación, 3 de agosto de
     2026](../../unidades/01_web_git_publicacion.md).
- **Recomendación:** convertir el bloque de siete diapositivas en tres
  diapositivas: responsabilidades de cada lenguaje, CSS responsive y JavaScript
  modular con comprobación de `response.ok`.
- **Impacto narrativo:** alinea el código introductorio con el ejemplo Leaflet
  mantenido y elimina terminología de versiones engañosa.

#### Contenido propuesto

````md
---
layout: two-cols
---

# HTML, CSS y JavaScript cumplen funciones distintas

::left::

- **HTML:** estructura y significado.
- **CSS:** presentación adaptable, contraste y foco visible.
- **JavaScript:** comportamiento, carga de datos y mensajes de estado.

::right::

```js
const response = await fetch('data/referencia.geojson');
if (!response.ok) throw new Error(`HTTP ${response.status}`);
const collection = await response.json();
```

El código de la interfaz se carga como módulo y comunica cualquier error de red.

<!--
Fuentes:
- WHATWG, HTML Living Standard, 2026-07-20:
  https://html.spec.whatwg.org/multipage/
- W3C, Cascading Style Sheets, 2026-07-29:
  https://www.w3.org/Style/CSS/Overview.en.html
- Unidad 1. Web, Git y publicación, 2026-08-03:
  ../../unidades/01_web_git_publicacion.md
-->
````

### Diapositivas 36–39 — Ejemplos y ejercicios dependientes de GitHub

- **Prioridad:** alta.
- **Categoría:** estructura.
- **Confianza:** alta.
- **Contenido original:** enlaces a ejemplos de una rama `master` y ejercicios
  para GitHub Pages, un “primer mapa web” y Markdown con GitHub.
- **Problema detectado:** no especifica resultado verificable, accesibilidad,
  atribución ni alternativa de datos; mezcla Git local con publicación remota y
  hace que GitHub parezca obligatorio.
- **Evidencia verificable:** el programa define un mapa Leaflet local con datos
  sintéticos, tabla equivalente y ausencia de cuentas SaaS obligatorias.
- **Estado de la evidencia:** verificado.
- **Fecha del dato:** 3 de agosto de 2026.
- **Fuente:**
  [Programa del curso, Unidad 1 y Entrega 1, 3 de agosto de 2026](../../../Programa.md).
- **Recomendación:** reemplazar los tres anuncios por una práctica única y
  progresiva: servir el mapa, observar una solicitud, filtrar datos y verificar
  leyenda, atribución y tabla.
- **Impacto narrativo:** concentra el tiempo en el producto de aprendizaje en
  vez de en una plataforma remota.

#### Contenido propuesto

```md
---
layout: default
---

# Práctica: primer mapa publicable

1. Sirve el repositorio por HTTP local.
2. Abre el mapa Leaflet básico y recorre el filtro solo con teclado.
3. Comprueba que mapa, leyenda, estado y tabla presentan el mismo conjunto de
   datos.
4. Provoca una ruta GeoJSON inexistente en una copia temporal y explica el HTTP
   404 mostrado.

**Resultado esperado:** un mapa local interpretable incluso si falla el mapa
base, porque conserva estado, atribución y tabla equivalente.

<!--
Fuentes:
- Programa del curso, 2026-08-03: ../../../Programa.md
-->
```

### Diapositivas 41–44 — HTTP, errores y tabla de métodos

- **Prioridad:** crítica.
- **Categoría:** tecnología.
- **Confianza:** alta.
- **Contenido original:** referencia HTTP acortada por `bit.ly`, captura 404,
  enlace histórico roto y una tabla basada en RFC 7231.
- **Problema detectado:** RFC 7231 fue obsoleto por RFC 9110. Las capturas no
  explican cómo interpretar una respuesta ni cómo comprobarla. El enlace HTTP
  acortado no es una fuente estable o segura para docencia.
- **Evidencia verificable:** RFC 9110 define semántica, métodos, códigos de
  estado, solicitudes de rango y sus propiedades; sustituyó expresamente
  RFC 7231. La unidad vigente usa 200, 404 y 500 en una práctica con `fetch`.
- **Estado de la evidencia:** verificado.
- **Fecha del dato:** junio de 2022; 3 de agosto de 2026.
- **Fuente:**
  [IETF, RFC 9110: HTTP Semantics, junio de 2022](https://www.rfc-editor.org/rfc/rfc9110.html);
  [Unidad 1. Web, Git y publicación, 3 de agosto de 2026](../../unidades/01_web_git_publicacion.md).
- **Recomendación:** sustituir las cuatro diapositivas por un ejemplo de
  solicitud/respuesta local y remitir el detalle de semántica de métodos a la
  Unidad 4.
- **Impacto narrativo:** evita enseñar un RFC obsoleto y conecta HTTP con una
  observación comprobable.

#### Contenido propuesto

````md
---
layout: default
---

# HTTP: comprueba la respuesta antes de usarla

```js
const response = await fetch('data/referencia.geojson');

if (!response.ok) {
  throw new Error(`HTTP ${response.status}`);
}
```

- `200`: la representación llegó correctamente.
- `404`: el recurso no existe en esa ruta.
- `500`: el servidor falló al procesar la solicitud.

La semántica completa de métodos, caché y APIs se desarrolla en la Unidad 4.

<!--
Fuentes:
- IETF, RFC 9110: HTTP Semantics, 2022-06:
  https://www.rfc-editor.org/rfc/rfc9110.html
-->
````

### Diapositivas 45–48 — RPC y caché

- **Prioridad:** media.
- **Categoría:** estructura.
- **Confianza:** alta.
- **Contenido original:** una definición de RPC y tres diapositivas sobre caché
  con imágenes de terceros.
- **Problema detectado:** RPC aparece sin relación con el recorrido del curso y
  la caché se presenta como una explicación genérica, sin `Cache-Control`,
  validación ni diferencia entre caché privada y compartida. Este nivel de
  detalle corresponde a la Unidad 7.
- **Evidencia verificable:** RFC 9111 define cachés HTTP, frescura, validación y
  directivas de control. El programa ubica caché y benchmark en la Unidad 7.
- **Estado de la evidencia:** verificado.
- **Fecha del dato:** junio de 2022; 3 de agosto de 2026.
- **Fuente:**
  [IETF, RFC 9111: HTTP Caching, junio de 2022](https://www.rfc-editor.org/rfc/rfc9111.html);
  [Programa del curso, Unidad 7, 3 de agosto de 2026](../../../Programa.md).
- **Recomendación:** conservar una definición breve de caché en la Unidad 1 y
  mover RPC y las explicaciones detalladas de caché a panorama de Unidad 4 y
  contenido principal de Unidad 7, respectivamente.
- **Impacto narrativo:** evita sobrecargar la introducción y preserva una
  progresión curricular coherente.

#### Contenido propuesto

```md
---
layout: default
---

# Caché: una respuesta no siempre viaja de nuevo por la red

Una caché puede reutilizar una respuesta HTTP para reducir tiempo y
transferencia. La reutilización depende de la frescura, la validación y
directivas como `Cache-Control`.

En esta unidad solo observaremos si una respuesta vino de caché. Configuraremos
directivas, validación y rendimiento en la Unidad 7.

<!--
Fuentes:
- IETF, RFC 9111: HTTP Caching, 2022-06:
  https://www.rfc-editor.org/rfc/rfc9111.html
-->
```

### Diapositivas 49–55 — XML, web services, API y REST

- **Prioridad:** alta.
- **Categoría:** estructura.
- **Confianza:** alta.
- **Contenido original:** XML, una respuesta de Last.fm, una definición de web
  service “generalmente basado en SOAP”, una API “de forma remota” y REST como
  CRUD con POST, GET, PUT y DELETE.
- **Problema detectado:** mezcla biblioteca, API local, API web, SOAP y REST;
  presenta SOAP como caso general y asocia REST a una lista incompleta de
  verbos. Las capturas de Last.fm dependen de un proveedor externo y no son un
  contrato reproducible.
- **Evidencia verificable:** OGC API - Features define recursos HTTP, página de
  inicio, colecciones, ítems, declaración de conformidad y OpenAPI. Su núcleo
  especifica descubrimiento y consulta por GET; otros métodos pertenecen a
  capacidades adicionales.
- **Estado de la evidencia:** verificado.
- **Fecha del dato:** 11 de mayo de 2022.
- **Fuente:**
  [OGC, OGC API - Features Part 1: Core corrigendum, 11 de mayo de 2022](https://docs.ogc.org/is/17-069r4/17-069r4.html).
- **Recomendación:** mover este bloque a la Unidad 4. Sustituir Last.fm por
  fixtures locales de WFS y OGC API - Features y definir una API como una
  interfaz con un contrato, que puede ser local o remota.
- **Impacto narrativo:** mantiene la Unidad 1 enfocada en publicación básica y
  hace reproducible el contenido de interoperabilidad.

#### Contenido propuesto

```md
<!-- Mover a la Unidad 4. APIs e interoperabilidad. -->

---

layout: default
---

# Una API web expone recursos mediante un contrato

Una API es una interfaz entre componentes; no toda API es remota. Una **API
web** usa tecnologías de la Web y documenta rutas, parámetros, representaciones
y respuestas.

En OGC API - Features, una persona cliente descubre la API, sus colecciones y
sus ítems mediante recursos enlazados y una definición de API.

<!--
Fuentes:
- OGC, OGC API - Features Part 1: Core corrigendum, 2022-05-11:
  https://docs.ogc.org/is/17-069r4/17-069r4.html
-->
```

### Diapositivas 56–58 — JSON y ejemplos de Twitter

- **Prioridad:** alta.
- **Categoría:** tecnología.
- **Confianza:** alta.
- **Contenido original:** “Mensajes más pequeños que SOAP”, una publicación de
  Twitter de 2017 y su estructura JSON.
- **Problema detectado:** JSON no garantiza mensajes menores que SOAP: el tamaño
  depende de estructura, valores, codificación y compresión. Las capturas de una
  plataforma social de 2017 no aportan un ejemplo estable, no cumplen el enfoque
  de datos sintéticos y requieren revisión de licencia.
- **Evidencia verificable:** RFC 8259 define JSON como formato textual, ligero e
  independiente del lenguaje; no afirma una relación universal de tamaño con
  SOAP.
- **Estado de la evidencia:** verificado.
- **Fecha del dato:** diciembre de 2017.
- **Fuente:**
  [IETF, RFC 8259: The JavaScript Object Notation Data Interchange Format, diciembre de 2017](https://www.rfc-editor.org/rfc/rfc8259.html).
- **Recomendación:** reemplazar la comparación absoluta por una definición
  precisa y usar un ejemplo GeoJSON sintético local. Mover el contenido a la
  Unidad 2 o 4 según se enseñe formato o contrato de API.
- **Impacto narrativo:** elimina una afirmación no universal y evita reutilizar
  contenido social de terceros.

#### Contenido propuesto

```md
<!-- Mover a la Unidad 2. Datos y calidad. -->

---

layout: default
---

# JSON: texto estructurado para intercambio de datos

JSON representa objetos, arreglos, cadenas, números, valores booleanos y `null`.
Es independiente del lenguaje de programación.

El tamaño de un mensaje depende de su contenido y de la codificación o
compresión usada; no debe compararse con SOAP mediante una regla universal.

<!--
Fuentes:
- IETF, RFC 8259: The JavaScript Object Notation Data Interchange Format,
  2017-12: https://www.rfc-editor.org/rfc/rfc8259.html
-->
```

### Diapositivas 59–67 — GML, KML, GeoJSON, ESRI JSON y TopoJSON

- **Prioridad:** alta.
- **Categoría:** tecnología.
- **Confianza:** alta.
- **Contenido original:** define GML, KML, GeoJSON y TopoJSON, presenta código
  heredado y compara un polígono “GeoJSON: 2 KB” con “TopoJSON: 554 bytes”.
- **Problema detectado:** estos formatos no pertenecen al resultado de la Unidad
  1; las comparaciones de tamaño no identifican dataset, precisión, topología ni
  proceso de generación; el enlace `tools.ietf.org` no es la referencia canónica
  actual; y el bloque no explica CRS ni el orden longitud/latitud.
- **Evidencia verificable:** RFC 7946 define GeoJSON sobre WGS 84 y orden
  longitud/latitud. GML es una codificación XML para información geográfica; KML
  es XML orientado a visualización geográfica. OGC API - Features recomienda
  GeoJSON cuando la representación es adecuada y mantiene GML para necesidades
  más complejas.
- **Estado de la evidencia:** verificado.
- **Fecha del dato:** agosto de 2016; 11 de mayo de 2022; documentación OGC
  consultada antes de la fecha de corte.
- **Fuente:**
  [IETF, RFC 7946: The GeoJSON Format, agosto de 2016](https://www.rfc-editor.org/rfc/rfc7946.html);
  [OGC, GML Standard, sin fecha de publicación visible](https://www.ogc.org/standards/gml/);
  [OGC, KML 2.3, sin fecha de publicación visible](https://www.ogc.org/standards/kml/);
  [OGC, OGC API - Features Part 1: Core corrigendum, 11 de mayo de 2022](https://docs.ogc.org/is/17-069r4/17-069r4.html).
- **Recomendación:** mover el bloque a Unidad 2 y Unidad 4. Enseñar GeoJSON con
  CRS, orden y precisión; presentar GML y KML como formatos XML de
  interoperabilidad; y conservar TopoJSON como comparación condicionada a una
  medición reproducible.
- **Impacto narrativo:** separa formato, codificación, servicio y rendimiento;
  evita que una cifra aislada se convierta en una promesa de compresión.

#### Contenido propuesto

```md
<!-- Mover a las Unidades 2 y 4. -->

---

layout: default
---

# GeoJSON: intercambio sencillo, con límites explícitos

- GeoJSON codifica geometrías y atributos mediante JSON.
- Sus coordenadas usan WGS 84 con orden **longitud, latitud**.
- La precisión debe justificarse: más decimales aumentan el tamaño sin
  garantizar mejor calidad.
- GML y KML son formatos XML que se conservan para interoperabilidad y
  visualización, respectivamente.

TopoJSON se evaluará con el mismo dataset, precisión, proceso y medición
reproducible; no con una cifra fija.

<!--
Fuentes:
- IETF, RFC 7946: The GeoJSON Format, 2016-08:
  https://www.rfc-editor.org/rfc/rfc7946.html
- OGC, GML Standard, sin fecha de publicación visible:
  https://www.ogc.org/standards/gml/
- OGC, KML 2.3, sin fecha de publicación visible:
  https://www.ogc.org/standards/kml/
-->
```

### Diapositivas 69–71 — Lenguajes de servidor, frameworks y scripting de mapas

- **Prioridad:** alta.
- **Categoría:** tecnología.
- **Confianza:** alta.
- **Contenido original:** catálogos de lenguajes y frameworks, seguidos por
  “Arcgis Server: Python” y “Geoserver: Python”.
- **Problema detectado:** un catálogo sin criterios no apoya el producto de la
  unidad. La diapositiva confunde software servidor, extensiones y scripts de
  automatización. El curso vigente usa scripts Python para configurar GeoServer,
  pero no convierte Python en el lenguaje de GeoServer ni en requisito de la
  Unidad 1.
- **Evidencia verificable:** GeoServer se presenta como servidor de datos
  geoespaciales interoperable y ofrece Docker, REST, WMS, WFS, OGC API -
  Features y extensiones. GeoServer 3.0.0 fue publicado el 11 de junio de 2026.
- **Estado de la evidencia:** verificado.
- **Fecha del dato:** 11 de junio de 2026.
- **Fuente:**
  [GeoServer, GeoServer 3.0.0 Release, 11 de junio de 2026](https://geoserver.org/);
  [GeoServer, User Manual 3.1, sin fecha de publicación visible](https://docs.geoserver.org/main/en/user/).
- **Recomendación:** mover este bloque a Unidad 5. Allí, separar lenguaje de
  automatización, servidor geoespacial, servicios OGC y REST de configuración.
- **Impacto narrativo:** previene que el alumnado deduzca erróneamente que debe
  escoger un framework backend o aprender Python para completar la introducción.

#### Contenido propuesto

```md
<!-- Mover a la Unidad 5. Servicios e infraestructura. -->

---

layout: default
---

# Servidor geoespacial y automatización

GeoServer publica datos geoespaciales mediante servicios y extensiones. En el
curso se ejecuta localmente con Docker Compose y se configura de forma
reproducible mediante la API REST.

Los scripts Python automatizan tareas del entorno; no sustituyen los contratos
WMS, WFS u OGC API - Features que consume el cliente.

<!--
Fuentes:
- GeoServer, GeoServer 3.0.0 Release, 2026-06-11: https://geoserver.org/
- GeoServer, User Manual 3.1, sin fecha de publicación visible:
  https://docs.geoserver.org/main/en/user/
-->
```

### Diapositivas 72–73 — Flash / Flex

- **Prioridad:** crítica.
- **Categoría:** tecnología.
- **Confianza:** alta.
- **Contenido original:** “Cliente Ligero — Flash / Flex” con imágenes de una
  lápida de Flash y de un geoportal que solicita habilitar Flash Player.
- **Problema detectado:** el bloque puede interpretarse como una alternativa de
  desarrollo vigente. Además, las capturas históricas no están licenciadas para
  publicación.
- **Evidencia verificable:** el programa vigente define JavaScript modular,
  Leaflet y MapLibre como núcleo, y clasifica Flash y Flex como tecnologías
  históricas retiradas.
- **Estado de la evidencia:** verificado.
- **Fecha del dato:** 3 de agosto de 2026.
- **Fuente:**
  [Unidad 1. Web, Git y publicación, Panorama posterior, 3 de agosto de 2026](../../unidades/01_web_git_publicacion.md).
- **Recomendación:** retirar ambas diapositivas del núcleo. Si se conserva una
  referencia histórica, usar una única nota textual sin imágenes y sin enseñar
  Flash/Flex como opción implementable. La fecha exacta de fin de Flash requiere
  verificación adicional con Adobe antes de incorporarla.
- **Impacto narrativo:** evita recomendar una tecnología retirada y reduce el
  riesgo de reutilización de capturas externas.

#### Contenido propuesto

```md
---
layout: default
---

# Nota histórica: plugins de navegador

Flash y Flex son tecnologías históricas retiradas. Se mencionan únicamente para
explicar por qué un geoportal antiguo puede dejar de funcionar en navegadores
actuales.

El núcleo del curso usa estándares web, JavaScript modular, Leaflet y MapLibre.

<!--
Fuentes:
- Unidad 1. Web, Git y publicación, 2026-08-03:
  ../../unidades/01_web_git_publicacion.md
-->
```

### Diapositiva 74 — Frameworks JavaScript y mapas

- **Prioridad:** alta.
- **Categoría:** tecnología.
- **Confianza:** alta.
- **Contenido original:** Angular, React, Vue, Leaflet, Openlayers, Mapbox gl /
  js y Arcgis Api for javascript.
- **Problema detectado:** mezcla frameworks de interfaz y clientes cartográficos
  sin criterio de selección. Omite MapLibre, que es el cliente mantenido del
  curso, y puede introducir Mapbox como requisito implícito.
- **Evidencia verificable:** el programa conserva Leaflet como introducción y
  usa TypeScript, Vite y MapLibre para el cliente moderno. React, Vue y Svelte
  son rutas electivas, no requisito.
- **Estado de la evidencia:** verificado.
- **Fecha del dato:** 3 de agosto de 2026.
- **Fuente:**
  [Programa del curso, Unidades 1 y 6, 3 de agosto de 2026](../../../Programa.md).
- **Recomendación:** dividir la comparación por función y presentar únicamente
  las decisiones del curso: Leaflet para introducción, MapLibre para cliente
  moderno y frameworks de interfaz como electivos.
- **Impacto narrativo:** reduce la carga cognitiva y evita dependencia de tokens
  o proveedores.

#### Contenido propuesto

```md
---
layout: default
---

# Clientes web del curso

- **Leaflet:** introducción de bajo umbral para cargar y explicar datos.
- **MapLibre + TypeScript + Vite:** cliente mantenible para filtros, fuentes,
  capas y rutas PMTiles o COG.
- **React, Vue y Svelte:** rutas electivas; no son requisito del proyecto base.

Selecciona la herramienta por la función requerida, no por una cuenta, token o
proveedor específico.

<!--
Fuentes:
- Programa del curso, 2026-08-03: ../../../Programa.md
-->
```

### Diapositiva 75 — Cliente pesado

- **Prioridad:** alta.
- **Categoría:** tecnología.
- **Confianza:** alta.
- **Contenido original:** “Arcgis Desktop”, “Arcgis Pro” y “Qgis” como clientes
  pesados, con lenguajes asociados.
- **Problema detectado:** ArcGIS Desktop y ArcMap se presentan sin estado de
  ciclo de vida; la lista de SDKs no aporta el resultado de la Unidad 1 y puede
  confundirse con una ruta obligatoria.
- **Evidencia verificable:** Esri describe ArcMap 10.8.x como la última serie,
  en soporte maduro y recomienda transición a ArcGIS Pro. El programa vigente
  usa QGIS en la Unidad 2 y no exige cliente de escritorio propietario.
- **Estado de la evidencia:** verificado.
- **Fecha del dato:** fuente de Esri sin fecha de publicación visible;
  consultada antes de la fecha de corte. Programa del 3 de agosto de 2026.
- **Fuente:**
  [Esri, ArcMap Life Cycle, sin fecha de publicación visible](https://support.esri.com/en-us/products/arcmap/life-cycle);
  [Programa del curso, 3 de agosto de 2026](../../../Programa.md).
- **Recomendación:** retirar la diapositiva de la Unidad 1. Si se conserva,
  ubicarla como panorama histórico/electivo junto a la Unidad 2 y rotular ArcMap
  como soporte maduro, no como punto de partida.
- **Impacto narrativo:** mantiene la ruta obligatoria independiente de software
  propietario y versiones retiradas.

#### Contenido propuesto

```md
<!-- Mover a material electivo de la Unidad 2. -->

---

layout: default
---

# Clientes de escritorio: panorama

QGIS es la herramienta de escritorio de referencia para preparar y validar los
datos de práctica. ArcGIS Pro puede ser una alternativa institucional.

ArcMap y ArcGIS Desktop se tratan como contexto histórico: ArcMap 10.8.x es la
última serie y Esri recomienda migrar a ArcGIS Pro.

<!--
Fuentes:
- Esri, ArcMap Life Cycle, sin fecha de publicación visible:
  https://support.esri.com/en-us/products/arcmap/life-cycle
- Programa del curso, 2026-08-03: ../../../Programa.md
-->
```

### Diapositiva 76 — Móviles

- **Prioridad:** alta.
- **Categoría:** tecnología.
- **Confianza:** alta.
- **Contenido original:** lista Android/Java, iOS/Objective-C/Swift, Ionic,
  Xamarin, React Native y web responsive.
- **Problema detectado:** presenta Xamarin como alternativa actual sin indicar
  que su soporte terminó el 1 de mayo de 2024. También amplía el núcleo con
  plataformas móviles que no tienen una actividad ni rúbrica asociada.
- **Evidencia verificable:** Microsoft confirmó el fin de soporte de todos los
  SDK de Xamarin el 1 de mayo de 2024 y recomienda actualizar a proyectos .NET
  SDK-style y .NET MAUI. El programa no hace obligatorio el desarrollo móvil.
- **Estado de la evidencia:** verificado.
- **Fecha del dato:** 1 de mayo de 2024; programa del 3 de agosto de 2026.
- **Fuente:**
  [Microsoft, Xamarin Support Policy, 1 de mayo de 2024](https://dotnet.microsoft.com/en-us/platform/support/policy/xamarin);
  [Programa del curso, 3 de agosto de 2026](../../../Programa.md).
- **Recomendación:** retirar la diapositiva del núcleo. Si se conserva como
  panorama, sustituir Xamarin por .NET MAUI, aclarar que los lenguajes no son
  exclusivos y explicar que el producto obligatorio es una interfaz web
  responsive.
- **Impacto narrativo:** evita recomendar una plataforma sin soporte y protege
  el límite de horas del curso.

#### Contenido propuesto

```md
<!-- Panorama electivo; no incorporar al núcleo obligatorio. -->

---

layout: default
---

# Móviles: rutas posteriores al núcleo web

El producto obligatorio es una interfaz web responsive. Las aplicaciones nativas
e híbridas son rutas electivas que requieren una decisión de plataforma,
presupuesto de mantenimiento y pruebas específicas.

Xamarin dejó de tener soporte el 1 de mayo de 2024; los proyectos existentes
deben evaluarse para migración a .NET y .NET MAUI.

<!--
Fuentes:
- Microsoft, Xamarin Support Policy, 2024-05-01:
  https://dotnet.microsoft.com/en-us/platform/support/policy/xamarin
-->
```

### Diapositiva 77 — Servidores de aplicaciones

- **Prioridad:** media.
- **Categoría:** estructura.
- **Confianza:** alta.
- **Contenido original:** Tomcat, JBoss, IIS y una lista de posibles
  aplicaciones de servidor.
- **Problema detectado:** el catálogo no define una actividad, no diferencia
  servidor de aplicaciones, servidor de mapas y servidor estático, y anticipa
  infraestructura que el programa asigna a la Unidad 5.
- **Evidencia verificable:** el programa ubica PostGIS, GeoServer, Docker
  Compose, healthchecks y restauración en la Unidad 5; la Unidad 1 publica un
  artefacto estático local.
- **Estado de la evidencia:** verificado.
- **Fecha del dato:** 3 de agosto de 2026.
- **Fuente:**
  [Programa del curso, Unidades 1 y 5, 3 de agosto de 2026](../../../Programa.md).
- **Recomendación:** trasladar la diapositiva a la Unidad 5 y reemplazar el
  catálogo por un diagrama que explique qué problema resuelve cada componente
  del stack local.
- **Impacto narrativo:** reduce la anticipación de herramientas no necesarias
  para el primer mapa.

#### Contenido propuesto

```md
<!-- Mover a la Unidad 5. Servicios e infraestructura. -->

---

layout: default
---

# El stack local se compone por responsabilidades

- **PostGIS:** almacena y consulta datos espaciales.
- **GeoServer:** publica servicios geoespaciales y estilos.
- **Servidor estático:** entrega HTML, JavaScript y activos con HTTP Range.
- **Cliente web:** consume recursos y comunica estados de carga o error.

Cada componente se valida con healthchecks y pruebas de humo reproducibles.

<!--
Fuentes:
- Programa del curso, 2026-08-03: ../../../Programa.md
-->
```

## 3. Mejoras transversales

- **Estructura narrativa:** reducir el núcleo de la Unidad 1 a Internet/Web,
  URL/HTTPS, cliente-servidor, HTML/CSS/JavaScript, HTTP observable, Git y
  publicación estática. El bloque de formatos debe ir a Unidad 2; APIs, REST,
  XML, GML y KML a Unidad 4; infraestructura a Unidad 5; clientes y frameworks a
  Unidad 6; caché y comparaciones de tamaño a Unidad 7.
- **Terminología:** usar `HTML`, `CSS`, `JavaScript`, `URL`, `GeoJSON`,
  `GeoServer`, `OpenLayers`, `ArcGIS` y `QGIS` con la capitalización oficial.
  Evitar presentar HTML como “HTML5” o CSS como una versión única.
- **Consistencia de cifras y fechas:** cada cifra debe declarar año, alcance,
  fuente y si es hecho observado, último dato disponible o proyección. La
  infografía de 2017 solo puede conservarse con fecha, licencia y propósito
  histórico explícitos.
- **Redundancias:** las diapositivas 18–23, 41–48, 49–67 y 69–77 repiten o
  adelantan contenido de unidades posteriores. Consolidarlas o moverlas reduce
  la carga sin perder los conceptos.
- **Adecuación a la audiencia:** el alumnado necesita una ruta práctica, no un
  catálogo de productos. Cada bloque debe terminar en una observación, un
  comando, una decisión o un artefacto verificable.
- **Accesibilidad:** sustituir las capturas por diagramas propios con texto
  equivalente. WCAG 2.2 exige alternativas textuales para contenido no textual y
  el curso debe comprobar teclado, foco visible, contraste, reflow y estados.
- **Seguridad y privacidad:** eliminar enlaces HTTP externos, URLs con
  credenciales, enlaces acortados y ejemplos de plataformas sociales. No mostrar
  tokens, datos personales o material de terceros sin revisión.
- **Referencias:** reemplazar Wikipedia, enlaces acortados, páginas de ejemplos
  de terceros y cuentas históricas por estándares, documentación oficial y
  fixtures locales. Las fuentes deben quedar en comentarios HTML de Slidev para
  no interferir con el diseño de la diapositiva.
- **Licencias y recursos visuales:** mantener la exclusión actual de
  `docs/slides/` del build público. Preferir imágenes de dominio público y
  diagramas propios. También se pueden generar imágenes propias con IA cuando
  sus términos permitan el uso previsto, pero se debe declarar la herramienta,
  versión o modelo, fecha, prompt no sensible, edición humana y licencia o
  condiciones de reutilización. Una salida de IA no queda automáticamente libre
  de restricciones: antes de publicarla debe tener procedencia, licencia,
  utilidad, texto alternativo y revisión humana resueltos.

## 4. Diapositivas revisadas sin cambios

- **Diapositiva 2 — “1. Fundamentos de Internet”:** división de sección clara y
  pertinente.
- **Diapositiva 6 — “Pero qué es la Internet?”:** pregunta de transición útil
  antes de la definición.
- **Diapositiva 10 — Protocolos:** la explicación general y los ejemplos POP3,
  IMAP, SMTP, FTP, SSH y HTTP siguen siendo correctos para una introducción.
- **Diapositiva 11 — Qué es la Web?:** mantiene correctamente que la Web es un
  sistema que usa Internet y conecta documentos por hipervínculos.
- **Diapositiva 16 — Navegador web:** la definición es correcta; puede
  conservarse tras la modernización visual de la diapositiva 17.
- **Diapositiva 24 — Anatomía de una página web:** división temática válida.
- **Diapositiva 40 — Otros conceptos:** división válida si el contenido se
  reorganiza hacia las unidades posteriores indicadas.
- **Diapositiva 68 — Tecnologías para el Desarrollo de Aplicaciones Web:**
  división temática válida, pero debe abrir un anexo o una unidad posterior, no
  el núcleo de la Unidad 1.
- **Diapositiva 78 — Gracias:** cierre pertinente.

## 5. Plan de actualización priorizado

1. **Cambios críticos inmediatos.** Retirar las cifras no fechadas de las
   diapositivas 4–5 y sustituirlas por el último dato de ITU con fecha.
   Reemplazar el HTML con atributos presentacionales de la diapositiva 25.
   Retirar HTTP externo, credenciales en URL y enlaces acortados de las
   diapositivas 12–15 y 41–44. Marcar Flash como histórico, eliminar Xamarin de
   opciones vigentes y rotular ArcMap como producto en soporte maduro. Mantener
   las imágenes históricas fuera del sitio público hasta resolver licencias.

2. **Actualizaciones de alto impacto.** Reestructurar el deck para que la Unidad
   1 tenga una práctica progresiva de mapa Leaflet servido localmente. Mover
   formatos a Unidad 2, APIs y servicios web a Unidad 4, servidores a Unidad 5,
   frameworks a Unidad 6 y caché a Unidad 7. Sustituir capturas externas por
   diagramas propios y fixtures locales.

3. **Mejoras editoriales opcionales.** Corregir capitalización, concordancia y
   nombres oficiales. Añadir comentarios HTML con fuentes en cada diapositiva
   factual. Reemplazar listas de productos por decisiones justificadas según
   función, accesibilidad, reproducibilidad y seguridad. Añadir una diapositiva
   de autoevaluación antes del cierre.

## 6. Fuentes consolidadas

1. [International Telecommunication Union — _Measuring digital development: Facts and Figures 2025_ — 2025](https://www.itu.int/itu-d/reports/statistics/facts-figures-2025/)
2. [WHATWG — _HTML Living Standard_ — 20 de julio de 2026](https://html.spec.whatwg.org/multipage/)
3. [WHATWG — _URL Standard_ — 6 de julio de 2026](https://url.spec.whatwg.org/)
4. [World Wide Web Consortium — _Web Content Accessibility Guidelines (WCAG) 2.2_ — 12 de diciembre de 2024](https://www.w3.org/TR/WCAG22/)
5. [World Wide Web Consortium — _Cascading Style Sheets_ — 29 de julio de 2026](https://www.w3.org/Style/CSS/Overview.en.html)
6. [Internet Engineering Task Force — RFC 9110: _HTTP Semantics_ — junio de 2022](https://www.rfc-editor.org/rfc/rfc9110.html)
7. [Internet Engineering Task Force — RFC 9111: _HTTP Caching_ — junio de 2022](https://www.rfc-editor.org/rfc/rfc9111.html)
8. [Internet Engineering Task Force — RFC 8259: _The JavaScript Object Notation Data Interchange Format_ — diciembre de 2017](https://www.rfc-editor.org/rfc/rfc8259.html)
9. [Internet Engineering Task Force — RFC 7946: _The GeoJSON Format_ — agosto de 2016](https://www.rfc-editor.org/rfc/rfc7946.html)
10. [Open Geospatial Consortium — _OGC API - Features - Part 1: Core corrigendum_ — 11 de mayo de 2022](https://docs.ogc.org/is/17-069r4/17-069r4.html)
11. [Open Geospatial Consortium — _GML Standard_ — sin fecha de publicación visible](https://www.ogc.org/standards/gml/)
12. [Open Geospatial Consortium — _KML 2.3_ — sin fecha de publicación visible](https://www.ogc.org/standards/kml/)
13. [GeoServer — _GeoServer 3.0.0 Release_ — 11 de junio de 2026](https://geoserver.org/)
14. [GitHub — _What is GitHub Pages?_ — sin fecha de publicación visible](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages)
15. [Microsoft — _Xamarin Support Policy_ — 1 de mayo de 2024](https://dotnet.microsoft.com/en-us/platform/support/policy/xamarin)
16. [Esri — _ArcMap Life Cycle_ — sin fecha de publicación visible](https://support.esri.com/en-us/products/arcmap/life-cycle)
17. [Repositorio del curso — _Programa del curso_ — 3 de agosto de 2026](../../../Programa.md)
18. [Repositorio del curso — _Unidad 1. Web, Git y publicación_ — 3 de agosto de 2026](../../unidades/01_web_git_publicacion.md)
19. [Repositorio del curso — _Política de Licencias Inicial_ — 3 de agosto de 2026](../../governance/licenses.md)
