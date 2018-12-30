import tweepy
from textblob import TextBlob

consumer_key = 'chfDf9PJMMU7Q9YqiBhz7yz4w'
consumer_secret = 'LBohmmIy6KTwvEYbAQ2qrtyM3yTH0BnGFxNDXzpA0mMdKqRut2'

access_token = '1055864877225455616-yJppbOzz07g8qdTrlw9Ia76yn9tk2e'
access_token_secret = 'YTGm6XbtI33yj6qTpu0JejexgYUCS2DyyOAu4ntO6dgp6'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search(input())

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
