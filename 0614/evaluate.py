"""
Write a progarm that gives the user 3 chances to guess a password.
"""


def evaluate_pass():

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


"""
Write a program that ask for two numbers. if their sum
is greater than 100,  print "too big".
"""


def evaluate_sum():
    a, b = input('insert two numbers: ').split()
    if float(a) + float(b) > 100:
        print('too big!')
    else:
        print('Nice.')


"""
Write a program that ask for user's name. if your name is input,
the program must answer with "this is a nice name", if the input
is "John Cleese" or "Michel Palin", with a joke, othewise with
the sentence "you have a nice name".
"""


def evaluate_name():

    mine = "Sergio Apreda"
    name = input("insert a name: ")
    if name == mine:
        print("This is a nice name!")
    elif name in ("John Cleese", "Michel Palin"):
        print("Get out, this is not a circus!")
    else:
        print('You have a nice name fella!')


if __name__ == '__main__':

    switch = {'password': evaluate_pass,
              'sum': evaluate_sum,
              'name': evaluate_name}

    choice = ''
    while choice not in switch:
        print('options:', '\n-' + str('\n-'.join(switch.keys())))
        choice = input('choose one: ')

    switch[choice]()
