"""Configure the course GeoServer using only its REST API."""

from __future__ import annotations

import argparse
from pathlib import Path

import requests


ROOT = Path(__file__).resolve().parents[1]


def request(session: requests.Session, method: str, url: str, path: str, body: str = "", content_type: str = "text/xml") -> None:
    response = session.request(
        method,
        f"{url.rstrip('/')}{path}",
        data=body.encode(),
        headers={"Content-Type": content_type},
        timeout=30,
    )
    if response.status_code in (200, 201, 202, 204, 409):
        return
    if response.status_code == 500 and "already exists" in response.text:
        return
    raise RuntimeError(f"{method} {path} devolvio {response.status_code}: {response.text[:400]}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-url", default="http://localhost:18080/geoserver/rest")
    parser.add_argument("--user-file", type=Path, default=ROOT / "infra/secrets/geoserver_user.example")
    parser.add_argument("--secret-file", type=Path, default=ROOT / "infra/secrets/geoserver_password.example")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not args.user_file.is_file() or not args.secret_file.is_file():
        raise FileNotFoundError("Falta un archivo de credenciales GeoServer; copie solo secretos ficticios para desarrollo local.")

    session = requests.Session()
    session.auth = (args.user_file.read_text(encoding="utf-8").strip(), args.secret_file.read_text(encoding="utf-8").strip())
    request(session, "POST", args.base_url, "/workspaces", "<workspace><name>curso</name></workspace>")
    request(
        session,
        "POST",
        args.base_url,
        "/workspaces/curso/datastores",
        """<dataStore><name>curso_postgis</name><connectionParameters>
        <entry key="host">postgis</entry><entry key="port">5432</entry><entry key="database">curso</entry>
        <entry key="user">curso_admin</entry><entry key="passwd">curso-postgis-password</entry>
        <entry key="dbtype">postgis</entry><entry key="schema">public</entry>
        </connectionParameters></dataStore>""",
    )
    request(session, "POST", args.base_url, "/workspaces/curso/datastores/curso_postgis/featuretypes", "<featureType><name>referencia</name><nativeName>referencia</nativeName><srs>EPSG:4326</srs></featureType>")
    sld = (ROOT / "infra/geoserver/referencia.sld").read_text(encoding="utf-8")
    style_response = session.get(f"{args.base_url.rstrip('/')}/styles/referencia.json", timeout=30)
    if style_response.status_code == 404:
        request(session, "POST", args.base_url, "/styles?name=referencia", sld, "application/vnd.ogc.sld+xml")
    elif style_response.status_code == 200:
        request(session, "PUT", args.base_url, "/styles/referencia", sld, "application/vnd.ogc.sld+xml")
    else:
        raise RuntimeError(f"No se pudo consultar el estilo referencia: {style_response.status_code}")
    request(session, "PUT", args.base_url, "/layers/curso:referencia", "<layer><defaultStyle><name>referencia</name></defaultStyle></layer>")
    request(session, "POST", args.base_url, "/workspaces/curso/layergroups", "<layerGroup><name>referencia</name><layers><layer>curso:referencia</layer></layers><styles><style>referencia</style></styles></layerGroup>")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
