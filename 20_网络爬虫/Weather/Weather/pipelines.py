# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class WeatherPipeline:
    def process_item(self, item, spider):
        print('日期:', item['date'])
        print('最高温度:', item['high'])
        print('最低温度:', item['low'])
