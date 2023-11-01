import datetime
import dateutil.tz

from flask import Blueprint, render_template


from . import model

bp = Blueprint("main", __name__)


@bp.route("/")
def index():
    user = model.User(id=1, email="mary@example.com", name="mary")
    return render_template("main/index.html")
