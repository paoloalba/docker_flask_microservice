FROM python:3.7-slim

ADD /application /app

WORKDIR /app/

RUN mkdir -p sharedstorage

RUN chmod +x ./progr_create_cert.sh

ENTRYPOINT ["./progr_create_cert.sh"]
