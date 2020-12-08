from flask import jsonify
from flask import Blueprint, render_template, request
from basic_twit_app.models import db, Users, Tweet # pylint: disable=import-error
from basic_twit_app.API.twitter_api import twitter_api # pylint: disable=import-error
from tweepy import API
from embedding_as_service_client import EmbeddingClient

update_routes = Blueprint('update_routes', __name__)
en = EmbeddingClient(host='54.180.124.154', port=8989)

@update_routes.route('/update', methods=["GET", "POST"])
def update():
	if request.method == "POST":
		print(dict(request.form))
		result = request.form
		db.session.query(Users).filter(Users.username == result['username']).update({'username': result['change_username']})
		# db.session.query(Users).filter(Users.full_name == result['full_name']).update({'full_name': result['change_full_name']})		
		db.session.commit()
		if result['name_type'] == '1':
			db.session.query(Users).filter(Users.username == result['username']).update({'username': result['change_username']})
			db.session.commit()
		elif result['name_type'] == '2':
			db.session.query(Users).filter(Users.username == result['username']).update({'full_name': result['change_full_name']})
			db.session.commit()

	return render_template('update.html')

# def update():
# 	if request.method == "POST":
# 		result = request.form
# 		username = result["username"]

# 		api = twitter_api()
# 		users = api.get_user(screen_name = username)
# 		# tweets = api.user_timeline(screen_name = username, count=300,
# 		# 							include_rts = False, exclude_replies=True)
# 		tweets = api.user_timeline(screen_name = username, tweet_mode ="extend")

# 		db_users = Users()
# 		db_users.id = users.id
# 		db_users.username = users.screen_name
# 		db_users.full_name = users.name
# 		db_users.followers = users.followers_count

# 		db.session.add(db_users)
# 		db.session.commit()

# 		for data in tweets:
# 			tweet = Tweet.query.get(data.id) or Tweet(id = data.id)
# 			tweet.text = data.text
#             tweet.embedding = en.encode(texts = [data.text])
#             tweet.user_id = data.user.id
# 			db.session.add(tweet)

# 		db.session.commit()
# 		# print(f"num tweets for {user.screen_name} is :", len(tweets))
# 	return render_template('update.html')
