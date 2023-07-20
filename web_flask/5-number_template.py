#!/usr/bin/python3
"""index only flask app"""
from flask import Flask, render_template

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


@app.route('/python', strict_slashes=False)
def python_is_cool():
    """python is cool route"""
    return 'Python is cool'


@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """python + text route"""
    return f'Python {text.replace("_", " ")}'


@app.route('/number/<int:n>', strict_slashes=False)
def number_n(n):
    """number n route"""
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_page_n(n):
    """number n with template route"""
    return render_template('5-number.html', number=n)


app.run('0.0.0.0', 5000)
