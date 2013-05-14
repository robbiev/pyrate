from twitter_access import *
import unittest

class TestTwitterAccess(unittest.TestCase):
  def setUp(self):
    self.config = TwitterAppConfig() 

  def test_read_config(self):
    a, b = self.config.get_app_config()
    print a

if __name__ == '__main__':
  unittest.main()
