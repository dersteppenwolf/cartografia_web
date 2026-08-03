CREATE EXTENSION IF NOT EXISTS postgis;

CREATE TABLE IF NOT EXISTS referencia (
  id text PRIMARY KEY,
  nombre text NOT NULL,
  valor integer NOT NULL,
  geom geometry(Point, 4326) NOT NULL
);

INSERT INTO referencia (id, nombre, valor, geom) VALUES
  ('zona-1', 'Zona 1', 12, ST_SetSRID(ST_MakePoint(-74.10, 4.70), 4326)),
  ('zona-2', 'Zona 2', 18, ST_SetSRID(ST_MakePoint(-74.08, 4.71), 4326)),
  ('zona-3', 'Zona 3', 25, ST_SetSRID(ST_MakePoint(-74.06, 4.72), 4326)),
  ('zona-4', 'Zona 4', 31, ST_SetSRID(ST_MakePoint(-74.04, 4.73), 4326))
ON CONFLICT (id) DO UPDATE SET
  nombre = EXCLUDED.nombre,
  valor = EXCLUDED.valor,
  geom = EXCLUDED.geom;

CREATE INDEX IF NOT EXISTS referencia_geom_gist ON referencia USING gist (geom);
