import tweepy
import keys

from datetime import date

# Authenticate
auth = tweepy.OAuthHandler(keys.api_key, keys.api_secret_key)
auth.set_access_token(keys.access_token, keys.access_secret_token)

# API
api = tweepy.API(auth)

#Credentials check
try:
    api.verify_credentials()
    print("Everything good")
except:
    print("Something's wrong")
