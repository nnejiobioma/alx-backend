#!/usr/bin/env python3
"""This is a simple flask app
"""


from flask import Flask, render_template
from flask_babel import Babel


class Config(object):
    """ Babel instantiate """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    BABEL_DEFAULT_LOCALE = 'en'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """ Locale language to determine the
    best match with support
    language
    """
    locale = request.args.get('locale', None)

    if locale and locale in app.config['LANGUAGES']:
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=['GET'], strict_slashes=False)
def hello_world():
    """welcome greetings
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(port="5000", host="0.0.0.0", debug=True)
