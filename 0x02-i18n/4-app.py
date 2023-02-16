#!/usr/bin/env python3
"""
simple flask app with I18n
support using flask_babel
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """babel config"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config())

babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    returns the correct
    or preferred locale
    """
    locale = request.args.get('locale')
    if locale:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=['GET'], strict_slashes=False)
def home():
    """index route"""
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)
