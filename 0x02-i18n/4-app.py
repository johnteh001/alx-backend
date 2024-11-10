#!/usr/bin/env python3
"""Flask App"""

from flask import Flask, render_template, session
from flask_babel import Babel, _
from flask import request
from flask_babel import lazy_gettext as _l


app = Flask(__name__)
app.config.from_object('config.Config')
babel = Babel(app)

@babel.localeselector
def get_locale():
    """language selector"""
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route("/", strict_slashes=False)
def index():
    """Renders simple index file"""
    return render_template('4-index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
