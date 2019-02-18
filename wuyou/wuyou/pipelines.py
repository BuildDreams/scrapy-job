# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import  pymysql
from  . import settings


class MysqlPipeline(object):
    def __init__(self):
        self.con = pymysql.Connect(host=settings.MYSQL_HOST,
                                   user=settings.MYSQL_USER,
                                   password=settings.MYSQL_PASSWORD,
                                   port=settings.MYSQL_PORT,
                                   database=settings.MYSQL_DATABASE)
        self.cursor = self.con.cursor()

    def process_item(self, item, spider):
        try:
            self.cursor.execute("""INSERT INTO job51 (name,provinces,area,workyear,edu,datatime,min_salary,high_salary,welfare)
                value (%s,%s,%s,%s,%s,%s,%s,%s,%s)""", (
            item['name'], item['provinces'], item['area'], item['workyear'], item['edu'],
            item['datatime'], item['min_salary'],item['high_salary'], item['welfare']))
            self.con.commit()
        except Exception as error:
            print(error)
        return item


