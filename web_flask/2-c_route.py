#!/usr/bin/python3

from flask import Flask, escape

app = Flask(__name__)

@app.route("/c/<text>", strict_slashes=False)
def show_message(text):
    text_with_spaces = escape(text).replace('_', ' ')
    return "C {}".format(text_with_spaces)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
