from flask import Blueprint, render_template, request, jsonify, flash, redirect, url_for
import sqlite3

views = Blueprint("views", __name__)


@views.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html", entries=entries, show=False)
