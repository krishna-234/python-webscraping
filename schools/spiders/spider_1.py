import scrapy

class Spider(scrapy.Spider):
    name = "schoolData"

    start_urls = [
       "https://www.cbseschool.org/schools/ranchi/"
    ]

    def parse(self, response):
        urls = response.css('div.catbox a::attr(href)').getall()
        for url in urls:
            yield scrapy.Request(url=url, callback=self.finalparse)


    def finalparse(self, response):
        x = response.css('td::text').getall()
        schoolData = {}
        for i in range(0, len(x), 2):
            schoolData[x[i]] = x[i+1]
        yield schoolData