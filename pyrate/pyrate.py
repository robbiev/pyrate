#!/usr/bin/env python
import re
from twitter_access import *

pirate = Pirate()
PLACE_HOLDER = 140 * '%'

def place_holders(count):
  for i in range(0, count):
    yield PLACE_HOLDER + str(i)

# myString = 
def parse_tweet(text):
  urls = re.findall(r'(https?://[^\s]+)', text)
  users = re.findall(r'@[a-zA-Z\-_]+', text)
  total = set(urls + users)
  replacements = dict(zip(place_holders(len(total)), total))

  for key, value in replacements.items():
    text = re.sub(value, key, text)

  print text

  print replacements

def run():
  factory = TwitterFactory()
  twitter = factory.create()

  tweets = twitter.statuses.user_timeline(include_rts=True)

  for t in tweets:
    print pirate.speak(t['text'])

def run_stream():
  factory = TwitterFactory()
  streamer = factory.create_stream()
  tweets = streamer.statuses.sample()
  for t in tweets:
    if t.get('text'):
      print pirate.speak(t['text'])

if __name__ == "__main__":
  parse_tweet("This is my tweet for @robbiev check it out http://tinyurl.com/blah")
