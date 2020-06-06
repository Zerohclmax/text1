# -*- coding: utf-8 -*-
import scrapy
from scrapy.http.response.html import HtmlResponse
from scrapy.selector.unified import SelectorList

class QsbkSpider(scrapy.Spider):
    name = 'qsbk'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['http://www.qiushibaike.com/text/page/2/']

    def parse(self, response):
        for contentLeft in response.xpath('//div[@class="col1 old-style-col1"]/div'):
            another = contentLeft.xpath('.//h2/text()').get().strip()
            content = contentLeft.xpath('.//div[@class="content"]/span[1]/text()').getall()
            content="".join(content).strip()
            print(another+" : ")
            print(content)
            print('=' * 50)
            print('=' * 50)