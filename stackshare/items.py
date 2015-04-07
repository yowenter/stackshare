# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy



class StackTypeName(scrapy.Item):
    stype=scrapy.Field()
    sname=scrapy.Field()
    
class StackReason(scrapy.Item):
    img_url=scrapy.Field()
    name=scrapy.Field()
    title=scrapy.Field()
    description=scrapy.Field()
    reason=scrapy.Field()