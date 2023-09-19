import requests
from bs4 import BeautifulSoup


class Scrapper:
    def __init__(self):
        self.data = []

    def scrap(self, url):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")

        for data in soup(['style', 'script']):
            # Remove tags
            data.decompose()

            # return data by retrieving the tag content
        return ' '.join(soup.stripped_strings)
