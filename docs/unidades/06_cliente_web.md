---
layout: default
title: Unidad 6. Cliente web con MapLibre
permalink: /unidades/06-cliente-web/
---

# Unidad 6. Cliente web con MapLibre

**Tiempo:** cuatro horas presenciales y seis horas autónomas. **Producto:** un
cliente TypeScript mantenible que carga datos, filtra entidades, conserva una
vista compartible, anuncia errores y ofrece tabla equivalente. El cliente no usa
un framework ni requiere un token de mapas.

## Resultados de aprendizaje

Al finalizar podrás:

- Explicar qué aporta TypeScript y qué produce Vite durante desarrollo y build.
- Identificar los módulos de configuración, estado, mapa, mensajes y arranque.
- Distinguir fuente, capa, evento y estilo en MapLibre.
- Conservar filtros y vista en una URL compartible sin aceptar valores
  inválidos.
- Probar carga, filtro, consulta, error y accesibilidad automatizada en un
  navegador.

## Arquitectura pequeña y explícita

El cliente mantenido vive en `examples/maplibre/app/`. TypeScript detecta
inconsistencias antes de ejecutar; Vite sirve módulos durante desarrollo y crea
archivos estáticos en `dist/` para publicación. MapLibre usa WebGL para dibujar
capas cartográficas. Ninguna de esas herramientas decide qué significa un dato:
esa decisión sigue siendo responsabilidad de la configuración, la interfaz y la
documentación.

| Módulo          | Responsabilidad                                  | Evidencia observable                         |
| --------------- | ------------------------------------------------ | -------------------------------------------- |
| `src/config.ts` | URLs, colección, atribución y fuente inicial     | Cambia entre stack local y assets publicados |
| `src/state.ts`  | Lee y escribe longitud, latitud, zoom y filtro   | La URL conserva una vista compartible        |
| `src/map.ts`    | Inicializa MapLibre, fuentes y capas             | El mapa contiene OSM y la capa seleccionada  |
| `src/status.ts` | Centraliza mensajes de estado                    | Carga, vacío y error se anuncian en texto    |
| `src/main.ts`   | Conecta controles, fetch, tabla, consulta y foco | Filtro, diálogo y tabla cambian juntos       |

Separar responsabilidades no significa crear archivos por costumbre. Aquí cada
módulo tiene una decisión observable y una prueba posible. Un cliente monolítico
puede funcionar al inicio, pero dificulta localizar un error de URL, una regla
de estado o una capa cuando el proyecto crece.

## Configuración local y sitio publicado

El mismo build puede ejecutarse localmente o como sitio estático. En
`config.ts`, `localhost` y `127.0.0.1` usan el GeoServer local para consultar
OGC API - Features y el Nginx local para PMTiles/COG. Fuera de esos hosts, el
cliente usa el GeoJSON y los assets publicados dentro del propio artefacto.

Esta diferencia evita un error común: publicar un cliente que intenta conectar a
`localhost` del visitante. En una página publicada, `localhost` no es el
servidor resuelven como rutas relativas al sitio ensamblado.

El mapa base OpenStreetMap aporta orientación visual, no datos temáticos.
Mantiene atribución visible y se agrega después de que el estilo esté listo para
que una tesela externa lenta no bloquee la capa de referencia. Si OSM falla, el
cliente sigue ofreciendo estado y tabla; no se usa el mapa base para validar
resultados.

## Fuente, capa y estilo

Una **fuente** indica de dónde llegan los datos: GeoJSON, vector tiles, raster o
un protocolo como PMTiles/COG. Una **capa** indica cómo dibujar esa fuente:
círculos, líneas, rellenos o raster. Un estilo MapLibre reúne fuentes y capas.
La fuente `referencia` se reemplaza cuando se cambia entre OGC API, PMTiles y
COG para evitar que dos versiones del mismo dato compitan en el canvas.

| Fuente seleccionada | Tipo          | Capa                        | Uso de aprendizaje                    |
| ------------------- | ------------- | --------------------------- | ------------------------------------- |
| OGC API - Features  | GeoJSON       | Círculos                    | Entidades y atributos web             |
| PMTiles             | Vector        | Círculos desde `referencia` | Teselas vectoriales estáticas         |
| COG                 | Raster        | Raster                      | Bloques de imagen optimizada          |
| OSM                 | Raster remoto | Raster                      | Contexto atribuible de mejor esfuerzo |

Una fuente vectorial no es un estilo: PMTiles entrega entidades por tesela y la
capa `circle` decide color y tamaño. Un COG no es un mapa base: es un activo
raster con sus propios valores, bloques y overviews. La Unidad 7 profundiza esas
rutas y sus mediciones.

## Estado URL y filtros

`MapState` contiene longitud, latitud, zoom y `minimumValue`. `readStateFromUrl`
lee esos valores y usa una vista segura si faltan, están vacíos o no son
números. `writeStateToUrl` actualiza la dirección con `history.replaceState`,
sin recargar la página. Así se puede copiar una vista filtrada sin convertir
cada movimiento del mapa en una entrada nueva del historial.

El filtro compara `valor` con el mínimo elegido y luego actualiza
simultáneamente la capa y la tabla. Mantener las dos representaciones a partir
de la misma lista filtrada evita que el mapa diga una cosa y la tabla otra. Un
filtro debe declarar atributo, unidad, tratamiento de valores faltantes y
significado territorial; comparar números sin contexto no es una decisión
cartográfica completa.

## Carga, error y consulta

La función `load()` solicita la colección, comprueba `response.ok`, filtra,
actualiza el mapa y construye filas de tabla. Si la red falla o el servidor
responde un código no exitoso, `setStatus()` anuncia un mensaje comprensible. Un
error no se trata como una colección vacía.

La consulta por clic busca una entidad renderizada y abre un `dialog`. Con el
mapa enfocado, <kbd>Enter</kbd> o <kbd>Espacio</kbd> consulta la entidad del
centro. Al cerrar, el foco vuelve al mapa. El diálogo complementa la tabla: no
es la única forma de obtener nombre, valor y coordenadas.

## Pruebas como parte del cliente

Vitest prueba funciones puras, por ejemplo la lectura segura de la URL.
Playwright abre Chromium, Firefox o WebKit y recorre la página real. Axe revisa
problemas automatizables de accesibilidad. Ninguna prueba automatizada sustituye
la revisión manual de teclado, contraste, reflow, lector de pantalla y Safari
real del piloto.

Las pruebas E2E comprueban carga, URL tras filtrar, error de red, PMTiles, COG y
fuente OSM. Si una tesela OSM externa tarda, la capa de referencia debe seguir
agregándose: el estilo está preparado aunque el contexto remoto sea de mejor
esfuerzo.

Consulta el [cliente MapLibre mantenido]({{ '/examples/maplibre/' |
relative_url }}) para probar la colección, el filtro, PMTiles y COG desde el
sitio publicado.

## Ejecución

Inicia primero el stack de la Unidad 5. Luego, desde la raíz del repositorio:

```powershell
npm run --workspace examples/maplibre/app dev
```

Abre la dirección que anuncia Vite. Aplica un valor mínimo, copia la URL y
comprueba que al abrirla de nuevo se recuperan la vista y el filtro. Luego
cambia la fuente a PMTiles y COG; confirma que la tabla sigue mostrando el mismo
resultado y que la atribución del mapa base permanece visible.

## Práctica guiada

1. Lee `config.ts` y escribe qué URLs se usan en local y cuáles se usan en el
   sitio publicado.
2. Abre `state.ts`, añade manualmente `?lng=-74.1&lat=4.7&zoom=12&min=18` a la
   URL y comprueba que el cliente interpreta la vista y el filtro.
3. Escribe un valor no numérico en `lng` y explica por qué el cliente vuelve a
   la vista de referencia.
4. Usa el selector de fuente para comparar OGC API, PMTiles y COG. Indica qué
   fuente y capa se agregan en cada caso.
5. En las herramientas de red o mediante la prueba E2E, provoca un fallo de OGC
   API. Comprueba que la región de estado explica el problema sin vaciar la
   página silenciosamente.
6. Navega con teclado hasta el mapa, abre el diálogo de consulta y confirma que
   el foco vuelve al mapa al cerrar.

## Errores frecuentes

- Publicar una URL `localhost` que funciona solo en el computador de desarrollo.
- Confundir fuente con capa o asumir que un PMTiles trae un estilo completo.
- Actualizar el mapa y olvidar actualizar la tabla equivalente.
- Escribir el filtro en la URL sin validar números faltantes o inválidos.
- Usar un popup como única alternativa a la consulta visual.
- Eliminar atribución OSM o usar el mapa base como evidencia temática.
- Marcar accesibilidad completa porque Axe no reportó problemas.

## Autoevaluación

1. ¿Qué error detecta TypeScript antes de abrir el navegador?
2. ¿Qué cambia Vite entre desarrollo y build?
3. ¿Qué diferencia hay entre una fuente GeoJSON y una capa de círculos?
4. ¿Por qué el cliente publicado no debe consultar `localhost`?
5. ¿Qué valores conserva `MapState` y por qué se validan?
6. ¿Qué prueba se usa para una función pura y cuál para un flujo de navegador?

Esta unidad prepara la aplicación mantenible de la [Entrega
3]({{ '/evaluacion/entrega-3/' | relative_url }}). La infraestructura local se
explica en la [Unidad 5]({{ '/unidades/05-servicios-infraestructura/' |
relative_url }}) y los formatos optimizados en la [Unidad
7]({{ '/unidades/07-rendimiento-cloud-native/' | relative_url }}).

## Diagnóstico

Desconecta temporalmente GeoServer o intercepta la solicitud en Playwright.
Identifica el mensaje de error, restaura el servicio y comprueba que tabla, mapa
tratarse como una colección vacía y por qué la fuente OSM no debe bloquear la
capa temática.
