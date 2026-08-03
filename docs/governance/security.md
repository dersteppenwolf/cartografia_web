# Seguridad Inicial

El arbol de trabajo debe superar un escaneo de secretos antes de publicar. La
auditoria del historial es informativa: no autoriza reescribir Git y requiere
evidencia externa de revocacion para cada hallazgo historico.

Los datos sociales geolocalizados estan en cuarentena y no pueden entrar en el
sitio publico, fixtures, notebooks ni ejemplos. Las interfaces administrativas
futuras se limitaran a `localhost` y los secretos futuros se leeran desde
archivos ignorados por Git.

Docker Desktop estuvo disponible el 2026-08-03. Gitleaks 8.24.2 pasó sobre el
árbol actual tras retirar cinco valores de token y limitar falsos positivos de
`Leaflet.VectorGrid` y checksums públicos de GeoServer mediante huellas exactas.
La auditoría histórica halló tres tokens históricos y dos falsos positivos; los
tokens quedan con evidencia de revocación pendiente y el historial no se
reescribe.

Trivy 0.59.1 completó el escaneo de vulnerabilidades, secretos y configuraciones
sin hallazgos de severidad alta o crítica. El informe advirtió que
`02_Conceptos/html/datos/limite_departamental.geojson` tiene 17 MB; se tratará
como dato histórico bloqueado hasta que el Hito 2 cree fixtures pequeños.

Los prototipos y digests de infraestructura siguen pendientes del Hito 5A.
