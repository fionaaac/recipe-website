from . import db
from flask_login import UserMixin
import uuid

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, default=lambda: uuid.uuid4().int >> (128 - 32), primary_key=True)
    # id = db.Column(db.String(36), default=str(uuid.uuid4()), primary_key=True)
    # email = db.Column(db.String(128), unique=True, nullable=False)
    email = db.Column(db.String(128), unique=False, nullable=False)
    name = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(100), default='')
    recipes = db.relationship('Recipe', back_populates='user')
    ratings = db.relationship('Rating', back_populates='user')
    photos = db.relationship('Photo', back_populates='user')

class Ingredient(db.Model):
    id = db.Column(db.Integer, default=lambda: uuid.uuid4().int >> (128 - 32), primary_key=True)
    name = db.Column(db.String(64), nullable=False)

    q_ingredients = db.relationship('Q_Ingredient', back_populates='ingredient')
    recipes = db.relationship('Recipe', back_populates='ingredient')

class Q_Ingredient(db.Model):
    id = db.Column(db.Integer, default=lambda: uuid.uuid4().int >> (128 - 32), primary_key=True)
    quantity = db.Column(db.Integer)
    units = db.Column(db.Integer)

    # ingredient_id = db.Column(db.Integer, db.ForeignKey("ingredient.id"), nullable=False)
    ingredient_id = db.Column(db.Integer, db.ForeignKey("ingredient.id"), default=lambda: uuid.uuid4().int >> (128 - 32), nullable=False)
    ingredient = db.relationship('Ingredient', back_populates='q_ingredients')
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipe.id"), nullable=False)
    recipe = db.relationship('Recipe', back_populates='q_ingredients')

class Step(db.Model):
    id = db.Column(db.Integer, default=lambda: uuid.uuid4().int >> (128 - 32), primary_key=True)
    text = db.Column(db.String(512), nullable=False)
    position = db.Column(db.Enum)

    # recipe_id = db.Column(db.Integer, db.ForeignKey("recipe.id"), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipe.id"), default=lambda: uuid.uuid4().int >> (128 - 32), nullable=False)
    recipe = db.relationship('Recipe', back_populates='steps')
    
class Recipe(db.Model):
    id = db.Column(db.Integer, default=lambda: uuid.uuid4().int >> (128 - 32), primary_key=True)
    title = db.Column(db.String(64), nullable=False)
    description = db.Column(db.Text, nullable=False)
    time = db.Column(db.Integer, nullable=False) # seconds
    persons = db.Column(db.Integer, nullable=False)
    is_saved = db.Column(db.Boolean, default=False)

    # user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), default=lambda: uuid.uuid4().int >> (128 - 32), nullable=False)
    user = db.relationship('User', back_populates='recipes')
    # ingredient_id = db.Column(db.Integer, db.ForeignKey("ingredient.id"), nullable=False)
    ingredient_id = db.Column(db.Integer, db.ForeignKey("ingredient.id"), default=lambda: uuid.uuid4().int >> (128 - 32), nullable=False)
    ingredient = db.relationship('Ingredient', back_populates='recipes')

    q_ingredients = db.relationship('Q_Ingredient', back_populates='recipe')
    steps = db.relationship('Step', back_populates='recipe')
    ratings = db.relationship('Rating', back_populates='recipe')
    photos = db.relationship('Photo', back_populates='recipe')

class Rating(db.Model):
    id = db.Column(db.Integer, default=lambda: uuid.uuid4().int >> (128 - 32), primary_key=True)
    value = db.Column(db.Integer, nullable=False)
    # user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), default=lambda: uuid.uuid4().int >> (128 - 32), nullable=False)
    user = db.relationship('User', back_populates='ratings')
    # recipe_id = db.Column(db.Integer, db.ForeignKey("recipe.id"), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipe.id"), default=lambda: uuid.uuid4().int >> (128 - 32), nullable=False)
    recipe = db.relationship('Recipe', back_populates='ratings')

class Photo(db.Model):
    id = db.Column(db.Integer, default=lambda: uuid.uuid4().int >> (128 - 32), primary_key=True)
    
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipe.id"), default=lambda: uuid.uuid4().int >> (128 - 32), nullable=False)
    recipe = db.relationship('Recipe', back_populates='photos')
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), default=lambda: uuid.uuid4().int >> (128 - 32), nullable=False)
    user = db.relationship('User', back_populates='photos')

    file_extension = db.Column(db.String(8), nullable=False)