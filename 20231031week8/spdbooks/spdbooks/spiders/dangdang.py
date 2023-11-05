import scrapy
from scrapy import Selector
from ..items import SpdbooksItem


# scrapy crawl dangdang -o books.txt



class DangdangSpider(scrapy.Spider):
    name = "dangdang"
    allowed_domains = ["category.dangdang.com"]
    start_urls = ["http://category.dangdang.com/cp01.54.00.00.00.00.html"]

    #解析页面 response响应
    def parse(self, response):
        sel = Selector(response)
        list_items = sel.css('ul.bigimg li')
        for list_item in list_items:

            book_item = SpdbooksItem()

            # va_name = list_item.css('p.name a::attr(titil)').get()
            # va_price = list_item.css('p.price span.search_now_price::text').get()
            # va_author = list_item.css('p.search_book_author span::text').get()
            
            #print('va_name :' , va_name)
            #print('va_price :' , va_price)
            #print('va_author :' , va_author)

            book_item['name'] = list_item.css('p.name a::attr(title)').get()
            book_item['price'] = list_item.css('p.price span.search_now_price::text').get()
            book_item['author'] = list_item.css('p.search_book_author span::attr(title)').get()

            yield book_item
