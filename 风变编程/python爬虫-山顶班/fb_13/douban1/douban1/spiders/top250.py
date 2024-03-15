import scrapy,bs4
from ..items import Douban1Item

class DoubanSpider(scrapy.Spider):
    name = 'douban1'
    allowed_dpmains = ['book.douban.com']
    start_urls = []
    for i in range(3):
        url = 'https://book.douban.com/top250?start=' + str(i * 25)
        start_urls.append(url)

    def parse(self, response):
        bs = bs4.BeautifulSoup(response.text,'html.parser')
        datas = bs.find_all('tr',class_='item')
        for data in datas:
            item = Douban1Item()
            item['title'] = data.find_all('test_1')[1]['title']
            item['publish'] = data.find('p',class_='pl').text
            item['score'] = data.find('span',class_='rating_nums').text
            print('书籍名称:{}\n出版信息:{}\n评分:{}\n'.format(item['title'],item['publish'],item['score']))
            yield item