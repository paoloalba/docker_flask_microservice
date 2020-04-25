from flask import Flask, request
from logging.handlers import RotatingFileHandler
from logging.config import dictConfig

import logging
import sys

from pprint import pprint

logFilename = '/app/permanentstorage/application.log'

dictConfig({
    'version': 1,
    'disable_existing_loggers' : False,
    'formatters': {
        'default': {
            'format': '{0} {1} in {2}: {3}'.format('[%(asctime)s]', '%(levelname)s', '%(module)s', '%(message)s')
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',
            'formatter': 'default'
        },
        'file': {
            'class':'logging.FileHandler',
            'filename': logFilename,
            'formatter': 'default',
            'level': 'INFO'
        }
    },
    'root': {
        'level': 'INFO',
        'handlers': ['console','file']
    }
})

rootLogger = logging.getLogger()
allLoggers = ["gunicorn.access", "gunicorn.error"]

for loggo in allLoggers:
    logging.getLogger(loggo).handlers = rootLogger.handlers

app = Flask(__name__)

def extract_cert_info():
    coded_cert = request.environ["HTTP_X_SSL_CERT"]
    info_cert = request.environ["HTTP_X_SSL_CERT_INFO"]

    res = info_cert.split(",")

    for elem in res:
        arro = elem.split("=")
        if "email" in arro[0]:
            print("Email: {0}".format(arro[-1]))
        if "O" == arro[0]:
            print("Company: {0}".format(arro[-1]))
        if "L" == arro[0]:
            print("City: {0}".format(arro[-1]))
        if "ST" == arro[0]:
            print("Region: {0}".format(arro[-1]))
        if "C" == arro[0]:
            print("Country: {0}".format(arro[-1]))
        if "CN" == arro[0]:
            print("User: {0}".format(arro[-1]))


@app.before_request
def before_request():
    try:
        extract_cert_info()
    except Exception as excp:
        print("no identified user")

    # body = request.environ["wsgi.input"]
    # print("These are the attributes of body")
    # pprint(vars(body))
    # print("End of attributes for body.\n")

app.count = 0

@app.route("/")
def hello():

    arrayOfMessages = []

    app.count = app.count + 1

    msg = "<h1 style='color:blue'>Hello There! You visited this page {0} times. Lucky you!</h1>".format(app.count)
    arrayOfMessages.append(msg)

    return "\n".join(arrayOfMessages)


@app.route("/httpsredirect/")
def hello_public():
    logging.info("It was redirected from an http request to https.")

    return hello()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
