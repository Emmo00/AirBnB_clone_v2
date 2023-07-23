#!/usr/bin/python3
"""index only flask app"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def close_db(exception=None):
    """ran after every request"""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """hbnb filters route"""
    return render_template("10-hbnb_filters.html")


if __name__ == '__main__':
    app.run('0.0.0.0', 5000)
