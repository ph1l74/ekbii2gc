import psycopg2


def open_db(db_config):
    user= db_config["user"]
    password = db_config["password"]
    host = db_config["address"]
    port = db_config["port"]
    dbname = db_config["db_name"]

    connect = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port= port)
    database = connect.cursor()
    return database, connect


def close_db(database, connect):
    database.close()
    connect.close()


def add_event(db_config, event_id):
    database, connect = open_db(db_config)
    SQL = "INSERT INTO games (game_id) VALUES (%s);"
    if database.execute(SQL, (event_id,)):
        print("Event {} created".format(event_id))
        connect.commit()
    else:
        print("Something goes wrong")
    close_db(database, connect)


def check_event(db_config, event_id):
    database, connect = open_db(db_config)
    database.execute("SELECT game_id FROM games")
    games = database.fetchall()
    close_db(database, connect)
    viewed_ids = {res[0] for res in games}
    if event_id not in viewed_ids:
        add_event(db_config, event_id)
        return True
    else:
        return False



