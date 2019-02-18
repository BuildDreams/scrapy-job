# -*- coding: utf-8 -*-
import scrapy
from wuyou.items import WuyouItem
import  re
from scrapy_redis.spiders import RedisSpider
class Job51Spider(scrapy.Spider):#RedisSpider
    name = 'job51'
    allowed_domains = ['search.51job.com', "jobs.51job.com"]
    redis_key = "job51:start_urls"#列表类型 setting里面redis优先
    start_urls = ['https://search.51job.com/list/000000,000000,0000,00,9,99,python,2,773.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=']
    pattrn  = re.compile(r'.*?\d{8,9}.*')


    def parse(self, response):
        href = response.xpath(r'//*[@class="el"]/p/span/a/@href').extract()
        for url in href:
            b = re.match(self.pattrn,url)
            if b:
                yield scrapy.Request(url=url,callback=self.parse_content)
            else:
                pass
        for i in range(3, 760):
            next_url ="https://search.51job.com/list/000000,000000,0000,00,9,99,python,2,{}.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=".format(i)
            yield scrapy.Request(url=next_url,callback=self.parse)

    def parse_content(self, response):

        newItem = WuyouItem()
        try:
            newItem['name'] = response.xpath(r'/html/body/div[3]/div[2]/div[2]/div/div[1]/h1/text()').extract()[0].strip().rstrip()
            newItem['provinces'] = response.xpath(r'/html/body/div[3]/div[2]/div[2]/div/div[1]/p[2]/text()').extract()[0].split("-")[0].strip().rstrip()
            res = response.xpath(r'/html/body/div[3]/div[2]/div[2]/div/div[1]/p[2]/text()').extract()[0]
            if "-" in res:
                newItem['area'] = res.strip().rstrip().split("-")[1]
            else:
                newItem['area'] = ""
            result = response.xpath(r'/html/body/div[3]/div[2]/div[2]/div/div[1]/p[2]/text()').extract()
            for rs in result:
                if "本科" in rs or "大专" in rs  or "硕士" in rs or "研究生" in rs or "博士" in rs or "中专" in rs:
                    newItem['edu'] = rs.rstrip().strip()
                if "经验" in rs:
                    newItem['workyear'] = rs.strip().rstrip()
                if "发布" in rs:
                    rt = ["2018"]
                    (rt.extend(rs.split("发布")[0].strip().rstrip().split("-")))
                    res = "-".join(rt)
                    newItem['datatime']  = res
            newItem['min_salary'] = float(response.xpath(r'/html/body/div[3]/div[2]/div[2]/div/div[1]/strong/text()').extract()[0].split("-")[0])*10000
            newItem['high_salary'] = float(response.xpath(r'/html/body/div[3]/div[2]/div[2]/div/div[1]/strong/text()').extract()[0].split("-")[1].split("万")[0])*10000
            welfare_1 = response.xpath(r'/html/body/div[3]/div[2]/div[2]/div/div[1]/div/div//span/text()').extract()
            newItem['welfare'] = ",".join(welfare_1)
        except:
            pass

        yield newItem

