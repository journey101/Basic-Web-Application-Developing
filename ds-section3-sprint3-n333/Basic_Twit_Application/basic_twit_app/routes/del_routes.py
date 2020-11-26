from flask import jsonify
from flask import Blueprint, render_template, request
from basic_twit_app.models import db, Users, Tweet
from basic_twit_app.API.api import api

del_routes = Blueprint('del_routes', __name__)


@del_routes.route('/<username>/delete/')
def delete(username = None):
	username = username
	id = Users.query.with_entities(Users.id).filter(Users.username == username).first()
	print(id)
	Users.query.filter_by(id = id[0]).delete() 
	Tweet.query.filter_by(user_id = id[0]).delete() 

	db.session.commit()

	return render_template("delete.html")


if __name__ == '__main__':
	new = api.get_user(screen_name = 'razar')
	db.session.add(Users(
		id = new.id,
		username = new.screen_name,
		full_name = new.name,
		followers = new.followers_count))

	tweets = api.user_timeline(screen_name = 'razar')
	for tweet in tweets:
		db.session.add(Tweet(
				text = tweet.text,
				user_id = new.id
		))

	db.session.commit() 