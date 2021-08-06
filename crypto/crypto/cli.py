"""
The candidate is required to realize a web scraper, i.e. a python program that etrieves and elaborates
the information about the cryptocurrencies from the website https://coinmarketcap.com/
The program must show a menu to the user with the following features, at least:
1) Information on the cryptocurrencies: the program will show a table containing the name of the
cryptocurrency along with all the pieces of information provided by the related details’ page
in the summary table at the bottom right, for each of the first 50 cryptocurrencies in the list.
E.g., for “bitcoin” cryptocurrency, the details’ page is https://coinmarketcap.com/currencies/
bitcoin/ containing the table shown here: https://imgur.com/a/NyEmhXn The resulting table
will be paged with 5 results at the most, and the program will ask user whether to keep on the
next page or go back to the main menu.
2) Search by name for information about cryptocurrencies: The user will be asked to type a search
key and the information about the cryptocurrency, whose name contains the search key, will be
shown. The results will include the same data as the previous requirement (1) and will be paged
in the same way.
3) Detailed information about the cryptocurrency The user will be asked to type the name of a
cryptocurrency and the details of that cryptocurrency will be shown on the screen.
4) The features can optionally be invoked by command line, without any interaction with the user,
who will be able to go through the results by selecting the proper page. The greatest number of
results per page and the name of the cryptocurrency are command line parameters.
"""


"""
Notes:
- the root of the website shows the list of cryptocurrency
- the table of details can be found at: root/currencies/-crypto_name-
- the requirement is a paging of 5 for the list.
- a prefetching function may be desirable
- both list and search return multiple "rows"
- the previous point implies a structure where each command name
  different than ? and l, will be interpreted as a name for the
  point 3.

Ex of commands:

v1
crypto dodgecoin: returns info about dodgecoin (currency not found error for 404)
crypto ? coin: a paged list of all the currencies containing the string "coin"
crypto l 20: a paged list of the first 20 currencies

v2

# single command behaviour:
    -   empty  => list
    -   empty + strict => first
    -   input => like
    -   input + strict => get
crypto dodge --results=20, --view=5, --strict/--all


Ex of options:
-p, --pagesize, int
-r, --results int
-s, --strict bool
"""

import click

"""
from spiders import ...
from filters import get, ordered, like
from pagers import pager
"""


@click.command()
@click.argument('name', default="")
@click.option('-v', '--view', type=int, default=5, help="view size")
@click.option('-r', '--results', type=int, default=50, help="max results returned")
@click.option('-s', '--strict', is_flag=True, help="search strictly")
@click.option('-a', '--all', is_flag=True, help="all possible results")
def cli(name, pagesize, results, cachesize, strict):
    """
    CryptoPI is a simple tool to retrieve infos
    about cryptocurrencies
    """

    # filter is a function that recieves an iterable
    # as input and returns the same iteratble minus
    # some values for which a certain condition isn't
    # met.
    # filter behaviour:
    # name + strict
    # None + True: table[:1]
    # None + False: table[:results]
    # str  + True:  table[str]
    # str  + False: {k, v for k,v in table if str in k}

    # filter definition
    if not name:
        pass
        # results = 1 if strict else results
        # results = None if all else results
        # f = range(results) => table[:results]
    else:
        pass
        # f = get(name) if strict else like(name)

    try:
        # get the page, a.k.a table and filter it
        pass
    except Exception as e:
        # if results is greater than n
        # where n: num of rows per page
        # if the table can't be somehow
        # retrieved
        raise e
    else:
        pass

    try:
        # iterate over paged results
        pass
    except Exception as e:
        raise e
    else:
        pass


if __name__ == '__main__':
    cli()
