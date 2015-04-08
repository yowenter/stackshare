# -*- coding: utf-8 -*-
import os

# Scrapy settings for stackshare project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'stackshare'

SPIDER_MODULES = ['stackshare.spiders']
NEWSPIDER_MODULE = 'stackshare.spiders'
ITEM_PIPELINES={'stackshare.pipelines.StacksharePipeline':100}
LOG_LEVEL = 'INFO'
# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36'
DATABASE_URL=os.getenv('DATABASE','mysql://root:dangerous@192.168.1.25/wwwapi')

if not os.path.exists(os.path.join(os.getcwd(),'filter_urls.txt')):
    with open(os.path.join(os.getcwd(),'filter_urls.txt'),'w') as f:
        f.write('HERE ARE THE URLS HAVE BEEN CRAWLED.\n')

FILTER_URLS=os.path.join(os.getcwd(),'filter_urls.txt')
