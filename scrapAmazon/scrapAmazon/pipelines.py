# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


import psycopg2


class ScrapamazonPipeline(object):

    def open_spider(self, spider):

        hostname = 'localhost'
        username = 'postgres'  # the username when you create the database
        password = 'Fender1580'  # change to your password
        database = 'goods_parsing'

        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
        self.cur = self.connection.cursor()

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()

    def process_item(self, item, spider):
        self.cur.execute("insert into products(art_id, name, date_insert, price, review_amt) values(%s,%s,%s,%s,%s)",
                         (item['id'], item['name'], item['date_insert'], item['price'], item['review_amt']))
        self.connection.commit()
        return item
