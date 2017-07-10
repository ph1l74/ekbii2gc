import config
import rss
import gcalendar
import db


database = db.open_db(config.db)


def check_ya_neck():
    for i in range(0, 21):
        game = rss.check_for_game(config.feed_url, i)
        if game:
            game_id = game["id"]
            if db.check_event(database, game_id):
                #gcalendar.make_event(game, config.calendar_id, config.token)
                print ('Event created')
            else:
                print('Event "{}" already in calendar'.format(game_id))
                break


db.check_event(database, 1)