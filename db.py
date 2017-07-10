import redis


def create():
    database = redis.StrictRedis(host='localhost', port=6379, db=0)
    return database


def check_event(database, even_name):
    event_db = database.get('events')
    if even_name not in event_db:
        event_db.set('events', even_name)
        return True
    else:
        return False
