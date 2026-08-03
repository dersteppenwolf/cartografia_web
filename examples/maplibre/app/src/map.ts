import { addProtocol, Map, setWorkerUrl, type GeoJSONSource, type MapGeoJSONFeature } from "maplibre-gl";
import { PMTiles, Protocol } from "pmtiles";
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
  removeReferenceSource(map);
  const source = map.getSource("referencia") as GeoJSONSource | undefined;
  if (source) {
    source.setData(features);
    return;
  }
  map.addSource("referencia", { type: "geojson", data: features });
  map.addLayer({ id: "referencia-circulos", type: "circle", source: "referencia", paint: { "circle-color": "#000000", "circle-radius": 6 } });
}

let pmtilesProtocol: Protocol | undefined;

declare global {
  interface Window {
    MaplibreCOGProtocol?: { cogProtocol: Parameters<typeof addProtocol>[1] };
  }
}

export function updateCloudAsset(map: Map, kind: "pmtiles" | "cog", assetsUrl: string): void {
  removeReferenceSource(map);
  if (kind === "pmtiles") {
    pmtilesProtocol ??= new Protocol();
    addProtocol("pmtiles", pmtilesProtocol.tile);
    const asset = `${assetsUrl}/referencia.pmtiles`;
    pmtilesProtocol.add(new PMTiles(asset));
    map.addSource("referencia", { type: "vector", url: `pmtiles://${asset}` });
    map.addLayer({ id: "referencia-circulos", type: "circle", source: "referencia", "source-layer": "referencia", paint: { "circle-color": "#000000", "circle-radius": 6 } });
    return;
  }
  if (!window.MaplibreCOGProtocol) throw new Error("El protocolo COG no está disponible.");
  addProtocol("cog", window.MaplibreCOGProtocol.cogProtocol);
  map.addSource("referencia", { type: "raster", url: `cog://${assetsUrl}/referencia.cog.tif`, tileSize: 256 });
  map.addLayer({ id: "referencia-raster", type: "raster", source: "referencia" });
}

function removeReferenceSource(map: Map): void {
  for (const layer of ["referencia-circulos", "referencia-raster"]) {
    if (map.getLayer(layer)) map.removeLayer(layer);
  }
  if (map.getSource("referencia")) map.removeSource("referencia");
}

export function featureDescription(feature: MapGeoJSONFeature): string {
  return `${feature.properties?.nombre ?? "Entidad"}: ${feature.properties?.valor ?? "sin valor"}`;
}
