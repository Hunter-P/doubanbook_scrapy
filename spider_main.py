# python
# encode utf-8
# 调度器
from urllib import error
import url_manager, html_downloader, html_parser, html_outputer
import time

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        try:
            while self.urls.has_new_url():
                try:
                    new_url = self.urls.get_new_url(count)
                    print('craw %d:%s' % (count, new_url))
                    html_cont = self.downloader.download(new_url)
                    new_urls, new_data = self.parser.parser(new_url, html_cont)

                    print("newUrls:", new_urls, "\nnewData:", new_data)

                    self.urls.add_new_urls(new_urls)
                    self.outputer.collect_data(new_data)  # 数据存储在内存中
                    self.outputer.output_csv()  # 数据导出
                    time.sleep(0.3)

                    if count == 2000:
                        break
                    count += 1
                except:
                    count += 1
                    print("跳过")
                    continue

        except Exception as e:
            print("craw failed!", e)


if __name__ == "__main__":
    root_url = "https://book.douban.com/subject/1200840/"  # 起始地址
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)

















