import json
import random 
import tweepy
import credentials
import time
import sys
from os import environ


consumer_key = environ['API_KEY']
consumer_secret_key = environ['API_SECRET_KEY']
access_token = environ['ACCESS_TOKEN']
access_token_secret = environ['ACCESS_TOKEN_SECRET']

def get_random_quote():
    with open('data.json') as f:
        quotes_json = json.load(f)
        x = random.randint(0,251)
    return quotes_json[x]['Quote:']

def format_tweet():
    quote = get_random_quote()
    Hashtag = " #ILoveBioinstrumentation"
    Funfact = "Fun fact: "
    Tweet = Funfact + quote + Hashtag
    return Tweet

def create_tweet():
    interval = 60 * 60 * 12
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    while True:
        print('getting a random tweet...')
        test_tweet = format_tweet()
        api.update_status(test_tweet)
        time.sleep(interval)


if __name__ == "__main__":
    create_tweet()



