---
layout: default
title: Unidad 8. Operación y publicación
permalink: /unidades/08-operacion-publicacion/
---

# Unidad 8. Operación y publicación

**Tiempo:** cuatro horas presenciales y cinco horas autónomas. **Producto:** un
artefacto estático desplegable y un backend local documentado, con validación,
seguridad, recuperación y límites operativos explícitos. El curso no publica
PostGIS ni GeoServer en Internet y no requiere una cuenta SaaS para completar
sus entregas.

## Resultados de aprendizaje

Al finalizar podrás:

- Distinguir fuente, artefacto, despliegue, CI, secreto, dependencia y evidencia
  de piloto.
- Ejecutar localmente los controles equivalentes a los workflows de referencia.
- Explicar por qué GitHub Pages publica `_site/` y no la raíz histórica.
- Interpretar Gitleaks, Trivy, healthchecks, logs, backup, checksum, RPO y RTO.
- Preparar una candidata sin declarar aprobada una evidencia manual o de piloto
  que aún no existe.

## Operar no es solo publicar

Una aplicación cartográfica es operable cuando una persona puede saber qué se
ejecuta, qué datos usa, cómo detectar un fallo, cómo recuperar estado y qué
límites tiene. Publicar una URL no demuestra eso. En este curso el frontend es
un artefacto estático; PostGIS y GeoServer son referencias locales
reproducibles. La separación evita convertir una práctica de aprendizaje en un
servicio público con credenciales, costes o datos sin un responsable
institucional.

| Término     | Significado en el curso                                            | Evidencia                           |
| ----------- | ------------------------------------------------------------------ | ----------------------------------- |
| Fuente      | Markdown, TypeScript, scripts, fixtures y configuración versionada | Git y validaciones locales          |
| Artefacto   | Directorio `_site/` ensamblado                                     | Build Jekyll/Vite y Pages           |
| CI          | Comandos automáticos ante cambios                                  | Workflows GitHub Actions            |
| Secreto     | Valor que da acceso y no se versiona                               | Archivos ignorados y escaneo        |
| Healthcheck | Prueba corta de disponibilidad del contenedor                      | `docker compose ps`                 |
| Backup      | Dump PostGIS y manifiesto SHA-256                                  | `.backups/manifest.json`            |
| RPO         | Datos máximos aceptables de perder                                 | Objetivo institucional futuro: 24 h |
| RTO         | Tiempo objetivo para recuperar                                     | Objetivo institucional futuro: 4 h  |

El RPO y RTO no son promesas de este repositorio local. Son términos para que
una institución defina responsables y nivel de servicio antes de exponer un
sistema. Para el curso, el requisito demostrable es reconstrucción local
completa.

## Modelo de amenaza y secretos

Un **secreto** es un valor que permite acceder a un servicio, por ejemplo una
contraseña, token o clave privada. No es un dato de ejemplo ni una variable
configurable pública. Los ejemplos bajo `infra/secrets/*.example` tienen valores
ficticios y solo enseñan el mecanismo de archivo. Un secreto real se entrega por
un canal institucional, se ignora en Git, se rota tras una exposición y no se
copia en notebooks, logs, capturas, issues ni herramientas externas.

Gitleaks busca patrones de secretos en el árbol actual. Trivy revisa
vulnerabilidades, secretos y configuraciones inseguras en dependencias. Un
hallazgo no se resuelve agregando su valor a una lista de exclusión. Primero se
determina si es secreto real, falso positivo o material histórico; después se
retira, revoca o documenta una excepción específica con responsable y fecha de
vencimiento.

```powershell
uv run python scripts/security_scan.py --scope worktree
uv run python scripts/security_scan.py --scope dependencies
```

Las excepciones viven en `docs/governance/security-exceptions.yml`. Una
excepción declara alcance, severidad, responsable, aprobador, justificación y
vencimiento. No permite ocultar secretos ni vulnerabilidades críticas directas.
Consulta también la [guía de
seguridad]({{ '/guias/seguridad/' | relative_url }}).

## Validación local e integración continua

La validación local es el contrato principal; CI ejecuta los mismos comandos en
un runner limpio. Así un fallo puede reproducirse antes de abrir una pull
request.

```powershell
npm run validate
npm test
docker compose -f infra/compose.yaml up -d --build --wait
uv run python scripts/configure_geoserver.py
npm run validate:stack
```

`npm run validate` comprueba formato, Markdown, HTML, CSS, inventario,
licencias, tipos y build del cliente. `npm test` ejecuta pruebas Python.
`validate:stack` consulta servicios OGC, MVT, STAC, Range y CORS. Las pruebas
E2E del cliente se ejecutan con:

```powershell
npm run --workspace examples/maplibre/app test:e2e -- --project=chromium
```

El workflow `.github/workflows/validate.yml` separa un job editorial del job
`stack`, que inicia Compose, configura GeoServer y conserva logs si falla. Sus
permisos son de solo lectura. No usa `pull_request_target`, secretos de
producción ni código de una pull request en un runner privilegiado.

El workflow `external-links.yml` es programado e informativo: un proveedor
externo puede estar temporalmente caído sin bloquear un cambio local válido. La
revisión de enlaces internos sí es bloqueante porque el sitio los controla.

## Artefacto estático y GitHub Pages

El artefacto publicable es `_site/`, no el árbol raíz. `npm run build` construye
Jekyll, el cliente MapLibre y ensambla documentación, Leaflet, MapLibre, PMTiles
secretos.

```powershell
npm run build
npm run links:internal
python -m http.server 8000 --directory _site
```

`.github/workflows/pages.yml` publica `_site/` cuando `master` cambia o el
workflow se ejecuta manualmente. Las acciones se fijan por SHA y el workflow usa
el `base_path` configurado por Pages para que los enlaces funcionen bajo
`/cartografia_web/`. GitHub Pages es una implementación de referencia: un
hosting institucional puede sustituirla si entrega HTTPS y conserva las rutas
relativas necesarias.

Después de desplegar, valida las rutas publicadas, unidades, ejemplos y activos
cloud-native. PMTiles y COG solo se declaran disponibles si el hosting responde
Range y CORS de forma compatible. Un 200 que descarga el archivo completo no
demuestra una ruta cloud-native eficiente; se espera `206 Partial Content`,
`Accept-Ranges` y `Content-Range`.

## Observabilidad mínima

No se necesita una plataforma comercial de observabilidad para aprender los
fundamentos. El curso usa healthchecks, `docker compose ps`, logs, estados de
interfaz y smoke tests. Cada mecanismo responde una pregunta diferente:

| Mecanismo           | Pregunta que responde                                   |
| ------------------- | ------------------------------------------------------- |
| Healthcheck         | ¿El proceso declara que está listo?                     |
| `docker compose ps` | ¿Qué servicios están activos y saludables?              |
| Logs                | ¿Qué ocurrió dentro de un servicio?                     |
| Smoke test          | ¿Responden las rutas esenciales con contenido esperado? |
| Estado del cliente  | ¿La persona entiende carga, vacío o error?              |

```powershell
docker compose -f infra/compose.yaml ps
docker compose -f infra/compose.yaml logs geoserver --tail 100
npm run validate:stack
```

No copies logs completos con secretos o datos personales a una entrega. Extrae
el mensaje mínimo necesario, redacta valores sensibles y explica cómo se
reprodujo el resultado.

## Backup, restauración y recuperación

El backup contiene un dump PostGIS y un manifiesto SHA-256. GeoServer no se
respalda como data directory: `scripts/configure_geoserver.py` y el SLD
versionado reconstruyen workspace, datastore, capa y estilo. Caches y teselas
regenerables no son parte del backup.

```powershell
uv run python scripts/test_restore.py --compose-file infra/compose.yaml --backup-dir .backups
```

La prueba inserta una fila centinela, crea el backup, destruye volúmenes de
práctica, restaura datos, vuelve a configurar GeoServer, comprueba la fila y
ejecuta smoke tests. Después elimina la fila centinela para devolver el fixture
a su línea base. Si falla, conserva `.backups/`, revisa logs y no restaures
sobre un volumen de estado desconocido. La [guía de restauración]({{
'/guias/restauracion/' | relative_url }}) detalla el proceso.

## Costes, ética y revisión de entregas

El núcleo no exige cuentas SaaS. Aun así, Docker, dependencias, transferencias,
CI y hosting consumen recursos. Antes de una cohorte o despliegue institucional,
revisa almacenamiento, transferencia, minutos de CI, políticas de retención y
límites de proveedor. Los activos cloud-native pueden aumentar transferencia si
el hosting no soporta Range o la caché está mal configurada.

La operación también es ética: no se publican datos sociales en cuarentena,
coordenadas individuales sin base de uso, secretos, tokens activos ni endpoints
HTTP inseguros externos. La revisión de una entrega considera cartografía,
procedencia, licencia, accesibilidad, privacidad, seguridad, rendimiento,
reproducibilidad y comunicación. Consulta [costes y límites]({{
'/guias/costes-limites/' | relative_url }}) y la [revisión de entregas]({{
'/guias/revision-entregas/' | relative_url }}).

## Piloto y gate de candidata

Las pruebas automáticas no pueden demostrar una experiencia humana completa. La
revisión WCAG manual, Safari real en macOS, participantes, horas, soporte e
incidencias se registran en:

- [Evidencia manual de accesibilidad]({{
  '/gobierno/evidencia-accesibilidad/' | relative_url }})
- [Plan del piloto]({{ '/pilot/plan/' | relative_url }})
- [Resultados del piloto]({{ '/pilot/resultados/' | relative_url }})
- [Incidencias del piloto]({{ '/pilot/incidencias/' | relative_url }})

El gate genera un reporte factual. No inventa evidencia para quedar verde:

```powershell
uv run python scripts/release_gate.py --mode prepared
```

Mientras falte revisión manual, Safari real o piloto, la salida esperada es
`blocked`. Ese resultado es correcto y debe orientar el siguiente trabajo. Solo
después de completar evidencia real, autorización para commit y ejecución desde
un clon limpio se puede usar el modo `ready`. Tags, releases y pushes requieren
autorización adicional.

## Práctica guiada

1. Lee `.github/workflows/validate.yml` y localiza qué comando local equivale a
   cada job.
2. Ejecuta `npm run validate`, `npm test` y `npm run validate:stack`. Clasifica
   cada fallo posible como editorial, datos, cliente, infraestructura o hosting.
3. Simula un incidente sin crear secretos: describe qué harías si Gitleaks
   detecta una credencial. Incluye retirar el valor, revocar externamente,
   documentar estado y repetir escaneo.
4. Construye `_site/` y explica qué se publica y qué queda local.
5. Ejecuta `scripts/test_restore.py` y anota qué evidencia ofrece el checksum y
   la fila centinela.
6. Ejecuta el gate y lista qué evidencia humana sigue faltando sin cambiar los
   documentos de piloto a resultados ficticios.

## Errores frecuentes

- Publicar la raíz histórica en lugar de `_site/`.
- Convertir secretos ficticios de ejemplo en contraseñas reutilizadas.
- Ignorar un escaneo, una excepción vencida o un log de error porque el sitio
  abre.
- Confundir un healthcheck saludable con una recuperación completa.
- Guardar un data directory manual y llamarlo infraestructura reproducible.
- Declarar Pages compatible con PMTiles/COG sin comprobar Range y CORS remotos.
- Forzar el gate a verde sin WCAG manual, Safari real o piloto.

## Autoevaluación

1. ¿Qué diferencia hay entre fuente, artefacto y despliegue?
2. ¿Qué comando local reproduce el job de infraestructura de CI?
3. ¿Qué no se publica cuando Pages despliega `_site/`?
4. ¿Qué verifica un SHA-256 durante una restauración?
5. ¿Qué información no puede producir CI sobre accesibilidad y piloto?
6. ¿Qué estado debe devolver el gate mientras falte esa evidencia?

Esta unidad integra la [Entrega
3]({{ '/evaluacion/entrega-3/' | relative_url }})
