"""
An italian town decided to digitalize their library realizing a bookeeping software for handling
and store the data about available tomes. It also manifested the need for future maintainance.
As such, the candidate will:

1)  Design and realize a python software, using elements of object oriented programming.
    the software must provide capabilities of:
    insertion, update and deletion of books and their parameters (isbn, title, etc..)
    search for parameter, and a print of all the books present in the archive.
    Provide the possibility to manage collections of books, as in organized in categories.
    More categories can exist and each book can belong to multiple categories;
2)  Extend the software, adding the possibility to save data permanently on a local database (sqlite);
3)  Extend the software, adding an ORM (peewee);
"""


class Item(object):
    """a generic item class"""

    # dunder goodness

    # WARNING: .arg access can be done as ['arg'] from now on

    def __getitem__(self, name):
        return self.__getattribute__(name)

    def __setitem__(self, name, value):
        # should excepts be handled here
        return self.__setattr__(name, value)


"""
brieef digression on persistence type:
non-binary methods only cover an handful
of native datatypes (set not being one of them).
So maybe pickling is the best use case here.
using shelf seems more appropriate in this instance
(even if not necessary, as always)
"""


class Collection(object):
    """a simple composite pattern"""

    search_char = ':'

    def __init__(self, name, itemlist=None):
        # same as before, it is possible to restrict
        # input domain by adding validation methods
        self.name = name
        self.itemlist = [] if itemlist is None else itemlist

    # helper methods

    @staticmethod
    def __getattr(obj, attr):
        try:
            return obj.__getattribute__(attr)
        except AttributeError:
            pass

    @classmethod
    def __isattr(cls, obj, attr, value):
        print(cls.__getattr(obj, attr))
        return cls.__getattr(obj, attr) == value

    @classmethod
    def __hasattr(cls, obj, attr, value):
        return value in cls.__getattr(obj, attr)

    def rows(self):
        # sintactic sugar, may be slower
        # than explicit call.
        # more maintainable, for sure.
        return enumerate(self.itemlist)

    # filter methods

    # [i[0] for i in self.itemlist if inverse ^ self.__isattr(i[1], key, value)]
    def search(self, key, value, inverse=False):
        for row in self.itemlist:
            if inverse ^ self.__isattr(row, key, value):
                yield row

    # [i[0] for i in self.itemlist if inverse ^ self.__hasattr(i[1], value, key)]

    def search_in(self, key, value, inverse=False):
        for row in self.rows():
            if inverse ^ self.__hasattr(row[1], key, value):
                yield row

    # list wrapper methods

    def append(self, item):
        return self.itemlist.append(item)

    def insert(self, index, item):
        return self.itemlist.insert(index, item)

    def extend(self, iterable):
        return self.itemlist.extend(iterable)

    def remove(self, item):
        return self.itemlist.pop(item)

    def drop(self):
        return self.itemlist.clear()

    # dunder methods, code footprint redux
    # improving: readability, maintainability
    # access patterns:
    # collection[int]: select row
    # collection[str]: select col
    # collection[int][str]: select cell

    def __len__(self):
        return len(self.itemlist)

    def __getitem__(self, name):
        if isinstance(name, int):
            return self.itemlist[name]
        elif isinstance(name, str):
            return [i.__getattribute__(name) for i in self.itemlist]

    def __setitem__(self, name, value):
        if isinstance(name, int):
            self.itemlist[name] = value
        elif isinstance(name, str):
            for i in self.itemlist:
                i.__setattr__(name, value)
        else:
            raise TypeError(
                'index must be of str, int or tuple (len:2) type')

    def __delitem__(self, name):
        if isinstance(name, int):
            del self.itemlist[name]
        elif isinstance(name, str):
            for i in self.itemlist:
                i.__delattr__(name)
        else:
            raise TypeError(
                'index must be of str, int or tuple (len:2) type')

    def __str__(self):
        return '\n'.join((f'{k}> {v}' for k, v in self.rows()))

    def __repr__(self):
        stop, el = 5, '...' if len(self.itemlist) > 5 else None, ''
        return f'Collection({self.itemlist[:stop]}{el})'
