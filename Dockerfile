FROM python:3.6-alpine
LABEL MAINTAINER="{{ .Maintainer }}"  CATEGORY="Codefresh Plugins"
WORKDIR /home
ENV CF_PLUGIN_NAME="{{ .Name }}"
COPY . .
ENTRYPOINT /home/entrypoint.py
