import scrapy

class HammadiSpider(scrapy.Spider):
    name = 'hammadi'
    start_urls = ['https://hammadi-jah.skyrock.com/']
    
    def parse(self, response):
        article_page_links = response.css('.bloc_title a')
        yield from response.follow_all(article_page_links, self.parse_articles)

        next_link = response.css('li.next a')
        yield from response.follow_all(next_link, self.parse)

    def parse_articles(self, response):
        url = response.url
        for paragraph in response.css('div.text-image-container span::text'):
            yield {
                'text': paragraph.get().strip(),
                'url': url
            }