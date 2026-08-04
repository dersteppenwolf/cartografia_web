---
layout: default
title: Unidad 1. Web, Git y publicación
permalink: /unidades/01-web-git-publicacion/
---

# Unidad 1. Web, Git y publicación

**Tiempo:** cuatro horas presenciales y cuatro horas autónomas. **Producto:** un
mapa Leaflet que se sirve por HTTP local, carga datos sintéticos y conserva una
tabla equivalente. No se requiere una cuenta, token, IP institucional ni
proveedor SaaS.

## Resultados de aprendizaje

Al finalizar podrás:

- Explicar qué ejecuta el navegador y qué entrega un servidor estático.
- Escribir una página con estructura HTML semántica y controles etiquetados.
- Aplicar CSS responsive sin ocultar información ni bloquear el zoom.
- Cargar un archivo con `fetch`, comprobar una respuesta HTTP y comunicar un
  error.
- Registrar cambios locales con Git y distinguir repositorio, commit, remoto y
  publicación estática.

## Internet, Web y publicación

**Internet** es una red de redes que intercambian información mediante
protocolos. La **Web** es uno de los sistemas que usa Internet para enlazar
recursos mediante URLs e hipervínculos. Correo electrónico, SSH y transferencia
de archivos también usan Internet, pero no son páginas web.

Un **protocolo** define reglas para que dos sistemas se entiendan. HTTP define
cómo un cliente solicita un recurso y cómo un servidor responde. HTTPS usa HTTP
sobre TLS para proteger esa comunicación. El curso usa HTTPS para recursos
publicados y reserva HTTP para `localhost` durante el desarrollo local.

Un **cliente** solicita recursos; en esta unidad es el navegador. Un
**servidor** responde. Un servidor estático entrega archivos ya construidos,
como HTML, CSS, JavaScript, GeoJSON, PMTiles o COG. Más adelante, GeoServer
responderá servicios geoespaciales y PostGIS conservará datos, pero una
publicación estática no necesita exponer esos servicios en Internet.

## Anatomía de una URL

Una URL identifica un recurso y puede contener varias partes:

```text
https://curso.example.org:443/unidades/01?tema=http#practica
\____/   \________________/ \_/ \__________/ \________/ \_______/
esquema          host        puerto    ruta      consulta   fragmento
```

- El **esquema** indica el protocolo, por ejemplo `https`.
- El **host** identifica el servidor, por ejemplo `curso.example.org`.
- El **puerto** identifica un servicio dentro del host; `443` es habitual para
  HTTPS y se puede omitir en una URL pública.
- La **ruta** localiza un recurso dentro del sitio.
- La **consulta** agrega parámetros, por ejemplo `tema=http`.
- El **fragmento** lleva a una sección del documento y no se envía al servidor.

No coloques credenciales, tokens ni información personal en una URL. Las URLs se
pueden guardar en historial, registros, marcadores y capturas.

## Del navegador al mapa

Cuando abres el ejemplo Leaflet, el navegador sigue un recorrido observable:

```text
Navegador
  -> GET /examples/leaflet/mapa_basico/
  <- HTML, CSS y JavaScript
  -> GET /examples/leaflet/mapa_basico/data/referencia.geojson
  <- GeoJSON con HTTP 200
  -> Renderiza la capa, la leyenda, el estado y la tabla
```

El documento HTML referencia CSS y JavaScript. JavaScript solicita el GeoJSON y
actualiza el mapa y la tabla. Si la solicitud devuelve 200, el recurso llegó; si
devuelve 404, la ruta no existe; si devuelve 500, el servidor falló al procesar
la solicitud. Un 200 no demuestra por sí solo que el dato responda la pregunta
territorial, y una colección vacía no es necesariamente un error.

Las herramientas de desarrollo permiten observar URL, método, código de estado,
tipo de contenido, tamaño, tiempo y si una respuesta vino de caché. Esa
evidencia es más útil que asumir que un recurso se cargó porque el mapa parece
visible.

## De un archivo a una página web

El navegador interpreta **HTML** para conocer la estructura y el significado del
contenido, **CSS** para presentarlo y **JavaScript** para reaccionar a acciones
o cargar datos. Un servidor estático entrega esos archivos sin ejecutar una
aplicación del lado del servidor. Git no publica páginas: registra una historia
local de cambios que después puede compartirse con un remoto si el proyecto lo
necesita.

Una página mantenible usa elementos por su función. `main` contiene el contenido
principal, `h1` nombra el tema, `label` explica un control, `button` ejecuta una
acción y `table` ofrece datos tabulares. Un `div` sigue siendo útil para
agrupar, pero no reemplaza los elementos que ya describen el propósito del
contenido.

```html
<main>
  <h1>Mapa de zonas</h1>
  <label for="filtro">Valor mínimo</label>
  <select id="filtro" name="filtro"></select>
  <p id="estado" role="status" aria-live="polite"></p>
</main>
```

El atributo `for` enlaza la etiqueta con el control. `role="status"` y
`aria-live="polite"` permiten anunciar cambios de carga o error sin interrumpir
innecesariamente a quien usa un lector de pantalla.

## CSS que se adapta

Una interfaz responsive no depende de una medida exacta de pantalla. Usa anchos
relativos, texto que puede crecer y una disposición que conserva controles,
leyenda y tabla a 320 CSS px o con zoom del navegador al 200 %. El foco visible
es obligatorio para navegar sin ratón; el color por sí solo no comunica que un
control tiene foco, está seleccionado o falló.

El ejemplo mantenido usa una superficie simple, bordes de alto contraste y una
tabla que puede desplazarse con la página. No usa sombras ni controles
decorativos sobre el mapa. Esta decisión deja espacio para que los datos y el
estado sean legibles.

## HTTP y carga de datos

`file://` abre un archivo directamente desde el disco. En ese modo los
navegadores aplican restricciones distintas y una solicitud `fetch` puede fallar
aunque el archivo exista. Un servidor HTTP responde solicitudes del navegador y
permite comprobar qué recurso se pidió y qué código devolvió.

En el ejemplo, `fetch('data/referencia.geojson')` solicita un GeoJSON relativo a
la página. La respuesta debe verificarse antes de leer JSON:

```js
const response = await fetch('data/referencia.geojson');
if (!response.ok) throw new Error(`HTTP ${response.status}`);
const collection = await response.json();
```

`await` espera la respuesta sin bloquear la interfaz. Un código 200 indica que
la solicitud terminó correctamente; 404 indica que el recurso no existe en esa
ruta; 500 indica un problema interno del servidor. Una colección vacía no es lo
mismo que un error: el primer caso puede ser un resultado válido y el segundo
debe explicarse en la región de estado.

## HTTPS, origen y caché

Un **origen** combina esquema, host y puerto. Por ejemplo,
`http://localhost:8000` y `https://curso.example.org` son orígenes distintos. El
navegador aplica reglas adicionales cuando una página solicita recursos de otro
origen; esas reglas se profundizan al trabajar CORS y activos cloud-native en
las Unidades 5 y 7.

La **caché** guarda temporalmente recursos para evitar solicitudes repetidas.
Puede estar en el navegador, un proxy o un servidor. Una respuesta rápida puede
provenir de caché y no de una nueva transferencia. La caché no autoriza
precargar grandes áreas, descargar teselas para uso offline ni presentar una
copia antigua como dato actual. Para comprobar una solicitud nueva, usa una
ventana privada o desactiva la caché en las herramientas de desarrollo.

## Arquitectura de una publicación cartográfica

El curso usa el mismo modelo cliente-servidor en distintas escalas:

```text
Datos y manifiesto -> cliente Leaflet o MapLibre -> servidor estático
Datos y servicios locales -> PostGIS y GeoServer -> cliente MapLibre
PMTiles o COG -> servidor con HTTP Range -> protocolo MapLibre
```

Los datos y su manifiesto explican qué se publica; el cliente presenta una
interfaz; el servidor entrega recursos. Una API, un servidor de mapas o un
catálogo STAC no son sinónimos: cada uno resuelve una parte de la arquitectura.
Las Unidades 2, 4, 5 y 7 desarrollan esos conceptos sin aumentar la carga de
esta introducción.

## Módulos y mapa base

Un módulo ES es un archivo JavaScript con dependencias explícitas cargado con
`type="module"`. El ejemplo Leaflet mantiene su código separado en `main.js` y
sus estilos en `styles.css`; esa separación permite localizar responsabilidades
sin editar una página monolítica.

El [mapa Leaflet básico]({{ '/examples/leaflet/mapa_basico/' | relative_url }})
carga zonas sintéticas, filtra por atributo, muestra una leyenda y actualiza una
tabla equivalente. OpenStreetMap aporta contexto visual mediante teselas HTTPS y
atribución visible. Es un servicio público de mejor esfuerzo: no se precargan
teselas, no se usa para descarga offline y el ejercicio sigue siendo
interpretable mediante la tabla si el mapa base no está disponible.

## Git y publicación estática

Git organiza cambios locales. Un recorrido mínimo y no destructivo es:

```powershell
git status --short
git diff
git add docs/unidades/01_web_git_publicacion.md
git commit -m "Mejorar unidad web"
git log --oneline -5
```

`git status` muestra qué cambió; `git diff` permite revisar el contenido antes
de prepararlo; `git add` elige cambios para el siguiente commit; `git commit`
registra una instantánea con mensaje; `git log` muestra la historia. Un remoto
es otra copia del repositorio y un `push` envía commits a ese remoto cuando
exista una política autorizada. No publiques secretos, datos sensibles ni
resultados de otras personas para completar esta actividad.

Un hosting estático entrega un artefacto ya construido. En este curso GitHub
Pages es una implementación de referencia: publica `_site/`, no la raíz
histórica del repositorio. Un entorno institucional puede sustituirlo si entrega
HTTPS y preserva las rutas relativas del sitio.

## Práctica guiada

1. Desde la raíz, sirve el repositorio con `python -m http.server 8000`.
2. Abre `http://localhost:8000/examples/leaflet/mapa_basico/`.
3. Recorre el selector con Tab, elige `Valor 20 o superior` y comprueba que el
   estado y la tabla muestran el mismo número de zonas que el mapa.
4. Abre las herramientas de desarrollo, selecciona la pestaña Network y recarga.
   Observa `data/referencia.geojson`: registra URL, método, código, tipo de
   contenido, tamaño y si la respuesta vino de caché.
5. En una copia temporal del ejemplo, cambia la ruta del GeoJSON a un nombre
   inexistente, recarga y observa el error 404. Restaura la ruta antes de
   terminar.
6. Crea una nota Markdown local con encabezado, lista, enlace relativo al
   ejemplo y bloque de código. Comprueba su formato con `npm run lint:markdown`;
   no publiques datos personales ni necesitas una cuenta remota.

## Panorama posterior

Algunas tecnologías aparecen en unidades posteriores:

- **JSON** es texto estructurado usado por GeoJSON y OGC API - Features. La
  Unidad 2 estudia datos geográficos y la Unidad 4 contratos de API.
- **XML**, **GML** y **KML** son formatos basados en etiquetas. WFS puede
  entregar GML; la Unidad 4 compara contratos y representaciones.
- **REST** es un estilo de arquitectura HTTP con recursos direccionables y
  operaciones bien definidas. OGC API - Features lo aplica en la Unidad 4.
- **RPC** y **SOAP** son modelos históricos o panorámicos para invocar
  operaciones remotas; no son requisitos del núcleo.
- Los frameworks de interfaz, servidores de aplicación, clientes de escritorio y
  móviles son opciones de arquitectura. El núcleo usa JavaScript modular,
  TypeScript, Vite, Leaflet y MapLibre sin exigir React, Vue o Svelte.
- Flash y Flex son tecnologías históricas retiradas; se mencionan solo para
  reconocer por qué el contenido antiguo no debe reutilizarse.

## Errores frecuentes

- Abrir la página con `file://` y concluir que `fetch` está roto.
- Usar un `div` clicable en vez de un `button` o un control sin `label`.
- Tratar cualquier respuesta como JSON sin revisar `response.ok`.
- Confundir Internet con la Web o una URL con el recurso que identifica.
- Poner una credencial en una URL o copiar una URL histórica sin revisar su
  origen y seguridad.
- Interpretar una respuesta en caché como una transferencia nueva.
- Ocultar la tabla porque “el mapa ya muestra los datos”.
- Eliminar la atribución del mapa base o usar una URL HTTP insegura.
- Confundir un commit local con una publicación remota.

## Autoevaluación

Antes de continuar, responde:

1. ¿Qué diferencia hay entre HTML, CSS y JavaScript en el ejemplo?
2. ¿Por qué `file://` no es una forma válida de probar `fetch`?
3. ¿Qué debe hacer la interfaz después de un HTTP 404 del GeoJSON?
4. ¿Qué registra un commit y qué no registra Git?
5. ¿Qué información ofrece la tabla que no debe depender de operar el mapa?
6. ¿Qué partes de una URL se envían al servidor y cuál usa solo el navegador?
7. ¿Qué diferencia hay entre una respuesta HTTP nueva y una respuesta desde
   caché?

La respuesta a estas preguntas y el mapa servido por HTTP preparan la [Entrega
1]({{ '/evaluacion/entrega-1/' | relative_url }}).

## Diagnóstico

Explica la diferencia entre abrir un HTML mediante `file://` y servirlo con
`python -m http.server 8000`. Demuestra la respuesta observando la solicitud
GeoJSON, el estado de carga, el filtro, la leyenda y la tabla del ejemplo.
