import config
import rss
import gcalendar
import db

database = db.create()


def check_ya_neck():
    for i in range(0, 16):
        game = rss.check_for_game(config.feed_url, i)
        if game:
            name = game["name"]
            if db.check_event(database, name):
                gcalendar.make_event(game, config.calendar_id, config.token)
            else:
                print('Event already in calendar')
