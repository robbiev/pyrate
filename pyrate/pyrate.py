#!/usr/bin/env python
from twitter_access import *

pirate = Pirate()

def run():
  factory = TwitterFactory()
  twitter = factory.create()

  tweets = twitter.statuses.user_timeline()

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
  run_stream() 
