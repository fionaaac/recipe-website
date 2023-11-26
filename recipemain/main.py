import datetime
import dateutil.tz

from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from . import db, model
import flask_login

import pathlib

bp = Blueprint("main", __name__)


@bp.route("/")
@flask_login.login_required
def index():
    # user = model.User(1, "mary@example.com", "mary")
    # return render_template("main/index.html", posts=posts)
    # user = model.User(id=1, email="mary@example.com", name="mary", password="test")
    title = "title"
    description = "description"
    persons = "persons"
    time = "time"
    # recipes = [
    #     model.Recipe(
    #         user = flask_login.current_user,
    #         id = uuid.uuid4().int >> (128 - 32),
    #         title = title,
    #         description = description,
    #         persons = persons,
    #         time = time,
    #         ingredient_id = uuid.uuid4().int >> (128 - 32)
    #     ),
    #     model.Recipe(
    #         user = flask_login.current_user,
    #         id = uuid.uuid4().int >> (128 - 32),
    #         title = title,
    #         description = description,
    #         persons = persons,
    #         time = time,
    #         ingredient_id = uuid.uuid4().int >> (128 - 32)
    #     ),
    #     model.Recipe(
    #         user = flask_login.current_user,
    #         id = uuid.uuid4().int >> (128 - 32),
    #         title = title,
    #         description = description,
    #         persons = persons,
    #         time = time,
    #         ingredient_id = uuid.uuid4().int >> (128 - 32)
    #     )
    # ]
    
    return render_template("main/index.html", recipes=model.Recipe.query.all(), photos=model.Photo.query.all())

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
        time = time, 
    )

    uploaded_file = request.files['photo']
    if uploaded_file.filename != '':
        content_type = uploaded_file.content_type
        if content_type == "image/png":
            file_extension = "png"
        elif content_type == "image/jpeg":
            file_extension = "jpg"
        else:
            abort(400, f"Unsupported file type {content_type}")

        photo = model.Photo (
            user=flask_login.current_user,
            recipe=recipe,
            file_extension=file_extension
        )

        db.session.add(photo)
    db.session.add(recipe)
    db.session.commit()

    path = (
        pathlib.Path(current_app.root_path)
        / "static"
        / "photos"
        / f"photo-{photo.id}.{file_extension}"
    )
    uploaded_file.save(path)

    all_recipes = model.Recipe.query.all()
    # Prints all recipes in the database
    for recipe in all_recipes:
        print(f"Recipe ID: {recipe.id}, Title: {recipe.title}, Description: {recipe.description}")
    return redirect(url_for("main.my_recipes"))

@bp.route("/my-recipes")
def my_recipes():
    all_recipes = model.Recipe.query.all()
    all_photos = model.Photo.query.all()
    return render_template("my_recipes.html", recipes=all_recipes, photos=all_photos, zip=zip)

@bp.route("/user/<username>")
@flask_login.login_required
def user(username):
    user = model.User(email="mary@example.com", name="mary")
    posts = [
        model.Message(
            user=user,
            text="Test post",
            timestamp=datetime.datetime.now(dateutil.tz.tzlocal()),
        ),
        model.Message(
            user=user,
            text="Another post",
            timestamp=datetime.datetime.now(dateutil.tz.tzlocal()),
        ),
        model.Message(
            user=user,
            text="third post to test grid",
            timestamp=datetime.datetime.now(dateutil.tz.tzlocal()),
        ),
    ]
    return render_template("main/user.html", user=user, posts=posts)
