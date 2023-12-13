import datetime
import json
import dateutil.tz

from flask import Blueprint, abort, render_template, request, redirect, url_for, flash, current_app
from flask_login import current_user
from . import db, model
import flask_login

import pathlib

bp = Blueprint("main", __name__)


@bp.route("/")
@flask_login.login_required
def index():
    return render_template("main/index.html", recipes=model.Recipe.query.all(), photos=model.Photo.query.all())

@bp.route("/new-recipe")
def new_recipe():
    ingredients = model.Ingredient.query.all()
    return render_template("main/new_recipe.html", ingredients=ingredients)

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
    db.session.add(recipe)

    ingredients_data = request.form.get('ingredientsData')
    q_ingredients = []
    if ingredients_data:
        ingredients_data = json.loads(ingredients_data)
        for ingredient in ingredients_data:
            name = ingredient['ingredientName']
            amount = ingredient['amount']
            unit = ingredient['unit']

            ingredient = model.Ingredient.query.filter_by(name=name).first()
            if not ingredient:
                new_ingredient =   model.Ingredient(name=name)
                db.session.add(new_ingredient)   
                q_ingredient = model.Q_Ingredient(
                    quantity=amount,
                    units=unit,
                    ingredient=new_ingredient,
                    recipe=recipe
            )       
            else:
                q_ingredient = model.Q_Ingredient(
                    quantity=amount,
                    units=unit,
                    ingredient=ingredient,
                    recipe=recipe
                )

            db.session.add(q_ingredient)
            q_ingredients.append(q_ingredient)
    
    print('Ingredients data:', ingredients_data)
    recipe.q_ingredients = q_ingredients

    steps_data = request.form.get('stepsData')
    steps = []
    if steps_data:
        steps_data = json.loads(steps_data)
        for step_text in steps_data:
            step = model.Step(text=step_text)
            db.session.add(step)
            steps.append(step)
    print("steps", steps_data)
    recipe.steps = steps

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

    db.session.commit()

    path = (
        pathlib.Path(current_app.root_path)
        / "static"
        / "photos"
        / f"photo-{photo.id}.{file_extension}"
    )
    uploaded_file.save(path)
    return redirect(url_for("main.my_recipes"))




@bp.route("/my-recipes")
def my_recipes():
    # all_recipes = model.Recipe.query.all()
    # all_photos = model.Photo.query.all()
    my_recipes = model.Recipe.query.filter_by(user_id=current_user.id).all()
    my_photos = model.Photo.query.filter_by(user_id=current_user.id).all()
    return render_template("my_recipes.html", recipes=my_recipes, photos=my_photos, zip=zip)


@bp.route('/recipe/<string:recipe_id>')
@flask_login.login_required
def recipe(recipe_id):
    recipe = model.Recipe.query.filter_by(id=str(recipe_id)).first()
    if recipe:
        # Here, 'recipe' holds the recipe object fetched from the database
        rating = model.Rating.query.filter_by(recipe_id=str(recipe_id)).first()
        return render_template("main/recipe_info.html", recipe=recipe, rating=rating)
    else:
        abort(400, f"Recipe with id {recipe_id} not found")

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


@bp.route("/saved-recipes")
@flask_login.login_required
def saved_recipes():
    saved_recipes = model.Recipe.query.filter(model.Recipe.is_saved == True).all()
    return render_template("main/saved_recipes.html", recipes=saved_recipes)

@bp.route('/recipe/<string:recipe_id>', methods=["POST"])
@flask_login.login_required
def save_recipe_post(recipe_id):

    if recipe_id is not None:
        recipe = model.Recipe.query.filter_by(id=str(recipe_id)).first()
        if recipe:
            recipe.is_saved = True
            db.session.commit()
            print('switched flag!!')
        else:
            abort(400, f"Recipe with id {recipe_id} not found")
    
    return render_template("main/recipe_info.html", recipe=recipe)

@flask_login.login_required
@bp.route('/saved-recipes/<string:recipe_id>', methods=["POST"])
def saved_recipe_delete(recipe_id):
    if recipe_id is not None:
        recipe = model.Recipe.query.filter_by(id=str(recipe_id)).first()
        if recipe:
            recipe.is_saved = False
            db.session.commit()
            print('switched flag!!')
        else:
            abort(400, f"Recipe with id {recipe_id} not found")
    
    saved_recipes = model.Recipe.query.filter(model.Recipe.is_saved == True).all()
    return render_template("main/saved_recipes.html", recipes=saved_recipes)

@bp.route('/add-rating/<string:recipe_id>', methods=['POST'])
def submit_rating_post(recipe_id):
    selected_star = request.form.get('star')
    print(f"The user selected {selected_star} stars!")
    recipe = model.Recipe.query.filter_by(id=str(recipe_id)).first()

    rating = model.Rating(
        value = selected_star,
        user = flask_login.current_user,
        recipe = recipe
    )

    return render_template("main/recipe_info.html", recipe=recipe, rating=rating)