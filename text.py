import tweepy
import random
import os
import keys

# Authenticate

auth = tweepy.OAuthHandler(keys.api_key, keys.api_secret_key)
auth.set_access_token(keys.access_token, keys.access_secret_token)

# Directory Path

memePath = "./memes/"
lyricPath = "./lyrics/"

# API

api = tweepy.API(auth)