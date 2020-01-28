FROM tiangolo/uwsgi-nginx-flask:python3.5

RUN apt-get update && apt-get install -y python3-pip
RUN pip3 install requests

LABEL maintainer="Sebastian Ramirez <tiangolo@gmail.com>"

# If STATIC_INDEX is 1, serve / with /static/index.html directly (or the static URL configured)
#ENV STATIC_INDEX 1
#ENV STATIC_INDEX 0

# Add demo app
COPY ./app /app
WORKDIR /app









