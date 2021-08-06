from scrapy import Spider, Item, Field

# the actual rows returned in a single page
MAX_ROWS = 100


class TableItem(Item):
    n = Field()  # useful to retain order
    name = Field()
    href = Field()


class TableSpider(Spider):
    """docstring for TableSpider"""

    name = 'tablespider'
    tname = None
    tail = False

    def __init__(self, arg):
        super(TableSpider, self).__init__()
        self.arg = arg

    # returns either (one or many) Response or Item objs
    def parse(self, response):

        if None in (self.tname, ):
            raise NotImplementedError('Not implemented for base driver')

        tpath = f'//table[contains(@class, \'{self.tname}\')]'
        rows = response.xpath(tpath)[0].css('tr')  # table-selector

        if self.tail:
            # remove tail if needed
            rows = rows[:-1]

        # instead of returning intermediate items
        # we can obtain lazyness by deriving the
        # Request class into LazyRequest
        # only launching the request and parse method
        # when directly accessed
        for row in rows:
            # table items could have declared
            # for each of their fields, the
            # relative xpath, and then bind them
            # togheter in a dict(field: xpath)
            i = TableItem()
            i['n'] = 0     # recover the 2nd col
            i['name'] = 0  # the 3rd col text
            i['href'] = 0  # the 3rd col href
            yield i


class CMCTableSpider(TableSpider):
    """CoinMarketCap table spider"""

    allowed_domains = ['coinmarketcap.com']
    start_urls = ['http://coinmarketcap.com']
