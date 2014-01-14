# coding: utf-8
from scrapy.selector import Selector
from scrapy.spider import BaseSpider
from sheltersscraper.items import ShelterItem

class DmozSpider(BaseSpider):
   name = "rishon"
   allowed_domains = ["rishonlezion.muni.il"]
   start_urls = [
       "http://www.rishonlezion.muni.il/service/mosdot_ironiyeem/Pages/miklatim.aspx"
   ]

   def parse(self, response):
       sel = Selector(response)
       rows = sel.xpath('//table[@class="ms-rteTable-2"]//tr')
       items = []
       rows = rows[1:-1]
       for row in rows:
           cols = row.xpath('td/text()').extract()
           item = ShelterItem()
           item['vendor_id'] = cols[0]
           item['address'] = cols[1]
           item['neighborhood'] = cols[2]
           item['city'] = "ראשון לציון"

           items.append(item)
       return items