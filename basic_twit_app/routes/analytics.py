from flask import jsonify
from flask import Blueprint, render_template, request
from basic_twit_app.models import db, Users, Tweet # pylint: disable=import-error
from basic_twit_app.API.twitter_api import twitter_api # pylint: disable=import-error
from tweepy import API
from embedding_as_service_client import EmbeddingClient
from sklearn.ensemble import RandomForestClassifier

analytics = Blueprint('/analytics', __name__)

@analytics.route('/analytics', methods=["GET", "POST"])
def analyze():
	if request.method == 'POST':
		users= Users.query.all()
		# prediction = ""
		# compare_text = ""

		raw_user_1 = request.form["User1"]
		raw_user_2 = request.form["User2"]
		
		user_1 = Users.query.filter_by(id=raw_user_1).one()
		user_2 = Users.query.filter_by(id=raw_user_2).one()

		embedding= []
		labels = []

		for tw_1 in user_1.tweets:
			embedding.append(tw_1.embedding)
			labels.append(user_1.username)

		for tw_2 in user_2.tweets:
			embedding.append(tw_2.embedding)
			labels.append(user_2.username)
		
		classifier = RandomForestClassifier()
		classifier.fit(embedding, labels)

		compare_text = request.form['text']
		en = EmbeddingClient(host='54.180.124.154', port=8989)
		predict_embedding = en.encode(texts=[compare_text])
		prediction = classifier.predict(predict_embedding)

		print(f"Compare string {compare_text}")
		print(f"Prediction Results {prediction}")

	return render_template("analytics.html", users=users, predict = prediction, compare_text=compare_text)

# @analytics.route('/analytics', methods=["GET", "POST"])
# def result():
#     # 분석된 결과값 가져오기. 
# 	data = prodiction
#     return render_template("users.html", data = data)
