import os
import time

from twitter import *

from speech import *

class TwitterApi:
  def __init__(self):
    self.consumer_key = 'teXFL6FkI2nE2KeBYWNs1A'
    self.consumer_secret = 'KdnLaOXH3kQnffcg07UgkT0IFQC9wepvmXmqU2LENo'
    self.my_twitter_creds = os.path.expanduser('~/.pyrate_credentials')

  def create(self):
    if not os.path.exists(self.my_twitter_creds):
      oauth_dance('pyrate', self.consumer_key, self.consumer_secret, self.my_twitter_creds)

    oauth_token, oauth_secret = read_token_file(self.my_twitter_creds)

    return Twitter(auth=OAuth(oauth_token, oauth_secret, self.consumer_key,
      self.consumer_secret))

  def rate_limit_status(self, twitter):
    r = twitter.application.rate_limit_status()
    print r

class TwitterCloner:
  def __init__(self, twitter):
    self.twitter = twitter

  def clone(self):
    pass
