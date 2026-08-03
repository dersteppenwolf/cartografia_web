"""Generate deterministic notebooks that use local fixtures by default."""

from __future__ import annotations

from pathlib import Path

import nbformat as nbf


ROOT = Path(__file__).resolve().parents[1]
NOTEBOOKS = ROOT / "notebooks"


def notebook(cells: list[nbf.NotebookNode]) -> nbf.NotebookNode:
    return nbf.v4.new_notebook(cells=cells, metadata={"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"}})


def write(name: str, cells: list[nbf.NotebookNode]) -> None:
    NOTEBOOKS.mkdir(exist_ok=True)
    nbf.write(notebook(cells), NOTEBOOKS / name)


def main() -> int:
    setup = nbf.v4.new_code_cell(
        "from pathlib import Path\nimport json\nimport os\n\nCWD = Path.cwd()\nROOT = CWD if (CWD / 'data').is_dir() else CWD.parent\nMODE = os.environ.get('COURSE_DATA_MODE', 'fixtures')\nassert MODE == 'fixtures', 'El modo local se habilita con Hito 5B.'"
    )
    write(
        "ogc_clasico.ipynb",
        [
            nbf.v4.new_markdown_cell("# WFS clásico con fixture local\n\nEste notebook no consulta Internet."),
            setup,
            nbf.v4.new_code_cell(
                "import xml.etree.ElementTree as ET\nxml = ROOT / 'data/fixtures/responses/ogc-clasico/wfs-capabilities.xml'\nroot = ET.parse(xml).getroot()\nns = {'wfs': 'http://www.opengis.net/wfs/2.0'}\nname = root.findtext('.//wfs:FeatureType/wfs:Name', namespaces=ns)\nassert name == 'curso:referencia'\nname"
            ),
        ],
    )
    write(
        "ogc_api_features.ipynb",
        [
            nbf.v4.new_markdown_cell("# OGC API - Features con fixtures locales\n\nCompara la colección con el nombre WFS."),
            setup,
            nbf.v4.new_code_cell(
                "base = ROOT / 'data/fixtures/responses/ogc-api-features'\nlanding = json.loads((base / 'landing.json').read_text())\nconformance = json.loads((base / 'conformance.json').read_text())\ncollections = json.loads((base / 'collections.json').read_text())\nitems = json.loads((base / 'items.json').read_text())\nassert collections['collections'][0]['id'] == 'referencia'\nassert items['features'][0]['id'] == 'zona-1'\nassert any('ogcapi-features' in value for value in conformance['conformsTo'])\ncollections['collections'][0]['title']"
            ),
        ],
    )
    write(
        "stac_estatico.ipynb",
        [
            nbf.v4.new_markdown_cell("# STAC estático\n\nCatalog, Collection e Item describen un activo ráster local."),
            setup,
            nbf.v4.new_code_cell(
                "base = ROOT / 'data/fixtures/stac'\ncatalog = json.loads((base / 'catalog.json').read_text())\ncollection = json.loads((base / 'collection.json').read_text())\nitem = json.loads((base / 'item-referencia.json').read_text())\nasset = (base / item['assets']['data']['href']).resolve()\nassert catalog['type'] == 'Catalog'\nassert collection['id'] == 'referencia'\nassert asset.is_file()\nitem['assets']['data']['title']"
            ),
        ],
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
