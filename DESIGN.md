# Sistema visual del curso

Este documento es la referencia visual para `docs/`, los ejemplos mantenidos y
los artefactos publicados. No describe una marca que deba copiarse literalmente.
Convierte dos ideas observadas en Memorisely y Uxcel en normas apropiadas para
un curso sin cuentas obligatorias: aprendizaje visible mediante practica y
feedback, y una ruta clara de lecciones pequenas que permite saber que hacer
despues.

La referencia anterior de portafolio se adapta al contenido docente. Un curso no
es una galeria: necesita navegacion, objetivos, ejercicios, estados, datos,
leyendas, atribuciones y alternativas accesibles. La funcion cartografica y WCAG
2.2 AA prevalecen sobre cualquier decision estetica.

## Principios

1. **Orientar antes de explicar.** Cada pagina deja claro donde esta la persona,
   que competencia trabaja, cuanto tiempo estima y cual es el siguiente
   artefacto verificable.
2. **Aprender haciendo.** La teoria se presenta en bloques cortos que culminan
   en una observacion, un comando, una decision cartografica o una pregunta de
   comprobacion. Una lectura no sustituye una practica reproducible.
3. **Hacer visible el progreso sin gamificacion vacia.** La ruta de ocho
   unidades, los resultados de aprendizaje y el producto de cada unidad se
   muestran como texto y estructura semantica. No se agregan rachas, puntos,
   medallas ni competencia entre estudiantes.
4. **Usar una jerarquia editorial contenida.** El texto base es pequeno y claro;
   la jerarquia aparece mediante encabezados semanticos, peso, espaciado,
   agrupacion y contraste, no mediante titulos gigantes o decoracion.
5. **Mostrar evidencia, no promesas.** Estados de carga, error, resultado de
   pruebas, tablas, checksum, atribucion y limites del dato son partes visibles
   del aprendizaje.
6. **Mantener la interfaz calmada.** Una superficie clara, una familia sans
   serif, bordes rectos y ausencia de sombras o gradientes permiten concentrarse
   en mapas, datos y ejercicios.
7. **No depender de una plataforma externa.** Un enlace a Pages, OSM u otra
   referencia debe ser contextual u optativo. El recorrido obligatorio conserva
   alternativa local y textual.

## Referencias transformadas

Memorisely aporta una secuencia enfocada en practica, retroalimentacion y
resultados concretos. En este curso se traduce en: resultado de aprendizaje al
inicio, bloque de practica, errores frecuentes, autoevaluacion y relacion con
una entrega. No se copian sus testimonios, contadores, ilustraciones, llamados
comerciales ni su identidad visual.

Uxcel aporta lecciones breves, rutas de aprendizaje, progreso legible y
ejercicios aplicados. En este curso se traduce en: ocho unidades ordenadas,
tiempo declarado, producto verificable, navegacion entre unidad anterior y
siguiente, y actividades de diagnostico. No se copian sus marcas, insignias,
rankings, precios, perfiles, certificaciones ni mecanismos de retencion.

## Tokens

Los valores se definen en `docs/assets/css/tokens.css`. No repetir literales de
color o espacio en componentes nuevos. Si hace falta un token, se agrega primero
en ese archivo y luego se sincroniza con el cliente MapLibre.

### Color

| Nombre        | Valor     | Token                  | Uso                                                           |
| ------------- | --------- | ---------------------- | ------------------------------------------------------------- |
| Blanco papel  | `#ffffff` | `--color-paper-white`  | Lienzo, superficies principales y texto invertido             |
| Negro tinta   | `#000000` | `--color-ink-black`    | Texto principal, bordes, foco y controles de alto contraste   |
| Gris galeria  | `#e5e5e5` | `--color-gallery-gray` | Bandas funcionales, ejercicios o contexto secundario          |
| Gris plinto   | `#d4d4d4` | `--color-plinth-gray`  | Separacion de secciones o pie de pagina                       |
| Negro carbono | `#0a0a0a` | `--color-carbon-black` | Bloques oscuros de codigo, aviso o navegacion invertida       |
| Negro pizarra | `#171717` | `--color-slate-black`  | Superficie oscura secundaria                                  |
| Piedra        | `#737373` | `--color-stone`        | Texto secundario solo si supera contraste AA                  |
| Grafito       | `#525252` | `--color-graphite`     | Texto secundario fuerte, metadatos y explicaciones auxiliares |

`#a3a3a3` no se usa como texto sobre blanco. El color no es el unico canal para
indicar estado, progreso, importancia, seleccion o error. Los mensajes incluyen
texto y los controles mantienen etiquetas visibles.

### Tipografia

- Usar una sola familia sans serif: `--font-abc-oracle`, que corresponde a Inter
  o la pila de sistema mientras no exista licencia documentada de ABC Oracle.
- Mantener `0.875rem` como apariencia base y pesos 400 y 500.
- Usar `line-height: 1.43` en prosa. No usar interlineado 1.0 en bloques de
  varias lineas.
- Conservar encabezados HTML `h1` a `h3`. Su jerarquia visual se resuelve con
  peso, espacio y posicion, no con una escala tipografica espectacular.
- Los metadatos, comandos y etiquetas se diferencian por agrupacion y contraste,
  no por convertir todo el contenido en mayusculas.

### Espacio y forma

La unidad base es 6 px. Preferir 6, 8, 12 y 48 px. Usar entre 48 y 96 px entre
secciones mayores. Los modulos de aprendizaje usan 12 px de separacion interna;
un bloque extenso necesita espacio adicional antes y despues, no una sombra.

Todos los radios son 0. No usar sombras, gradientes, blur, glassmorphism ni
elevacion. Los bordes de 1 px se reservan para controles, tablas, bloques de
estado y limites funcionales; no se usan para decorar cada parrafo.

## Arquitectura de pagina

### Pagina de inicio

La portada presenta primero el proposito del curso y la ruta de ocho unidades.
Cada unidad muestra numero, tema, producto verificable y enlace. Los ejemplos
mantenidos aparecen despues como entradas funcionales, no como una coleccion de
tarjetas promocionales. La informacion de gobierno, planes y desarrollo queda
visible pero subordinada al recorrido de aprendizaje.

### Pagina de unidad

Cada unidad mantenida sigue esta secuencia:

1. Titulo semantico, tiempo presencial/autonomo y producto verificable.
2. Resultados de aprendizaje en una lista breve y accionable.
3. Conceptos explicados en secciones pequenas, con terminos definidos antes de
   usarlos.
4. Ejemplo o artefacto mantenido enlazado con una frase que explique que
   observar.
5. Practica guiada con pasos numerados, resultado esperado y limite de
   seguridad.
6. Errores frecuentes que previenen interpretaciones o comandos peligrosos.
7. Autoevaluacion o diagnostico que conecta con la entrega correspondiente.
8. Navegacion textual hacia unidad anterior, siguiente, ejemplo y rubrica cuando
   esas rutas existan.

No agregar una barra de progreso falsa. La ruta de unidades y el producto
verificable ya comunican avance de forma honesta.

### Paginas de referencia

Las guias, rubricas, gobierno y planes usan encabezados claros, prosa con ancho
de lectura contenido y tablas solo cuando comparan valores o contratos. Los
planes de ejecucion conservan el formato exigido por `PLANS.md`; esta guia no lo
reemplaza.

### Ejemplos cartograficos

El mapa es una region funcional, no un fondo decorativo. Debe conservar
controles propios de la biblioteca cuando sean necesarios, atribucion legible,
leyenda, estado, tabla o resumen equivalente y mensajes de error. Los controles
de filtro primarios se sitúan fuera del canvas. Se permite un mapa base solo con
atribucion, HTTPS, politica de uso compatible y alternativa cuando falle.

## Componentes docentes

### Franja de contexto

Se usa al inicio de una unidad para indicar tiempo, producto y prerequisito. Es
texto corto sobre blanco o gris galeria; no usa iconos decorativos. Si un
prerrequisito falta, se enlaza a la guia o unidad correspondiente.

### Resultado de aprendizaje

Lista de verbos observables: explicar, comparar, generar, validar, justificar o
recuperar. Evitar objetivos vagos como “comprender todo”. Cada resultado debe
conectar con un ejercicio, prueba o criterio de rubrica.

### Bloque de practica

Agrupa proposito, pasos, comando, resultado esperado y recuperacion. Puede usar
gris galeria para separarse de la prosa, pero mantiene texto negro, enlaces
subrayados y comandos copiables. Un comando destructivo declara primero backup,
alcance y recuperacion.

### Bloque de evidencia

Muestra un estado de prueba, respuesta HTTP, checksum, tabla o resultado de
validacion. No se colorea unicamente en verde o rojo: incluye palabras como
“correcto”, “error”, “pendiente” o “bloqueado” y explica la siguiente accion.

### Diagnostico y autoevaluacion

Las preguntas aparecen al final de la leccion y exigen aplicar conceptos, no
memorizar definiciones. Deben poder responderse con el material y los artefactos
locales; no deben exigir un login ni consultar una API externa.

### Navegacion de unidad

Usar enlaces de texto claros: “Unidad anterior”, “Siguiente unidad”, “Abrir
ejemplo”, “Ver rubrica”. El estado actual se comunica con texto, `aria-current`
cuando corresponda y foco visible. No sustituir enlaces por flechas sin
etiqueta.

### Tablas y datos

Usar tablas HTML para equivalentes de mapa, resultados comparables o contratos
de servicio. Incluir `caption`, encabezados `th`, unidades y orden de lectura.
En pantallas pequenas, permitir desplazamiento horizontal o una version
resumida; nunca ocultar los valores esenciales para proteger una composicion.

## Interaccion y estados

- Todo control se opera con teclado y muestra `:focus-visible` de alto
  contraste.
- Los enlaces se distinguen por subrayado, no solo por color.
- Hover es opcional y nunca contiene informacion exclusiva.
- Los estados de carga, exito, vacio y error usan una region de estado con texto
  claro. No dejar un mapa, tabla o panel vacio sin explicacion.
- Los dialogos gestionan foco al abrir y devolverlo al cerrar.
- La URL conserva filtros y vista cuando esa informacion sea compartible.
- Respetar `prefers-reduced-motion`; no introducir animacion decorativa. Una
  transicion funcional debe ser breve y nunca impedir leer o operar contenido.

## Responsive y accesibilidad

La interfaz se prueba a 320 CSS px, zoom de texto y zoom de navegador al 200 %.
No bloquear escalado, usar alturas fijas para prosa ni depender de arrastre. El
contenido sigue una columna de lectura en movil y amplía el margen en pantallas
grandes. Los mapas pueden usar mayor ancho cuando su funcion lo exige, pero la
leyenda, filtros y tabla mantienen una lectura lineal fuera o junto al canvas.

Toda imagen usa texto alternativo util. Una imagen decorativa usa `alt=""`; una
captura que enseña un resultado describe la observacion relevante. Video incluye
subtitulos o transcripcion. Axe y Playwright son apoyo; la revision manual de
teclado, foco, contraste, reflow, lector de pantalla y Safari real se registra
en `docs/governance/manual-accessibility-review.md`.

## Imagenes, iconos y mapas base

Las imagenes se incorporan solo si tienen procedencia, licencia y alternativa
textual resueltas. No usar fotos de relleno ni ilustraciones que compitan con un
mapa o ejercicio. Los iconos son funcionales, tienen nombre accesible y no
sustituyen una etiqueta necesaria.

Un mapa base aporta orientacion, no evidencia tematica. Si se usa OSM Standard,
mostrar atribucion visible, usar HTTPS, no precargar teselas ni ofrecer descarga
interpretables si ese servicio externo no responde.

## Patrones que se deben evitar

- Hero con imagen o eslogan que retrase la ruta de aprendizaje.
- Carruseles, autoavance, contadores, rankings, medallas o gamificacion sin
  valor curricular.
- Tarjetas con sombra, radios grandes, degradados, efectos de cristal o iconos
  decorativos.
- Texto centrado de varias lineas, enlaces sin subrayado o controles solo por
  hover.
- Lienzos de mapa sin leyenda, atribucion, estado ni alternativa tabular.
- Repetir datos de progreso o testimonios como sustituto de ejercicios y
  evidencia verificable.
- Ocultar complejidad operativa relevante, por ejemplo CORS, licencia, secreto,
  sensibilidad, error o recuperacion, para mantener una pagina “limpia”.

## Aplicacion tecnica

`docs/assets/css/tokens.css` es la fuente de tokens. `docs/assets/css/site.css`
aplica la composicion editorial del sitio. `scripts/sync_design_tokens.py`
sincroniza tokens con `examples/maplibre/app/src/styles/tokens.css`; ejecutar su
modo `--check` despues de modificar tokens. Los ejemplos pueden ampliar estilos
por necesidad cartografica, pero conservan los colores, foco, tipografia, radios
y espaciado definidos aqui.

No agregar Tailwind, un framework de frontend ni una biblioteca de componentes
solo para aplicar esta guia. CSS nativo y componentes semanticos son la opcion
por defecto.

## Lista de revision visual

Antes de publicar una pagina o ejemplo, comprobar:

- La pagina identifica unidad, resultado y siguiente accion sin depender de una
  imagen.
- Los encabezados mantienen orden semantico y la prosa usa interlineado legible.
- Los enlaces, foco, estados y controles se distinguen con mas de un canal.
- La practica incluye resultado esperado y recuperacion cuando hay riesgo.
- El mapa tiene atribucion, leyenda, estado y alternativa equivalente.
- Las tablas conservan encabezados y lectura a 320 CSS px.
- Las dependencias externas son opcionales o tienen alternativa local.
- El contraste y la revision manual se registran donde corresponda.

## Revision

2026-08-03: reemplazo de la referencia de portafolio por un sistema visual para
aprendizaje guiado. Se adoptan lecciones breves, rutas claras, practica y
feedback inspirados en Memorisely y Uxcel, sin copiar su identidad, componentes,
marcas ni mecanismos comerciales. Se preservan las restricciones de
accesibilidad, monocromia, CSS nativo y contenido cartografico del repositorio.
