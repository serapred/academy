import re

"""
Write a program that looks up a word in a txt file, count its occurrences and
returns the lines in which it appears.
"""


def word_counter(file, word):

    found = []
    word = rf'\b{word}\b'
    lines = f.read().split('.')

    for line in enumerate(lines):
        toadd = len(re.findall(word, line[1]))
        if toadd:
            found.append(line[0])
    return found


if __name__ == '__main__':

    key = input('please insert a keyword: ')
    with open('files/words.txt', 'r') as f:
        lines = word_counter(f, key)

    print(f'the keyword ({key}) was found {len(lines)} times.')
    if lines:
        print('at lines: ', ' '.join((str(l) for l in lines)))
