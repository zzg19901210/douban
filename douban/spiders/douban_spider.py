# -*- coding: utf-8 -*-
import scrapy

from douban.items import DoubanItem

class DoubanSpiderSpider(scrapy.Spider):
    name = 'douban_spider'
    # 抓取域名
    allowed_domains = ['movie.douban.com']
    # 开始时间
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        # 开始解析xpath
        # print(response )

        movie_list=response.xpath("//div[@class='article']//ol[@class='grid_view']//li")
        for i_item in movie_list:
            # print(i_item)
            # 初始化itm文件
            douban_item=DoubanItem()

            douban_item['serial_number']=i_item.xpath(".//div[@class='item']//em/text()").extract_first()
            douban_item['movie_name']=i_item.xpath(".//div[@class='item']//div[@class='info']//div[@class='hd']//a//span[@class='title'][1]/text()").extract_first()
            # 多行的文件处理
            context=i_item.xpath(".//div[@class='item']//div[@class='info']//div[@class='bd']//p[1]/text()").extract();
            for i_context in context:
                context_s="".join(i_context.split())
                douban_item['introduce']=context_s
            douban_item['star']=i_item.xpath(".//div[@class='item']/div[@class='info']/div[@class='bd']/div[@class='star']/span[@class='rating_num']/text()").extract_first()
            douban_item['evaluate']=i_item.xpath(".//div[@class='item']/div[@class='info']/div[@class='bd']/div[@class='star']/span[4]/text()").extract_first()
            douban_item['describe']=i_item.xpath(".//div[@class='item']/div[@class='info']/div[@class='bd']/p[@class='quote']/span[@class='inq']/text()").extract_first()

            # print(douban_item)
            # 需要奖数据pipelines做数据的存储和清洗
            yield douban_item
        # 解析下一页 获取后一页的xpath 若果获取到继续解析如果解析不到停止
        next_link=response.xpath("//div[@class='paginator']/span[@class='next']/a/@href").extract()
        # print(next_link)
        if next_link:
            next_link=next_link[0]
            yield scrapy.Request("https://movie.douban.com/top250"+next_link,callback=self.parse)
        pass
