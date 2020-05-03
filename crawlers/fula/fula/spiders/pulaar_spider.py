import scrapy

class PulaarSpider(scrapy.Spider):
    name = 'pulaar'
    start_urls = ['https://pulaar.org/']
    
    def parse(self, response):
        article_page_links = response.css('.td_module_11 h3 a')
        yield from response.follow_all(article_page_links, self.parse_articles)

        next_link = response.css('.page-nav span.current + a')
        yield from response.follow_all(next_link, self.parse)

    def parse_articles(self, response):
        for paragraph in response.css('div.td-post-content p::text'):
            yield {
                'text': paragraph.get().strip(),
                'date': response.css('.entry-date::text').get().strip(),
                'url': response.url
            }