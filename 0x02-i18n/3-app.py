#!/usr/bin/env python3
'''
Basic Flask Application'''
from flask import Flask
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
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@route('/', strict_slashes=False)
def index() -> str:
    '''
    Presents a basic html template'''
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run()
