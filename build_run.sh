#!/usr/bin/env sh

export host_path_to_sharedstorage="/host/path/to/permanentstorage"

docker-compose build
docker-compose up
docker-compose down