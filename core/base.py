from abc import ABC, abstractmethod
from enum import Enum


class PageType(Enum):
    HOME = 1
    SEARCH_RESULTS = 2
    POST = 3

    
class PlatformNavigator(ABC):

    @abstractmethod
    def login():
        pass

    @abstractmethod
    def search(self, query):
        pass

    @abstractmethod
    def go_to(self, url):
        pass

    @abstractmethod
    def get_post_content(self):
        pass

    @abstractmethod
    def get_comments(self):
        pass

    @abstractmethod
    def make_comment(self, comment):
        pass

    @abstractmethod
    def scroll_down(self):
        pass