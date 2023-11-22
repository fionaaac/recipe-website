from flask import Blueprint, render_template, request, redirect, url_for, flash
from . import db, bcrypt

from . import model
import flask_login

bp = Blueprint("auth", __name__)


@bp.route("/signup")
def signup():
    return render_template("auth/signup.html")


@bp.route("/signup", methods=["POST"])
def signup_post():
    email = request.form.get("email")
    username = request.form.get("username")
    password = request.form.get("password")
    # Check that passwords are equal
    if password != request.form.get("password_repeat"):
        flash("Sorry, passwords are different")
        return redirect(url_for("auth.signup"))
    # Check if the email is already at the database
    query = db.select(model.User).where(model.User.email == email)
    user = db.session.execute(query).scalar_one_or_none()
    if user:
        flash("Sorry, the email you provided is already registered")
        return redirect(url_for("auth.signup"))
    password_hash = bcrypt.generate_password_hash(password).decode("utf-8")
    new_user = model.User(email=email, name=username, password=password_hash)
    db.session.add(new_user)
    db.session.commit()
    print("all users after signup")
    all_users = model.User.query.all()

    # Display or iterate through the recipes
    for user in all_users:
        print(f"User ID: {user.id}, Name: {user.name}, Email: {user.email}")
    flash("You've successfully signed up! Please log in.")
    return redirect(url_for("auth.login"))

@bp.route("/login")
def login():
    return render_template("auth/login.html")

@bp.route("/login", methods=["POST"])
def login_post():
    email = request.form.get("email")
    password = request.form.get("password")
    query = db.select(model.User).where(model.User.email == email)
    user = db.session.execute(query).scalar_one_or_none()
    if user and bcrypt.check_password_hash(user.password, password):
        # The user exists and the password is correct
        flask_login.login_user(user)
        flash("You've successfully logged in!")
        print("all users after login: ")
        all_users = model.User.query.all()

        # Display or iterate through the recipes
        for user in all_users:
            print(f"User ID: {user.id}, Name: {user.name}, Email: {user.email}")
        return redirect(url_for("main.index"))
    else:
        flash("Invalid email or password")
        return redirect(url_for("auth.login"))
    
@bp.route("/logout")
def logout():
    flask_login.logout_user()
    return render_template("auth/login.html")

@bp.route("/logout", methods=["POST"])
def logout_post():
    # flask_login.logout_user()
    flash("You've successfully logged out!")
    return redirect(url_for("auth.login"))
