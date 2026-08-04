# plan_0009 - Hacer autonoma la Unidad 8 de operacion y publicacion

**Fecha**: 2026-08-03
**Ambito**: `docs/unidades/08_operacion_publicacion.md`, guias operativas,
workflows, release gate y piloto
**Estado**: cerrado técnicamente; gate y piloto pendientes en `plan_0001`
**Prioridad**: alta; cierre curricular y operativo del curso

Este ExecPlan es un documento vivo. Debe mantenerse conforme a `PLANS.md`,
`AGENTS.md`, `UPGRADE_PLAN.md` y `DESIGN.md`.

## Proposito / Panorama general

Al terminar, una persona podra explicar como validar, publicar y recuperar un
artefacto estatico sin exponer servicios administrativos ni secretos. Podra
distinguir CI, artefacto, despliegue, secreto, vulnerabilidad, backup,
restauracion, RPO, RTO y evidencia de piloto; y podra ejecutar los controles
locales que reflejan los workflows de referencia.

## Progress

- [x] (2026-08-03) Se identifico que la unidad actual tiene dos parrafos y
      enlaces, insuficientes para CI, seguridad, Pages, costes, recuperacion,
      observabilidad, etica y gate de candidata.
- [x] (2026-08-03) Se reescribieron teoría y recorridos de seguridad, CI,
      artefacto, Pages, observabilidad, recuperación, costes, ética y piloto.
- [x] (2026-08-03) Se integraron guías operativas, práctica de workflow,
      incidente ficticio, restauración y autoevaluación.
- [x] (2026-08-03) Pasaron validación local, stack, escaneos, restauración y el
      gate devolvió `blocked` por evidencia externa pendiente, como corresponde.

## Surprises & Discoveries

- Observacion: los workflows de validacion, stack, Pages y enlaces externos ya
  existen, pero requieren explicacion de permisos, artefactos y limites para ser
  material docente. Evidencia: `.github/workflows/validate.yml`,
  `.github/workflows/pages.yml` y `.github/workflows/external-links.yml`.

- Observacion: el gate se bloquea deliberadamente sin WCAG manual, Safari real y
  piloto; ese bloqueo es evidencia correcta, no un error a ocultar. Evidencia:
  `scripts/release_gate.py`, `docs/governance/manual-accessibility-review.md` y
  `docs/pilot/`.

## Decision Log

- Decision: enseñar GitHub Actions y Pages como implementacion de referencia, no
  como cuenta o proveedor obligatorio. Justificacion: el curso debe poder
  validarse localmente y adoptar hosting institucional equivalente. Fecha/Autor:
  2026-08-03 / OpenCode.

## Outcomes & Retrospective

La Unidad 8 quedó convertida en una lección de seguridad, CI, Pages, artefacto,
observabilidad, recuperación, costes, ética y gate. Los controles técnicos pasan
Safari real y piloto. Esas dependencias siguen abiertas en `plan_0001`.

## Contexto y orientacion

CI es la ejecucion automatica de validaciones ante cambios. Un artefacto es la
salida versionada o empaquetada que se publica; en este curso es `_site/`
ensamblado. Un secreto es un valor que otorga acceso y no debe versionarse.
Gitleaks busca secretos; Trivy busca vulnerabilidades y configuraciones
inseguras. Un backup es una copia verificable de estado; restauracion
reconstruye ese estado. RPO es la perdida maxima de datos tolerada y RTO el
tiempo objetivo para recuperar servicio. Un gate es un control que declara
candidata solo cuando todas las evidencias exigidas existen.

## Plan de trabajo

Reescribir la unidad en bloques: modelo de amenaza y secretos; validacion local
y CI; artefacto estatico y Pages; observabilidad minima; backup y restauracion;
costes y limites; accesibilidad y etica; y piloto/gate. Explicar por que Pages
publica `_site/` y no la raiz historica, por que el backend sigue local, y por
que PMTiles/COG requieren comprobar Range y CORS despues de desplegar.

Convertir las guias `seguridad`, `publicacion`, `restauracion`, `accesibilidad`,
`costes_limites` y `revision_entregas` en lecturas integradas con tareas.
Agregar una actividad que lea un workflow, identifique permisos, reproduzca
localmente su comando y explique la diferencia entre fallo bloqueante e
informativo. Agregar una actividad de respuesta a incidente ficticio sin crear
secretos: detectar, retirar del arbol, revocar externamente, documentar y
repetir escaneos.

Explicar el piloto como evidencia real: tiempos, participantes, Safari real y
WCAG manual no se pueden generar desde CI. El texto debe mostrar el estado de
`release_gate.py --mode prepared` como `blocked` hasta que esas evidencias
existan.

## Pasos concretos

Desde la raiz ejecutar:

    npm run validate
    npm run validate:stack
    uv run python scripts/security_scan.py --scope worktree
    uv run python scripts/security_scan.py --scope dependencies
    uv run python scripts/test_restore.py --compose-file infra/compose.yaml --backup-dir .backups
    uv run python scripts/release_gate.py --mode prepared

El ultimo comando debe devolver `blocked` mientras falten Safari real, revision
WCAG manual o piloto. Ese resultado se documenta como limite operativo, no se
fuerza a verde.

## Validacion y aceptacion

La unidad se acepta cuando una persona puede explicar el contenido de cada
workflow, ejecutar sus equivalentes locales, identificar donde se publica el
artefacto, describir una restauracion, interpretar un escaneo y diferenciar una
validacion automatica de la evidencia del piloto. Debe incluir ejercicio,
autoevaluacion, errores frecuentes y conexion con Entrega 3.

Los comandos tecnicos deben pasar salvo el gate, cuyo estado bloqueado debe
explicarse. La publicacion de referencia debe comprobarse en la URL Pages con
HTTP 200 para las unidades y HTTP 206 para PMTiles/COG cuando el proveedor lo
soporte.

## Idempotencia y recuperacion

Los escaneos y validaciones no modifican fuentes. `test_restore.py` conserva
backup antes de destruir volumenes. Un deploy Pages no publica PostGIS ni
GeoServer. Si un proveedor no da Range, mantener los assets cloud-native en el
servidor local y registrar la limitacion.

## Artefactos y notas

El documento debe enlazar las guias operativas, los workflows,
`scripts/release_gate.py`, `CHANGELOG.md`, `docs/pilot/` y
`docs/governance/security-exceptions.yml`. Debe explicar que una excepcion
necesita alcance, justificacion, responsable y vencimiento.

## Interfaces y dependencias

Mantener acciones GitHub fijadas por SHA, permisos minimos, `pull_request` y no
`pull_request_target`. No agregar secretos al workflow. Mantener GitHub Pages
como referencia y permitir hosting institucional que cumpla HTTPS, Range y CORS.

## Revision

2026-08-03: creado para convertir Unidad 8 en una leccion autonoma de operacion,
publicacion y limites de evidencia.
