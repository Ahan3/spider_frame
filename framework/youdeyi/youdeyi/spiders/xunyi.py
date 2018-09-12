# -*- coding: utf-8 -*-
import re
import scrapy
from scrapy import Request
from scrapy_redis.spiders import RedisSpider
class XunyiSpider(RedisSpider):

    redis_key = "xunyispider:strat_urls"
    name = "39"
    allowed_domains = ['ask.39.net']

    # start_urls = ['http://ask.39.net/news/4378-1.html']
    # start_urls = ['http://ask.39.net/news/4376-1.html','http://ask.39.net/news/4378-1.html','http://ask.39.net/news/4377-1.html','http://ask.39.net/news/319465683-1.html']




    def parse(self, response):
        lis = response.xpath('//*[@id="list_tag"]/ul/li')

        for li in lis:
            item = {}
            item['全部问题'] = li.xpath('./span[1]/p/a/text()').extract_first()
            item['问题url链接'] = li.xpath('./span[1]/p/a/@href').extract_first()
            if item['问题url链接']:
                item['问题url链接'] = response.urljoin(item['问题url链接'])
            item['回答数'] =  li.xpath('./span[2]/span/text()').extract_first()
            item['提问时间'] = li.xpath('./span[2]/cite/text()').extract_first()

            yield Request(url=item['问题url链接'],callback=self.parse_detail,meta={'item':item})
        next_url = response.xpath('//a[@class="next"]/@href').extract()
        if len(next_url) != 0:
            next_url = response.urljoin(next_url[0])
            print('开始下一页')
            yield Request(url=next_url,callback=self.parse)

    def parse_detail(self,response):
        item = response.meta['item']
        spans = response.xpath('//p[@class="mation"]/span').extract()
        if len(spans) == 3:
            item['性别'] = response.xpath('//p[@class="mation"]/span[1]/text()').extract_first()
            item['年龄'] = response.xpath('//p[@class="mation"]/span[2]/text()').extract_first()
            item['年龄'] = re.sub('\s+','',item['年龄'],re.S)

        else:
            item['年龄'] = None
            item['性别'] = None
        item['关键字'] = response.xpath('//p[@class="txt_label"]/span/a/text()').extract()
        item['科室'] = response.xpath('//*[@id="sub"]/span[3]/a/text()').extract_first()
        item['疾病标签'] = response.xpath('//*[@id="sub"]/span[4]/a/text()').extract_first()
        yield item

