import tweepy
import pandas as pd
import json
from datetime import datetime
import s3fs

# Input your API keys
API_KEY = ""
API_SECRET_KEY = ""
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""

# Twitter authentication
auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# # # Creating an API object
api = tweepy.API(auth)
tweets = api.user_timeline(screen_name='@elonmusk',
                           # 200 is the maximum allowed count
                           count=200,
                           include_rts=False,
                           # Necessary to keep full_text
                           # otherwise only the first 140 words are extracted
                           tweet_mode='extended'
                           )

list = []
for tweet in tweets:
    text = tweet._json["full_text"]

    #Dictionary is being created which i will later append into the list

    refined_tweet = {"user": tweet.user.screen_name,
                     'text': text,
                     'favorite_count': tweet.favorite_count,
                     'retweet_count': tweet.retweet_count,
                     'created_at': tweet.created_at}

    list.append(refined_tweet)

df = pd.DataFrame(tweet_list)
df.to_csv('elonmusk_tweets.csv') # Paste the S3 bucket link inside the paranthesis
