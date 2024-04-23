from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time, random
from base import PlatformNavigator, PageType
from exceptions import WrongPage

class YoutubeNavigator(PlatformNavigator):

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.current_page = PageType.HOME
        self.go_home()
    
    def go_home(self):
        self.driver.get('https://www.youtube.com')
        self.current_page = PageType.HOME

    def go_to(self, url:str, page:PageType):
        self.driver.get(url)
        self.current_page = page

    def search(self, query):
        search_bar = self.driver.find_element(By.XPATH, '//*[@id="search"]')
        search_bar.send_keys(query)
        search_bar.submit()
        self.current_page = PageType.SEARCH_RESULTS

    def get_search_results(self):
        if self.current_page != PageType.SEARCH_RESULTS:
            raise WrongPage('Not on search results page')
        
        search_results = self.driver.find_element(By.XPATH, '//*[@id="contents"]')
        search_results_html = search_results.get_attribute('innerHTML')
        soup = BeautifulSoup(search_results_html, 'html.parser')
        
        # Create a dictionary of title and link pairs
        results = {}
        for video in soup.find_all('a', {'id': 'video-title'}):
            title = video.get('title')
            link = video.get('href')
            results[title] = link

        return results

    def get_comments(self):
        self.scroll_down()

        comments_section = self.driver.find_element_by_xpath('//*[@id="comments"]')
        comments_html = comments_section.get_attribute('innerHTML')
        soup = BeautifulSoup(comments_html, 'html.parser')

        comments = []
        for comment in soup.find_all('yt-formatted-string', {'id': 'content-text'}):
            comments.append(comment.text)

        return comments

    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, 1000);")
        time.sleep(random.randint(1, 3))

    def make_comment(self, comment):
        pass

    def login(self):
        pass
    