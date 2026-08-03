FROM docker.osgeo.org/geoserver@sha256:d8ff66a3e0f956415e048494a876e03f6475ddabcf1b1e6e9a8adba82ca50ee7

ARG OGCAPI_FEATURES_URL=https://sourceforge.net/projects/geoserver/files/GeoServer/3.0.0/extensions/geoserver-3.0.0-ogcapi-features-plugin.zip/download
ARG OGCAPI_FEATURES_SHA256=1d338a1b89ca7a02cde8aae47ede387a1b28ffa51388e104aa1b1f75c3e41296
ARG VECTOR_TILES_URL=https://netix.dl.sourceforge.net/project/geoserver/GeoServer/3.0.0/extensions/geoserver-3.0.0-vectortiles-plugin.zip
ARG VECTOR_TILES_SHA256=b763248cf13e66678cae456f64c8e93c4e5762aebe7a9ce01cab67f408fc7263

USER root

RUN mkdir -p /opt/additional_libs \
    && curl -fsSL "$OGCAPI_FEATURES_URL" -o /tmp/ogcapi-features.zip \
    && echo "$OGCAPI_FEATURES_SHA256  /tmp/ogcapi-features.zip" | sha256sum -c - \
    && unzip -qo /tmp/ogcapi-features.zip -d /opt/additional_libs \
    && rm /tmp/ogcapi-features.zip \
    && curl -fsSL "$VECTOR_TILES_URL" -o /tmp/vectortiles.zip \
    && echo "$VECTOR_TILES_SHA256  /tmp/vectortiles.zip" | sha256sum -c - \
    && unzip -qo /tmp/vectortiles.zip -d /opt/additional_libs \
    && rm /tmp/vectortiles.zip

# The prototype follows the same root-to-tomcat handoff as the promoted image.
USER root
