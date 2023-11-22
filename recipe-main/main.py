import datetime
import dateutil.tz

from flask import Blueprint, render_template, request, redirect, url_for, flash
from . import db
from . import model

bp = Blueprint("main", __name__)


@bp.route("/")
def index():
    user = model.User(id=1, email="mary@example.com", name="mary")
    return render_template("main/index.html")

@bp.route("/new-recipe")
def new_recipe():
    return render_template("main/new-recipe.html")

@bp.route("/new-recipe", methods=["POST"])
def new_recipe_post():
    title = request.form.get("title")
    description = request.form.get("description")
    persons = request.form.get("persons")
    time = request.form.get("time")
    
    recipe = model.Recipe(
        user = flask_login.current_user,
        title = title,
        description = description,
        persons = persons,
        time = time
    )

    print(recipe)
    db.session.add(recipe)
    db.session.commit()
    
