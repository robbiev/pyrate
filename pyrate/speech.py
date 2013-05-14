#!/usr/bin/env python
import sys
import subprocess

class Pyrate:
  def speak(english):
    translater = subprocess.Popen('pirate', stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    translater.stdin.write(english.encode("utf8")+"\n")
    piratese, _ = translater.communicate()
    return piratese[:-1]

if __name__ == "__main__":
  print Pyrate().speak(' '.join(sys.argv[1:]))
