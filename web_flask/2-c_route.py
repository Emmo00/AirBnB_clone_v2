#!/usr/bin/python3
"""index only flask app"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """index route"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """hbnb route"""
    return 'HBNB!'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """c + text route"""
    return f'C {text.replace("_", " ")}'


if __name__ == '__main__':
    app.run('0.0.0.0', 5000)
