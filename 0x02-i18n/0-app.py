#!/usr/bin/env python3
"""
simple flask app
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def home():
    """index route"""
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)
