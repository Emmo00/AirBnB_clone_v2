#!/usr/bin/python3
"""index only flask app"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.user import User

app = Flask(__name__)


@app.teardown_appcontext
def close_db(exception=None):
    """ran after every request"""
    storage.close()


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """hbnb route"""
    states = list(storage.all(State).values())
    states.sort(key=lambda x: x.name)

    def get_cities(state):
        cities = state.cities
        cities.sort(key=lambda x: x.name)
        return cities
    amenities = list(storage.all(Amenity).values())
    amenities.sort(key=lambda x: x.name)
    places = list(storage.all(Place).values())
    places.sort(key=lambda x: x.name)

    def get_owner_name(user_id):
        users = list(storage.all(User).keys())
        user_index = users.index(f'User.{user_id}')
        owner = list(storage.all(User).values())[user_index]
        return f'{owner.first_name} {owner.last_name}'
    return render_template("100-hbnb.html",
                           states=states, get_cities=get_cities,
                           amenities=amenities,
                           places=places, get_owner_name=get_owner_name)


if __name__ == '__main__':
    app.run('0.0.0.0', 5000, debug=True)
