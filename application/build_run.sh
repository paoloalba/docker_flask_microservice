#!/usr/bin/env sh

docker build -f "Dockerfile" -t myimage:latest .
docker run -it -p 5000:5000 --name mycontainer -v /host/path/to/permanentstorage:/app/permanentstorage/ myimage
docker container rm mycontainer