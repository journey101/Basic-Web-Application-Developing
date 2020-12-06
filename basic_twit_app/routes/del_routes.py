from flask import jsonify
from flask import Blueprint, render_template, request
from basic_twit_app.models import db, Users, Tweet # pylint: disable=import-error
from basic_twit_app.API.twitter_api import twitter_api # pylint: disable=import-error

del_routes = Blueprint('del_routes', __name__)


@del_routes.route('/delete', methods=["GET", "POST"])
def delete():	
	if request.method == "POST":
		result = request.form
		username = result["username"]

		id = Users.query.with_entities(Users.id).filter(Users.username == username).first()
		# print(id)
		
		Tweet.query.filter_by(user_id = id[0]).delete() 
		Users.query.filter_by(id = id[0]).delete() 
		# db.session.flush()
		
		# db.session.flush()
		
		db.session.commit()

	return render_template("delete.html")


if __name__ == '__main__':
	if request.method == "POST":
		result = request.form
		username = result["username"]
		api = twitter_api()
			
		new = api.get_user(screen_name = 'razer')
		db.session.add(Users(
			id = new.id,
			username = new.screen_name,
			full_name = new.name,
			followers = new.followers_count))

		tweets = api.user_timeline(screen_name = 'razer')
		for tweet in tweets:
			db.session.add(Tweet(
					text = tweet.text,
					user_id = new.id
			))

		db.session.commit() 