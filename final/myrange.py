"""
The candidate is required to implement a function new_range which behaves exactly like the range

function from the standard library. It is not allowed to use the implementation provided by
the standard library, as well. The required implementation must be a drop-in replacement
of the original function, and it will be invoked in the same documented ways as the original range function. The

candidate can refer to the following link for the details on the signature and the behaviour of the func-
tion: https:docs.python.org3.7librarystdtypes.html#range
"""

# it looks like range would be an iterator,
# but in fact, it only acts like it, since
# most of the methods can be  algebraically implemented.
# implement simply a funcion would not reflect
# that range is an object derived from sequence
# and as such with its own methods and attributes.


# since technically a function is required
# but range is in fact a class...

DEFAULT_STOP = 0
DEFAULT_STEP = 1

import itertools
import random


def eval_int(value):
    if isinstance(value, int):
        return value
    raise TypeError(
        f'\'{type(value).__name__}\' object cannot be interpreted as an integer')


def desc(*args):
    return sorted(args, reverse=True)


class Myrange(object):
    """docstring for Myrange"""

    def __init__(self, start, stop=DEFAULT_STOP, step=DEFAULT_STEP):

        a, b, c = (eval_int(obj) for obj in ((start, stop, step)))
        if step == 0:
            raise ValueError('Range() arg 3 must not be zero')

    def __bool__(self):
        # Return self != 0
        return len(self) != 0

    def __contains__(self, key):
        # Return key in self.
        if not self.start < key < self.stop or not key % self.step == 0:
            return False
        return True

    def __eq__(self, value):
        # Return self==value.
        try:
            start = self.start == value.start
            stop = self.stop == value.stop
            step = self.step == value.step
        except AttributeError:
            return False
        else:
            return all((start, stop, step))

    def __ge__(self, value):
        # Return self>=value.
        return self.__gt__ and self.__eq__

    #  compatibility with 2.7 (slice objs is a 3.x thing)
    @ classmethod
    def __slice__(cls, subs):
        if not isinstance(subs, slice):
            raise TypeError(' subs must be \'slice\', not str')

        # faster than lambda, single instancing
        def isNone(x):
            return x == None

        if all(map(isNone, (subs.start, subs.stop, subs.step))):
            return cls

        rangecls = super(Myrange, cls).__new__(cls)
        rangecls.__init__(subs.start, subs.stop, subs.step)
        return rangecls

    def __getitem__(self, key):
        # Return self[key].

        if isinstance(key, slice):
            return self.__slice__(key)
        else:
            dist = self.start + (self.step * key)
            if not isinstance(key, int):
                raise TypeError(
                    f' range indices must be integers or slices, not \'{type(key)}\'')

        return dist

    def __gt__(self, value):
        # Return self>value, lexiographic.
        for i in self:
            if i != value[i]:
                return i > value[i]
        return False

    def __iter__(self):
        # Implement iter(self).
        value = self.start
        if self.step > 0:
            while value < self.stop:
                yield value
                value += self.step
        else:
            while value > self.stop:
                yield value
                value += self.step

    def __le__(self, value):
        # Return self <= value.
        return self.__lt__ and self.__eq__

    def __len__(self):
        # Return len(self).
        a, b = desc(self.start, self.stop)
        length = (b - a) // self.step
        return length if length > 0 else 0

    def __lt__(self, value):
        # Return self < value.
        for i in self:
            if i != value[i]:
                return i < value[i]
        return False

    def __ne__(self, value):
        # Return self != value.
        return not self.__eq__

    def __reduce__(self):
        # Helper for pickle.
        pass

    def __repr__(self):
        # Return repr(self).
        stop = ',' + str(self.stop) if self.stop != 0 else ''
        step = ',' + str(self.step) if self.step != 1 else ''
        return f'Myrange({self.start}{stop}{step})'

    def __reversed__(self):
        # Return a reverse iterator.
        return reversed(self.__iter__)


def new_range(start, stop=None, step=None):
    return Myrange(start, stop, step)


def main():
    r1 = new_range(-2, 4, -1)
    r2 = new_range(-2, -4, 1)
    r3 = new_range(-2, 4, 1)

    for q in range(0, 100000):
        s = random.randint(0, 100)
        i = random.randint(1, 100)
        i *= -1 if random.random() > 0.5 else 1

        e = s + (i * random.randint(1, 100))
        params = [s, e, i][:random.randint(1, 3)]
        for i, j in itertools.zip_longest(range(*params), range(*params), fillvalue=object):
            assert i == j, f"Test fallito {i} != {j}"

    print('OK')


if __name__ == '__main__':
    main()
