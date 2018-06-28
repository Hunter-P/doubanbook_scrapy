# python
# encode,utf-8
# html下载器
from urllib import request, error

class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return
        print('Downloading:', url)
        header = {'user-agent': 'Mozilla/5.0'}  # 伪装成Mozilla/5.0浏览器
        req = request.Request(url, headers=header)

        maxNum = 10
        for tries in range(maxNum):
            try:
                with request.urlopen(req) as reponse:  # 访问这个url
                    html = reponse.read()  # HTML的数据
                    if reponse.getcode() != 200:
                        return None
                    return html
            except:  # 异常处理
                if tries < maxNum-1:
                    continue
                else:
                    print("Has tried %d times to access url, all failed!" % maxNum)
                    return None







