#!/usr/bin/python3

from flask import Flask

app = Flask("__name__")


@app.route('/', strict_slashes=False)
def display_hello_hbnb():
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def display_hbnb():
    return ("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def display_cText(text):
    return "C {}".format(text.replace("_", " "))


@app.route('/python', strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def display_pythonText(text="is cool"):
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def display_isNumber(n):
    if isinstance(n, int):
        return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
