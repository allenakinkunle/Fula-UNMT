import scrapy

class WikipediaSpider(scrapy.Spider):
    name = 'wikipedia'
    start_urls = ['https://ff.wikipedia.org/w/index.php?title=Sp%C3%A9cial:Toutes_les_pages&hideredirects=1']
    
    def parse(self, response):
        article_page_links = response.css('div.mw-allpages-body li a')
        yield from response.follow_all(article_page_links, self.parse_articles)

        next_link = response.css('div.mw-allpages-nav a')
        yield from response.follow_all(next_link, self.parse)

    def parse_articles(self, response):
        url = response.url
        for paragraph in response.css('#mw-content-text p'):
            line = ' '.join(paragraph.css('*::text').extract())

            yield {
                'text': line.strip(),
                'url': url
            }