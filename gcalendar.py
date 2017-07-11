"""
This module works with Google-API. The main function is 'make_event' that create an event in Google Calendar with
game information.
"""

import httplib2
from datetime import datetime, timedelta
from apiclient import discovery
from oauth2client import file, client, tools
import os


def get_flags():
    """
    This function get the flags for Google-API
    :return: list of flags
    :rtype: list
    """
    try:
        import argparse
        flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
    except ImportError:
        flags = None
    return flags


def get_credentials():
    """
    This function returns the user credentials for Google-API
    :return: flow-object
    :rtype: object
    """
    auth_url = 'https://www.googleapis.com/auth/calendar'
    token_filename = 'client_secret.json'
    app_name = 'ekbii2gcalendar'
    flags = get_flags()
    credential_dir = os.path.join('', '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir, 'calendar-python-quickstart.json')
    store = file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(token_filename, auth_url)
        flow.user_agent = app_name
        if flags:
            credentials = tools.run_flow(flow, store, flags)
    return credentials


def make_event(game, calendar_id):
    """
    This function make a new event in Google Calendar
    :param game: dict with game info
    :param calendar_id: calendar-ID
    :type game: dict
    :type calendar_id: str
    """
    name = game["name"]
    description = game["text"]
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)
    date_start = game["date"]
    date_end = date_start + timedelta(hours=2)
    date_start = date_start.isoformat()
    date_end = date_end.isoformat()
    event_data = {
        "summary": name,
        "description": description,
        "start": {"dateTime": date_start, "timeZone": "Asia/Yekaterinburg"},
        "end": {"dateTime": date_end, "timeZone": "Asia/Yekaterinburg"},
    }
    event = service.events().insert(calendarId=calendar_id, body=event_data).execute()
    print("Event created: {}".format(event.get('htmlLink')))
