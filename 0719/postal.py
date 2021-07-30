class Item(object):
    """docstring for Item"""

    def __init__(self, name, price):
        super(Item, self).__init__()
        self.name = name
        self.price = price


class Package(object):
    """docstring for Package"""

    def __init__(self, items=None):
        super(Package, self).__init__()

        if items is None:
            items = []

        self.items = items

    def append_item(self, item):
        self.items.append(item)

    def append_items(self, items):
        self.items.extend(items)

    @property
    def prices(self):
        return [i.price for i in self.items]

    @property
    def value(self):
        return sum(self.prices)
