#!/usr/bin/env python3
"""Flask App"""

from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)

@app.route("/", strict_slashes=False)
def index():
    """Renders simple index file"""
    return render_template('0-index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
