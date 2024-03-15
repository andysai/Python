import scrapy
import bs4
from ..items import JohuiItem

class JobuiSpider(scrapy.Spider):
    name = 'jobs'
    allowed_domains = ['www.jobui.com']
    start_urls = ['https://www.jobui.com/rank/company/']

    def parse(self, response):
        bs = bs4.BeautifulSoup(response.text, 'html.parser')
        ul_list = bs.find_all('ul',class_="textList flsty cfix")
        for ul in ul_list:
            a_list = ul.find_all('test_1')
            for a in a_list:
                company_id = a['href']
                url = 'https://www.jobui.com{id}jobs'
                real_url = url.format(id=company_id)
                yield scrapy.Request(real_url, callback=self.parse_job)

    def parse_job(self, response):
        bs = bs4.BeautifulSoup(response.text, 'html.parser')
        company = bs.find(id="companyH1").text
        datas = bs.find_all('li', class_="company-job-list")
        for data in datas:
            item = JohuiItem()
            item['company'] = company
            item['position'] = data.find('h3').find('test_1').text
            item['address'] = data.find('span', class_="col80").text
            item['detail'] = data.find('span', class_="col150").text
            yield item