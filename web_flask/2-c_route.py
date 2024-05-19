#!/usr/bin/python3
""" Sript that starts a Flask web application """

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbn():
    """ Return Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Return HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def text_var(text):
    """Display text variable passed in"""
    return "C {}".format(text.replace("_", " "))

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)