import scrapy

class DingiralSpider(scrapy.Spider):
    name = 'dingiral'
    start_urls = ['https://dingiralfulbe.com/category/renndo-e-kabaruuji/',
                  'https://dingiralfulbe.com/category/pinal/',
                  'https://dingiralfulbe.com/category/winndere/'
                  ]
    
    def parse(self, response):
        article_page_links = response.css('h2.title a')
        yield from response.follow_all(article_page_links, self.parse_articles)

        next_link = response.css('a.next')
        yield from response.follow_all(next_link, self.parse)

    def parse_articles(self, response):
        url = response.url
        for paragraph in response.css('div.entry-content p::text'):
            yield {
                'text': paragraph.get().strip(),
                'url': url
            }