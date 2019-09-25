# coding:utf-8
from urllib.request import urlopen

class HtmlDownloader(object):
    """A HTML DOWNLOAD MACHINE"""
    def __init__(self):
        pass

    def download(self, url):
        """
        GET THE HTML CONTENT WITH A DECODE UTF-8 FROM A URL
        :param url: A URL
        :return: THR CONTENT FROM A URL
        """
        if url is None:
            return
        response = urlopen(url)
        return response.read().decode('UTF-8')
