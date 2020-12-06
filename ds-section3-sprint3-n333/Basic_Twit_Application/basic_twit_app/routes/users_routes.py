from flask import Blueprint, render_template, request
from basic_twit_app import models # pylint: disable=import-error
from basic_twit_app.models import db, Users, Tweet # pylint: disable=import-error
from basic_twit_app.API.twitter_api import twitter_api # pylint: disable=import-error

users_routes = Blueprint('users_routes', __name__)

# #'/users/
# 기존 코드 
# @users_routes.route('/users')
# def users():
#     data = users.query.all()
#     return render_template("users.html", data = data)

# 1202수_9:04pm 수정코드
# @users_routes.route('/users/', methods=["GET", "POST"])
# def users():
#     data = models.Users.query.all()
#     return render_template("users.html", data = data)

# @users_routes.route('/users/', methods=["GET", "POST"])
# def tweets():
#     tweet_data = tweets
#     return render_template("users.html", tweet_data = tweets)

# @users_routes.route('/users/', methods=["GET", "POST"])
# def gettweets():
# 	tweets = []
# 	if request.method == "POST":
# 		print(dict(request.form))
# 		result = request.form

# 		id = Users.query.with_entities(Users.id).filter(Users.username == result['username']).first()
# 		print(id)
# 		tweet_data = Tweet.query.filter(Tweet.user_id == id[0]).all()
#         # data = Tweet.query.filter(Tweet.user_id == Users.id).all()
# 		for tweet in tweet_data:
# 			tweets.append(tweet.text)

# 	return render_template("users.html", tweet_data = tweets)

import numpy as np
import pickle
import os
from flask import Blueprint, render_template, request
from basic_twit_app.models import db, Users, Tweet # pylint: disable=import-error
from basic_twit_app.API.twitter_api import twitter_api # pylint: disable=import-error
from embedding_as_service_client import EmbeddingClient
from sklearn.linear_model import LogisticRegression


# Model File
FILEPATH = './model.pkl'


# Encoding Server
en = EmbeddingClient(host='54.180.124.154', port=8989)
tweet_routes = Blueprint('tweet_routes', __name__)


# View tweets page
@users_routes.route('/users', methods=["GET", "POST"])
def gettweets():
    tweets = []
    data = models.Users.query.all()
    if request.method == "POST":
        print(dict(request.form))
        result = request.form
        # breakpoint()
        id = Users.query.with_entities(Users.id).filter(Users.username == result['username']).first()
        print(id)
        tweet_data = Tweet.query.filter(Tweet.user_id == id[0]).all()
        # data = Tweet.query.filter(Tweet.user_id == Users.id).all()
        for tweet in tweet_data:
            tweets.append(tweet.text)

    return render_template("users.html", tweet_data = tweets, data = data)

def append_to_with_label(to_arr, from_arr, label_arr, label):
    """
    from_arr 리스트에 있는 항목들을 to_arr 리스트에 append 하고
    레이블도 같이 추가해주는 함수입니다.
    """

    for item in from_arr:
        to_arr.append(item)
        label_arr.append(label)

# Predict the user by the tweet
@users_routes.route('/analytics', methods=["GET", "POST"])
def analyze():
    users = Users.query.all()
    text = []
    id = []
    prediction = 0
    if request.method == "POST":
        print(dict(request.form))
        result = request.form

        # import all datas from the table
        for user in users:
            tweets = Tweet.query.with_entities(Tweet.embedding).filter(Tweet.user_id == user.id).all()
            for tweet in tweets:
                append_to_with_label(text, tweet, id, user.id)
        
		# # 3D array to 2D array
        # text_array = np.array(text)
        # nsamples, nx, ny = text_array.shape
        # text_2d = text_array.reshape(nsamples, nx * ny)

		# Model import
        if os.path.isfile(FILEPATH):
            en = EmbeddingClient(host='54.180.124.154', port=8989)
            model = pickle.load(open('model.pkl', 'rb'))
            pred_id = model.predict(en.encode(texts = [result['text']]))
            prediction = int(pred_id[0])

        else:
            model = LogisticRegression(warm_start=True)
            model.fit(text, id)
            pred_id = model.predict(en.encode(texts = [result['text']]))
            prediction = int(pred_id[0])
            pickle.dump(model, open('model.pkl', 'wb'))
		
	# Predction result
    pred_res = Users.query.filter(Users.id == prediction).first()

    return render_template('analytics.html', prediction = pred_res)