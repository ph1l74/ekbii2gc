import feedparser
import re


def clear_tags(raw_text):
    pattern = re.compile('<.*?>')
    text = raw_text.replace('<br />', '\n')
    text = text.replace('&quot;', '"')
    text = re.sub(pattern, '', text)

    return text


def check_for_game(feed_url, number=0):
    game = {"name" : '',
            "date" : ''}

    pattern_what = re.compile('Что: (.*)')
    pattern_when = re.compile('Когда: (.*)')

    feed_data = feedparser.parse(feed_url)
    items = feed_data["items"]

    item_body = items[number].summary_detail.value
    item_text = clear_tags(item_body)

    match_what = pattern_what.search(item_text)
    if match_what:
        game["name"] = match_what.group(1)

    match_when = pattern_when.search(item_text)
    if match_when:
        game["date"] = match_when.group(1)

    if game["name"] and game["date"]:
        return game
    else:
        return "It's not a game-post"
