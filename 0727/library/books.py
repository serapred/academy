from base import Item, Collection


class Book(Item):
    """a simple book class"""

    def __init__(self, isbn, title, authors, publisher,
                 published, edition=1, categories=None):
        super(Book, self).__init__()

        # type checking done at higher level
        # and value enforcing done elswhere
        self.isbn = isbn              # str
        self.title = title            # str
        self.authors = authors        # set
        self.publisher = publisher    # str
        self.published = published    # date
        self.edition = edition        # int
        self.categories = categories  # set

    def __str__(self):
        return f'{self.isbn}: {self.title} ({" ".join(self.authors)})'

    def __repr__(self):
        return f'Book({self.isbn})'


class Category(Collection):
    """Collection of books"""

    # imagine some useful specialization

    def __repr__(self):
        stop, el = 5, '...'
        return f'Category({self.itemlist[:stop]}{el})'
