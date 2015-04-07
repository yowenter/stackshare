# -*- coding: utf-8 -*-
import scrapy
import re
from bs4 import BeautifulSoup as Soup
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors import LinkExtractor
from stackshare.items import StackTypeName,StackReason


class StackserviceSpider(CrawlSpider):
    name = "stackservice"
    allowed_domains = ["stackshare.io"]
    start_urls = (
        'http://stackshare.io/categories',
    )
    rules=(Rule(LinkExtractor(allow=('/[a-z]{4,20}',)),callback='parse_service_card'),)
    
    def parse_service_card(self,response):
        s=Soup(response.body)
        cards=s.find_all('div',class_="col-lg-4 col-md-4 col-sm-4 stacked-service")
        for card in cards:
            card_type=card.find('a',class_='btn btn-ss-g-a btn-xs').text.encode('utf-8')
            stack=card.find('div',class_="landing-stack-name").find('a')
            if stack:
                card_name=stack.text.encode('utf-8')
                stack_link=stack['href']
                yield StackTypeName(stype=card_type,sname=card_name)
                yield scrapy.Request('http://stackshare.io/'+stack_link,callback=self.parse_service)
    
    def parse_service(self,response):
        name=re.search('stackshare.io/(.*)',response.url).groups()[0]
        s=Soup(response.body)
        img_url=s.find('div',class_="sp-service-logo col-md-2 col-xs-12").find('img')['src']
        reasons=s.find_all('div',class_='col-md-12 col-sm-6 reason_item')
        all_reasons={}
        for reason in reasons:
            count=reason.find('span',class_='reason-count').text.encode('utf-8').strip()
            text=reason.find('div',id="reason-text").text.encode('utf-8').strip()
            all_reasons[text]=count
        yield StackReason(img_url=img_url,name=name,reason=all_reasons)
            
        
        
        
         
            
        


