
from flask import Flask, request

app = Flask(__name__)

wsgi_app = app.wsgi_app

import localwebsite.views