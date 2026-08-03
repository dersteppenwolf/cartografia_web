# plan_0006 - Hacer autonoma la Unidad 5 de servicios e infraestructura

**Fecha**: 2026-08-03 **Ambito**:
`docs/unidades/05_servicios_infraestructura.md`, `infra/`, scripts de
configuracion, smoke y restauracion **Estado**: propuesto **Prioridad**: alta;
base de Entrega 2 y de los modos locales posteriores

Este ExecPlan es un documento vivo. Debe mantenerse conforme a `PLANS.md`,
`AGENTS.md`, `UPGRADE_PLAN.md` y `DESIGN.md`.

## Proposito / Panorama general

Al terminar, una persona podra explicar como se relacionan PostGIS, GeoServer,
Nginx y el cliente; iniciar el stack desde volumenes vacios; identificar que
publica WMS, WFS, OGC API - Features y MVT; y comprobar que un backup restaura
la fila centinela sin pasos manuales. Podra observar el resultado con
`npm run validate:stack` y `scripts/test_restore.py`.

## Progress

- [x] (2026-08-03) Se identifico que la unidad actual privilegia comandos y no
      explica SQL espacial, roles, indices, stores, capas, estilos, salud, logs
      ni el modelo de recuperacion.
- [x] (2026-08-03) Se reescribió la unidad con arquitectura, PostGIS, GiST,
      GeoServer REST, SLD, Compose, healthchecks, logs, interfaces y
      recuperación.
- [x] (2026-08-03) Se agregaron prácticas SQL, lectura de configuración REST,
      smoke test, logs, backup, recuperación, errores y autoevaluación.
- [x] (2026-08-03) Pasaron stack vacío, notebooks locales, restauración de fila
      centinela, build y enlaces internos.

## Surprises & Discoveries

- Observacion: `05_Servidores_Mapas/Readme.md` contiene SQL y GeoServer, pero
  depende de servidores cloud de clase, Mapbox y direcciones HTTP historicas.
  Evidencia: `05_Servidores_Mapas/Readme.md` lineas 18 a 134 y
  `06_Simbologia/Readme.md`.

- Observacion: el stack mantenido puede reconstruir PostGIS, GeoServer y Nginx
  desde volumenes vacios y restaurar una fila centinela. Evidencia:
  `infra/compose.yaml`, `scripts/configure_geoserver.py`,
  `infra/smoke/smoke_stack.py` y `scripts/test_restore.py`.

- Observacion: la descarga dinámica de Vector Tiles en el arranque podía dejar
  un ZIP vacío y MVT dejaba de estar disponible después de una restauración
  desde volúmenes vacíos. Evidencia: respuesta WMS `InvalidFormat` y ZIP de 0
  bytes en `/opt/additional_libs` el 2026-08-03.

- Observacion: el plugin Vector Tiles 3.0.0 descargado desde un mirror explícito
  y verificado por SHA-256 mantuvo MVT disponible antes y después de la
  restauración. Evidencia: SHA-256
  `b763248cf13e66678cae456f64c8e93c4e5762aebe7a9ce01cab67f408fc7263` y smoke
  test correcto el 2026-08-03.

## Decision Log

- Decision: enseñar GeoServer como configuracion declarada por REST y SLD
  versionado, no como secuencia de clics en una interfaz. Justificacion: la
  reconstruccion debe ser demostrable desde un clon limpio y no depender de un
  data directory opaco. Fecha/Autor: 2026-08-03 / OpenCode.

- Decision: instalar Vector Tiles durante el build de GeoServer desde un mirror
  explícito, con SHA-256 verificado, y desactivar la descarga dinámica al
  arranque. Justificacion: elimina una dependencia no determinista de
  SourceForge y hace que MVT sobreviva una reconstrucción desde volúmenes
  vacíos. Fecha/Autor: 2026-08-03 / OpenCode.

## Outcomes & Retrospective

El resultado sera una unidad capaz de explicar por que existe cada servicio y
como operarlo localmente, no solo una receta para ejecutar Compose.

## Contexto y orientacion

PostGIS es PostgreSQL con tipos, funciones e indices espaciales. Una tabla
guarda filas; una geometria guarda la ubicacion; un indice GiST acelera filtros
espaciales. GeoServer conecta un datastore, publica una capa y aplica un estilo
SLD. Un healthcheck es una comprobacion corta de que un proceso esta listo.
Docker Compose describe contenedores, redes, volumenes, secretos y dependencias.
Un volumen conserva estado entre reinicios; destruirlo prueba que la
configuracion esta realmente versionada. Nginx sirve archivos estaticos y
soporta HTTP Range para PMTiles y COG.

## Plan de trabajo

Reescribir la unidad en cinco bloques: arquitectura de extremo a extremo; modelo
de datos PostGIS; publicacion GeoServer; operacion Compose; y recuperacion.
Explicar con el fixture `referencia` como una tabla se vuelve capa, WFS, OGC
API, WMS y MVT. Definir por que la misma coleccion puede tener diferentes
representaciones y contratos.

Agregar una actividad SQL que lea la tabla, interprete el indice GiST y compare
una consulta atributiva con una espacial. Agregar una actividad REST que lea
`scripts/configure_geoserver.py` y explique workspace, datastore, feature type,
layer, estilo y grupo. Presentar SLD como una regla de dibujo versionada.
Explicar secretos ficticios, puertos localhost, CORS, logs y healthchecks.

Finalizar con una practica de backup y recuperacion: insertar centinela, generar
dump con checksum, destruir volumenes, restaurar y consultar la fila. Incluir
errores frecuentes, por ejemplo confundir configuracion persistente con
reproducible, exponer un puerto administrativo o restaurar sin verificar
checksum.

## Pasos concretos

Desde la raiz ejecutar:

    docker compose -f infra/compose.yaml config --quiet
    docker compose -f infra/compose.yaml up -d --build --wait
    uv run python scripts/configure_geoserver.py
    npm run validate:stack
    uv run python scripts/run_notebooks.py --mode local
    uv run python scripts/test_restore.py --compose-file infra/compose.yaml --backup-dir .backups

La salida esperada de `validate:stack` confirma WMS, WFS, OGC API - Features,
MVT, Range y CORS. La restauracion debe informar que preservo la fila centinela.

## Validacion y aceptacion

La unidad se acepta cuando una persona puede dibujar el recorrido tabla PostGIS
a cliente, explicar GiST, datastore, capa, SLD, volumen, healthcheck, CORS y
backup; y ejecutar la recuperacion completa. Debe incluir una actividad de
lectura de logs y una matriz que relaciona interfaz, salida y caso de uso. Debe
vincularse con Entrega 2.

Todos los comandos indicados, `npm run lint:markdown` y `git diff --check` deben
pasar. La unidad no debe pedir una IP, interfaz remota ni credencial de una
cohorte anterior.

## Idempotencia y recuperacion

`configure_geoserver.py` se puede ejecutar varias veces. `test_restore.py` es
destructivo solo sobre los volumenes de practica y primero crea un backup
verificado. Si falla, conservar `.backups/`, revisar logs y repetir solo despues
de obtener un stack vacio conocido.

## Artefactos y notas

El documento debe enlazar `infra/compose.yaml`, `infra/smoke/smoke_stack.py`,
`scripts/configure_geoserver.py`, `scripts/backup_stack.py`,
`scripts/restore_stack.py` y `docs/guias/restauracion.md`. Los diagramas deben
ser texto o Mermaid accesible, no imagenes sin alternativa.

## Interfaces y dependencias

Mantener PostgreSQL/PostGIS, GeoServer, Nginx y sus digests fijados. No agregar
un servidor alternativo ni servicios cloud. Usar solo secretos ficticios
versionados como `.example`; los secretos reales permanecen ignorados por Git.

## Revision

2026-08-03: creado para transformar Unidad 5 en una explicacion autonoma de
infraestructura reproducible.
