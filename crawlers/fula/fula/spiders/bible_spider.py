import scrapy

class BibleSpider(scrapy.Spider):
    name = 'bible'
    books = {
        'MAT': 28, 'MRK': 16, 'LUK': 24, 'JHN': 21,
        'ACT': 28, 'ROM': 16, '1CO': 16, '2CO': 13,
        'GAL': 6, 'EPH': 6, 'PHP': 4, 'COL': 4,
        '1TH': 5, '2TH': 3, '1TI': 6, '2TI': 4,
        'TIT': 3, 'PHM': 1, 'HEB': 13, 'JAS': 5,
        '1PE': 5, '2PE': 3, '1JN': 5, '2JN': 1,
        '3JN': 1, 'JUD': 1, 'REV': 22
    }

    start_urls = [f'https://live.bible.is/bible/FUFPBT/{book}/{num}' for book, num_chap in books.items() for num in range(1, num_chap+1)]
    
    def parse(self, response):
        url = response.url

        for paragraph in response.css('div.chapter span span::text'):
            yield {
                'text': paragraph.get().strip(),
                'url': url
            }