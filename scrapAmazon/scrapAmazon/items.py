# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ProductItem(scrapy.Item):

    id = scrapy.Field()
    name = scrapy.Field()
    date_insert = scrapy.Field()
    price = scrapy.Field()
    review_amt = scrapy.Field()