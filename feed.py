from typing import List

import feedparser

from podcast import Podcast


class Feed:
    def __init__(self, url: str) -> None:
        self._d = feedparser.parse(url)

        self.title = self._d['feed']['title']
        self.link = self._d['feed']['link']
        self.description = self._d['feed']['description']
        self.podcasts: List[Podcast] = []

        self._parse_items()

    def _parse_items(self):
        for item in self._d.entries:
            self.podcasts.append(Podcast(title=item.title,
                                         link=item.link,
                                         description=item.description))
