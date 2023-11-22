import datetime
import dateutil.tz

from flask import Blueprint, render_template, request, redirect, url_for, flash
from . import db
import flask_login

from . import model

bp = Blueprint("main", __name__)


@bp.route("/")
@flask_login.login_required
def index():
    # user = model.User(1, "mary@example.com", "mary")
    # return render_template("main/index.html", posts=posts)
    # user = model.User(id=1, email="mary@example.com", name="mary")
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
    temp_user = model.User(id=7, email="bonnie@example.com", name="bonnie")
    # temp_user = model.User()
    recipe = model.Recipe(
        # user = flask_login.current_user,
        id = 5,
        user = temp_user,
        title = title,
        description = description,
        persons = persons,
        time = time,
        ingredient_id = 5
    )

    print(recipe)
    db.session.add(recipe)
    db.session.commit()

    return redirect(url_for("main.index"))
