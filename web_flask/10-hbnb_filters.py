#!/usr/bin/python3
"""index only flask app"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.teardown_appcontext
def close_db(exception=None):
    """ran after every request"""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """hbnb filters route"""
    states = list(storage.all(State).values())
    states.sort(key=lambda x: x.name)

    def get_cities(state):
        cities = state.cities
        cities.sort(key=lambda x: x.name)
        return cities
    amenities = list(storage.all(Amenity).values())
    amenities.sort(key=lambda x: x.name)
    return render_template("10-hbnb_filters.html",
                           states=states, get_cities=get_cities,
                           amenities=amenities)


if __name__ == '__main__':
    app.run('0.0.0.0', 5000, debug=True)
