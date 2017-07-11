import psycopg2


def open_db(db_config):
    user = db_config["user"]
    password = db_config["password"]
    host = db_config["address"]
    port = db_config["port"]
    db_name = db_config["db_name"]
    connect = psycopg2.connect(dbname=db_name, user=user, password=password, host=host, port=port)
    database = connect.cursor()
    return database, connect


def close_db(database, connect):
    database.close()
    connect.close()


def add_event(db_config, event_id):
    database, connect = open_db(db_config)
    database.execute("INSERT INTO games (game_id) VALUES (%s);", (event_id,))
    connect.commit()
    close_db(database, connect)
    print("Event {} added to database".format(event_id))


def check_event(db_config, event_id):
    database, connect = open_db(db_config)
    database.execute("SELECT * FROM games WHERE game_id = %s;", (event_id,))
    viewed = database.fetchall()
    close_db(database, connect)
    if not viewed:
        add_event(db_config, event_id)
        return True
    else:
        return False
