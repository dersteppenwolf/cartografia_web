import "maplibre-gl/dist/maplibre-gl.css";
import { Map, addProtocol } from "maplibre-gl";
import { PMTiles, Protocol } from "pmtiles";
import { cogProtocol } from "@geomatico/maplibre-cog-protocol";

const status = document.querySelector("#estado");
const params = new URLSearchParams(location.search);
const asset = params.get("asset") || "pmtiles";
const map = new Map({ container: "mapa", style: { version: 8, sources: {}, layers: [] }, center: [-74.07, 4.72], zoom: 10 });

function ready(message) {
  status.dataset.protocolState = "ready";
  status.textContent = message;
}

function failed(error) {
  status.dataset.protocolState = "error";
  status.textContent = `No fue posible cargar el asset: ${error.message}`;
}

try {
  if (asset === "pmtiles") {
    const protocol = new Protocol();
    addProtocol("pmtiles", protocol.tile);
    const source = new PMTiles("http://localhost:18081/assets/referencia.pmtiles");
    protocol.add(source);
    map.on("load", () => {
      map.addSource("referencia", { type: "vector", url: "pmtiles://http://localhost:18081/assets/referencia.pmtiles" });
      map.addLayer({ id: "referencia", type: "circle", source: "referencia", "source-layer": "referencia", paint: { "circle-color": "#000000", "circle-radius": 6 } });
      ready("PMTiles cargado.");
    });
  } else {
    addProtocol("cog", cogProtocol);
    map.on("load", () => {
      map.addSource("referencia", { type: "raster", url: "cog://http://localhost:18081/assets/referencia.cog.tif", tileSize: 256 });
      map.addLayer({ id: "referencia", type: "raster", source: "referencia" });
      ready("COG cargado.");
    });
  }
  map.on("error", (event) => failed(event.error));
} catch (error) {
  failed(error);
}
