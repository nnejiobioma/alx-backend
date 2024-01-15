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

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

@app.before_request
def before_request(login_as: int = None):
    """ Request of each function
    """
    user: dict = get_user()
    print(user)
    g.user = user


def get_user() -> Union[dict, None]:
    """ Get the user.
    """
    login_user = request.args.get('login_as', None)

    if login_user is None:
        return None

    user: dict = {}
    user[login_user] = users.get(int(login_user))

    return user[login_user]


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
