#!/usr/bin/env python
import re
from twitter_access import *

TWEET_CHARS = 140
TWEET_TRUNCATE = u'...'

# anything longer than 140 can be used as a safe placeholder
PLACE_HOLDER = TWEET_CHARS * u'%'

'''
Tweet pirate handles not converting
links and user names to piratese
'''
class TweetPirate:
  def __init__(self, pirate):
    self.pirate = pirate

  def place_holders(self, count):
    for i in range(0, count):
      yield PLACE_HOLDER + str(i)

  def to_pirate(self, text, replacements):
    pirate_input = text 
    for key, value in replacements.items():
      pirate_input = re.sub(value, key, pirate_input)

    pirate_output = self.pirate.speak(pirate_input)
    for key, value in replacements.items():
      pirate_output = re.sub(key, value, pirate_output)

    return pirate_output

  def generate_tweet(self, text):
    replacements = self.find_snippets_to_replace_in_tweet(text)
    piratese = self.to_pirate(text, replacements)
    return piratese if len(piratese) <= TWEET_CHARS else piratese[:TWEET_CHARS - len(TWEET_TRUNCATE)]+TWEET_TRUNCATE

  # no piratese for user names and URLs
  def find_snippets_to_replace_in_tweet(self, text):
    urls = re.findall(r'(https?://[^\s]+)', text)
    users = re.findall(r'@[a-zA-Z\-_]+', text)
    total = set(urls + users)
    replacements = dict(zip(self.place_holders(len(total)), total))
    return replacements

def process_tweet(pirate, twitter, t):
  if t.get('text'):
    tweet = t['text'] 
    retweet_count = t['retweet_count']
    reply = t['in_reply_to_user_id']
    print 'TWEET   ' + tweet

    if retweet_count is 0 and reply is None:
      tweet = pirate.generate_tweet(t['text'])
      print 'PIRATE  ' + tweet
      twitter.statuses.update(status=tweet)

def run_stream():
  config = TwitterAppConfig().get_app_config()
  factory = TwitterFactory(config)
  twitter = factory.create()
  streamer = factory.create_stream()
  tweets = streamer.statuses.filter(follow=config.clone)
  pirate = TweetPirate(Pirate())

  print 'Following %s' % config.clone

  for t in tweets:
    process_tweet(pirate, twitter, t)

if __name__ == '__main__':
  run_stream()
