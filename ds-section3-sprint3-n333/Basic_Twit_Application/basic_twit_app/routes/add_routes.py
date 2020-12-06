from flask import jsonify
from flask import Blueprint, render_template, request
from basic_twit_app.models import db, Users, Tweet # pylint: disable=import-error
from basic_twit_app.API.twitter_api import twitter_api # pylint: disable=import-error
from tweepy import API
from embedding_as_service_client import EmbeddingClient

add_routes = Blueprint('add_routes', __name__)
en = EmbeddingClient(host='54.180.124.154', port=8989)

# @add_routes.route('/add/')

# @add_routes.route('/<username>/add/')
# def add_twit_user(username=None):
# 	username = username

@add_routes.route('/add', methods=["GET", "POST"])
def add_twit_user():
	if request.method == "POST":
		result = request.form
		username = result["username"]

		api = twitter_api()
		users = api.get_user(screen_name = username)
		# tweets = api.user_timeline(screen_name = username, count=300,
		# 							include_rts = False, exclude_replies=True)
		# tweets = api.user_timeline(screen_name = username, tweet_mode ="extend")
		
		db_users = Users()
		db_users.id = users.id
		db_users.username = users.screen_name
		db_users.full_name = users.name
		db_users.followers = users.followers_count

		db.session.add(db_users)
		print('Users')
		
		#tweet text
		raw_tweets = api.user_timeline(users.screen_name, count=300,
                                        include_rts=False, exclude_replies=True,
                                        tweet_mode="extended")
		print('raw_tweets')

        # 해당 user가 트윗을 한 개 이상 한 경우에만 db에 저장
		if len(raw_tweets) >= 1:
			for tweet in raw_tweets:
				en = EmbeddingClient(host='54.180.124.154', port=8989)
				one_tweet = [tweet.full_text]
				print('one_tweet')
				embedding_result = en.encode(texts=one_tweet)
				print('embedding_result')
				
				insert_tweet = Tweet(
					id = tweet.id,
					text = tweet.full_text,
					embedding = embedding_result[0],
					user_id = users.id)
				db.session.add(insert_tweet)
			db.session.commit()

	
	return render_template('add_routesdd.html')
