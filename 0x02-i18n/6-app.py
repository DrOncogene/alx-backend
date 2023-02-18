#!/usr/bin/env python3
"""
simple flask app with I18n
support using flask_babel
"""
from typing import Union
from flask import Flask, render_template, request, g
from flask_babel import Babel


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """babel config"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config())

babel = Babel(app)


def get_user(user_id: int) -> Union[dict, None]:
    """fetches a user"""
    if user_id is None:
        return None
    return users.get(user_id)


@app.before_request
def before_request():
    """
    runs before any request
    """
    try:
        user_id = int(request.args.get('login_as'))
    except (ValueError, TypeError):
        user_id = None

    g.user = get_user(user_id)


@babel.localeselector
def get_locale():
    """
    returns the correct
    or preferred locale
    """
    param_locale = request.args.get('locale') if request.args else None
    user_locale = g.user.get('locale') if g.user else None
    locale = param_locale or user_locale

    if locale and locale in app.config['LANGUAGES']:
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=['GET'], strict_slashes=False)
def home():
    """index route"""
    return render_template('6-index.html')


if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)
