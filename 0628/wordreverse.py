"""
Given an english text return it with the words
in reverse order
"""


def reflect(text, dcset):
    reflection = ''
    while text[-1] in dcset:
        reflection += text[-1]
        text = text[:-1]
    return ''.join((reflection, text))


def reverse(text, sep=' ', dcset=None, newline='\n'):
    dcset = dcset if dcset is not None else set()
    ans = []
    for line in reversed(text):
        line = line.rstrip(newline)
        words = line.split(sep)
        words.reverse()
        ans.append(sep.join(map(lambda w: reflect(w, dcset), words)))
    return newline.join(ans)


if __name__ == '__main__':

    dcset = set(',.;()!?:\"')
    with open('../files/words.txt', 'r') as f:
        text = f.readlines()
        ans = reverse(text, dcset=dcset)

    print(f'Original:\n{"".join(text)}\nReversed:\n{ans}')
