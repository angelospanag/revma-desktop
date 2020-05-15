import sys

from PySide2.QtWidgets import QApplication, QDialog, QWidget, QPushButton, QVBoxLayout

from database import DatabaseConnection
from feed import Feed


class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setWindowTitle("Revma")


if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)

    database_conn = DatabaseConnection()
    database_conn.create_database()
    # feed = Feed('http://podcasts.joerogan.net/feed')
    # database_conn.add_feed(feed)

    feeds_db = database_conn.get_all_feeds()
    window = QWidget()
    layout = QVBoxLayout()
    for feed_db in feeds_db:
        feed = Feed(feed_db[2])
        for episode in feed.episodes:
            button1 = QPushButton(episode.link)
            layout.addWidget(button1)

    window.setLayout(layout)
    window.show()
    # Run the main Qt loop
    sys.exit(app.exec_())
