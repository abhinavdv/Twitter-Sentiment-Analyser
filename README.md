# Twitter Sentiment Analyser
The twitter-Sentiment-Analyser uses the tweepy library to authenticate with twitter. It uses textblob to analyse the data and give an anlaysis of the sentiment value to the tweet on a scale of -1 to 1.

The tweeepy library help authenticate into twitter to retrive the tweets which will be fetched using the search meathod in tweepy.API. The textblob library consists of a TextBlob meathod which on being called gives a sentiment analysis for the respective tweet.

The user interacts with the code via the terminal where the user gives a key word. The most recent occurances of the key word will then be displayed along with its sentiment values.
