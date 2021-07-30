"""
Write a program that extracts a secret from a text file.
The program must recognize that the file may contain a secret.
If the file contains a secret, the first word of each line is
in lexiographic order with the next. The message is contained in
the diagonal of the file, meaning in the n'th word of the n'th line.

Es:

Adesso mangio il provolone
Bianco, bruciare il pennacchio
Celeste dopo la mezzanotte mentre
Dante prende la bandiera.

Adesso bruciare la bandiera.
"""


def extract_secret_1(stream, dcset='(),.!;:-\"\'', sep=' '):

    i = 0
    last = ''
    ans = ''

    while stream:
        line = stream.readline()

        # base condition
        if line == '':
            break

        # the first word of the line
        # minus eventual suffix in the dcset
        words = line.split(maxsplit=i + 1)
        first = words[0].strip(dcset)
        ith = words[i].strip(dcset)
        if first < last:
            last = None
            break

        ans += ith
        last = first
        i += 1

    if last is None:
        return last
    return ans


'''
# one liner, without lexiographic check
def extract_secret(path, dcset=None):
    with open(path, 'r') as f:
        return ''.join((line[i] for i, line in enumerate(f.readlines())))
'''


"""
Write a steganography program to extract a secret text from a plain one.
To verify that the file contains a secret the first word of each line must
appear in lexiographic order. For each line the secret word is positioned
according to another word of the same line having the property of containing
the textual form of a number. in case of multiple occurrence of such words,
the first one must be chosen.
The word representing the number must appear as a whole (distributions are not valid).

Es:
Anna non voleva avvelenare quattro gatti
Così perse la trebisonda e non andò alla
Festa del Sensei, dove la cameriera
Giocava facendo gran rumore alla morra russa nel mese di settembre.
"""


def has_digit(line, sep=' '):
    nummap = {'uno': 1, 'due': 2,
              'tre': 3, 'quattro': 4,
              'cinque': 5, 'sei': 6,
              'sette': 7, 'otto': 8,
              'nove': 9}

    for i in nummap:
        if i in line:
            return nummap[i]
    return None


def extract_secret_2(stream, dcset='(),.!;:-\"\'', sep=' '):

    last = ''
    ans = ''

    while stream:
        line = stream.readline()

        # base condition
        if line == '':
            break

        words = line.split(sep)
        if words[0] <= last:
            break

        i = has_digit(line)

        try:
            ans += words[i - 1] + sep
        except (TypeError, IndexError):
            return ''

        last = words[0]

    return ans.rstrip(sep)


if __name__ == '__main__':

    from sys import argv

    with open(argv[1], 'r') as f:
        secret = extract_secret_2(f)

    if secret:
        print(f'secret found, "{secret}".')
    else:
        print('nothing to see here!')
