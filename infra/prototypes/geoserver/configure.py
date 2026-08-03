"""Configure the isolated GeoServer prototype through its REST API."""

from __future__ import annotations

from pathlib import Path

import requests


ROOT = Path(__file__).resolve().parents[3]
BASE = "http://localhost:18080/geoserver/rest"
USER = (ROOT / "infra/prototypes/geoserver/secrets/geoserver_user.txt").read_text().strip()
PASSWORD = (ROOT / "infra/prototypes/geoserver/secrets/geoserver_password.txt").read_text().strip()
AUTH = (USER, PASSWORD)


def request(method: str, path: str, body: str = "", content_type: str = "text/xml") -> None:
    response = requests.request(method, f"{BASE}{path}", auth=AUTH, data=body.encode(), headers={"Content-Type": content_type}, timeout=30)
    if response.status_code not in (200, 201, 202, 204, 409):
        if response.status_code == 500 and "already exists" in response.text:
            return
        raise RuntimeError(f"{method} {path} returned {response.status_code}: {response.text[:400]}")


def main() -> int:
    request("POST", "/workspaces", "<workspace><name>curso</name></workspace>")
    request("POST", "/workspaces/curso/datastores", """<dataStore><name>curso_postgis</name><connectionParameters>
      <entry key="host">postgis</entry><entry key="port">5432</entry><entry key="database">curso</entry>
      <entry key="user">curso_admin</entry><entry key="passwd">prototype-postgis-password</entry>
      <entry key="dbtype">postgis</entry><entry key="schema">public</entry>
    </connectionParameters></dataStore>""")
    request("POST", "/workspaces/curso/datastores/curso_postgis/featuretypes", "<featureType><name>referencia</name><nativeName>referencia</nativeName><srs>EPSG:4326</srs></featureType>")
    sld = (ROOT / "infra/prototypes/geoserver/reference.sld").read_text()
    request("POST", "/styles?name=referencia", sld, "application/vnd.ogc.sld+xml")
    request("PUT", "/layers/curso:referencia", "<layer><defaultStyle><name>referencia</name></defaultStyle></layer>")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
