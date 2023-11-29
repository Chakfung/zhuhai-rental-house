import scrapy
import time
from scrapy.http import Request
from zhuhai_crawler.items import ZhuhaiCrawlerItem

class ZhuhaiSpider(scrapy.Spider):
    name = "zhuhai"
    allowed_domains = ["zh.lianjia.com"]
    start_urls = ["https://zh.lianjia.com/zufang/"]
    custom_settings = {
            'ITEM_PIPELINES': {},  # ban pipline delete it can save data to database
            'FEED_FORMAT': 'csv',
            'FEED_URI': 'output.csv',
    }
    def __init__(self):
        self.url_num = 0
        self.apartment_num = 0

    def parse(self, response):
        print(response.url)
        regions = response.css('#filter > ul:nth-child(2) > li.filter__item--level2 > a')
        for region in regions[1:2]:
            print(region.attrib['href'])
            url = 'https://zh.lianjia.com' + region.attrib['href']
            yield Request(url, callback=self.parse_region)

    # Traverse all pages
    def parse_region(self, response):
        # Display a maximum of 100 pages, 30 pieces of data per page, 
        # if the number of houses in this area exceeds 3000 need to enter the subdivision traversal
        house_num = int(response.css('#content > div.content__article > p > span.content__title--hl::text').get()) 
        if house_num > 3000:
            print('more than 3000, need to use sub region')
            subregions = response.css('#filter > ul:nth-child(4) > li.filter__item--level3 > a')
            for subregion in subregions[1:2]:
                sub_url = 'https://zh.lianjia.com' + subregion.attrib['href']
                # self-calling
                yield Request(sub_url, callback=self.parse_region)
        else:        
            print('house number', house_num)
            page_num = min(house_num // 30 + 1, 100) 
            for i in range(1, page_num + 1):
                # time.sleep(0.1)
                url = response.url + 'pg{}'.format(i)
                print(url)
                yield Request(url, callback=self.parse_overview)

    # crawl basic info
    def parse_overview(self, response):
        infos = response.css('div.content__list--item')
        for info in infos:
            suburl = info.css('.content__list--item--aside').attrib['href']
            if 'zufang' in suburl:
                item = ZhuhaiCrawlerItem()
                item['title'] = info.css('.content__list--item--aside').attrib['title']
                item['location'] = '-'.join(info.css('.content__list--item--des a::text').getall())
                des = info.css('.content__list--item--des::text').getall()
                item['house_type'] = [x.strip() for x in des if '室' in x][0]
                item['house_code'] = suburl.split('.')[0].split('/')[2]
                url = 'https://zh.lianjia.com' + suburl
                self.url_num += 1
                print(url)
                yield Request(url, meta={'item': item}, callback=self.parse_info)
            else:
                self.apartment_num += 1

    # crawl detail
    def parse_info(self, response):
        try:
            item = response.meta['item']
            item['price'] = response.css('div.content__aside--title span::text').get() + \
                response.css('div.content__aside--title::text').getall()[1].strip()
            item['tags'] = ','.join(response.css('p.content__aside--tags i::text').getall())
            item['lease'] = response.css('#aside > ul > li:nth-child(1)::text').get()
            item['area'] = response.css('#info > ul:nth-child(2) > li:nth-child(2)::text').get().split('：')[1]
            item['orientation'] = response.css('#info > ul:nth-child(2) > li:nth-child(3)::text').get().split('：')[1]
            item['floor'] = response.css('#info > ul:nth-child(2) > li:nth-child(8)::text').get().split('：')[1]
            item['elevator'] = response.css('#info > ul:nth-child(2) > li:nth-child(9)::text').get().split('：')[1]
            item['stall'] = response.css('#info > ul:nth-child(2) > li:nth-child(11)::text').get().split('：')[1]
            item['water'] = response.css('#info > ul:nth-child(2) > li:nth-child(12)::text').get().split('：')[1]
            item['electricity'] = response.css('#info > ul:nth-child(2) > li:nth-child(14)::text').get().split('：')[1]
            item['fuel_gas'] = response.css('#info > ul:nth-child(2) > li:nth-child(15)::text').get().split('：')[1]
            item['heating'] = response.css('#info > ul:nth-child(2) > li:nth-child(17)::text').get().split('：')[1]
            item['stall'] = response.css('#info > ul:nth-child(2) > li:nth-child(11)::text').get().split('：')[1]
            facilities = response.css('body > div.wrapper > div:nth-child(2) > div.content.clear.w1150 > div.content__detail > div.content__article.fl > ul > li')
            facility_list = []
            for facility in facilities[1:]:
                if 'no' not in facility.attrib['class']:
                    facility_list.append(facility.css('::text').getall()[-1].strip())
            item['facility'] = ','.join(facility_list)
            item['description'] = ''.join([x.strip() for x in response.css('#desc > p:nth-child(3)::text').getall()])
            print('response', item)
            yield item   #return data
        except AttributeError as e:
            print(e)
            time.sleep(3)
