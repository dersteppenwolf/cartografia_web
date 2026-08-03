import "maplibre-gl/dist/maplibre-gl.css";
import "./styles.css";
import { config } from "./config";
import { createMap, featureDescription, updateFeatures } from "./map";
import { readStateFromUrl, writeStateToUrl } from "./state";
import { setStatus } from "./status";

const state = readStateFromUrl();
const map = createMap(state);
const input = document.querySelector<HTMLInputElement>("#valor-minimo")!;
const table = document.querySelector<HTMLTableSectionElement>("#tabla-datos")!;
input.value = state.minimumValue?.toString() ?? "";

async function load(): Promise<void> {
  try {
    const response = await fetch(`${config.ogcApiUrl}/collections/${config.collection}/items`);
    if (!response.ok) throw new Error(`El servicio respondió HTTP ${response.status}.`);
    const data = (await response.json()) as GeoJSON.FeatureCollection;
    const features = data.features.filter((feature) => state.minimumValue === null || Number(feature.properties?.valor) >= state.minimumValue);
    const filtered = { ...data, features };
    if (map.loaded()) updateFeatures(map, filtered); else map.once("load", () => updateFeatures(map, filtered));
    table.replaceChildren(...features.map((feature) => {
      const [longitude, latitude] = feature.geometry?.type === "Point" ? feature.geometry.coordinates : ["", ""];
      const row = document.createElement("tr");
      row.innerHTML = `<td>${String(feature.properties?.nombre ?? "")}</td><td>${String(feature.properties?.valor ?? "")}</td><td>${longitude}</td><td>${latitude}</td>`;
      return row;
    }));
    setStatus(`${features.length} entidades cargadas.`);
  } catch (error) {
    setStatus(`No fue posible cargar los datos: ${(error as Error).message}`, true);
  }
}

document.querySelector("#aplicar-filtro")?.addEventListener("click", () => {
  state.minimumValue = input.value === "" ? null : Number(input.value);
  writeStateToUrl(state);
  void load();
});
map.on("moveend", () => {
  const center = map.getCenter();
  state.longitude = center.lng;
  state.latitude = center.lat;
  state.zoom = map.getZoom();
  writeStateToUrl(state);
});
map.on("click", (event) => {
  const feature = map.queryRenderedFeatures(event.point, { layers: ["referencia-circulos"] })[0];
  if (feature) setStatus(featureDescription(feature));
});
void load();
