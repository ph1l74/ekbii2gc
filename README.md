# What?

ekbii2gc is a tiny script to add special kind of livejournal posts to
specified google calendar

## Why?

Because it's convenient when the computer does all the work for you.

## How?

The principle of script-work is very easy. Firstly, it get the rss-feed.
Then it parse every item in feed and try to find the game-post. When the
game-post will be find the script starts to check the database. If the
game-id already in database the even won't be create. In the other case
the even will be created with the game information.

## Files

- config.py - configuration file
- db.py - database module
- gcalendar.py - Google Calendar module
- LICENSE - LICENSE file
- main.py - main module
- README.md - README file
- requirements.txt - list of libs
- rss.py - rss-feed module

## Requirements

- [feedparser](https://pypi.python.org/pypi/feedparser)
- [google-api-python-client](https://pypi.python.org/pypi/google-api-python-client/)
- [psycopg2](https://pypi.python.org/pypi/psycopg2)


## Contributors

- [Filat Astakhov](mailto:astakhovfilat@gmail.com)


## License

MIT License