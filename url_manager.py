# python
# encode,utf-8


# url管理器
class UrlManager(object):
    def __init__(self):
        self.new_urls = []  # 未爬取url列表
        self.old_urls = []  # 已爬取url列表

    # 添加新的单个url，只添加不在新旧集合中的url
    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.old_urls and url not in self.new_urls:
            self.new_urls.append(url)

    # 添加新的一堆url，调用add_new_url添加
    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    # 是否还有未爬取的url
    def has_new_url(self):
        return len(self.new_urls) != 0

    # 获取一个新的url，将该url从未爬取集合删除，添加到已爬取集合中
    # 优先获取距离上一次链接最近的链接
    def get_new_url(self, count):
        new_url = self.new_urls[count-1]
        self.old_urls.append(new_url)
        return new_url