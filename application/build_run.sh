#!/usr/bin/env sh

export host_path_to_sharedstorage="/host/path/to/permanentstorage"

docker build -f "Dockerfile" -t myimage:latest .
docker run -it -p 5000:5000 --name mycontainer -v ${host_path_to_sharedstorage}:/app/permanentstorage/ myimage
docker container rm mycontainer