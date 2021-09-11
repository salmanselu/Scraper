import scrapy


class KTUSpider(scrapy.Spider):
    name = 'notifs'
    start_urls = [
        'https://ktu.edu.in/eu/core/announcements.htm',
    ]

    def parse(self, response):
        for notif in response.css('ul'):
            yield {
                'notif': notif.css('li').get()
                
            }
