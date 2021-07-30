import pickle
import shelve

fav_cryptos = [
    "Steem",
    "Steem Backed Dollars",
    "Bitcoin",
    "IoTeX",
    "Litecoin",
    "Stellar",
    "Byteball",
    "Tether"
]

# pickled objects are saved in a single file
with open('cryptos.p', 'wb') as f:
    pickle.dump(fav_cryptos, f)

rec_cryptos = None

with open('cryptos.p', 'rb') as f:
    pickle.load(rec_cryptos, f)

assert(rec_cryptos == fav_cryptos)

fav_colors = [
    'Green',
    'Yellow',
    'Orange',
    'Red',
    'Blue',
    'Brown',
    'White',
    'Black'
]

with open('colors.p', 'wb') as f:
    pickle.dump(fav_colors, f)

rec_colors = None

with open('colors.p', 'rb') as f:
    pickle.load(rec_colors, f)

assert(rec_colors == fav_colors)


# shelve is built on top of pickle
# manages multiple pickle istance
# at once (think composite pattern)

with shelve.open('test_shelf') as shelf:

    shelf['cryptos'] = rec_cryptos
    shelf['colors'] = rec_colors

rec_colors.extend(('Cyan', 'Magenta'))

with shelve.open('test_shelf') as shelf:
    # the whole thing is overritten...
    shelf['colors'] = rec_colors


with shelve.open('test_shelf') as shelf:
    # reading looks pretty much like writing
    shelved = shelf['colors']


with shelve.open('test_shelf') as shelf:
    # this won't actually append the value
    shelf['cryptos'].append('Monero')


with shelve.open('test_shelf') as shelf:
    # this would be the way...
    cryptos = shelf['cryptos']
    cryptos.append('Monero')
    shelf['cryptos'] = cryptos

with shelve.open('test_shelf') as shelf:
    # deleting is trivial
    del shelf[cryptos]

with shelve.open('test_shelf', writeback=True) as shelf:
    # writeback allows this to work
    # slower and more ram intensive
    # performs the same operation as
    # above
    shelf['cryptos'].append('Dash')


# can't this be more efficient ?
