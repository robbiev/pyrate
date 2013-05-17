import unittest

from pirate_filter import *
from pyrate import *

user_tweet = u'hello @robbiev'
url_tweet = u'I like http://www.google.com'
class TestTweetPirate(unittest.TestCase):
  def setUp(self):
    self.pirate = TweetPirate(Pirate())

  def test_simple_username_not_in_piratese(self):
    self.assertEqual(user_tweet, self.pirate.generate_tweet(user_tweet))

  def test_username_valid_so_not_replaced(self):
    user = '@w0rD_ing'
    # from the sources of the pirate program
    # any word ending on "ing" followed by another word
    # will always be replaced by "in'"
    tweet = user + ' secondword'
    self.assertEqual(user, self.pirate.generate_tweet(tweet)[:len(user)]) 

  def test_url_not_in_piratese(self):
    self.assertEqual(url_tweet, self.pirate.generate_tweet(url_tweet))

  def test_multiple_urls_and_usernames_not_in_piratese(self):
    tweet = url_tweet + user_tweet + url_tweet + url_tweet + user_tweet
    self.assertEqual(tweet, self.pirate.generate_tweet(tweet))

  def test_simple_sentence_in_piratese(self):
    tweet = u'I like going out with my friends'
    self.assertEqual(u"I like goin' out wi' me maties", self.pirate.generate_tweet(tweet))

  def test_gt_140_truncated(self):
    self.assertEqual(137*u'a' + u'...', self.pirate.generate_tweet(141*u'a'))

  def test_eq_140_not_truncated(self):
    self.assertEqual(140*u'a', self.pirate.generate_tweet(140*u'a'))

  def test_unicode(self):
    self.assertEqual(u'http://\u03AB \u03AB', self.pirate.generate_tweet(u'http://\u03AB \u03AB'))

  def test_pirate_uses_unicode_type(self):
    self.assertTrue(isinstance(Pirate().speak('hello'), unicode))


if __name__ == '__main__':
  unittest.main()
