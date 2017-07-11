import config
import rss
import gcalendar
import db


def check_ya_neck():
    for i in range(0, 21):
        game = rss.check_for_game(config.feed_url, i)
        if game:
            game_id = game["id"]
            game_name = game["name"]
            if db.check_event(config.db, game_id):
                gcalendar.make_event(game, config.calendar_id, config.token)
            else:
                print('Event "{}" already in calendar'.format(game_name))
                #break


check_ya_neck()
