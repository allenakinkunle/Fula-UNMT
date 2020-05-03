import scrapy

class KoodeSpider(scrapy.Spider):
    name = 'koode'
    
    with open('fula/spiders/koode_link.txt', 'r') as f:
        start_urls = f.readlines()

    def parse(self, response):
        date = response.css('time.published::text').get()
        url = response.url
    
        for paragraph in response.css('div.entry-content p::text'):
            yield {
                'text': paragraph.get().strip(),
                'date': date,
                'url': url
            }