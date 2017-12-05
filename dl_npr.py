#!/usr/bin/env python
import subprocess
import feedparser
import alsaaudio


def dl_npr(ramdrive='/mnt/ram/'):
      rss_url = 'http://www.npr.org/rss/podcast.php?id=500005'
      rss = feedparser.parse(rss_url)
      rval = True

      media_url = rss.entries[0].links[0].href
      head = 'wget -q -U Mozilla'
      st = head + ' -O ' + ramdrive + 'npr.mp3 ' + media_url
      m = alsaaudio.Mixer(alsaaudio.mixers[0]) # alsaaudio.mixers = ["PCM"] for me.
      print alsaaudio.mixers
      print m.getvolume()
      m.setvolume(80, 'MIXER_CHANNEL_ALL') # Or whatever
      print m.getvolume()
      print subprocess.call (st, shell=True)