# Scrivere un programma che in un file di testo cerchi una parola data in input,
# ne conti le occorrenze e indichi in che riga occorre

import re


def count_words(word, file):

    cnt = 0
    lines = []
    word = rf'\\b{word}\\b'
    with open(file, 'r') as f:
        for line in enumerate(f):
            toadd = len(re.findall(word, line[1]))
            if toadd:
                cnt += toadd
                lines.append(line[0])
    return cnt, lines


# Scrivere un programma che identifica i numeri all'interno di un file di testo e calcola
# a) le occorrenze delle cifre (da 1 a 9)
# b) i numeri con l'occorrenza minima
# c) i numeri con l'occorrenza massima


def find_digits(file):
    cnt = [0] * 10
    with open(file, 'r') as f:
        for line in f:
            for char in line:
                if char.isdigit():
                    cnt[int(char)] += 1
    return cnt


def minmax_digits(digits):
    minval, maxval = min(digits), max(digits)
    mindex, maxdex = [], []

    for i, q in enumerate(digits):
        if q == minval:
            mindex.append(i)
        if q == maxval:
            maxdex.append(i)

    return {'value': minval, 'index': mindex}, {'value': maxval, 'index': maxdex}


def count_digits(file):

    d = find_digits(file)
    mind, maxd = minmax_digits(d)
    return {'digits': d, 'min': mind, 'max': maxd}


if __name__ == '__main__':

    path = 'files/'

    '''
    cnt, lines = count_words('test', path + 'words.txt')
    print(f'total: {cnt}\nlines: {lines}')
    '''

    import pprint as pp
    cnt = count_digits(path + 'numbers.txt')
    pp.pprint(cnt)
