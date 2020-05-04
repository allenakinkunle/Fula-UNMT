import scrapy

class TeddungalSpider(scrapy.Spider):
    name = 'teddungal'
    
    with open('fula/spiders/teddungal_link.txt', 'r') as f:
        start_urls = f.readlines()

    def parse(self, response):
        date = response.css('span.post-meta-date::text').get()
        url = response.url
    
        for paragraph in response.css('div.post-content p'):
            line = ' '.join(paragraph.css('*::text').extract())
            
            yield {
                'text': line.strip(),
                'date': date,
                'url': url
            }