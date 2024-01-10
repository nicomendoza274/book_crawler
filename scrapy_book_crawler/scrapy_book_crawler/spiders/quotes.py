from typing import Iterable
import scrapy
from scrapy.http import Request

from scrapy_book_crawler.items import Quote


class QuoteSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        url = "https://quotes.toscrape.com/js"
        yield scrapy.Request(
            url,
            meta=dict(
                playwright=True,
                playwright_include_page=True,
                errback=self.errback,
            ),
        )

    async def parse(self, response):
        page = response.meta["playwright_page"]
        await page.close()

        for book in response.css("div.quote"):
            book = Quote(
                author=book.css("small.author::text").get(),
                # price=book.css("p.price_color::text").get(),
            )
            yield book

    async def errback(self, failure):
        page = failure.request.meta["playwright_page"]
        await page.close()
