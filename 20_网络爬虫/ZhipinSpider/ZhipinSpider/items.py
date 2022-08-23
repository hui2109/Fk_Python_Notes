# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhipinspiderItem(scrapy.Item):
    title = scrapy.Field()
    salary = scrapy.Field()
    company = scrapy.Field()
    url = scrapy.Field()
    work_addr = scrapy.Field()
    industry = scrapy.Field()
    company_size = scrapy.Field()
    recruiter = scrapy.Field()
    publish_date = scrapy.Field()
