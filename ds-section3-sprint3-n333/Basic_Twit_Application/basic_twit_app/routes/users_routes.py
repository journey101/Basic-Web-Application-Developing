from flask import Blueprint, render_template, request
from basic_twit_app.models import db, Users

users_routes = Blueprint('users_routes', __name__)

#'/users/
@users_routes.route('/')
def users():
    data = Users.query.all()
    return render_template("user.html", data = data)