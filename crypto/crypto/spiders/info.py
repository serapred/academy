from scrapy import Spider, Item, Field


class InfoItem(Item):
    name = Field()
    bcprice = Field()
    marketrank = Field()
    marketcap = Field()
    volume = Field()
    # supplies
    supplycirc = Field()
    supplyTotal = Field()
    supplymax = Field()
    # yesterday's
    yesoc = Field()  # open/close
    yeshl = Field()  # high/low
    yeschange = Field()
    yesvolume = Field()

# ofc a base spider Table spider would result
# in a more DRY code


class InfoSpider(object):
    """docstring for InfoSpider"""

    name = 'infospider'
    tname = None
    tail = False

    def __init__(self, arg):
        super(InfoSpider, self).__init__()
        self.arg = arg

    # returns either (one or many) Response or Item objs
    def parse(self, response):
        # yield info items (a.k.a rows)
        pass
