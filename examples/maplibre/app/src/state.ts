export interface MapState {
  longitude: number;
  latitude: number;
  zoom: number;
  minimumValue: number | null;
}

const defaults: MapState = { longitude: -74.07, latitude: 4.72, zoom: 11, minimumValue: null };

function numberValue(value: string | null, fallback: number): number {
  if (value === null || value === "") return fallback;
  const parsed = Number(value);
  return Number.isFinite(parsed) ? parsed : fallback;
}

export function readStateFromUrl(search = window.location.search): MapState {
  const params = new URLSearchParams(search);
  const minimum = params.get("min");
  return {
    longitude: numberValue(params.get("lng"), defaults.longitude),
    latitude: numberValue(params.get("lat"), defaults.latitude),
    zoom: numberValue(params.get("zoom"), defaults.zoom),
    minimumValue: minimum === null || minimum === "" ? null : numberValue(minimum, 0),
  };
}

export function writeStateToUrl(state: MapState): void {
  const params = new URLSearchParams();
  params.set("lng", state.longitude.toFixed(5));
  params.set("lat", state.latitude.toFixed(5));
  params.set("zoom", state.zoom.toFixed(2));
  if (state.minimumValue !== null) params.set("min", String(state.minimumValue));
  window.history.replaceState(null, "", `${window.location.pathname}?${params}`);
}
