import { Map, setWorkerUrl, type GeoJSONSource, type MapGeoJSONFeature } from "maplibre-gl";
import workerUrl from "maplibre-gl/dist/maplibre-gl-worker.mjs?worker&url";
import type { MapState } from "./state";

export function createMap(state: MapState): Map {
  setWorkerUrl(workerUrl);
  return new Map({
    container: "mapa",
    style: { version: 8, sources: {}, layers: [] },
    center: [state.longitude, state.latitude],
    zoom: state.zoom,
  });
}

export function updateFeatures(map: Map, features: GeoJSON.FeatureCollection): void {
  const source = map.getSource("referencia") as GeoJSONSource | undefined;
  if (source) {
    source.setData(features);
    return;
  }
  map.addSource("referencia", { type: "geojson", data: features });
  map.addLayer({ id: "referencia-circulos", type: "circle", source: "referencia", paint: { "circle-color": "#000000", "circle-radius": 6 } });
}

export function featureDescription(feature: MapGeoJSONFeature): string {
  return `${feature.properties?.nombre ?? "Entidad"}: ${feature.properties?.valor ?? "sin valor"}`;
}
