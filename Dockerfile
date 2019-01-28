FROM alpine
LABEL MAINTAINER={{ .Maintainer }}  CATEGORY="Codefresh Plugins"
WORKDIR /home
ENV CF_PLUGIN_NAME="{{ .Name }}"
COPY . .
ENTRYPOINT /home/entrypoint.sh
