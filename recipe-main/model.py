from . import db
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    name = db.Column(db.String(64), nullable=False)
class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipe.id"), nullable=False)
    recipe = db.relationship('Recipe', back_populates='ratings')

class Q_Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ingredient_id = db.Column(db.Integer, db.ForeignKey("ingredient.id"), nullable=False)
    ingredient = db.relationship('Ingredient', back_populates='ingredients')
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipe.id"), nullable=False)
    recipe = db.relationship('Recipe', back_populates='q_ingredients')
    quantity = db.Column(db.Integer)
    units = db.Column(db.Integer)
class Step(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(512), nullable=False)
    recipe_id = db.Column(db.Integer, nullable=False)
    recipe = db.relationship('Recipe', back_populates='steps')
    position = db.Column(db.Enum)
class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), nullable=False)
    description = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    user = db.relationship('User', back_populates='recipes')
    ingredient_id = db.Column(db.Integer, db.ForeignKey("ingredient.id"), nullable=False)
    ingredient = db.relationship('Ingredient', back_populates='recipes')
    step_id = db.Column(db.Integer, db.ForeignKey("step.id"), nullable=False)
    step = db.relationship('Step', back_populates='recipes')
    time = db.Column(db.Integer, nullable=False) # seconds
    persons = db.Column(db.Integer, nullable=False)

class Rating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    user = db.relationship('User', back_populates='ratings')
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipe.id"), nullable=False)
    recipe = db.relationship('Recipe', back_populates='ratings')
