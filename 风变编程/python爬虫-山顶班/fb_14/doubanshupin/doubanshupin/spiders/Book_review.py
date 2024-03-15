import bs4,scrapy
from ..items import DoubanshupinItem

class doubanshupin(scrapy.Spider):
    name = 'doubanshupin'
    allowed_domains = ['book.douban.com']
    start_urls = []
    for i in range(2):
        url = 'https://book.douban.com/top250?start=' + str(i * 25)
        start_urls.append(url)
    print(start_urls)

    def parse(self, response):
        res = bs4.BeautifulSoup(response.text, 'html.parser')
        datas = res.find_all('tr', class_='item')
        for data in datas:
            book_name = data.find_all('test_1')[1]['title']
            book_link = data.find_all('test_1')[1]['href'] + 'comments/hot?p=1'
            yield scrapy.Request(book_link,callback=self.parse_job)

    def parse_job(self, response):
        book_name = 1
        res = bs4.BeautifulSoup(response.text,'html.parser')
        datas = res.find_all('li', class_='comment-item')
        for data in datas:
            item = DoubanshupinItem()
            item['book_name'] = book_name
            item['comment_IDcomment_ID'] = data.find_all('test_1')[0]['title']
            item['Short_commentary_content'] = data.find('span', class_='short').text.strip()
            print('书名:{}\n评论ID:{}\n短评内容:{}\n'.format(item['book_name'], item['comment_IDcomment_ID'], item['Short_commentary_content']))
            yield item

