# python
# encode utf-8
# html输出器
import csv
class HtmlOutputer(object):
    def __init__(self):
        self.datas = []
        self.header = ['url', 'bookName', 'score', 'author', 'publisher', 'time', 'price', 'intro']
        self.writer = csv.writer(open(r"D:\PycharmProjects\doubanbook_scrapy\doubanbooks4.csv", 'w', newline=''))  # 防止写入有空行
        self.writer.writerow(self.header)

    def collect_data(self, data):
        if data is None:
            return
        self.datas = []  # 数据提取出来。存入列表
        self.datas.append(data['url'])
        self.datas.append(data['bookName'])
        self.datas.append(data['score'])
        self.datas.append(data['author'])
        self.datas.append(data['publisher'])
        self.datas.append(data['time'])
        self.datas.append(data['price'])
        self.datas.append(data['intro'])

    def output_csv(self):
        self.writer.writerow(self.datas)  # 写入数据


















