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


@app.route('/states', strict_slashes=False)
def states():
    """state list route"""
    states = []
    for state in storage.all(State).values():
        states.append(state)
    states.sort(key=lambda x: x.name)
    return render_template("7-states_list.html", states=states)


@app.route('/states/<id>', strict_slashes=False)
def state(id):
    """single state and sities"""
    states = storage.all(State)
    try:
        index = list(states.keys()).index(f'State.{id}')
    except ValueError:
        index = -1
    if index == -1:
        state = None
        cities = []
    else:
        state = list(states.values())[index]
        cities = state.cities
        cities.sort(key=lambda x: x.name)
    return render_template("9-states.html", state=state, cities=cities)


if __name__ == '__main__':
    app.run('0.0.0.0', 5000)
