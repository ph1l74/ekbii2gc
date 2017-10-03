"""
This module works with PostgreSQL and check if event in DB or not.
"""

import psycopg2


def open_db(db_config):
    """
    This function open posgresql-session with db-config
    :param db_config: dict of db-parameters
    :type db_config: dict
    :return: 2 objects - connect-object and cursor-object
    :rtype: object
    """
    user = db_config["user"]
    password = db_config["password"]
    host = db_config["address"]
    port = db_config["port"]
    db_name = db_config["db_name"]
    connect = psycopg2.connect(dbname=db_name, user=user, password=password, host=host, port=port)
    cursor = connect.cursor()
    return cursor, connect


def close_db(cursor, connect):
    """
    This function close the connection to db
    :param database: database-object
    :param connect: connection-object
    :type database: object
    :type connect: object
    """
    cursor.close()
    connect.close()


def add_event(db_config, event_id, event_name, event_date):
    """
    This function add an event to db.
    :param db_config: db config dict
    :param event_id: event id to add
    :type db_config: dict
    :type event_id: int
    """
    cursor, connect = open_db(db_config)
    cursor.execute("INSERT INTO games (game_id, game_name, game_date) VALUES (%s, %s, %s);", (event_id, event_name, event_date,))
    connect.commit()
    close_db(cursor, connect)
    print("Event {} added to database".format(event_id))


def check_event(db_config, event_id):
    """
    This function check if event with event_id is in the db.
    :param db_config: db config dict
    :param event_id: event id to check
    :type db_config: dict
    :type event_id: int
    :return: If event in db: False, if not: True
    :rtype: bool
    """
    cursor, connect = open_db(db_config)
    cursor.execute("SELECT * FROM games WHERE game_id = %s;", (event_id,))
    viewed = cursor.fetchall()
    close_db(cursor, connect)
    if not viewed:
        return True
    else:
        return False


def get_events(db_config):
    cursor, connect = open_db(db_config)
    cursor.execute("SELECT game_id FROM games;")
    games_list = cursor.fetchall()
    close_db(cursor, connect)
    return games_list


def get_event_info(db_config, event_id):
    game = {"name": '',
            "date": '',
            "text": '',
            "id": '',
            "url": ''}

    cursor, connect = open_db(db_config)
    cursor.execute("SELECT * FROM games WHERE game_id = %s", (event_id,))
    game_raw = cursor.fetchone()
    game["id"] = game_raw[0]
    game["date"] = game_raw[1]
    game["name"] = game_raw[2]
    game["url"] = 'https://ekbii.livejournal.com/{}.html'.format(game["id"])
    close_db(cursor, connect)
    return game


