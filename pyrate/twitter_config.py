import ConfigParser

LOCATION = '.pyrate'

class Config:
  def __init__(self, location):
    self.config = ConfigParser.ConfigParser()
    self.location = location

  def read_sections(self):
    self.config.read(self.location)
    return self.config.sections()

  def get_value(self, section, key):
    return self.config.get(section, key)
