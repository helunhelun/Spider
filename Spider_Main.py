# coding:utf-8

from utils import html_download, html_outputer, html_parser, url_manager

root_url = "https://baike.baidu.com/"
start_url = "https://baike.baidu.com/item/Python/407313"

class SpiderMain(object):
    """Entrance to spider"""

    def __init__(self, root_url):
        self.count = 1
        self.root_url = root_url
        self.downloader = html_download.HtmlDownloader()
        self.outputer = html_outputer.HtmlOutputer()
        self.parser = html_parser.HtmlParser(root_url=self.root_url)
        self.urls = url_manager.UrlManager()

    def craw(self, start_url):
        """ Start crawl the baike's data """
        self.urls.add_new_url(start_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print("craw %d : %s" % (self.count, new_url))
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parser(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                if self.count == 1000:
                    self.count = 1
                    break
                self.count += 1
            except:
                print("craw failed")

        self.outputer.output_html()

if __name__ == "__main__":
    """MAIN FUNCTION"""
    print("main is runing")
    obj_spider = SpiderMain(root_url)
    obj_spider.craw(start_url)
