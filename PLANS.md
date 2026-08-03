# Planes de Ejecución de Codex (ExecPlans)

Este documento describe los requisitos para un plan de ejecución ("ExecPlan"), un documento de diseño que un agente de código puede seguir para entregar una funcionalidad operativa o un cambio de sistema. Trata a la persona lectora como principiante total en este repositorio: solo tiene el árbol de trabajo actual y el único archivo ExecPlan que le entregas. No hay memoria de planes previos ni contexto externo.

## Cómo usar ExecPlans y PLANS.md

Al redactar una especificación ejecutable (ExecPlan), sigue `PLANS.md` _al pie de la letra_. Si no está en tu contexto, vuelve a leer el archivo completo `PLANS.md`. Lee y relee con cuidado el material fuente para producir una especificación precisa. Al crear una especificación, empieza desde el esqueleto y complétalo a medida que investigas.

Al implementar una especificación ejecutable (ExecPlan), no preguntes al usuario por "siguientes pasos"; avanza directamente al siguiente hito. Mantén todas las secciones actualizadas, agrega o divide entradas en la lista en cada punto de pausa para declarar de forma afirmativa el progreso realizado y los siguientes pasos. Resuelve ambigüedades de manera autónoma y haz confirmaciones (`commits`) con frecuencia.

Al discutir una especificación ejecutable (ExecPlan), registra las decisiones en un registro dentro de la especificación para preservar el contexto. Debe quedar inequívocamente claro por qué se hizo cualquier cambio a la especificación. Los ExecPlans son documentos vivos, y siempre debe ser posible reiniciar el trabajo usando _solo_ el ExecPlan y ningún otro contexto.

Al investigar un diseño con requisitos difíciles o incógnitas importantes, usa hitos para implementar pruebas de concepto, implementaciones de juguete u otros ejercicios que permitan validar si la propuesta del usuario es viable. Lee el código fuente de las bibliotecas encontrándolas u obteniéndolas, investiga en profundidad e incluye prototipos que orienten una implementación completa.

Usa un ExecPlan cuando se cumpla al menos una condición:

- El cambio toca más de 2 módulos o capas (`frontend`, `backend`, `tests`, `scripts`).
- El cambio modifica un contrato público de herramientas (`tools`) o una estructura de errores.
- El cambio requiere migración, despliegue gradual (`rollout`) por fases o mitigación de riesgo.

Convención de nombres para archivos de plan:

- Guarda los ExecPlans en `plans/` y nombra los archivos con: `plan_<nnnn>_<objetivo>.md`.
- `<nnnn>` es un identificador incremental con ceros a la izquierda (`0001`, `0002`, ...).
- `<objetivo>` va en minúsculas y separado por guiones bajos.
- Ejemplo: `plans/plan_0001_catalogo_busqueda_mvp.md`.

## Requisitos

REQUISITOS NO NEGOCIABLES:

* Todo ExecPlan debe ser completamente autocontenido. Autocontenido significa que, en su forma actual, contiene todo el conocimiento y las instrucciones necesarias para que una persona principiante tenga éxito.
* Todo ExecPlan es un documento vivo. Las personas contribuidoras deben revisarlo a medida que avanza el progreso, aparecen descubrimientos y se finalizan decisiones de diseño. Cada revisión debe permanecer completamente autocontenida.
* Todo ExecPlan debe permitir que una persona principiante implemente la funcionalidad de punta a punta sin conocimiento previo de este repositorio.
* Todo ExecPlan debe producir un comportamiento demostrablemente funcional, no solo cambios de código para "cumplir una definición".
* Todo ExecPlan debe definir cada término especializado en lenguaje sencillo; si no puede definirlo, no debe usarlo.

El propósito y la intención van primero. Empieza explicando, en pocas frases, por qué el trabajo importa desde la perspectiva del usuario: qué podrá hacer alguien después del cambio que antes no podía hacer, y cómo puede ver que funciona. Luego guía a la persona lectora por los pasos exactos para lograr ese resultado, incluyendo qué editar, qué ejecutar y qué debería observar.

El agente que ejecuta tu plan puede listar archivos, leer archivos, buscar, ejecutar el proyecto y correr pruebas. No conoce contexto previo ni puede inferir lo que quisiste decir a partir de hitos anteriores. Repite cualquier supuesto del que dependas. No apuntes a blogs o documentación externos; si se requiere conocimiento, inclúyelo en el plan con tus propias palabras. Si un ExecPlan se apoya en un ExecPlan anterior y ese archivo está versionado, incorpóralo por referencia. Si no lo está, debes incluir todo el contexto relevante de ese plan.

## Formato

El formato y la envoltura son simples y estrictos. Cada ExecPlan debe ser un único bloque de código cercado, etiquetado como `md`, que empieza y termina con tres comillas invertidas. No anides bloques de código adicionales con tres comillas invertidas; cuando necesites mostrar comandos, transcripciones, diferencias (`diffs`) o código, preséntalos como bloques indentados dentro de ese único bloque. Usa indentación para claridad, en lugar de cercas de código dentro del ExecPlan, para evitar cerrar prematuramente el bloque principal. Usa dos saltos de línea después de cada encabezado, usa `#`, `##` y así sucesivamente, y emplea sintaxis correcta para listas ordenadas y no ordenadas.

Cuando escribas un ExecPlan en un archivo Markdown (`.md`) cuyo contenido sea únicamente ese ExecPlan, debes omitir las tres comillas invertidas.

Escribe en prosa clara. Prefiere oraciones antes que listas. Evita listas de verificación, tablas y enumeraciones largas salvo que la brevedad oscurezca el sentido. Las listas de verificación solo están permitidas en la sección `Progress`, donde son obligatorias. Las secciones narrativas deben permanecer orientadas a prosa.

## Guías

El autocontenido y el lenguaje claro son esenciales. Si introduces una frase que no es español ordinario ("daemon", "middleware", "RPC gateway", "filter graph"), defínela de inmediato y recuerda a la persona lectora cómo se manifiesta en este repositorio, por ejemplo nombrando los archivos o comandos donde aparece. No digas "como se definió previamente" ni "según el documento de arquitectura". Incluye aquí la explicación necesaria, incluso si debes repetirla.

Evita modos comunes de falla. No dependas de jerga sin definir. No describas "la letra de una funcionalidad" de forma tan estrecha que el código resultante compile pero no haga nada significativo. No traslades decisiones clave a la persona lectora. Cuando exista ambigüedad, resuélvela dentro del plan y explica por qué elegiste ese camino. Prefiere explicar en exceso los efectos visibles para el usuario y especificar menos los detalles incidentales de implementación.

Ancla el plan en resultados observables. Indica qué puede hacer el usuario después de la implementación, los comandos a ejecutar y las salidas que debería ver. La aceptación debe formularse como comportamiento verificable por una persona ("después de iniciar el servidor, navegar a [http://localhost:8080/health](http://localhost:8080/health) devuelve HTTP 200 con cuerpo OK") en lugar de atributos internos ("se agregó un struct HealthCheck"). Si un cambio es interno, explica cómo puede demostrarse su impacto, por ejemplo mediante pruebas que fallan antes y pasan después, o mostrando un escenario que use el nuevo comportamiento.

Especifica explícitamente el contexto del repositorio. Nombra archivos con rutas completas relativas al repositorio, nombra funciones y módulos con precisión, y describe dónde deben crearse archivos nuevos. Si se tocan varias áreas, incluye un párrafo corto de orientación que explique cómo encajan esas partes para que una persona principiante pueda navegar con confianza. Al ejecutar comandos, muestra el directorio de trabajo y la línea exacta de comando. Cuando los resultados dependan del entorno, declara los supuestos y ofrece alternativas cuando sea razonable.

Sé idempotente y seguro. Escribe los pasos para que puedan ejecutarse varias veces sin causar daño ni deriva. Si un paso puede fallar a mitad de camino, incluye cómo reintentar o adaptar. Si una migración u operación destructiva es necesaria, detalla respaldos o rutas seguras de recuperación. Prefiere cambios aditivos y verificables que puedan validarse a medida que avanzas.

La validación no es opcional. Incluye instrucciones para correr pruebas, iniciar el sistema si aplica y observar que haga algo útil. Describe pruebas completas para cualquier funcionalidad o capacidad nueva. Incluye salidas y mensajes de error esperados para que una persona principiante pueda distinguir éxito de falla. Cuando sea posible, muestra cómo probar que el cambio es efectivo más allá de la compilación, por ejemplo con un pequeño escenario de punta a punta, una invocación de interfaz de línea de comandos (`CLI`) o una transcripción de solicitud/respuesta HTTP. Indica los comandos exactos de prueba apropiados para la herramienta del proyecto y cómo interpretar sus resultados.

Captura evidencia. Cuando tus pasos produzcan salida de terminal, diferencias (`diffs`) cortas o registros (`logs`), inclúyelos dentro del bloque cercado único como ejemplos indentados. Mantenlos concisos y enfocados en lo que prueba el éxito. Si necesitas incluir un parche, prefiere diferencias (`diffs`) acotadas por archivo o extractos pequeños que la persona lectora pueda recrear siguiendo tus instrucciones, en lugar de pegar bloques grandes.

## Hitos

Los hitos son narrativos, no burocráticos. Si divides el trabajo en hitos, introduce cada uno con un párrafo breve que describa el alcance, qué existirá al final del hito que antes no existía, los comandos a ejecutar y la aceptación que esperas observar. Mantén la lectura como una historia: objetivo, trabajo, resultado, prueba. Progreso e hitos son distintos: los hitos cuentan la historia; `Progress` rastrea el trabajo granular. Ambos deben existir. Nunca abrevies un hito solo por brevedad ni omitas detalles que podrían ser cruciales para una implementación futura.

Cada hito debe ser verificable de forma independiente e implementar incrementalmente el objetivo general del plan de ejecución.

## Planes vivos y decisiones de diseño

* Los ExecPlans son documentos vivos. A medida que tomes decisiones clave de diseño, actualiza el plan para registrar tanto la decisión como el razonamiento detrás de ella. Registra todas las decisiones en la sección `Decision Log`.
* Los ExecPlans deben contener y mantener una sección `Progress`, una sección `Surprises & Discoveries`, una sección `Decision Log` y una sección `Outcomes & Retrospective`. Estas secciones no son opcionales.
* Cuando descubras comportamiento del optimizador, compromisos de rendimiento, errores (`bugs`) inesperados o semánticas inversas/de deshacer que hayan dado forma al enfoque, captura esas observaciones en la sección `Surprises & Discoveries` con evidencias breves; la salida de pruebas es ideal.
* Si cambias de rumbo a mitad de implementación, documenta por qué en `Decision Log` y refleja las implicaciones en `Progress`. Los planes son guías para la siguiente persona contribuidora tanto como listas de seguimiento para ti.
* Al completar una tarea mayor o el plan completo, escribe una entrada en `Outcomes & Retrospective` que resuma qué se logró, qué queda pendiente y las lecciones aprendidas.

## Hitos de prototipado e implementaciones paralelas

Es aceptable, y a menudo recomendable, incluir hitos explícitos de prototipado cuando reduzcan el riesgo de un cambio mayor. Ejemplos: agregar un operador de bajo nivel a una dependencia para validar viabilidad, o explorar dos órdenes de composición mientras se miden efectos del optimizador. Mantén los prototipos aditivos y verificables. Etiqueta claramente el alcance como "prototipado"; describe cómo ejecutar y observar resultados; e indica los criterios para promover o descartar el prototipo.

Prefiere cambios de código aditivos seguidos por eliminaciones que mantengan las pruebas pasando. Las implementaciones paralelas, por ejemplo mantener un adaptador junto a una ruta anterior durante una migración, son aceptables cuando reducen riesgo o permiten que las pruebas sigan pasando durante una migración grande. Describe cómo validar ambas rutas y cómo retirar una de forma segura con pruebas. Al trabajar con varias bibliotecas nuevas o áreas funcionales, considera crear exploraciones técnicas (`spikes`) que evalúen la viabilidad de estas capacidades _independientemente_ unas de otras, probando que la biblioteca externa se comporta como se espera e implementa de forma aislada las capacidades que necesitamos.

## Esqueleto de un buen ExecPlan

    # plan_xxxx - <Descripción corta y orientada a la acción>

    **Fecha**: xxxx-xx-xx
    **Ámbito**: `xxx`
    **Estado**:  xxx
    **Prioridad**: xxx

    Este ExecPlan es un documento vivo. Las secciones `Progress`, `Surprises & Discoveries`, `Decision Log` y `Outcomes & Retrospective` deben mantenerse actualizadas a medida que avanza el trabajo.

    Si el archivo PLANS.md está versionado en el repositorio, referencia aquí su ruta desde la raíz del repositorio e indica que este documento debe mantenerse de acuerdo con PLANS.md.

    ## Propósito / Panorama general

    Explica en pocas frases qué gana alguien después de este cambio y cómo puede ver que funciona. Indica el comportamiento visible para el usuario que habilitarás.

    ## Progress

    Usa una lista con casillas de verificación para resumir pasos granulares. Todo punto de pausa debe documentarse aquí, incluso si requiere dividir una tarea parcialmente completada en dos ("hecho" vs. "pendiente"). Esta sección siempre debe reflejar el estado actual real del trabajo.

    - [x] (2025-10-01 13:00Z) Ejemplo de paso completado.
    - [ ] Ejemplo de paso incompleto.
    - [ ] Ejemplo de paso parcialmente completado (completado: X; pendiente: Y).

    Usa marcas de tiempo (`timestamps`) para medir ritmos de progreso.

    ## Surprises & Discoveries

    Documenta comportamientos inesperados, errores (`bugs`), optimizaciones o aprendizajes descubiertos durante la implementación. Aporta evidencia concisa.

    - Observación: ...
      Evidencia: ...

    ## Decision Log

    Registra cada decisión tomada durante el trabajo en el plan con el formato:

    - Decisión: ...
      Justificación: ...
      Fecha/Autor: ...

    ## Outcomes & Retrospective

    Resume resultados, brechas y aprendizajes en hitos mayores o al completar el trabajo. Compara el resultado contra el propósito original.

    ## Contexto y orientación

    Describe el estado actual relevante para esta tarea como si la persona lectora no supiera nada. Nombra los archivos y módulos clave por ruta completa. Define cualquier término no obvio que usarás. No hagas referencia a planes anteriores.

    ## Plan de trabajo

    Describe, en prosa, la secuencia de ediciones y adiciones. Para cada edición, nombra el archivo y la ubicación (función, módulo) y qué insertar o cambiar. Mantén el plan concreto y mínimo.

    ## Pasos concretos

    Indica los comandos exactos a ejecutar y dónde ejecutarlos (directorio de trabajo). Cuando un comando genere salida, muestra una transcripción corta esperada para que la persona lectora pueda comparar. Esta sección debe actualizarse a medida que avanza el trabajo.

    ## Validación y aceptación

    Describe cómo iniciar o ejercitar el sistema y qué observar. Formula la aceptación como comportamiento, con entradas y salidas específicas. Si hay pruebas involucradas, di "ejecuta <comando de pruebas del proyecto> y espera <N> pruebas aprobadas; la nueva prueba <nombre> falla antes del cambio y pasa después".

    ## Idempotencia y recuperación

    Si los pasos pueden repetirse de forma segura, dilo. Si un paso es riesgoso, proporciona una ruta segura de reintento o reversión (`rollback`). Mantén el entorno limpio al completar el trabajo.

    ## Artefactos y notas

    Incluye las transcripciones, diferencias (`diffs`) o fragmentos más importantes como ejemplos indentados. Mantenlos concisos y enfocados en lo que prueba el éxito.

    ## Interfaces y dependencias

    Sé prescriptivo. Nombra las bibliotecas, módulos y servicios que deben usarse y por qué. Especifica los tipos, rasgos (`traits`)/interfaces y firmas de función que deben existir al final del hito. Prefiere nombres y rutas estables como `crate::module::function` o `package.submodule.Interface`. Por ejemplo:

    En crates/foo/planner.rs, define:

        pub trait Planner {
            fn plan(&self, observed: &Observed) -> Vec<Action>;
        }

Si sigues la guía anterior, un único agente sin estado, o una persona principiante, puede leer tu ExecPlan de principio a fin y producir un resultado funcional y observable. Ese es el estándar: AUTOCONTENIDO, AUTOSUFICIENTE, ORIENTADO A PRINCIPIANTES Y ENFOCADO EN RESULTADOS.

Cuando revises un plan, debes asegurarte de que tus cambios se reflejen de forma integral en todas las secciones, incluyendo las secciones de documento vivo, y debes escribir una nota al final del plan que describa el cambio y la razón. Los ExecPlans deben describir no solo el qué, sino también el porqué de casi todo.
