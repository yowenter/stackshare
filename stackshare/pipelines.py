# -*- coding: utf-8 -*-
import logging
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

LOG=logging.getLogger(__name__)


class StacksharePipeline(object):
    def process_item(self, item, spider):
        if type(item).__name__=='StackTypeName':
            print 'TYPE:::%s   NAME:::%s '%(item['stype'],item['sname'])
        else:
            print item
