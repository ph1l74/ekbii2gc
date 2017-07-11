import feedparser
import re


def clear_tags(raw_text):
    pattern = re.compile('<.*?>')
    text = raw_text.replace('<br />', '\n')
    text = text.replace('&quot;', '"')
    text = re.sub(pattern, '', text)

    return text


def convert_date(text):

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

    pattern = re.compile('(.*?), ([\d]{2}) (.*?), ([\d]{2})-([\d]{2})')
    match = pattern.search(text)
    if match:
        day = int(match.group(2))
        month = match.group(3)
        hours = int(match.group(4))
        mins = int(match.group(5))
        for key in days:
            if key in month:
                month = days[key]
                return month, day, hours, mins
    else:
        return False


def get_id(url):
    pattern = re.compile('com\/(.*?).html')
    match = pattern.search(url)
    if match:
        post_id = int(match.group(1))
        return post_id
    else:
        return False


def check_for_game(feed_url, number=0):
    game = {"name": '',
            "date": '',
            "text": '',
            "id": ''}

    pattern_what = re.compile('Что: (.*).')
    pattern_when = re.compile('Когда: (.*).')

    feed_data = feedparser.parse(feed_url)
    items = feed_data["items"]
    game["id"] = get_id(items[number]['link'])

    item_body = items[number].summary_detail.value
    item_text = clear_tags(item_body)

    match_what = pattern_what.search(item_text)
    if match_what:
        game["name"] = match_what.group(1)
        game["name"] = game["name"][0].upper() + game["name"][1:]

    match_when = pattern_when.search(item_text)
    if match_when:
        game["date"] = convert_date(match_when.group(1))

    if game["name"] and game["date"]:
        game["text"] = item_text
        return game
    else:
        return False
