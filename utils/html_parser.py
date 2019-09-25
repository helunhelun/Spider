#coding:utf-8
import re
from urllib.parse import urljoin
from bs4 import BeautifulSoup

class HtmlParser(object):
    """kernel code --HtmlParser"""
    def __init__(self, root_url):
        self.root_url = root_url
        pass


    def parser(self, page_url, html_cont):
        """
        A PAGE PARSER
        :param page_url: CURRENT PAGE URL
        :param html_cont: CONTENT IN CURRENT PAGE
        :return: ALL NEW LINKS AND THE DATA IN THIS PAGE
        """
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return  new_urls, new_data

    def _get_new_urls(self, page_url, soup):
        """
        GET ALL LINKS IN THIS PAGE
        :param page_url: CURRENT PAGE
        :param soup: A BeautifulSoup OBJECT
        :return: ALL NEW LINKS IN THIS PAGE
        """
        new_urls = set()
        links  = soup.find_all('a', href=re.compile(r'/item/.*'))
        for link in links:
            new_url = link['href']
            new_full_url = urljoin(self.root_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        """
        GET NEW DATA IN CURRENT PAGE
        :param page_url: CURRENT PAGE
        :param soup: A BeautifulSoup OBJECT
        :return: THE NEW DATA IN THIS PAGE
        """
        res_data = {}
        res_data['url'] = page_url
        #<dd class="lemmaWgt-lemmaTitle-title"><h1>百度百科</h1>
        title_node = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        res_data['title'] = title_node.get_text()

        #<div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div', class_='lemma-summary')
        res_data['summary'] = summary_node.get_text()
        # RETURN
        return res_data



