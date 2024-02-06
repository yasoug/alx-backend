#!/usr/bin/env python3
"""basic babel setup"""

from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config:
    """Configuration class for Flask application"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """returns user info if login_as is provided"""
    user_id = request.args.get("login_as")
    if user_id:
        return users.get(int(user_id))
    return None


@app.before_request
def before_request():
    """find a user if any, and set it as a global"""
    g.user = get_user()


@babel.localeselector
def get_locale():
    """determine the best match with supported languages"""
    url_locale = request.args.get("locale")
    if url_locale in Config.LANGUAGES:
        return url_locale
    if g.user:
        user_locale = g.user.get("locale")
        if user_locale in Config.LANGUAGES:
            return user_locale
    hdr_locale = request.accept_languages.best_match(app.config["LANGUAGES"])
    if hdr_locale:
        return hdr_locale
    return Config.BABEL_DEFAULT_LOCALE


@app.route("/")
def basic():
    """renders 6-index.html"""
    return render_template("6-index.html", user=g.user)
