#!/usr/bin/env python3
'''
Basic Flask Application'''
from typing import (
    Dict, Union
)

from flask import Flask
from flask import g, request
from flask import render_template
from babel_label import Babel


class Config(object):
    '''
    The application configuration class'''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'utc'


# Instantiation of application object
app = Flask(__name__)
app.config.from_object(Config)


# Wrapping application with Babel
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    '''
    Getting the locale from request object'''
    locale = request.args.get('locale', '').strip()
    if locale and locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(id) -> Union[Dict[str, Union[str, None]], None]:
    '''
    Validation of users login details
    Args:
        id (str): user id
    Returns:
        (Dict): user dictionary if the id is valid else None'''
    return users.get(int(id), 0)


@app.before_request
def before_request():
    '''
    Adds valid user to the global session object `g`'''
    setattr(g, 'user', get_user(request.args.get('login_as', 0)))

@route('/', strict_slashes=False)
def index() -> str:
    '''
    Presents a basic html template'''
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run()
