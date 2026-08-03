---
layout: default
title: Unidad 3. Cartografía accesible y UX
permalink: /unidades/03-cartografia-accesible/
---

# Unidad 3. Cartografía accesible y UX

**Tiempo:** cuatro horas presenciales y cuatro horas autónomas. **Producto:** un
mapa temático que comunica una pregunta territorial, declara sus límites y
ofrece una alternativa equivalente a la lectura visual. La accesibilidad no es
una capa final de revisión: condiciona qué controles, símbolos y explicaciones
se eligen desde el inicio.

## Resultados de aprendizaje

Al finalizar podrás:

- Formular una pregunta territorial y elegir una variable que la responda.
- Distinguir conteos, tasas, proporciones y valores normalizados.
- Justificar una clasificación, una paleta y una leyenda.
- Comunicar incertidumbre, cobertura, fecha, fuente y límites de interpretación.
- Revisar teclado, foco, reflow, contraste, estados y alternativa tabular de un
  mapa según el alcance WCAG 2.2 AA.

## Del dato a la afirmación cartográfica

Un mapa temático no es una decoración de una tabla. Afirma algo sobre un lugar,
un fenómeno y un momento. Antes de simbolizar, formula una pregunta precisa:
“¿Dónde es mayor el valor observado?” no equivale a “¿Dónde es mayor la tasa por
habitante?”. La primera puede usar un conteo; la segunda necesita una medida
normalizada.

Un **conteo** expresa cuántos casos hay. Una **tasa** relaciona casos con una
base comparable, como población, superficie o tiempo. La **normalización**
convierte valores que no son directamente comparables en una medida común. Un
mapa de coropletas con conteos de población suele favorecer territorios grandes;
un mapa con densidad o tasa puede responder otra pregunta. Ninguna opción es
automáticamente correcta: la leyenda y la explicación deben declarar qué se
mide.

La capa sintética del ejemplo contiene puntos con el atributo `valor`. Es útil
para practicar filtros y símbolos, pero no representa una tasa ni permite sacar
conclusiones sobre un territorio real. Este límite debe escribirse junto al
mapa, no quedar implícito en el código.

## Clasificación y símbolos

**Clasificar** significa agrupar valores numéricos en intervalos o categorías.
Los cortes pueden ser iguales, seguir cuantiles, usar rupturas naturales o
responder a umbrales de una política pública. Cada método muestra una historia
distinta: cambiar los cortes puede cambiar qué zonas parecen altas o bajas.

Una clasificación es adecuada cuando los intervalos son comprensibles y están
justificados. Si hay pocos valores, una escala continua o etiquetas directas
pueden ser más claras. Si hay categorías nominales, no se debe fingir un orden
con una paleta secuencial.

| Tipo de dato                     | Símbolo inicial         | Riesgo que debes revisar            |
| -------------------------------- | ----------------------- | ----------------------------------- |
| Categorías sin orden             | Tonos distinguibles     | Sugerir jerarquía inexistente       |
| Magnitud ordenada                | Paleta secuencial       | Cortes arbitrarios o contraste bajo |
| Desviación respecto a referencia | Paleta divergente       | Punto medio no explicado            |
| Conteo localizado                | Símbolos proporcionales | Confundir tamaño visual y área      |
| Tasa por área                    | Coropleta               | Usar totales sin normalizar         |

No uses color como único canal. Combina leyenda, texto, valores en tabla,
etiquetas o patrones cuando la interpretación dependa de una distinción crítica.
Una persona con visión del color diferente, con pantalla de bajo contraste o que
lee el resultado desde una tabla debe poder llegar a la misma conclusión
principal.

## Paleta, contraste y jerarquía

Una **paleta secuencial** cambia de claro a oscuro para comunicar menor a mayor
valor. Una **paleta divergente** usa dos direcciones desde un punto central, por
ejemplo una meta o cero. Una **paleta cualitativa** separa categorías que no
tienen orden. Elige colores que mantengan contraste con el fondo y entre clases
adyacentes, pero no prometas precisión que el dato no contiene solo porque el
degradado sea suave.

La jerarquía visual indica qué debe leerse primero. En un mapa temático, la capa
de interés debe distinguirse del mapa base, que aporta contexto sin competir con
los datos. OpenStreetMap se usa en el ejemplo como contexto atribuible; si no
carga, la tabla, leyenda y estado siguen explicando las zonas sintéticas.

Una leyenda completa nombra la variable, indica unidad, explica símbolos o
clases y declara cualquier umbral relevante. Una escala aclara la relación entre
distancia del mapa y distancia territorial. La atribución identifica fuente de
datos, licencia y proveedor del mapa base cuando corresponde.

## Incertidumbre y límites

La incertidumbre no se reduce a una barra de error. Puede aparecer como fecha
desactualizada, cobertura parcial, geocodificación aproximada, atributos
faltantes, clasificación discutible o escala que oculta variación local. Escribe
lo que el mapa no permite concluir. Por ejemplo: “los valores son sintéticos y
solo demuestran el funcionamiento del filtro; no representan distribución real”.

El mapa debe indicar fuente, versión, licencia, CRS cuando sea relevante y el
periodo temporal. Si un dato puede identificar personas o rutas sensibles, no se
publica hasta que se resuelvan base de uso, minimización y sensibilidad. Una
visualización atractiva no elimina ese riesgo.

## Accesibilidad aplicada a mapas

WCAG 2.2 AA se aplica a la interacción y al contenido alrededor del canvas. Un
mapa accesible debe ofrecer:

- Un nombre accesible que explique qué representa.
- Controles etiquetados, operables por teclado y con foco visible.
- Estados de carga, vacío y error anunciados en texto.
- Leyenda y atribución visibles y comprensibles.
- Reflow a 320 CSS px y con zoom de texto sin perder controles o datos.
- Una tabla, resumen o descarga que exprese el hallazgo principal sin arrastrar,
  hacer zoom o interpretar color.

El popup puede complementar la consulta, pero no es la única forma de obtener
los valores. El ejemplo Leaflet muestra cada zona en una tabla y comunica el
número de zonas visibles en una región `role="status"`. El foco visible permite
ver dónde está la interacción; no basta con responder al ratón.

Las pruebas Axe detectan algunos problemas automatizables. No sustituyen revisar
orden de foco, significado de la leyenda, reflow, contraste o lector de
pantalla. La evidencia manual se conserva en la [hoja de revisión]({{
'/gobierno/evidencia-accesibilidad/' | relative_url }}).

## Práctica guiada

1. Abre el [mapa Leaflet básico]({{ '/examples/leaflet/mapa_basico/' |
   relative_url }}) por HTTP.
2. Lee la leyenda y la atribución. Escribe qué variable representa el círculo y
   qué no permite concluir el fixture.
3. Usa solo Tab, Shift+Tab, Enter y las teclas del selector para aplicar
   `Valor 20 o superior`. Comprueba que estado, círculos y tabla coinciden.
4. Reduce la ventana a 320 CSS px o usa zoom al 200 %. Verifica que selector,
   estado, leyenda, mapa y tabla siguen disponibles.
5. Propón una versión coroplética de una variable real. Indica si usarías total,
   tasa o proporción; método de clasificación; paleta; unidad; fuente; fecha;
   incertidumbre y alternativa tabular.
6. Revisa la propuesta de otra persona con los criterios de la Entrega 1.

## Errores frecuentes

- Usar una coropleta con totales cuando la pregunta exige una tasa.
- Ocultar cortes, unidad o método de clasificación en la leyenda.
- Elegir colores solo por preferencia estética y sin contraste suficiente.
- Presentar un mapa base como si fuera fuente de los datos temáticos.
- Omitir incertidumbre, fecha, cobertura o licencia.
- Reemplazar tabla y texto por un popup que requiere ratón.
- Declarar conformidad WCAG solo porque Axe no reportó errores.

## Autoevaluación

1. ¿Qué pregunta respondería un conteo y cuál una tasa normalizada?
2. ¿Cuándo usarías una paleta secuencial y cuándo una divergente?
3. ¿Qué debe contener una leyenda para que una clase sea interpretable?
4. ¿Qué límite del dato debes comunicar aunque el mapa funcione técnicamente?
5. ¿Qué información ofrece la tabla si una persona no puede usar el canvas?

El resultado de esta unidad se integra en la [Entrega
1]({{ '/evaluacion/entrega-1/' | relative_url }}) y se revisa con la [guía de
accesibilidad]({{ '/guias/accesibilidad/' | relative_url }}).

## Diagnóstico

Con el mapa básico abierto, usa solo teclado para llegar al selector y al mapa.
Luego reduce el ancho de la ventana a 320 CSS px y verifica que la tabla y la
leyenda siguen disponibles. Explica qué decisión cartográfica tomarías si el
atributo `valor` fuese un conteo de población y la pregunta fuera comparar zonas
de tamaños distintos.
