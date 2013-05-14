import os
import time
import ConfigParser

from twitter import *

class TwitterFactory:
  def __init__(self, config):
    self.config = config 
    self.my_twitter_creds = os.path.expanduser('~/.pyrate_credentials')

  def oauth(self):
    if not os.path.exists(self.my_twitter_creds):
      oauth_dance('pyrate', self.config.consumer_key, self.config.consumer_secret, self.my_twitter_creds)

    oauth_token, oauth_secret = read_token_file(self.my_twitter_creds)
    return OAuth(oauth_token, oauth_secret, self.config.consumer_key, self.config.consumer_secret)

  def create(self):
    return Twitter(auth=self.oauth())

  def create_stream(self):
    return TwitterStream(auth=self.oauth())

class TwitterAppConfig:
  location = os.path.join(os.environ['HOME'], '.pyrate')
  def __init__(self):
    self.config = ConfigParser.ConfigParser() 

  def get_app_config(self):
    self.config.read(TwitterAppConfig.location)
    sections = self.config.sections()

    configuration = Configuration()

    app_section = 'App'
    configuration.consumer_key = self.config.get(app_section, 'consumer_key')
    configuration.consumer_secret = self.config.get(app_section, 'consumer_secret')
    configuration.clone = self.config.get('Pirate', 'clone')
    return configuration

class Configuration: pass
