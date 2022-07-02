import tweepy
import random
import os
import keys

# Authenticate
auth = tweepy.OAuthHandler(keys.api_key, keys.api_secret_key)
auth.set_access_token(keys.access_token, keys.access_secret_token)

# Directory Path
textPath = "./texts/"

# API
api = tweepy.API(auth)

def textTweet():
    textList = os.listdir(textPath)                         # List files in your local directory
    chooseText = random.choice(textList)                    # Choose a random text file from the directory
    f = open(textPath + chooseText, "r")                    # Open the text file
    api.update_status("Text Tweet" + "\n" + f.read())       # Actual Tweet