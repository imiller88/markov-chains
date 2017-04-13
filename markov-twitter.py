import os
import twitter
import sys
from markov import open_and_read_file, make_chains, make_text, char_limit
from tweetcleaner import clean_tweets
import cleantrumptweets
# from tweet_dumper import get_all_tweets

api = twitter.Api(
    consumer_key=os.environ['TWITTER_CONSUMER_KEY'],
    consumer_secret=os.environ['TWITTER_CONSUMER_SECRET'],
    access_token_key=os.environ['TWITTER_ACCESS_TOKEN_KEY'],
    access_token_secret=os.environ['TWITTER_ACCESS_TOKEN_SECRET'])

# print api.VerifyCredentials()

input_text = sys.argv[1]
# input_text = clean_tweets("green-eggs.txt")

text = open_and_read_file(input_text)
chains = make_chains(text)
long_text = make_text(chains)
tweet = char_limit(long_text)

status = api.PostUpdate(tweet)
print status.text


# tweet source brainstorm
#   Oscar Wilde
#   Mark Twain
#   Shakespeare
#   Miley Cyrus
#   Andy Borowitz
#   The Onion 
#   Internation Declaration of Human Rights
#   Taylor Swift
#   Arrested Development
#   Tweety Bird