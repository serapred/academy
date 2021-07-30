"""
Persistence Layer
"""

import shelve


# at filesystem level, with shelf


class PersistenceHandler(object):
    """simple fs persistence handler"""

    # weak constraint: collection obj must have
    # a not null attribute "name"
    @classmethod
    def save(cls, dbname, collection):
        with shelve.open(dbname, 'c') as shelf:
            shelf[collection.name] = collection

    @classmethod
    def load(cls, dbname, collection):
        with shelve.open(dbname, 'r') as shelf:
            return shelf[collection]
