from speech import *
from pyrate import *
import unittest

class TestTweetPirate(unittest.TestCase):
    def setUp(self):
      self.pirate = TweetPirate(Pirate())

    def test_username_not_in_piratese(self):
      self.assertEqual('hello @robbiev', self.pirate.generate_tweet('hello @robbiev'))

if __name__ == '__main__':
    unittest.main()
