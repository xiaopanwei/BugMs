from flask import Blueprint, url_for,redirect
from flask_login import login_required, logout_user

logout = Blueprint("logout", __name__, static_folder="static",template_folder="template", url_prefix="/logout")


@logout.route("/")
@login_required
def index():
    logout_user()
    return redirect(url_for('index'))