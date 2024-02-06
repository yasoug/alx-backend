#!/usr/bin/env python3
"""basic babel setup"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, format_time
import pytz


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


@babel.timezoneselector
def get_timezone():
    """determine the appropriate timezone"""
    url_timezone = request.args.get("timezone")
    if url_timezone:
        try:
            pytz.timezone(url_timezone)
            return url_timezone
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    if g.user and g.user.get("timezone"):
        return g.user.get("timezone")
    return Config.BABEL_DEFAULT_TIMEZONE


@app.route("/")
def basic():
    """renders index.html"""
    g.time = format_datetime()
    return render_template("index.html", user=g.user, time=g.time)
