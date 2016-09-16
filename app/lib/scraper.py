import scrapy

class CNNSpider (scrapy.Spider):
    name = "CNN"

    start_urls = ['http://www.cnn.com/']

    def parse(self,response):

        for href in response.css ('ul.cn--idx-1 a::attr(href)'):
            full_url = response.urljoin(href.extract())
            yield scrapy.Request(full_url, callback=self.parse_article)

    def parse_article(self,response):

        yield{
            'title': response.css('h1.pg-headline::text').extract_first(),
            'article': response.xpath(
                '//div[@class="zn-body__paragraph"]/text()'
            ).extract()
        }

