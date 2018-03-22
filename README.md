# NewsSpider - ScrapyCrawler

## A little play around with Scrapy

The little toy program in ```News``` is used to crawl the head news on NY times.

## Description

Spiders: 

Set allowed domains = ```allowed_domains = ["nytimes.com"]```

Feed the start url link = ```'http://www.nytimes.com'```

Set the rules:
```Rule(LinkExtractor(allow = '.*'), callback = 'parse_item', follow = True)```

The rule allows all urls being added to comsuming queue, and provide a callback function ```parse_item```,
the item is chained to a new class ```NewsItem```. To get the target resource from html, a customized xpath is provided for the response ```response.xpath("//a/@href").extract()```

## Author
**EasonJackson @2016**
