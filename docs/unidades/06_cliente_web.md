---
layout: default
title: Unidad 6. Cliente web con MapLibre
permalink: /unidades/06-cliente-web/
---

# Unidad 6. Cliente web con MapLibre

El cliente mantenido usa TypeScript, Vite y MapLibre sin framework. Consulta la
colección local mediante OGC API - Features y muestra el mismo resultado en un
mapa y una tabla. El mapa no es la única forma de obtener el resultado.

El estado compartible describe longitud, latitud, zoom y valor mínimo en la URL.
La función `readStateFromUrl()` aplica valores seguros cuando un parámetro falta
o es inválido; `writeStateToUrl()` actualiza la URL tras mover el mapa o
filtrar.

## Ejecución

Inicia primero el stack de la Unidad 5. Luego, desde la raíz del repositorio:

```powershell
npm run --workspace examples/maplibre/app dev
```

Abre la dirección que anuncia Vite. Aplica un valor mínimo, copia la URL y
comprueba que al abrirla de nuevo se recuperan la vista y el filtro.

## Accesibilidad y errores

El control de filtro está fuera del canvas. Una consulta por clic abre un
detalle con foco gestionado; con el mapa enfocado, <kbd>Enter</kbd> o
<kbd>Espacio</kbd> consulta la entidad situada en el centro de la vista. Cerrar
el detalle devuelve el foco al mapa. Si la red falla, la región de estado
anuncia un mensaje textual en lugar de dejar un canvas vacío.

## Diagnóstico

Desconecta temporalmente GeoServer o modifica la URL de OGC API. Identifica el
mensaje de error, restaura el servicio y comprueba que tabla, mapa y estado
vuelven a mostrar las entidades. Explica por qué un error HTTP no debe tratarse
como una colección vacía.
