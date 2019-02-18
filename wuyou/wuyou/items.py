# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field,Item


class WuyouItem(Item):
    name = Field()
    provinces = Field()
    area = Field()
    workyear = Field()
    edu = Field()
    datatime = Field()
    min_salary = Field()
    high_salary = Field()
    welfare = Field()

    pass
