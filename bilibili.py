# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest

class BilibiliSpider(scrapy.Spider):
    name = 'bilibili'
    allowed_domains = ['www.bilibili.com']
    start_urls = ['https://www.bilibili.com/v/game/stand_alone/?spm_id_from=333.8.game_stand_alone.27#/']

    currently_page = 1

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, args={'images': 0, 'timeout': 10})

    def parse(self, response):
        for sel in response.css('div.l'):
            href = sel.xpath('.//@href').extract()
            yield {'href': href}
        

        self.currently_page += 1
        next_url = f'https://www.bilibili.com/v/game/stand_alone/?spm_id_from=333.8.game_stand_alone.27#/all/default/0/{self.currently_page}/'
        if self.currently_page < 6:
            yield SplashRequest(next_url, args={'images': 0, 'timeout': 10}) 