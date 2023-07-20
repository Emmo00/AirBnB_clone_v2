#!/usr/bin/python3
"""index only flask app"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """index route"""
    return 'Hello HBNB!'


app.run('0.0.0.0', 5000)
