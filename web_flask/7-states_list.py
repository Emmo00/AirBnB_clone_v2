#!/usr/bin/python3
"""index only flask app"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

@app.teardown_appcontext
def close_db():
    """ran after every request"""
    storage.close()

@app.route('/states_list', strict_slashes=False)
def state_list():
    """state list route"""
    states = storage.all(State)
    return render_template("7-states_list.html", states=states)


if __name__ == '__main__':
    app.run('0.0.0.0', 5000)
