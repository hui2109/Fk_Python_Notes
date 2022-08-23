# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WeatherItem(scrapy.Item):
    high = scrapy.Field()
    low = scrapy.Field()
    date = scrapy.Field()
