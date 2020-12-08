from flask import jsonify
from flask import Blueprint, render_template, request
from basic_twit_app.models import Tweet, Users
from basic_twit_app.API.twitter_api import twitter_api # pylint: disable=import-error


get_routes = Blueprint('get_routes', __name__)

@get_routes.route('/<username>/get/')
def get(username = None):
    username = username
    id = Users.query.with_entities(Users.id).filter(Users.username == username).first()
    print(id)
    data = Tweet.query.filter(Tweet.user_id == id[0]).all()
    for tweet in data:
        print(tweet.text)
    return render_template("get.html", data = data)
