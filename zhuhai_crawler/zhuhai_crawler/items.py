# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhuhaiCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    location = scrapy.Field()
    house_type = scrapy.Field()     
    house_code = scrapy.Field()   
    price = scrapy.Field()
    tags = scrapy.Field()   
    lease = scrapy.Field()  
    area = scrapy.Field()   
    orientation = scrapy.Field()
    floor = scrapy.Field()
    elevator = scrapy.Field() 
    stall = scrapy.Field()
    water = scrapy.Field()
    electricity = scrapy.Field()  
    fuel_gas = scrapy.Field() 
    heating = scrapy.Field()  
    facility = scrapy.Field()    
    description = scrapy.Field()    
    pass

