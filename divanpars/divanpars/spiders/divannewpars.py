import scrapy

##### class="wYUX2"
class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        lights = response.css('div.wYUX2')

        for light in lights:
            yield {
                'name': light.css('span::text').get(),
                'price': light.css('meta::attr(content)').get(),
                'url': light.css('link::attr(href)').get()
            }
