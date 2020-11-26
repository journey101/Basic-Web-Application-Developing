from tweepy import OAuthHandler, API
import os
from dotenv import load_dotenv
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

load_dotenv()
consumer_key = os.getenv('consumer_key')
consumer_secret = os.getenv('consumer_secret')
access_token = os.getenv('access_token')
access_token_secret = os.getenv('access_token_secret')

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

if __name__ == '__main__':
    twitter_user = api.get_user(screen_name = 'razer')
    tweets = api.user_timeline(screen_name = 'nike')
    tmp = [{'text':tweet.text, 'user_id':tweet.user.id} for tweet in tweets]
    for i, tweet in enumerate(tmp):
        if i < 5:
            print(tweet['text'])
            print(tweet['user_id'])
    breakpoint()