import scrapy
from Weather.items import WeatherItem


class GetWeatherSpider(scrapy.Spider):
    name = 'get_weather'
    allowed_domains = ['lishi.tianqi.com']
    start_urls = ['https://lishi.tianqi.com/chengdu/202101.html']

    def parse(self, response):
        for main in response.xpath('//ul[@class="thrui"]/li'):
            item = WeatherItem()

            date_query = main.xpath('./div[1]/text()')
            item['date'] = date_query.extract_first()

            high_query = main.xpath('./div[2]/text()')
            item['high'] = high_query.extract_first()

            low_query = main.xpath('./div[3]/text()')
            item['low'] = low_query.extract_first()

            yield item
