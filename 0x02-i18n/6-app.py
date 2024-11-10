#!/usr/bin/env python3
"""Flask App"""

from flask import Flask, render_template, g
from flask_babel import Babel, _
from flask import request
from flask_babel import lazy_gettext as _l


app = Flask(__name__)
app.config.from_object('config.Config')
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

@babel.localeselector
def get_locale():
    """language selector"""
    locale = request.args.get('locale')
    usr_l = None
    if g.user:
        usr_l = g.user.get("locale")
    if locale and locale in app.config['LANGUAGES']:
        return locale
    elif usr_l and usr_l in app.config['LANGUAGES']:
        return usr_l
    locale = request.headers.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])

def get_user():
    """Selects a user"""
    login = request.args.get("login_as")
    if login:
        user = users.get(int(login))
        return user
    return None

@app.before_request
def before_request():
    """Executed before all functions"""
    us = get_user()
    g.user = us

@app.route("/", strict_slashes=False)
def index():
    """Renders simple index file"""
    u = g.user
    if u == None:
        username = None
    elif u:
        username = u.get("name")
    return render_template('6-index.html', username=username)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
