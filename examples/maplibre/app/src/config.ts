export interface AppConfig {
  ogcApiUrl: string;
  collection: string;
  attribution: string;
}

export const config: AppConfig = {
  ogcApiUrl: "http://localhost:18080/geoserver/ogc/features/v1",
  collection: "curso:referencia",
  attribution: "Datos sintéticos del curso",
};
