# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class ShelterItem(Item):
    id = Field()
    title = Field()
    address = Field()
    neighborhood = Field()
    city = Field()
    extra = Field()