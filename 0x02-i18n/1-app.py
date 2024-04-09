#!/usr/bin/env python3
'''
Basic Flask Application'''
from flask import Flask
from flask import template
from flask_babel import Babel


class Config(object):
    '''
    Application configuration class'''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Instantiation of application object
app = Flask(__name__)
app.config.from_object(Config)


# Wrapping application with Babel
babel = Babel(app)


@route('/', strict_slashes=False)
def index() -> str:
    '''
    Presents a basic html template'''
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()