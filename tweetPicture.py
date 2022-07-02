import tweepy
import random
import os
import keys

auth = tweepy.OAuthHandler(keys.api_key, keys.api_secret_key)
auth.set_access_token(keys.access_token, keys.access_secret_token)

# Directory Path

picturePath = "./pictures/"

# API

api = tweepy.API(auth)

def imageTweet():
    pictureList = os.listdir(picturePath)       # List directories in your file
    printPicture = random.choice(pictureList)   # Choose a random picture from your directory
    api.update_status_with_media("My Picture Tweet", picturePath + printPicture)

