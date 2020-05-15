import logging
import sqlite3
from typing import List, Tuple

from feed import Feed


class DatabaseConnection:

    def __init__(self):
        self.DB_NAME = 'revma.db'
        self.FEED_TABLE_NAME = 'feeds'

        try:
            self.conn = sqlite3.connect(self.DB_NAME)
        except sqlite3.Error as e:
            logging.error(f'Failed to connect to database: {str(e)}')

    def create_database(self):
        try:
            create_feeds_table_query = f'CREATE TABLE {self.FEED_TABLE_NAME} ' \
                                       f'(id INTEGER PRIMARY KEY, ' \
                                       f'title TEXT NOT NULL, ' \
                                       f'link TEXT NOT NULL, ' \
                                       f'description TEXT NOT NULL' \
                                       f'second INTEGER);'

            cursor = self.conn.cursor()
            cursor.execute(create_feeds_table_query)
            self.conn.commit()

            cursor.close()
        except sqlite3.Error as e:
            logging.error(f'Error while creating feeds table: {str(e)}')

    def add_feed(self, feed: Feed):
        try:
            cursor = self.conn.cursor()

            add_feed_query = f'INSERT INTO {self.FEED_TABLE_NAME}(title, link, description) VALUES (?, ?, ?);'

            data_tuple = (feed.title, feed.link, feed.description)
            cursor.execute(add_feed_query, data_tuple)
            self.conn.commit()
            logging.info('Added feed to database')
            cursor.close()

        except sqlite3.Error as e:
            logging.error(f'Failed to add feed to database: {str(e)}')

    def set_feed_time(self, feed_id: int, seconds: int) -> None:
        try:
            cursor = self.conn.cursor()

            set_feed_time = f'UPDATE {self.FEED_TABLE_NAME} SET seconds = {seconds} WHERE id={feed_id};'
            cursor.execute(set_feed_time)
            self.conn.commit()
            cursor.close()

        except sqlite3.Error as e:
            logging.error(f'Failed set time to feed {feed_id}: {str(e)}')

    def get_all_feeds(self) -> List[Tuple]:
        feeds: List[Tuple] = []
        try:
            cursor = self.conn.cursor()
            get_feeds_query = f'SELECT * FROM {self.FEED_TABLE_NAME};'
            cursor.execute(get_feeds_query)
            rows = cursor.fetchall()
            for row in rows:
                feeds.append(row)
            cursor.close()
        except sqlite3.Error as e:
            logging.error(f'Failed get feeds: {str(e)}')
        finally:
            return feeds
