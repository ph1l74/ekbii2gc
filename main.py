"""
This is the main function of my script.
"""
import config
import rss
import gcalendar
import db


def check(count=1):
    """
    This is the main function
    :param count: (Optional) count of RSS-items to parse. Default=1.
    :type count: int
    :return: Parse RSS, check if game, if so then check if it in db, then if it not, create and Google Calendar
    event anb add it to db.
    """
    for i in range(0, count):
        game = rss.check_for_game(config.feed_url, i)
        if game:
            game_id = game["id"]
            game_name = game["name"]
            if db.check_event(config.db, game_id):
                gcalendar.make_event(game, config.calendar_id)
            else:
                print('Event "{}" already in calendar'.format(game_name))
                break

check()
