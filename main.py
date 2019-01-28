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
    """
    for i in range(0, count):
        game = rss.check_for_game(config.feed_url, i)
        if game:
            game_id = game["id"]
            game_name = game["name"]
            print("parsed feed: {}".format(game_id, game_name))
            if db.check_event(config.db, game_id):
                gcalendar.make_event(game, config.calendar_id)
                db.add_event(config.db, game_id)
            else:
                print('Event "{}" already in calendar'.format(game_name))
                break

check()
