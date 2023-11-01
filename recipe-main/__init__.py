from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(test_config=None):
    app = Flask(__name__)

# A secret for signing session cookies
    app.config["SECRET_KEY"] = "93220d9b340cf9a6c39bac99cce7daf220167498f91fa"

    # app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqldb://recipewebsite:hello@localhost/RecipeWebsite"
    
    # this one runs on sqlite which we can use until we figure out db
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///recipe-main.db"

    # Register blueprints
    # (we import main from here to avoid circular imports in the next lab)
    from . import main

    db.init_app(app)
    app.register_blueprint(main.bp)
    return app
