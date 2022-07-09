import tweepy
import keys
import tweet_logic
from datetime import date

# Authenticate


auth = tweepy.OAuthHandler(keys.api_key, keys.api_secret_key)
auth.set_access_token(keys.access_token, keys.access_secret_token)

# API
api = tweepy.API(auth)

# Credentials check
try:
    api.verify_credentials()
    print("Everything good")
except:
    print("Something's wrong")


def letsTweet():
    if date.today().weekday() == 0:
        tweet_logic.imageTweet()
    elif date.today().weekday() == 2:
        tweet_logic.textTweet()

# You Tweet here finally
letsTweet()

