import scrapy
import datetime
from scrapy import Request
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import ProductItem
import re


class ReviewspiderSpider(scrapy.Spider):
    name = 'reviewsspider'
    allowed_domains = ["goods.ru"]
    start_urls = ["https://goods.ru/catalog/details/napolnitel-cat-step-selikagelevyy-152-l-100022760079/",
                  "https://goods.ru/catalog/details/voda-mineralnaya-novoterskaya-gazirovannaya-15-l-plastik-100022961239/",
                  "https://goods.ru/catalog/details/smart-chasy-apple-watch-se-44mm-space-gray-aluminium-case-with-black-sport-band-mydt2ru-a-100027259585/"
                  ]


    def parse(self, response):
        # self.logger.info('A response from %s just arrived', response.url)

        id_art = response.url[-13:-1]
        date_insert = datetime.datetime.now().strftime("%Y-%m-%d")
        name = response.xpath('//h1[@itemprop="name"]/text()').extract_first()
        price = re.sub("\D","",response.xpath('//div[@class="price__final"]/text()').extract_first())
        review_amt = re.sub("\D","",response.xpath('//span[@class="tooltipster card-prod--reviews-count"]/text()').extract_first())
#pdp-header__sku desktop-only
        product = ProductItem()

        product['id'] = id_art
        product['name'] = name
        product['date_insert'] = date_insert
        product['price'] = price
        product['review_amt'] = review_amt

        yield product