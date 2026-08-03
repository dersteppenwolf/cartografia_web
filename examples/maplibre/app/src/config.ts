export interface AppConfig {
  ogcApiUrl: string;
  featuresUrl: string;
  assetsUrl: string;
  collection: string;
  attribution: string;
  initialSource: "api" | "pmtiles";
}

const isLocal = ["localhost", "127.0.0.1"].includes(window.location.hostname);

export const config: AppConfig = {
  ogcApiUrl: "http://localhost:18080/geoserver/ogc/features/v1",
  featuresUrl: isLocal
    ? "http://localhost:18080/geoserver/ogc/features/v1/collections/curso:referencia/items"
    : new URL("../../examples/leaflet/mapa_basico/data/referencia.geojson", window.location.href).href,
  assetsUrl: isLocal
    ? "http://localhost:18081/assets"
    : new URL("../../assets/data", window.location.href).href,
  collection: "curso:referencia",
  attribution: "Datos sintéticos del curso",
  initialSource: isLocal ? "api" : "pmtiles",
};
