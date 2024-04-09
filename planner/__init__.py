"""
auth: AJ Boyd
date: 4/8/24
desc: sample CRUD app using the Flask framework
file: __init__.py
"""

from flask import Flask
import sqlite3
from .views import views


def createApp():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = (
        "asdf-sdfgl jfd aspidufhasf apo8f ywef-asdoif hasd;fja"  # random key
    )

    # register blueprint
    app.register_blueprint(views, url_prefix="/")
    return app
