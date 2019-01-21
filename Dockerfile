FROM alpine
LABEL MAINTAINER=Engineer CATEGORY="Codefresh Plugins"
WORKDIR /home
ENV CF_PLUGIN_NAME="Codefresh Sample Plugin"
COPY . .
ENTRYPOINT /home/entrypoint.sh