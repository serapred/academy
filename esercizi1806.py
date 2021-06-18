# slide 121

def numsToNames(numbers):

    nummap = {
        '0': 'zero',
        '1': 'uno',
        '2': 'due',
        '3': 'tre',
        '4': 'quattro',
        '5': 'cinque',
        '6': 'sei',
        '7': 'sette',
        '8': 'otto',
        '9': 'nove',
    }

    return ' '.join(tuple(nummap[i] for i in numbers))
