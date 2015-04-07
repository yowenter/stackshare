# -*- coding: utf-8 -*-
import scrapy
import re
from bs4 import BeautifulSoup as Soup
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors import LinkExtractor
from stackshare.items import StackTypeName


class StackserviceSpider(CrawlSpider):
    name = "stackservice"
    allowed_domains = ["stackshare.io"]
    start_urls = (
        'http://stackshare.io/categories',
    )
    rules=(Rule(LinkExtractor(allow=('^/.*',)),callback='parse_service_card'),)
    
    def parse_service_card(self,response):
        s=Soup(response.body)
        cards=s.find_all('div',class_=re.compile('col-lg-4'))
        for card in cards:
            card_type=card.find('a',class_=re.compile('btn btn-ss-g-a btn-xs')).text.encode('utf-8')
            stack=card.find('div',class_="landing-stack-name").find('a')
            if stack:
                card_name=stack.text.encode('utf-8')
                stack_link=stack['href']
                yield StackTypeName(stype=card_type,sname=card_name)
                yield scrapy.Request(stack_link,callback=self.parse_service)
    
    def parse_service(self,response):
        s=Soup(response.body)
         
            
        


