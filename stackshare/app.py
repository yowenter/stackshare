#-*-encoding:utf-8-*-
import flask
from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy.settings import Settings
from scrapy import log
from spiders.stackservice import StackserviceSpider

app=flask.Flask(__name__)

@app.route('/',methods=['GET'])
def home_page():
	return 'Hey,Danan!'

@app.route('/start_crawl',methods=['GET'])
def crawl():
	spider = StackserviceSpider()
	crawler = Crawler(Settings())
	crawler.configure()
	crawler.crawl(spider)
	crawler.start()
	log.start()
	reactor.run() # the script will block here


if __name__=='__main__':
	app.run(host='0.0.0.0',port=3000)