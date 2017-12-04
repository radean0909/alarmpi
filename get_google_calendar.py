#!/bin/python
# -*- coding: utf-8 -*-
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from apcontent import alarmpi_content

import datetime

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

class google_calendar(alarmpi_content):
  def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'alarmpi-calendar-service.json')

    store = Storage(credential_path)

    credentials = store.get()
    print credentials
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store, noauth_local_webserver=True)
        print('Storing credentials to ' + credential_path)
    return credentials

  def build(self):
    """Shows basic usage of the Google Calendar API.

    Creates a Google Calendar API service object and outputs a list of the next
    10 events on the user's calendar.
    """
    try:
      credentials = get_credentials()
    except Exception:
      print('Error authenticating')
      print Exception

    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)
    print('service loaded')
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    eod = (datetime.datetime(
        year=datetime.datetime.utcnow().year,
        month=datetime.datetime.utcnow().month,
        day=datetime.datetime.utcnow().day
    ) + datetime.timedelta(hours=24, microseconds=-1)).isoformat() + 'Z'
    print('Getting the upcoming 10 events')
    eventsResult = service.events().list(
        calendarId='primary', timeMin=now, maxResults=10, singleEvents=True,
        orderBy='startTime').execute()
    events = eventsResult.get('items', [])

    if not events:
        message = 'Lucky you, nothing scheduled today.'
    else:
        message = 'You have ' + len(events) + ' meetings scheduled today.'
    print(message)
    self.content = message
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])
