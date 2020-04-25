#!/usr/bin/env sh

# if you want to creat
# set create_verifier="y"
# if you do not want to create it
# set create_verifier
set create_verifier="y"
set verifier_name=Rossi, Mario
set verifier_country=AU
set ca_key_name=verifier.key
set ca_cert_name=verifier.crt

set create_server="y"
set server_name=Useful Service
set server_country=US
set server_key_name=server.key
set server_cert_name=server.csr
set server_autosigned_cert_name=server.crt
set server_serial=01

set client_generic_name=tizio_caio
set client_name=Caio Tizio
set client_country=IT
set client_key_name=%client_generic_name%.key
set client_cert_name=%client_generic_name%.csr
set client_signed_cert_name=%client_generic_name%.crt
set client_serial=01

set bundled_client_certificate_name=%client_generic_name%.p12
set bundle_password=audacesfortunaiuvat

docker-compose build
docker-compose up
docker-compose down