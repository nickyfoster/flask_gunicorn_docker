import logging
import sys

from flask import Flask, request

# Create a Flask application instance
app = Flask(__name__)

logging.basicConfig(format=f'%(asctime)s %(levelname)s [%(module)s:%(lineno)d] %(message).2000s')


@app.route("/")
def index():
    version = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    message = f"Flask Gunicorn Docker Python {version}"
    app.logger.info(request)

    return message, 200
