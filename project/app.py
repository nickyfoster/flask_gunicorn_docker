import logging
import sys

from flask import Flask, request

app = Flask(__name__)
logging.basicConfig(filename='logs/app.log',
                    level=logging.DEBUG,
                    format=f'%(asctime)s %(levelname)s [%(module)s:%(lineno)d] %(message).2000s')


@app.route("/")
def index():
    version = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    message = f"Flask Gunicorn Docker Python {version}"
    app.logger.info(request)
    print(request)
    return message
