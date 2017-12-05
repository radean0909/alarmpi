#!/usr/bin/env python
import subprocess
import feedparser

from apcontent import alarmpi_content

class npr(alarmpi_content):
  def build(self, ramdrive='/mnt/ram/'):
    try:
      rss_url = 'http://www.npr.org/rss/podcast.php?id=' + str(self.sconfig['podcast'])
      rss = feedparser.parse(rss_url)
      rval = True

      media_url = rss.entries[0].links[0].href
      print(media_url)
      head = self.sconfig['head']
      tail = self.sconfig['tail']
      st = head + ' ' + media_url
      print(st)
      print subprocess.call (st, shell=True)
      play = self.sconfig['player'] + ' ' + ramdrive + '*' + tail
    except rss.bozo:
      news = 'Failed to reach NPR News'
      rval = False

    print subprocess.call (play, shell=True)

    rmcmd = 'rm -f ' + ramdrive + '*.' + tail
    if self.debug:
      print 'cleaning up now'
      print rmcmd
    print subprocess.call (rmcmd, shell=True)
    return rval

if __name__ == '__main__':
  rss_url = 'http://www.npr.org/rss/podcast.php?id=500005'
  rss = feedparser.parse(rss_url)

  print rss.entries[0].links[0].href

