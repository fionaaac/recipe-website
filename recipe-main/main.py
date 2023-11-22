import datetime
import dateutil.tz

from flask import Blueprint, render_template
import flask_login


from . import model

bp = Blueprint("main", __name__)


@bp.route("/")
@flask_login.login_required
def index():
    # user = model.User(1, "mary@example.com", "mary")
    # return render_template("main/index.html", posts=posts)
    return render_template("main/index.html")
