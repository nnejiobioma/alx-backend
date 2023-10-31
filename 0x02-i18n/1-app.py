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

@app.route('/')
def hello_world():
    """welcome greetings
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(port="5000", host="0.0.0.0", debug=True)
