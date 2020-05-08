from database import DatabaseConnection
from feed import Feed

feed = Feed('http://podcasts.joerogan.net/feed')

database_conn = DatabaseConnection()
database_conn.create_database()
database_conn.add_feed(feed)

