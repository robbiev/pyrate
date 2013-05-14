from speech import *
from pyrate import *
import unittest

class TestTweetPirate(unittest.TestCase):
    def setUp(self):
      self.pirate = TweetPirate(Pirate())

    def test_username_not_in_piratese(self):
      self.assertEqual('hello @robbiev', self.pirate.generate_tweet('hello @robbiev'))

    def test_gt_140_truncated(self):
      self.assertEqual(137*'a' + '...', self.pirate.generate_tweet(141*'a'))

    def test_eq_140_not_truncated(self):
      self.assertEqual(140*'a', self.pirate.generate_tweet(140*'a'))

if __name__ == '__main__':
    unittest.main()
