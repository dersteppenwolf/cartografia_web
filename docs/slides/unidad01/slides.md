---
theme: default
title: Unidad 1. Web, Git y publicación
transition: slide-left
mdc: true
layout: cover
---

<!-- markdownlint-disable MD024 -->
<!-- Diapositiva modernizada: 1 -->

# Publicación de cartografía para la web

## Unidad 1. Web, Git y publicación

Una ruta local, accesible y reproducible para publicar el primer mapa.

---

<!-- Diapositiva modernizada: 2 -->

# Panorama histórico y tecnológico

El contexto histórico explica decisiones actuales. No convierte tecnologías
antiguas ni productos concretos en requisitos del curso.

- Conservamos los conceptos de arquitectura, formatos, clientes y servidores.
- El desarrollo práctico se concentra en una publicación cartográfica local.

---

<!-- Diapositiva modernizada: 3 -->

# De documentos web a publicaciones cartográficas

```text
Documento HTML estático
  -> datos y servicios geoespaciales
  -> cliente web interactivo
  -> activos optimizados y operación reproducible
```

Cada etapa añadió capacidades, pero no reemplazó por completo a la anterior. Un
archivo HTML, un servicio, una API y un mapa resuelven necesidades distintas.

---

<!-- Diapositiva modernizada: 4 -->

# Modelos de integración: contexto y compatibilidad

| Modelo             | Idea principal                         | Papel en el curso            |
| ------------------ | -------------------------------------- | ---------------------------- |
| RPC                | Invoca una operación remota            | Panorama histórico           |
| SOAP/XML           | Intercambia mensajes y operaciones     | Panorama y compatibilidad    |
| WMS/WFS            | Publica mapas y entidades OGC clásicas | Compatibilidad institucional |
| REST/HTTP          | Organiza recursos y representaciones   | Base conceptual              |
| OGC API - Features | Descubre y consulta colecciones        | Núcleo de la Unidad 4        |

<!--
Fuentes:
- Programa del curso, Unidad 4. APIs e interoperabilidad, 2026-08-03:
  ../../../Programa.md
- OGC, OGC API - Features Part 1: Core corrigendum, 2022-05-11:
  https://docs.ogc.org/is/17-069r4/17-069r4.html
-->

---

<!-- Diapositiva modernizada: 5 -->

# Formatos geográficos: cada uno cumple una función

- **GML:** codificación XML para intercambio geográfico complejo.
- **KML:** XML orientado a anotación y visualización geográfica.
- **GeoJSON:** intercambio sencillo de geometrías y atributos en la Web.
- **TopoJSON:** codifica topología; se compara con medidas reproducibles.
- **GeoPackage:** archivo para datos y trabajo local.
- **MVT/PMTiles y COG:** entrega optimizada de vector y ráster, respectivamente.

Formato, codificación, empaquetado, catálogo y servicio no son equivalentes.

<!--
Fuentes:
- IETF, RFC 7946: The GeoJSON Format, 2016-08:
  https://www.rfc-editor.org/rfc/rfc7946.html
- Programa del curso, Unidades 2 y 7, 2026-08-03: ../../../Programa.md
-->

---

<!-- Diapositiva modernizada: 6 -->

# Clientes: de escritorio, web y móviles

| Contexto             | Ejemplos                        | Alcance curricular                      |
| -------------------- | ------------------------------- | --------------------------------------- |
| Escritorio histórico | ArcMap, ArcGIS Desktop          | Contexto institucional e histórico      |
| Escritorio actual    | ArcGIS Pro, QGIS                | Preparación y validación de datos       |
| Plugins retirados    | Flash, Flex                     | Explican fallos de geoportales antiguos |
| Web                  | Leaflet, MapLibre               | Ruta obligatoria del curso              |
| Móvil                | Aplicaciones nativas o híbridas | Panorama electivo                       |

<!--
Fuentes:
- Programa del curso, Unidades 1, 2 y 6, 2026-08-03: ../../../Programa.md
- Esri, ArcMap Life Cycle, sin fecha de publicación visible:
  https://support.esri.com/en-us/products/arcmap/life-cycle
-->

---

<!-- Diapositiva modernizada: 7 -->

# Servidores y lenguajes: responsabilidades antes que catálogos

- Java, .NET, Python, Go, Ruby y Node.js son opciones de implementación de
  servicios; no son requisitos de esta unidad.
- Un servidor estático entrega archivos ya construidos; un servidor de
  aplicaciones ejecuta lógica, como Tomcat o IIS en otros contextos.
- PostGIS almacena y consulta datos espaciales.
- GeoServer publica servicios geoespaciales: datos, imágenes o teselas según el
  contrato.
- Nginx entrega activos estáticos con HTTP Range.
- Scripts automatizan configuración; no reemplazan contratos de servicio.

El stack reproducible se construye y valida en la Unidad 5.

<!--
Fuentes:
- Programa del curso, Unidad 5. Servicios e infraestructura, 2026-08-03:
  ../../../Programa.md
- GeoServer, GeoServer 3.0.0 Release, 2026-06-11: https://geoserver.org/
-->

---

<!-- Diapositiva modernizada: 8 -->

# Qué se conserva y qué se traslada

| Contexto en esta unidad                                   | Desarrollo práctico posterior                             |
| --------------------------------------------------------- | --------------------------------------------------------- |
| Historia de Web, cliente-servidor y tecnologías retiradas | Unidad 1: HTML, CSS, JavaScript, Git y mapa Leaflet local |
| Formatos, CRS y calidad de datos                          | Unidad 2                                                  |
| Accesibilidad cartográfica y experiencia de uso           | Unidad 3                                                  |
| APIs, REST, WMS, WFS y OGC API - Features                 | Unidad 4                                                  |
| PostGIS, GeoServer y Docker Compose                       | Unidad 5                                                  |
| MapLibre, rendimiento, PMTiles, COG y operación           | Unidades 6 a 8                                            |

El panorama facilita decisiones informadas sin ampliar el núcleo obligatorio.

---

<!-- Diapositiva modernizada: 9 -->

# Resultado de la unidad

Al finalizar podrás publicar un mapa Leaflet básico que se sirve por HTTP local,
carga datos sintéticos y conserva una tabla equivalente.

- No requiere cuenta SaaS, token ni IP histórica.
- Usa HTML semántico, CSS responsive y JavaScript modular.
- Comunica carga, datos vacíos y errores de red de forma comprensible.

<!--
Fuentes:
- Programa del curso, Unidad 1. Web, Git y publicación, 2026-08-03:
  ../../../Programa.md
-->

---

<!-- Diapositiva modernizada: 10 -->

# Ruta de aprendizaje

1. Entender qué intercambian el navegador y el servidor.
2. Construir y servir una página mínima con HTML, CSS y un módulo ES.
3. Comprobar que el módulo actualiza una región de estado.
4. Cargar un GeoJSON y comprobar su respuesta HTTP en el mapa.
5. Registrar los cambios con Git y verificar una interfaz accesible.

---

<!-- Diapositiva modernizada: 11 -->

# Conectividad global: contexto, no garantía de acceso

<img
  src="/assets/generated/connectividad_2025.svg"
  alt="Gráfico propio de conectividad mundial en 2025: aproximadamente seis mil millones de personas en línea, 2.2 mil millones sin conexión y cobertura 5G del 55 por ciento."
  style="display: block; height: 15rem; margin: 0 auto;"
/>

La disponibilidad, calidad y asequibilidad de la red condicionan cómo se
publican y usan los mapas web. Diseñar una alternativa textual y evitar
transferencias innecesarias sigue siendo parte del problema técnico.

<!--
Fuentes:
- International Telecommunication Union, Measuring digital development: Facts
  and Figures 2025, 2025:
  https://www.itu.int/itu-d/reports/statistics/facts-figures-2025/
-->

---

<!-- Diapositiva modernizada: 11a -->

# Antes del mapa: una página que puedes construir

`examples/leaflet/pagina_minima/` separa estructura, presentación y
comportamiento antes de introducir datos geográficos.

```html
<main>
  <h1>Mi primera página publicada por HTTP</h1>
  <button id="actualizar-estado">Actualizar mensaje</button>
  <p id="estado" role="status"></p>
</main>
<script type="module" src="main.js"></script>
```

1. Sirve el repositorio con `python -m http.server 8000`.
2. Abre `http://localhost:8000/examples/leaflet/pagina_minima/`.
3. Cambia el encabezado y activa el botón: `main.js` importa `status.js` para
   actualizar el estado.

---

<!-- Diapositiva modernizada: 12 -->

# Internet y Web no son sinónimos

<img
  src="/assets/generated/internet_web.svg"
  alt="Diagrama propio que diferencia Internet como una red de sistemas conectados y la Web como recursos HTML y GeoJSON enlazados mediante HTTP."
  style="display: block; height: 10rem; margin: 0 auto;"
/>

**Internet** conecta redes y sistemas independientes mediante protocolos.

**La Web** es uno de los sistemas que usa Internet para enlazar recursos
mediante URLs e hipervínculos. El **hipertexto** permite que un recurso enlace a
otro sin exigir una lectura lineal.

- Correo electrónico, SSH y FTP usan Internet, pero no son páginas web.
- HTTP define cómo un cliente solicita recursos y un servidor responde.
- El navegador presenta las representaciones recibidas.

<!--
Fuentes:
- IETF, RFC 9110: HTTP Semantics, 2022-06:
  https://www.rfc-editor.org/rfc/rfc9110.html
-->

---

<!-- Diapositiva modernizada: 13 -->

# Protocolos: reglas compartidas

<img
  src="/assets/generated/protocolos.svg"
  alt="Diagrama propio que relaciona correo electrónico con POP3, IMAP y SMTP; administración con SSH; archivos con FTP; y recursos web con HTTP y HTTPS."
  style="display: block; height: 14rem; margin: 0 auto;"
/>

En esta unidad observaremos HTTP; otros protocolos son contexto, no requisitos
del mapa inicial.

---

<!-- Diapositiva modernizada: 14 -->

# Una URL identifica un recurso

<img
  src="/assets/generated/url_segura.svg"
  alt="Diagrama propio de una URL segura que identifica esquema HTTPS, host, puerto, ruta, consulta y fragmento sin credenciales."
  style="display: block; height: 17rem; margin: 0 auto;"
/>

- El esquema indica el protocolo; usa `https` fuera de desarrollo local.
- Host, puerto, ruta y consulta localizan o describen el recurso.
- El fragmento lo interpreta el navegador.
- No pongas contraseñas, tokens ni información personal en una URL.

<!--
Fuentes:
- WHATWG, URL Standard, 2026-07-06: https://url.spec.whatwg.org/
-->

---

<!-- Diapositiva modernizada: 15 -->

# HTTP, HTTPS y origen

<img
  src="/assets/generated/https_origen.svg"
  alt="Diagrama propio donde un navegador se comunica por HTTPS con un origen compuesto por esquema, host y puerto, y muestra que otro origen requiere autorización."
  style="display: block; height: 13rem; margin: 0 auto;"
/>

- **HTTP** define solicitudes, respuestas, métodos, códigos de estado y
  representaciones.
- **HTTPS** usa HTTP sobre una conexión protegida por TLS.
- Un **origen** combina esquema, host y puerto.

Una página puede solicitar recursos de otro origen solo cuando el servidor los
autoriza. Más adelante estudiaremos CORS y políticas de seguridad.

<!--
Fuentes:
- IETF, RFC 9110: HTTP Semantics, 2022-06:
  https://www.rfc-editor.org/rfc/rfc9110.html
-->

---

<!-- Diapositiva modernizada: 16 -->

# Del navegador al mapa

<img
  src="/assets/generated/cliente_servidor_mapa.svg"
  alt="Diagrama propio donde un navegador solicita HTML, CSS, JavaScript y GeoJSON a un servidor estático y después representa mapa, leyenda, estado y tabla."
  style="display: block; height: 16rem; margin: 0 auto;"
/>

El cliente solicita recursos. Un servidor estático entrega archivos ya
construidos. El mapa no prueba por sí solo que el dato cargó correctamente:
también se debe observar la respuesta y su estado.

<!--
Fuentes:
- Unidad 1. Web, Git y publicación, Del navegador al mapa, 2026-08-03:
  ../../unidades/01_web_git_publicacion.md
-->

---

<!-- Diapositiva modernizada: 16a -->

# Del territorio a una entidad geográfica

```text
Fenómeno territorial
  -> observación y documentación
  -> entidad: geometría + atributos
  -> GeoJSON
  -> mapa, leyenda y tabla
```

- La **geometría** indica dónde está una entidad o qué extensión ocupa.
- Los **atributos** explican qué representa, por ejemplo su nombre, fecha o
  valor.
- En `referencia.geojson`, cada zona es un punto con `nombre` y `valor`: Leaflet
  usa la geometría para ubicarla; el filtro y la tabla usan los atributos.

Un mapa representa un modelo del territorio, no el territorio mismo. El CRS, el
orden de coordenadas, la precisión y la validez se estudian en la Unidad 2.

<!--
Fuentes:
- Unidad 2. Datos y calidad, Modelo de datos geográficos, 2026-08-03:
  ../../unidades/02_datos_calidad.md
-->

---

<!-- Diapositiva modernizada: 17 -->

# Observa una solicitud real

<img
  src="/assets/generated/network_request.svg"
  alt="Panel de red propio que muestra una solicitud GET a data/referencia.geojson con estado 200 y los campos que deben registrarse."
  style="display: block; height: 12rem; margin: 0 auto;"
/>

1. Abre las herramientas de desarrollo y la pestaña **Network**.
2. Recarga el mapa local y busca `data/referencia.geojson`.
3. Registra URL, método, código HTTP, tipo de contenido, tamaño y caché.

La evidencia observada es más útil que asumir que un recurso cargó porque el
mapa parece visible.

---

<!-- Diapositiva modernizada: 18 -->

# HTML, CSS y JavaScript cumplen funciones distintas

- **HTML:** estructura y significado.
- **CSS:** presentación adaptable, contraste y foco visible.
- **JavaScript:** comportamiento, carga de datos y mensajes de estado.

```text
index.html  -> estructura
styles.css  -> presentación
main.js     -> comportamiento
```

---

<!-- Diapositiva modernizada: 19 -->

# HTML semántico desde el inicio

<img
  src="/assets/generated/html_semantico_resultado.svg"
  alt="Diagrama propio que relaciona un elemento main, un encabezado, una etiqueta, un selector y una región de estado con su resultado visible en una interfaz."
  style="display: block; height: 19rem; margin: 0 auto;"
/>

`main` identifica el contenido principal. Los encabezados nombran secciones. Un
elemento semántico comunica mejor su propósito que un `div` genérico.

<!--
Fuentes:
- WHATWG, HTML Living Standard, 2026-07-20:
  https://html.spec.whatwg.org/multipage/
-->

---

<!-- Diapositiva modernizada: 20 -->

# CSS que se adapta y mantiene el foco

```css
main {
  max-width: 70rem;
  margin: 0 auto;
  padding: 1rem;
}

button:focus-visible {
  outline: 3px solid #ffc21a;
  outline-offset: 3px;
}
```

- Usa anchos relativos y texto que puede crecer.
- Comprueba reflow a 320 CSS px y zoom al 200 %.
- El foco visible permite navegar sin ratón.
- No dependas solo del color para comunicar estado o selección.

<!--
Fuentes:
- W3C, Cascading Style Sheets, 2026-07-29:
  https://www.w3.org/Style/CSS/Overview.en.html
- W3C, Web Content Accessibility Guidelines (WCAG) 2.2, 2024-12-12:
  https://www.w3.org/TR/WCAG22/
-->

---

<!-- Diapositiva modernizada: 21 -->

# JavaScript carga datos y verifica la respuesta

```js
async function loadCollection() {
  const response = await fetch('data/referencia.geojson');

  if (!response.ok) {
    throw new Error(`HTTP ${response.status}`);
  }

  return response.json();
}
```

- Carga el archivo con `fetch`.
- Comprueba `response.ok` antes de leer JSON.
- Usa `async` y `await` para esperar la respuesta.
- Comunica el resultado en una región de estado.

---

<!-- Diapositiva modernizada: 22 -->

# Un estado no siempre es un error

| Observación             | Qué significa            | Qué debe comunicar la interfaz                |
| ----------------------- | ------------------------ | --------------------------------------------- |
| HTTP 200                | El recurso llegó         | Datos disponibles y actualizados              |
| HTTP 404                | La ruta no existe        | Recurso no encontrado y cómo recuperarse      |
| Fallo de red            | No llegó una respuesta   | No se pudo conectar; reintentar o revisar red |
| Colección vacía         | La solicitud fue válida  | No hay entidades para el filtro actual        |
| Mapa base no disponible | Falló el contexto visual | La tabla y la leyenda siguen disponibles      |

<!--
Fuentes:
- IETF, RFC 9110: HTTP Semantics, 2022-06:
  https://www.rfc-editor.org/rfc/rfc9110.html
-->

---

<!-- Diapositiva modernizada: 22a -->

# Un 404 debe explicar qué ocurrió

<img
  src="/assets/generated/estado_404.svg"
  alt="Interfaz propia de mapa que comunica un error HTTP 404, indica que no se cargaron los datos de referencia y recomienda verificar la ruta solicitada."
  style="display: block; height: 16rem; margin: 0 auto;"
/>

Una interfaz útil no se limita a mostrar un código. Explica qué recurso faltó,
qué parte sigue disponible y cuál es la siguiente acción para recuperarse.

---

<!-- Diapositiva modernizada: 23 -->

# Caché: observa, no adivines

<img
  src="/assets/generated/cache_observacion.svg"
  alt="Diagrama propio donde el navegador consulta una caché y solicita al servidor cuando falta una respuesta reutilizable o requiere validación."
  style="display: block; height: 13rem; margin: 0 auto;"
/>

Una caché puede reutilizar una respuesta para reducir tiempo y transferencia.
Para comprobar una solicitud nueva, usa una ventana privada o desactiva la caché
en DevTools. `Cache-Control`, validación y rendimiento se estudian en la
Unidad 7.

<!--
Fuentes:
- IETF, RFC 9111: HTTP Caching, 2022-06:
  https://www.rfc-editor.org/rfc/rfc9111.html
-->

---

<!-- Diapositiva modernizada: 24 -->

# Git registra cambios; el hosting entrega archivos

<img
  src="/assets/generated/git_hosting.svg"
  alt="Diagrama propio que distingue directorio de trabajo, Git local, remoto opcional y hosting estático HTTPS."
  style="display: block; height: 15rem; margin: 0 auto;"
/>

Git conserva una historia local de cambios. Un hosting estático entrega archivos
ya construidos mediante HTTP o HTTPS. Son responsabilidades distintas.

---

<!-- Diapositiva modernizada: 25 -->

# Git no publica una página

```powershell
git status --short
git diff
git add ruta/al/archivo
git commit -m "Describir el cambio"
git log --oneline -5
```

- El repositorio local registra historia de cambios.
- Un remoto es otra copia del repositorio.
- Un `push` envía commits cuando existe una política autorizada.
- Revisa el diff antes de preparar un cambio.

Nunca registres tokens, contraseñas, datos personales o resultados de otras
personas.

---

<!-- Diapositiva modernizada: 26 -->

# Sirve el proyecto por HTTP local

```powershell
python -m http.server 8000
```

Abre:

```text
http://localhost:8000/examples/leaflet/mapa_basico/
```

No pruebes `fetch` con `file://`: el navegador aplica restricciones distintas y
no podrás observar la misma solicitud HTTP que verá una persona usuaria.

---

<!-- Diapositiva modernizada: 27 -->

# Un hosting estático es una decisión de despliegue

Un hosting estático entrega HTML, CSS, JavaScript y datos ya construidos
mediante HTTPS. GitHub Pages es una implementación de referencia, no un
requisito del curso ni la única forma de publicar.

El artefacto debe conservar rutas relativas, no depender de credenciales en el
cliente y poder alojarse en un entorno institucional o compatible con HTTPS.

<!--
Fuentes:
- GitHub, What is GitHub Pages?, sin fecha de publicación visible:
  https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages
-->

---

<!-- Diapositiva modernizada: 28 -->

# Un mapa es una interfaz, no una imagen

<img
  src="/assets/generated/mapa_accesible.svg"
  alt="Diagrama propio de un mapa accesible con filtro etiquetado, estado de carga, leyenda y tabla equivalente de datos."
  style="display: block; height: 16rem; margin: 0 auto;"
/>

El mapa base aporta orientación y contexto; no es la fuente de la capa temática.
La capa temática contiene la variable que responde a la pregunta territorial. Si
el mapa base falla, la interfaz conserva leyenda, atribución, estado y tabla
equivalente.

<!--
Fuentes:
- W3C, Web Content Accessibility Guidelines (WCAG) 2.2, 2024-12-12:
  https://www.w3.org/TR/WCAG22/
- Programa del curso, Entrega 1, 2026-08-03: ../../../Programa.md
-->

---

<!-- Diapositiva modernizada: 29 -->

# Publicar una ubicación también tiene riesgos

<img
  src="/assets/generated/privacidad_ubicacion.svg"
  alt="Diagrama propio que muestra una coordenada precisa pasando por una revisión de sensibilidad, licencia y minimización antes de publicarse."
  style="display: block; height: 11rem; margin: 0 auto;"
/>

Antes de publicar datos geográficos, identifica:

<ul class="compact-list">
  <li>Quién produjo el dato, con qué licencia y en qué fecha.</li>
  <li>Qué precisión y sensibilidad tienen las coordenadas.</li>
  <li>Si pueden identificar personas, viviendas, especies sensibles o infraestructura crítica.</li>
  <li>Qué atribución, límites de uso y medidas de minimización deben acompañarlo.</li>
</ul>

No uses datos sociales geolocalizados en cuarentena para completar la práctica.

<!--
Fuentes:
- Programa del curso, Competencias específicas y política de IA, 2026-08-03:
  ../../../Programa.md
-->

---

<!-- Diapositiva modernizada: 30 -->

# Recursos visuales e IA: documenta antes de publicar

- Prefiere dominio público, diagramas propios o recursos con licencia
  compatible.
- Una imagen asistida por IA requiere declarar herramienta, versión o modelo,
  fecha, prompt no sensible, términos de uso y revisión humana.
- La salida de IA no elimina obligaciones de atribución, licencia, accesibilidad
  o exactitud.
- Toda imagen informativa necesita texto alternativo útil; una decorativa debe
  poder ignorarse.

<!--
Fuentes:
- Programa del curso, Política de uso responsable de IA, 2026-08-03:
  ../../../Programa.md
- Repositorio, Política de Licencias Inicial, 2026-08-03:
  ../../governance/licenses.md
-->

---

<!-- Diapositiva modernizada: 31 -->

# Práctica guiada: primer mapa publicable

1. Sirve el repositorio por HTTP local.
2. Abre la página mínima, cambia su encabezado y comprueba el mensaje del
   módulo.
3. Abre el mapa Leaflet básico y recorre el filtro solo con teclado.
4. Comprueba que mapa, leyenda, estado y tabla representan el mismo conjunto de
   datos.
5. Abre Network, inspecciona la respuesta de `referencia.geojson` e identifica
   una geometría y los atributos `nombre` y `valor`; registra también URL,
   método, código, tipo, tamaño y caché.
6. En una copia temporal, cambia la ruta del GeoJSON y observa el mensaje 404.
7. Restaura la ruta, crea una nota Markdown local y registra un cambio pequeño
   con Git.

**Resultado esperado:** un mapa local que conserva una alternativa interpretable
cuando falla una solicitud o el mapa base.

---

<!-- Diapositiva modernizada: 32 -->

# Diagnóstico de salida

Puedes continuar si demuestras que:

- explicas la diferencia entre `file://` y un servidor HTTP local;
- identificas método, código, tipo y tamaño de una solicitud GeoJSON;
- distingues un 404, un fallo de red y una colección vacía;
- operas el filtro con teclado y encuentras el foco visible;
- verificas la misma información en el mapa y en la tabla;
- describes la procedencia, licencia y sensibilidad del dato usado.

---

<!-- Diapositiva modernizada: 33 -->

# Qué sigue

- **Unidad 2:** datos, GeoJSON, CRS, precisión, licencia y privacidad; GML, KML
  y ESRI JSON se clasifican como compatibilidad, no como formato inicial.
- **Unidad 3:** cartografía temática, accesibilidad y experiencia de uso.
- **Unidad 4:** HTTP en detalle, WFS, OGC API - Features y OpenAPI; RPC y SOAP
  se conservan como panorama histórico de contratos.
- **Unidades 5 a 8:** infraestructura, MapLibre, rendimiento, operación y
  publicación.

El primer mapa sirve para conectar esas etapas sin añadir dependencias remotas.

<!--
Fuentes:
- Programa del curso, Unidades 2 a 8, 2026-08-03: ../../../Programa.md
-->

---

<!-- Diapositiva modernizada: 34 -->

# Gracias

<!-- markdownlint-restore -->
