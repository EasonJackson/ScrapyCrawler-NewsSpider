# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor
from item.items import AmazonitemItem


class ItemspiderSpider(CrawlSpider):
    name = "itemSpider"
    allowed_domains = ["amazon.com"]
    start_urls = ['http://www.amazon.com/']

    rules = (
    	Rule(LinkExtractor(allow = '/s/ref=nb_sb_noss_\?\?url=search-alias\*\Map&field-keywords=computer'), callback = 'parse_item', follow = True),
    	)

    def parse_item(self, response):
        ul = response.xpath("//ul")
        for li in ul.xpath("//li"):
        	item = AmazonitemItem()
	        item['name'] = li.css("").extract_first()
	        item['image'] = li.xpath().extract_first()
	        item['price'] = li.xpath().extract_first()

	        yield(item)