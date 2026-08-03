FROM docker.osgeo.org/geoserver@sha256:d8ff66a3e0f956415e048494a876e03f6475ddabcf1b1e6e9a8adba82ca50ee7

ARG OGCAPI_FEATURES_URL=https://sourceforge.net/projects/geoserver/files/GeoServer/3.0.0/extensions/geoserver-3.0.0-ogcapi-features-plugin.zip/download
ARG OGCAPI_FEATURES_SHA256=1d338a1b89ca7a02cde8aae47ede387a1b28ffa51388e104aa1b1f75c3e41296

USER root

RUN mkdir -p /opt/additional_libs \
    && curl -fsSL "$OGCAPI_FEATURES_URL" -o /tmp/ogcapi-features.zip \
    && echo "$OGCAPI_FEATURES_SHA256  /tmp/ogcapi-features.zip" | sha256sum -c - \
    && unzip -q /tmp/ogcapi-features.zip -d /opt/additional_libs \
    && rm /tmp/ogcapi-features.zip

# GeoServer's startup script must run privileged to install extensions, then
# RUN_UNPRIVILEGED=true drops the serving process to its dedicated tomcat user.
USER root
