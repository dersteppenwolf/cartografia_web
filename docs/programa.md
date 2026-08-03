---
layout: default
title: Programa
permalink: /programa/
---

# Publicacion de cartografia via web

## Programa

Area de formacion: Desarrollo de nuevas tecnologias.

Instructor: Juan Carlos Mendez.

## Proposito

El curso desarrolla la capacidad de publicar cartografia y datos geograficos de
forma comprensible, accesible, interoperable y reproducible. La meta no es usar
una plataforma especifica, sino documentar un problema territorial, preparar
datos, publicar servicios o archivos adecuados y demostrar el resultado desde un
clon limpio.

## Duracion y carga

El curso tiene 32 horas presenciales y 40 horas de trabajo autonomo. Las ocho
unidades tienen cuatro horas presenciales cada una. El trabajo autonomo se
distribuye en 4, 5, 4, 5, 6, 6, 5 y 5 horas, respectivamente.

Las herramientas de software libre con licencia compatible pueden instalarse en
computadores personales sin licencia adicional. Ninguna entrega obligatoria
requiere una cuenta SaaS, un token, una IP de cohortes anteriores ni un servicio
de pago.

## Competencia global

Diseñar, implementar, documentar y evaluar una publicación cartográfica web que
respete calidad de datos, interoperabilidad, accesibilidad WCAG 2.2 AA,
seguridad básica y reproducibilidad.

## Competencias específicas

- Explicar la relación entre datos geográficos, cartografía, clientes web,
  servicios y formatos de entrega.
- Preparar y documentar datos con sistema de referencia, esquema, licencia,
  procedencia y sensibilidad conocidos.
- Diseñar mapas temáticos con clasificación, simbología, incertidumbre,
  atribución y alternativas accesibles.
- Consumir y comparar WMS/WFS con OGC API - Features.
- Levantar y comprobar un stack local con PostGIS, GeoServer y servidor
  estático.
- Construir un cliente TypeScript con MapLibre, estados de carga/error y URL
  compartible.
- Elegir y justificar PMTiles para vector o COG para raster, con STAC estático
  cuando existan activos espaciotemporales.
- Publicar un artefacto estático y documentar validación, riesgos, restauración
  y límites de la solución.

## Unidades

### Unidad 1. Web, Git y publicación

Cuatro horas presenciales y cuatro autónomas. HTML semántico, CSS responsive,
JavaScript moderno, módulos ES, `fetch`, manejo de errores, Git y hosting
estático neutral. Producto: mapa Leaflet básico construido localmente.

### Unidad 2. Datos y calidad

Cuatro horas presenciales y cinco autónomas. QGIS, GeoPackage, GeoJSON, TopoJSON
como comparación, CRS, orden de coordenadas, precisión, geometrías, manifiestos,
licencias y privacidad. Producto: pipeline reproducible de datos.

### Unidad 3. Cartografía accesible y experiencia de uso

Cuatro horas presenciales y cuatro autónomas. Clasificación, normalización,
incertidumbre, paletas no dependientes solo del color, leyendas, escalas,
reflow, teclado, foco y alternativas tabulares. Producto: mapa temático conforme
al alcance WCAG 2.2 AA.

### Unidad 4. APIs e interoperabilidad

Cuatro horas presenciales y cinco autónomas. HTTP, WMS, WFS, OGC API Common, OGC
API - Features, OpenAPI, filtros, STAC estático y comparación entre WFS y
Features. WCS, CSW, WPS, Records, Processes y EDR son panorámicos o electivos.
Producto: consulta reproducible de la misma colección mediante ambas interfaces.

### Unidad 5. Servicios e infraestructura

Cuatro horas presenciales y seis autónomas. PostGIS, SQL espacial, índices GiST,
GeoServer, SLD, Docker Compose, secretos por archivo, healthchecks y
restauración. Producto: stack local reconstruible.

### Unidad 6. Cliente web moderno

Cuatro horas presenciales y seis autónomas. TypeScript, Vite, MapLibre, fuentes,
capas, filtros, estado compartible, consulta, mensajes y pruebas. Producto:
aplicación mantenible con datos y alternativa accesible.

### Unidad 7. Rendimiento y datos cloud-native

Cuatro horas presenciales y cinco autónomas. MVT, PMTiles, COG, HTTP Range,
STAC, caché y benchmark. Todo el grupo consume PMTiles y COG; cada proyecto
genera una única ruta: PMTiles para vector o COG para raster. Producto: entrega
optimizada y comparación reproducible.

### Unidad 8. Operación y publicación

Cuatro horas presenciales y cinco autónomas. CI, secretos, cabeceras,
observabilidad básica, build estático, costes, restauración, ética y narrativa.
Producto: artefacto desplegable y backend local documentado.

## Evaluación

La ponderación propuesta es 20% ejercicios y diagnósticos, 10% quizzes
conceptuales, 20% Entrega 1, 20% Entrega 2 y 30% Entrega 3.

### Entrega 1. Mapa publicable y accesible

Usa uno o dos datasets documentados, procesamiento reproducible, atribución y
licencia. Entrega un mapa responsive con teclado, leyenda, alternativa tabular o
descarga y justificación cartográfica.

### Entrega 2. Servicio interoperable reproducible

Usa PostGIS y GeoServer mediante Docker Compose. Publica la misma colección por
WFS y OGC API - Features, aplica un estilo SLD, documenta SQL, roles,
healthchecks y reconstrucción desde un clon limpio.

### Entrega 3. Aplicación geoespacial desplegable

Construye un cliente TypeScript con filtros, narrativa, manejo de errores y
datos reproducibles. Elige PMTiles/MVT para vector o COG para raster, incluye
STAC estático cuando corresponda y entrega un sitio estático, pruebas,
documentación de arquitectura y evaluación de privacidad, ética y accesibilidad.

## Política de uso responsable de IA

El uso de IA generativa debe declararse en cada entrega, incluyendo herramienta,
propósito, fragmentos revisados y fuentes verificadas. No se pueden introducir
datos sensibles, tokens ni credenciales en herramientas externas. La persona
estudiante conserva responsabilidad sobre la exactitud técnica, la atribución y
la decisión cartográfica.

## Revisión por cohorte

Antes de cada cohorte se revisan versiones, enlaces, datasets, licencias,
sensibilidad, costes, resultados del piloto y prerrequisitos. Los contenidos
electivos no se convierten en obligatorios sin ajustar horas, rúbricas y
criterios del piloto.
