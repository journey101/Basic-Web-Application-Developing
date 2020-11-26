from flask import jsonify
from flask import Blueprint, render_template, request
from basic_twit_app.models import db, Users, Tweet
from basic_twit_app.API.api import api

add_routes = Blueprint('add_routes', __name__)

@add_routes.route('/<username>/add/')
def add(username=None):
	username = username

	new = api.get_user(screen_name = username)
	tweets = api.user_timeline(screen_name = username, tweet_mode ="extend")
	tmp = [{'text':tweet.text, 'user_id':tweet.user.id} for tweet in tweets]

	db.session.add(
		Users(
			id = new.id,
            username = new.screen_name.casefold(),
            full_name = new.name,
            followers = new.followers_count
			))

	for tweet in tweets:
		db.session.add(Tweet(
			text = tweet.text,
			user_id = tweet.user.id
		))

	db.session.commit()

	return render_template('add.html', data = new)


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