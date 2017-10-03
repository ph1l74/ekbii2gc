"""
This is the main function of my script.
"""
import re
import config
import rss
import db
import telebot
import datetime


bot = telebot.TeleBot(config.bot_token)

now = datetime.datetime.now()
now_date = datetime.time(now.hour, now.minute, now.second)


def convert_date(date_string):
    pattern = re.compile('([\d]{4})-([\d]{2})-([\d]{2}) ([\d]{2}):([\d]{2}):([\d]{2})')
    match = pattern.search(date_string)
    if match:
        year = int(match.group(1))
        month = int(match.group(2))
        day = int(match.group(3))
        hours = int(match.group(4))
        mins = int(match.group(5))
        secs = int(match.group(6))
        date = datetime.datetime(year, month, day, hours, mins, secs)
        return date
    else:
        pass


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
            game_date = game["date"]
            if now < game_date:
                db.add_event(config.db, game_id, game_name, game_date)
            else:
                break


check(10)


@bot.message_handler(commands = ['games'])
def games(message):
    games_list = db.get_events(config.db)
    markup = telebot.types.InlineKeyboardMarkup()
    for games in games_list:
        for game_el in games:
            game = db.get_event_info(config.db, game_el)
            button = telebot.types.InlineKeyboardButton(text=game["name"], callback_data=str(game["id"]))
            markup.add(button)
    bot.send_message(message.chat.id, 'Игры:', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_data(call):
    if call.message:
        game_id = call.data
        game = db.get_event_info(config.db, game_id)
        bot.send_message(call.message.chat.id, text="{}\n{}\n{}".format(game["name"], game["date"], game["url"]))


if __name__ == '__main__':
    bot.polling(none_stop=True)
