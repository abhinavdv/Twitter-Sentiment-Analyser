import tweepy
from textblob import TextBlob

# consumer_key, consumer_secret are different for different individuals

consumer_key = 'write your here'
consumer_secret = 'write your here'

access_token = 'write your here'
access_token_secret = 'write your here'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search(input())

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
