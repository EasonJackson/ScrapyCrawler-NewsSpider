# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from News.items import NewsItem

class NewscrawlerSpider(CrawlSpider):
    name = "newscrawler"
    allowed_domains = ["nytimes.com"]
    start_urls = ['http://www.nytimes.com']
    rules = (
	    	Rule(LinkExtractor(allow = '.*'), callback = 'parse_item', follow = True),
    	)

    def parse_item(self, response):
    	item = NewsItem()
        item["page"] = response.xpath("//a/@href").extract()
        yield item