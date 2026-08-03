export interface AppConfig {
  ogcApiUrl: string;
  assetsUrl: string;
  collection: string;
  attribution: string;
}

export const config: AppConfig = {
  ogcApiUrl: "http://localhost:18080/geoserver/ogc/features/v1",
  assetsUrl: "http://localhost:18081/assets",
  collection: "curso:referencia",
  attribution: "Datos sintéticos del curso",
};
