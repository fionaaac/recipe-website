class User:
    def __init__(self, user_id, email, name):
        self.user_id = user_id
        self.email = email
        self.name = name

class Recipe:
    def __init__(self, recipe_id, title, description, user_id, persons, time, ingredients, q_ingredients, steps):
        self.recipe_id = recipe_id
        self.title = title
        self.description = description
        self.user_id = user_id
        self.persons = persons
        self.time = time
        self.ingredients = ingredients
        self.q_ingredients = q_ingredients
        self.steps = steps

class Ingredient:
    def __init__(self, ingredient_id, name):
        self.ingredient_id = ingredient_id
        self.name = name

class Q_Ingredient:
    def __init__(self, q_ingredient_id, ingredient_id, quantity, units, recipe_id):
        self.q_ingredient_id = q_ingredient_id
        self.ingredient_id = ingredient_id
        self.quantity = quantity
        self.units = units
        self.recipe_id = recipe_id

class Step:
    def __init__(self, step_id, text, recipe_id, position):
        self.step_id = step_id
        self.text = text
        self.recipe_id = recipe_id
        self.position = position

class Rating:
    def __init__(self, rating_id, user_id, recipe_id, value):
        self.rating_id = rating_id
        self.user_id = user_id
        self.recipe_id = recipe_id
        self.value = value