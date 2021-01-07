# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst


class StockstarItemLoader(ItemLoader):
    # 自定义itemloader，用于存储爬虫所抓取的字段内容
    default_output_processor = TakeFirst()


class StockstarItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 股票代码
    code = scrapy.Field()
    # 股票简介
    abbr = scrapy.Field()
    # 流通价值
    tradeValue = scrapy.Field()
    # 总价值
    totalValue = scrapy.Field()