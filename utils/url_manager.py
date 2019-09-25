

class UrlManager(object):
    """KERNEL CODE"""
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def add_new_url(self, url):
        """
        ADD A NEW URL TO URL MANAGER
        :param url: A NEW URL
        :return: NONE
        """
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        """
        ADD SOME URLS TO URL MANAGER
        :param urls: SOME URLS
        :return: NONE
        """
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def get_new_url(self):
        """
        GET A NEW URL FROM THE END OF URL MANAGER
        :return: A END OF URL IN URL MANAGER
        """
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

    def has_new_url(self):
        """
        JUAGE WHETHER HAS A NEW URL
        :return: BOOL
        """
        return len(self.new_urls) != 0
