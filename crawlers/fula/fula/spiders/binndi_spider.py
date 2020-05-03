import scrapy

class BinndiSpider(scrapy.Spider):
    name = 'binndi'
    
    with open('fula/spiders/binndi_link.txt', 'r') as f:
        start_urls = f.readlines()

    def parse(self, response):
        date = response.css('time::text').get()
        url = response.url
    
        for paragraph in response.css('p.has-text-align-justify::text'):
            yield {
                'text': paragraph.get().strip(),
                'date': date,
                'url': url
            }