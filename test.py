# -*- coding:utf-8 -*-
#author xin
import requests
from scrapy.selector import Selector
def get_html(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = 'gbk'
        return r.text
    except:
        print('get html error')

def get_content(url):

    html = get_html(url)

    dates = Selector(text=html).xpath('//div/ul[@class="week"]/li').extract()
    weas = Selector(text=html).xpath('//ul[@class="txt txt2"]/li').extract()
    tems =Selector(text=html).xpath('//div[@class="zxt_shuju"]/ul/li').extract()
    wind = Selector(text=html).xpath('//ul[@class="txt"]/li').extract()

    items = []
    for i in range(7):
        item = {}
        item['date'] = Selector(text=dates[i]).xpath('//b/text()').extract()[0]
        item['week'] = Selector(text=dates[i]).xpath('//span/text()').extract()[0]
        item['img'] = Selector(text=dates[i]).xpath('//img/@src').extract()[0]
        item['weather'] = Selector(text=weas[i]).xpath('//text()').extract()[0]
        temlow = Selector(text=tems[i]).xpath('//b/text()').extract()[0]
        temtop = Selector(text=tems[i]).xpath('//span/text()').extract()[0]
        item['temperature'] = temlow+'~~ '+temtop
        item['wind'] = Selector(text=wind[i]).xpath('//text()').extract()[0]
        items.append(item)
    print(items)


if __name__=='__main__':
    get_content('https://www.tianqi.com/suzhou/')