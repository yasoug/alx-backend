#!/usr/bin/env python3
"""basic flask app"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def basic():
    """renders 0-index.html"""
    return render_template("0-index.html")
