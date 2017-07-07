import requests
import httplib2
from datetime import datetime
from apiclient import discovery
from oauth2client import file, client, tools
import os

def iso_date(date):
    year = 2017
    month = date[0]
    day = date[1]
    hours = date[2]
    mins = date[3]
    date = datetime(year, month, day, hours, mins).isoformat()
    date += 'Z'
    return date


def add_2_hours(date):
    datelist = list(date)
    datelist[2] += 2
    result = tuple(datelist)

    return result


def get_flags():
    try:
        import argparse
        flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
    except ImportError:
        flags = None
    return flags


def get_credentials():

    auth_url = 'https://www.googleapis.com/auth/calendar'
    token_filename = 'secret_token.json'
    app_name = 'ekbii2gcalendar'

    flags = get_flags()
    credential_path = os.path.join('', token_filename)
    store = file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(token_filename, auth_url)
        flow.user_agent = app_name
        if flags:
            credentials = tools.run_flow(flow, store, flags)
    return credentials


def make_event(game, calendar_id, token):

    name = game["name"]
    date = game["date"]
    description = game["text"]
    calendar_url = 'https://www.googleapis.com/calendar/v3/' \
                   'calendars/{calendar_id}/events?access_token={token}'.format(calendar_id=calendar_id, token=token)

    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('Мантисса', 'v3', http=http)

    date_start = iso_date(date)
    new_date = add_2_hours(date)
    date_end = iso_date(new_date)

    event_data = {
        "summary": name,
        "description": description,
        "start": {"dateTime": date_start},
        "end": {"dateTime": date_end},
    }

    event = service.events().insert(calendarId='primary', body=event_data).execute()
    return "Event created: {}".format(event.get('htmlLink'))
