import scrapy
from scrapy import Request
import time


class ChedrauiSpider(scrapy.Spider):
    name = "zandparts"
    allowed_domains = ["zandparts.com"]
    start_urls = ["https://www.zandparts.com/en/search?q=samsung&InStock=InStock"]

    def parse(self, response):
        next_items = response.xpath(
            '//ul[@class="row product-list"]//li/article/div/div/a/@href'
        ).extract()
        for next_item in next_items:
            time.sleep(1)
            yield Request(response.urljoin(next_item), callback=self.parse_item)

        next_urls = response.xpath('//*[@id="search-result"]//li/a/@href').extract()
        for next_url in next_urls:
            yield Request(response.urljoin(next_url), callback=self.parse)

    def parse_item(self, response):
        yield {
            "Brand": response.xpath('//*[@itemprop="brand"]/text()').extract(),
            "Type": response.xpath("/html/body/nav/ul/li[3]/a/text()").extract(),
            "Family": response.xpath("/html/body/nav/ul/li[4]/a/text()").extract(),
            "Model": response.xpath("/html/body/nav/ul/li[5]/a/text()").extract(),
            "Category": response.xpath(
                "/html/body/main/div/div/div/div/div[1]/div[2]/div[1]/ul/li[4]/text()"
            ).extract(),
            "Name": response.xpath("/html/body/nav/ul/li[6]/a/text()").extract(),
            "PartNo": response.xpath(
                "/html/body/main/div/div/div/div/div[1]/div[2]/div[1]/ul/li[1]/text()"
            ).extract(),
            "Quality": response.xpath(
                "/html/body/main/div/div/div/div/div[1]/div[2]/div[1]/ul/li[3]/text()"
            ).extract(),
            "Price": response.xpath(
                "/html/body/main/div/div/div/div/div[1]/div[2]/div[1]/div[1]/div/span[1]/text()"
            ).extract(),
            "Description": response.xpath(
                "/html/body/main/div/div/div/div/div[2]/div/div/div/section/section/div[1]/div/text()"
            ).extract(),
            "description_alternative": response.xpath(
                "/html/body/main/div/div/div/div/div[2]/div/div/div/section/section/div[1]/div/p/text()"
            ).extract(),
            "FitsTo": response.xpath(
                "/html/body/main/div/div/div/div/div[2]/div/div/div/section/section/div[2]/ul/li/a/text()"
            ).extract(),
            "Alternative": response.xpath(
                "/html/body/main/div/div/div/div/div[2]/div/div/div/section/section/div[3]/div/div/ul/li/article/div/div[1]/a/h3/text()"
            ).extract(),
            "ImageLinks": response.xpath(
                '//img[@class="product-detail__image--main"]/@src'
            ).extract(),
            "OriginalLink": response.url,
        }
