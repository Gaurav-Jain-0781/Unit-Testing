import requests


class PageRequester:
    def __init__(self, url):
        self.url = url

    def get(self):
        url = self.url
        return requests.get(url).content

    
