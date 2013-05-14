#!/usr/bin/env python
import re
from twitter_access import *

# anything longer than 140 can be used as a safe placeholder
PLACE_HOLDER = 140 * '%'

"""
Tweet pirate handles not converting
links and user names to piratese
"""
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
    replacements = self.parse_tweet(text)
    return self.to_pirate(text, replacements)

  def parse_tweet(self, text):
    urls = re.findall(r'(https?://[^\s]+)', text)
    users = re.findall(r'@[a-zA-Z\-_]+', text)
    total = set(urls + users)
    replacements = dict(zip(self.place_holders(len(total)), total))
    return replacements


def run():
  factory = TwitterFactory()
  twitter = factory.create()

  tweets = twitter.statuses.user_timeline(include_rts=False)

  pirate = TweetPirate(Pirate())

  for t in tweets:
    print pirate.generate_tweet(t['text'])

def run_stream():
  factory = TwitterFactory()
  streamer = factory.create_stream()
  tweets = streamer.statuses.sample()
  pirate = Pirate()
  for t in tweets:
    if t.get('text'):
      print pirate.speak(t['text'])

if __name__ == "__main__":
  run()
