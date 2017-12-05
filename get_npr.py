#!/usr/bin/env python
import subprocess
import feedparser

from apcontent import alarmpi_content

class npr(alarmpi_content):
  def begin(self):
    pass

  def end(self, ramdrive='/mnt/ram/'):

    play = self.sconfig['player'] + ' ' + ramdrive + 'npr.mp3'
    print subprocess.call (play, shell=True)
    return rval

if __name__ == '__main__':
  rss_url = 'http://www.npr.org/rss/podcast.php?id=500005'
  rss = feedparser.parse(rss_url)

  print rss.entries[0].links[0].href

