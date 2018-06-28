# python
# encode utf-8
# html解析器
import re
from bs4 import BeautifulSoup as bs


class HtmlParser(object):
    def parser(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        # 解析为一个beautifulsoup对象,html.parser为内置的Python标准库中的HTML解析器
        soup = bs(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(soup)  # 调用内部方法提取url
        new_data = self._get_new_data(page_url, soup)  # 调用内部方法提取有价值数据
        return new_urls, new_data

    def _get_new_urls(self, soup):
        new_urls = []  # 新爬取的链接
        # 同样喜欢的区域：
        # <div id="db-rec-section" class="block5 subject_show knnlike">
        recommend = soup.find('div', class_="block5 subject_show knnlike")  # 找到推荐书籍的区域
        # <a href="https://book.douban.com/subject/27039404/" class="">三岛由纪夫追记</a>
        # 在推荐区域找到所有的链接
        links = recommend.find_all('a', href=re.compile(r"https://book.douban.com/subject/\d+/$"))
        for link in links:
            new_url = link['href']  # 从结点中提取超链接，即url
            new_urls.append(new_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        res_data = {}
        # url
        res_data['url'] = page_url
        # <span property="v:itemreviewed">代码大全</span>
        res_data['bookName'] = soup.find('span', property='v:itemreviewed').string
        # <strong class="ll rating_num " property="v:average"> 9.3 </strong>
        res_data['score'] = soup.find('strong', class_='ll rating_num ').string

        '''
        <div id="info" class="">
            <span>
              <span class="pl"> 作者</span>:
              <a class="" href="/search/Steve%20McConnell">Steve McConnell</a>
            </span><br>
            <span class="pl">出版社:</span> 电子工业出版社<br>
            <span class="pl">出版年:</span> 2007-8<br>
            <span class="pl">页数:</span> 138<br>
            <span class="pl">定价:</span> 15.00元<br>
        </div>
        '''
        info = soup.find('div', id='info')
        try:  # 有的页面信息不全
            res_data['author'] = info.find(text=['作者:', ' 作者']).next_element.next_element.string
            res_data['publisher'] = info.find(text='出版社:').next_element
            res_data['time'] = info.find(text='出版年:').next_element
            res_data['price'] = info.find(text='定价:').next_element
            res_data['intro'] = 'None'
            # res_data['intro'] = soup.find('div', class_='intro').find('p').string
        except:
            return res_data

        return res_data
        # if res_data['intro'] == None:
        #     return None










