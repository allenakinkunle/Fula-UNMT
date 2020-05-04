import scrapy

class NdiayeSpider(scrapy.Spider):
    name = 'ndiaye'
    start_urls = ['http://www.pulaaronline.com/']
    
    def parse(self, response):
        article_page_links = response.css('.post-title a')
        yield from response.follow_all(article_page_links, self.parse_articles)

        next_link = response.css('a.blog-pager-older-link')
        yield from response.follow_all(next_link, self.parse)

    def parse_articles(self, response):
        url = response.url
        date = response.css('.date-header span::text').get()
        for paragraph in response.css('div.post-body span::text'):
            yield {
                'text': paragraph.get().strip(),
                'date': date,
                'url': url
            }