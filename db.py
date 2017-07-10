import redis


def create():
    database = redis.StrictRedis(host='localhost', port=6379, db=0)
    return database


def check_event(database, event_id):
    event_db = database.get('events')
    if event_id not in event_db:
        event_db.set('events', event_id)
        return True
    else:
        return False
