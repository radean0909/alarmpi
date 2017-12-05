#!/usr/bin/env python

import feedparser

from apcontent import alarmpi_content

class npr(alarmpi_content):
  def build(self):
    try:
      rss_url = 'http://www.npr.org/rss/podcast.php?id=' + str(self.sconfig['podcast'])
      rss = feedparser.parse(rss_url)

      print rss

      #for entry in rss.entries[:4]:
      #    print entry['title']
      #    print entry['description']
      #
      #print rss.entries[0]['title']
      #print rss.entries[0]['description']
      #print rss.entries[1]['title']
      #print rss.entries[1]['description']
      #print rss.entries[2]['title']
      #print rss.entries[2]['description']
      #print rss.entries[3]['title']
      #print rss.entries[3]['description']


    except rss.bozo:
      news = 'Failed to reach BBC News'

    if self.debug:
      print news

    self.content = news
