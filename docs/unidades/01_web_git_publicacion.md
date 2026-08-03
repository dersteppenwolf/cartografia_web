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
4. Abre las herramientas de desarrollo del navegador y observa la solicitud de
   `data/referencia.geojson`: registra URL, código, tipo de contenido y tamaño.
5. En una copia temporal del ejemplo, renombra el GeoJSON, recarga y lee el
   mensaje de error. Restaura el nombre antes de terminar.

## Errores frecuentes

- Abrir la página con `file://` y concluir que `fetch` está roto.
- Usar un `div` clicable en vez de un `button` o un control sin `label`.
- Tratar cualquier respuesta como JSON sin revisar `response.ok`.
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

La respuesta a estas preguntas y el mapa servido por HTTP preparan la [Entrega
1]({{ '/evaluacion/entrega-1/' | relative_url }}).

## Diagnóstico

Explica la diferencia entre abrir un HTML mediante `file://` y servirlo con
`python -m http.server 8000`. Demuestra la respuesta observando la solicitud
GeoJSON, el estado de carga, el filtro, la leyenda y la tabla del ejemplo.
