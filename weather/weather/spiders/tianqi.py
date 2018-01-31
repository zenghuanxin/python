# -*- coding: utf-8 -*-
import scrapy

from weather.weather.items import WeatherItem
class SztianqiSpider(scrapy.Spider):
    name = 'tianqi'
    allowed_domains = ['tianqi.com']

    start_urls = []


    citys = ['nanjing','suzhou','fujian']

    for city in citys:
        start_urls.append('https://www.tianqi.com/'+city)
    def parse(self, response):
        '''
        筛选信息的函数
        date = 今天日期
        week = 星期几
        img = 表示天气的图标
        temperature = 当天的温度
        weather = 当天的天气
        wind = 当天的风向
        :param response:
        :return:
        '''

        items = []

        dates = response.xpath('//div/ul[@class="week"]/li').extract()
        weas = response.xpath('//ul[@class="txt txt2"]/li').extract()
        tems = response.xpath('//div[@class="zxt_shuju"]/ul/li').extract()
        wind = response.xpath('//ul[@class="txt"]/li').extract()

        for i in range(len(dates)):
            item = WeatherItem()

            item['date'] = dates[i].xpath('//b/text()').extract()[0]
            item['week'] = dates[i].xpath('//span/text()').extract()[0]
            item['img'] = dates[i].xpath('//img/@src').extract()[0]




