# slide 60


def isItBig(a, b):
    if a + b > 100:
        print('too big!')
    else:
        print('Nice.')


def guessPW():

    pw = 'thisisit'
    i = 3

    ans = input('Welcome, do you want to try to guess the password?(Yes/No): ')

    if ans.lower() in ('n, no'):
        print('Farwell')
        exit()

    while i > 0 and ans != pw:
        ans = input('insert your guess: ')
        i -= 1

    if ans == pw:
        print('You are a genius!')
    else:
        print('You wouldn\'t get it')


def evaluateNumber(name):

    mine = 'Sergio Apreda'
    if name == mine:
        print('This is a nice name!')
    elif name in ("John Cleese", "Michel Palin"):
        print('Get out, this is not a circus!')
    else:
        print('You have a nice name fella!')


# slide 61

def isPrime(n):

    # with n in N set
    # check for negative values
    if n <= 1:
        return False

    # base case
    if n <= 3:
        return True

    # edge cases
    if n % 2 == 0 or n % 3 == 0:
        return False

    # n.b. all unique divisors will be <= sqrt(n)
    # and in the form (6k + 1)
    i = 5
    while i**2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


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


"""
scrivere un programma che richieda l'inserimento di numeri da parte dell'utente, con lo '0' come carattere di uscita. Se il numero inserito è multiplo di 2 stampare flip, se è multiplo di 3 stampare flop.
"""


def fizzBuzz(n=-1):

    while n != 0:
        try:
            n = float(input('insert number: '))
        except ValueError:
            print('Not a Number')
            return -1
        print(inner(n))

    return n


def inner(n=-1):

    res = ''
    if n == 0:
        return ''
    if n % 2 == 0:
        res += 'flip'
    if n % 3 == 0:
        res += 'flop'

    return res


"""
def cipher(input, output=None, disp=0, buff_size=5):

    import threading
    import Queue

    q = Queue.Queue(buff_size)

    # producer Agent
    class Producer(threading.Thread):


        def __init__(self, arg):
            super(Producer, self).__init__()
            self.arg = arg

    # consumer Agent
    class Producer(threading.Thread):

        def __init__(self, arg):
            super(Producer, self).__init__()
            self.arg = arg
"""

if __name__ == '__main__':

    fizzBuzz()
