#!/usr/bin/env sh

gunicorn --bind 0.0.0.0:5000 hello:app --config gunicorn_conf.py
