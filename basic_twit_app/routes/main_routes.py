from flask import Blueprint, render_template
from basic_twit_app.models import Users, db
from basic_twit_app.API.twitter_api import twitter_api # pylint: disable=import-error

main_routes = Blueprint('main_routes', __name__)

# '/'
@main_routes.route('/')
def index():
    return render_template("index.html")

# '/reset'
@main_routes.route('/reset')
def reset_db():
    db.drop_all()
    db.create_all()
    return 'DB refreshed!'