import os
from twitter import *

consumer_key = 'teXFL6FkI2nE2KeBYWNs1A'
consumer_secret = 'KdnLaOXH3kQnffcg07UgkT0IFQC9wepvmXmqU2LENo'

my_twitter_creds = os.path.expanduser('~/.pyrate_credentials')
if not os.path.exists(my_twitter_creds):
  oauth_dance('pyrate', consumer_key, consumer_secret, my_twitter_creds)

oauth_token, oauth_secret = read_token_file(my_twitter_creds)

twitter = Twitter(auth=OAuth(oauth_token, oauth_secret, consumer_key, consumer_secret))

tweets = twitter.statuses.user_timeline()
for t in tweets:
  print t['text']
