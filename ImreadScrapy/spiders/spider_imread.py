# -*- coding: utf-8 -*-
import scrapy
from pyquery import PyQuery as pq
from ..items import BookItem


class SpiderImreadSpider(scrapy.Spider):
    name = 'spider_imread'
    allowed_domains = ['www.qidian.com','https://book.qidian.com']
    start_urls = ['https://www.qidian.com/all?orderId=&style=1&pageSize=20&siteid=1&pubflag=0&hiddenField=0&page=4864']
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept - Encoding': 'gzip, deflate, br',
        'Accept - Language': 'zh-CN,zh;q=0.9,en;q=0.8,pt;q=0.7,la;q=0.6',
        'Cache - Control': 'no - cache',
        'Connection': 'keep - alive',
        'Cookie': '_csrfToken=0OBeqYeBu3awq7apD0Vrtq3pgUkfTqJ3H8vxKzdx; newstatisticUUID=1506390420_1429509889; focusGame=1; e1=%7B%22pid%22%3A%22qd_P_limitfree%22%2C%22eid%22%3A%22qd_E05%22%2C%22l1%22%3A5%7D; e2=%7B%22pid%22%3A%22qd_P_all%22%2C%22eid%22%3A%22qd_A18%22%2C%22l1%22%3A3%7D',
        'Host': 'www.qidian.com',
        'Pragma': 'no - cache',
        'Upgrade-Insecure-Requests':'1',
    }
    Num = 0

    def start_requests(self):
        yield scrapy.Request(self.start_urls[0], callback=self.parse,headers=self.headers)

    def parse(self, response):
        print('sun', 'response-success')
        indexHtml = pq(response.text)
        html = indexHtml('.all-book-list')
        html = html.find('li')
        for item in html.items():
            bookItem = BookItem()
            if item.find('a').attr('href'):
                bookItem['bDetail'] = 'https://'+item.find('a').attr('href').replace('//','').strip()
            else:
                bookItem['bDetail'] = 'empty'

            if item.find('a').attr('data-bid'):
                bookItem['bid'] = item.find('a').attr('data-bid')
            else:
                bookItem['bid'] = 'empty'

            if item.find('a').find('img'):
                bookItem['bImg'] = 'https://'+item.find('a').find('img').attr('src').replace('//','').strip()
            else:
                bookItem['bImg'] = 'empty'

            if item.find('h4').find('a'):
                bookItem['bName'] = item.find('h4').find('a').text()
            else:
                bookItem['bName'] = 'empty'

            if item.find('p').find('a'):
                bookItem['bAuthor'] = item.find('p').find('a').eq(0).text()
            else:
                bookItem['bAuthor'] = 'empty'

            if item.find('p').find('a').eq(1):
                bookItem['bClassify'] = item.find('p').find('a').eq(1).text()
            else:
                bookItem['bClassify'] = 'empty'

            if item.find('p').find('a'):
                bookItem['bTag'] = item.find('p').find('a').eq(2).text()
            else:
                bookItem['bTag'] = 'empty'

            if item.find('p').eq(0).find('span'):
                bookItem['bState'] = item.find('p').eq(0).find('span').text()
            else:
                bookItem['bState'] = 'empty'

            if item.find('p').eq(1):
                bookItem['bIntro'] = item.find('p').eq(1).text().strip()
            else:
                bookItem['bIntro'] = 'empty'

            if item.find('p').find('a'):
                bookItem['bSubType'] = item.find('p').find('a').eq(2).text()
            else:
                bookItem['bSubType'] = 'empty'

            if item.find('p').eq(2).find('span'):
                bookItem['bTextNum'] = item.find('p').eq(2).find('span').text()
            else:
                bookItem['bTextNum'] = 'empty'
            self.Num += 1
            # print('sun', bookItem.get('bDetail')+'\n',bookItem.get('bid')+'\n',bookItem.get('bImg')+'\n',bookItem.get('bName')+'\n',bookItem.get('bAuthor')+'\n',
            #       bookItem.get('bClassify')+'\n',bookItem.get('bTag')+'\n',bookItem.get('bState')+'\n',bookItem.get('bIntro')+'\n',bookItem.get('bSubType')+'\n',bookItem.get('bTextNum')+'\n',self.Num)
            yield bookItem
        nextUrl = indexHtml('.lbf-pagination-item-list').find('li')
        # nextUrl = nextUrl.eq(len(nextUrl)-1).find('a').attr('href').strip()
        if nextUrl.eq(len(nextUrl)-1).find('a').attr('href'):
            nextUrl=nextUrl.eq(len(nextUrl)-1).find('a').attr('href')
            nextUrl='https:'+str(nextUrl.strip())
        if nextUrl and self.Num<=10000:
            print('sun-nextUrl', nextUrl,self.Num)
            yield scrapy.Request(nextUrl, callback=self.parse,headers=self.headers,errback=self.error)

    def error(self):
        print('sun','error\nerror\nerror\nerror\nerror')