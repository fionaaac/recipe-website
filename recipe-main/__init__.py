from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

db = SQLAlchemy()
bcrypt = Bcrypt()

def create_app(test_config=None):
    app = Flask(__name__)

# A secret for signing session cookies
    app.config["SECRET_KEY"] = "93220d9b340cf9a6c39bac99cce7daf220167498f91fa"

    # app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqldb://recipewebsite:hello@localhost/RecipeWebsite"
    
    # this one runs on sqlite which we can use until we figure out db
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///recipe-main.db"
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    from . import model

    # function to load a user from the database given its ID
    @login_manager.user_loader
    def load_user(user_id):
        return db.session.get(model.User, int(user_id))


    # Register blueprints
    # (we import main from here to avoid circular imports in the next lab)
    from . import main
    from . import auth

    db.init_app(app)
    app.register_blueprint(auth.bp)
    app.register_blueprint(main.bp)
    return app
