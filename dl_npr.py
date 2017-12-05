#!/usr/bin/env python
import subprocess
import feedparser

def dl_npr(ramdrive='/mnt/ram/'):
      rss_url = 'http://www.npr.org/rss/podcast.php?id=500005'
      rss = feedparser.parse(rss_url)
      rval = True

      media_url = rss.entries[0].links[0].href
      print(media_url)
      head = 'wget -q -U Mozilla'
      st = head + ' -O ' + ramdrive + 'npr.mp3 ' + media_url
      print(st)
      print subprocess.call (st, shell=True)