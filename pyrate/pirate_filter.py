#!/usr/bin/env python
import sys
import subprocess

class Pirate:
  def speak(self, english):
    translater = subprocess.Popen('pirate', stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    translater.stdin.write(english.encode('utf8')+'\n')
    piratese, _ = translater.communicate()
    return piratese[:-1].decode('utf-8')

if __name__ == '__main__':
  print Pirate().speak(' '.join(sys.argv[1:]))
