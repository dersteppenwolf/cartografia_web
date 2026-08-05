import { setStatus } from './status.js';

async function initializeMap() {
  const status = document.querySelector('#estado');
  const filter = document.querySelector('#filtro-valor');
  const tableBody = document.querySelector('#tabla-datos tbody');
  const map = L.map('mapa', { keyboard: true, zoomControl: true }).setView(
    [4.715, -74.07],
    12,
  );
  L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution:
      '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
  }).addTo(map);
  let layer;
  let features = [];

  function render() {
    const minimum = Number(filter.value);
    const visible = features.filter(
      (feature) => feature.properties.valor >= minimum,
    );
    if (layer) map.removeLayer(layer);
    layer = L.geoJSON(visible, {
      pointToLayer(feature, coordinates) {
        return L.circleMarker(coordinates, {
          color: '#000000',
          fillColor: '#ffffff',
          fillOpacity: 1,
          radius: 8,
          weight: 2,
        });
      },
      onEachFeature(feature, marker) {
        marker.bindPopup(
          `<strong>${feature.properties.nombre}</strong><br>Valor: ${feature.properties.valor}`,
        );
      },
    }).addTo(map);
    tableBody.replaceChildren(
      ...visible.map((feature) => {
        const row = document.createElement('tr');
        row.innerHTML = `<td>${feature.properties.nombre}</td><td>${feature.properties.valor}</td>`;
        return row;
      }),
    );
    setStatus(status, `${visible.length} zonas visibles.`);
  }

  try {
    const response = await fetch('data/referencia.geojson');
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    const collection = await response.json();
    features = collection.features;
    render();
    filter.addEventListener('change', render);
  } catch (error) {
    setStatus(
      status,
      `No fue posible cargar los datos de referencia: ${error.message}. Consulte la tabla cuando el servicio esté disponible.`,
    );
  }
}

initializeMap();
