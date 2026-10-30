import scrapy


class BookSpiderSpider(scrapy.Spider):
    name = "book_spider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response):
        next_page = resonse.css('li.next a::attr("href")').get()
        if next_page is not None:
            if 'catalogue' in next_page:
                next_page_url = ('https://books.toscrape.com/' + next_page)
            else:
                next_page_url = ('https://books.toscrape.com/catalogue/' + next_page)

            yield response.follow(next_page_url, callback=self.parse)
            
