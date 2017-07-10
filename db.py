import psycopg2


def open_db(db_config):
    user= db_config["user"]
    password = db_config["password"]
    host = db_config["address"]
    port = db_config["port"]
    dbname = db_config["db_name"]

    connect = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port= port)
    database = connect.cursor()
    return database


def add_event(database, event_id):
    database.execute("INSERT INTO games (game_id) VALUES (%s)", (event_id,))


def check_event(database, event_id):
    database.execute("SELECT game_id FROM games")
    games = database.fetchall()
    viewed_ids = {res[0] for res in games}
    if event_id not in viewed_ids:
        add_event(database, event_id)
        print('Event {} added'.format(event_id))
        return True
    else:
        print('Event {} already in list'.format(event_id))
        return False
