# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class AmazonitemItem(scrapy.Item):
    # define the fields for your item here like:
    name = Field()
    image = Field()
    price = Field()
    
