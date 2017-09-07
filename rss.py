"""
This module works with rss-feed. The main function is 'check_for_game' that parse RSS-feed and return the game info.
"""
import feedparser
import re
from datetime import datetime, date


def clear_tags(raw_text):
    """
    This function returns text without html/xml tags
    :param raw_text: raw html/xml text
    :type raw_text: str
    :return: string-text without tags
    :rtype: str
    """
    pattern = re.compile('<.*?>')
    text = raw_text.replace('<br />', '\n')
    text = text.replace('&quot;', '"')
    text = re.sub(pattern, '', text)
    return text


def convert_date(text_date):
    """
    This function convert date from text format to datetime-format
    :param text_date: date in text-format
    :type text_date: str
    :return: date in datetime-format
    :rtype: datetime
    """
    days = {'январ': 1,
            'феврал': 2,
            'март': 3,
            'апрел': 4,
            'ма': 5,
            'июн': 6,
            'июл': 7,
            'август': 8,
            'сентябр': 9,
            'октябр': 10,
            'ноябр': 11,
            'декабр': 12}
    pattern = re.compile('(.*?)[, ]([\d]{1,2}) (.*?), ([\d]{1,2})[-:]([\d]{1,2})')
    match = pattern.search(text_date)
    if match:
        day = int(match.group(2))
        month = match.group(3)
        hours = int(match.group(4))
        mins = int(match.group(5))
        year = date.today().year
        for key in days:
            if key in month:
                month = days[key]
                event_date = datetime(year, month, day, hours, mins)
                return event_date


def get_id(url):
    """
    This function pop postID from text-url
    :param url: url in text-format
    :type url: str
    :return: postID
    :rtype: int
    """
    pattern = re.compile('(\d*).html')
    match = pattern.search(url)
    if match:
        post_id = int(match.group(1))
        return post_id


def get_feed_items(feed_url):
    """
        This function parse the rss-feed and return the dict with feed-items.
        :param feed_url: URL of RSS-feed in string-format
        :type feed_url: str
        :return: Dict with items
        :rtype: dict
        """
    feed_data = feedparser.parse(feed_url)
    items = feed_data["items"]
    return items


def check_for_game(items, number=0):
    """
    This function take the dict with feed-items and returns the dict with game info.
    :param items: dict of feed-items
    :param number: (Optional) number of items to parse. Default = 0.
    :type items: dict
    :type number: int
    :return: Dict with game info ("name", "date", "text", "id").
    :rtype: dict
    """
    game = {"name": '',
            "date": '',
            "text": '',
            "id": ''}
    pattern_what = re.compile('Что: (.*).')
    pattern_when = re.compile('Когда: (.*).')
    item_body = items[number].summary_detail.value
    item_text = clear_tags(item_body)
    match_what = pattern_what.search(item_text)
    if match_what:
        game["name"] = match_what.group(1)
        game["name"] = game["name"][0].upper() + game["name"][1:]
    match_when = pattern_when.search(item_text)
    if match_when:
        game["date"] = convert_date(match_when.group(1))
    if get_id(items[number]['link']):
        game["id"] = get_id(items[number]['link'])
    if game["name"] and game["date"] and game["id"]:
        game["text"] = item_text
        return game
