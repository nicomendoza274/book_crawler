import scrapy


class Book(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()


class Quote(scrapy.Item):
    author = scrapy.Field()
