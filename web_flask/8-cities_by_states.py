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


@app.route('/cities_by_states', strict_slashes=False)
def cities_state_list():
    """city by state list route"""
    states = []
    for state in storage.all(State).values():
        states.append(state)
    states.sort(key=lambda x: x.name)

    def get_cities(state):
        cities = state.cities
        cities.sort(key=lambda x: x.name)
        return cities
    return render_template("8-cities_by_states.html",
                           states=states, get_cities=get_cities)


if __name__ == '__main__':
    app.run('0.0.0.0', 5000)
