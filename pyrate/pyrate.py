#!/usr/bin/env python
from twitter_access import *

def run():
  api = TwitterApi()
  twitter = api.create()
  tweets = twitter.statuses.user_timeline()
  pirate = Pirate()
  for t in tweets:
    print pirate.speak(t['text'])

if __name__ == "__main__":
  run() 
