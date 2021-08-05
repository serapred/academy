"""
The candidate is required to implement a function new_range which behaves exactly like the range

function from the standard library. It is not allowed to use the implementation provided by
the standard library, as well. The required implementation must be a drop-in replacement
of the original function, and it will be invoked in the same documented ways as the original range function.
The candidate can refer to the following link for the details on the signature and the
behaviour of the function: https:docs.python.org3.7librarystdtypes.html#range
"""

# it looks like range would be an iterator,
# but in fact, it only acts like it, since
# most of the methods can be  algebraically implemented.
# implement a funcion would not reflect
# that range is an object derived from a sequence
# with its own methods and attributes.

from collections import Iterator

# defaults
DEF_STOP = 0
DEF_STEP = 1


def eval_obj(obj):
    # The arguments to the range constructor must be integers
    # (either built-in int or any object that
    # implements the __index__ special method).
    if hasattr(obj, '__index__'):
        return obj.__index__()
    raise TypeError(
        f'\'{type(obj).__name__}\''
        f' object cannot be interpreted as an integer')


def eval_args(*args):
    # for variadics arguments
    length = len(args)
    if length < 1:
        raise TypeError(f'range expected 1 arguments,'
                        f' got {len(args)}')
    if length > 3:
        raise TypeError(f'range expected at most 3 arguments,'
                        f' got {len(args)}')
    if length == 1:
        args = (DEF_STOP, args[0], DEF_STEP)
    elif length == 2:
        args = (*args, DEF_STEP)

    return args


#  simplest functional approach
def new_range_fun(*args):
    start, stop, step = (eval_obj(obj) for obj in eval_args(*args))
    if step == 0:
        raise ValueError('Range() arg 3 must not be zero')

    if step > 0:
        while start < stop:
            yield start
            start += step
    else:
        while start > stop:
            yield start
            start += step


# 2nd version
def new_range_fun(*args):
    start, stop, step = (eval_obj(obj) for obj in eval_args(*args))
    if step == 0:
        raise ValueError('Range() arg 3 must not be zero')
    if (start - stop) // step < 0:
        # replace stop with next element
        # in the sequence of integers that
        # are congruent to start modulo step.
        stop += (start - stop) % step
        while start != stop:
            yield start
            start += step


# since a function is required
# but range is in fact a class...
def new_range(*args):
    # range(stop) -> range object
    # range(start, stop[, step]) -> range object
    return Myrange(*args)


# since __iter__ and __reverse__ methods of range
# return an iterator...


class Rangeiter(Iterator):
    """MyRange iterator"""

    def __init__(self, robj):

        self._rng = robj
        self._cnt = 0

        # last returned value
        # starting one step back enable pre-increment
        self._lst = self._rng.start - self._rng.step

    def __iter__(self):
        return self

    def __next__(self):
        self._lst += self._rng.step
        self._cnt += 1

        if self._cnt > self._rng._len:
            raise StopIteration()
        return self._lst


class Myrange(object):
    """
    Implementation of the range class

    Produces a sequence of integers
    from start (inclusive)to stop (exclusive) by step.
    range(i, j) produces i, i+1, i+2, ..., j-1.
    start defaults to 0, and stop is omitted!
    range(4) produces 0, 1, 2, 3.
    These are exactly the valid indices for a list of 4 elements.
    When step is given, it specifies the increment (or decrement).

    n.b.: while behaving like a sequence
    range doesn't use in memory representation (in 3.x).
    """

    # improves object memory alloc
    # while preventing new attrs declaration
    __slots__ = ('start', 'stop', 'step', '_len')

    def __init__(self, *args):
        start, stop, step = (eval_obj(obj) for obj in eval_args(*args))

        if step == 0:
            raise ValueError('Range() arg 3 must not be zero')
        # these should not be accessible from outside
        # yet, we make use of the possibility of doing so
        self.start = start
        self.stop = stop
        self.step = step
        # bool to account for congruence
        self._len = bool((stop - start) % step) + (stop - start) // step

    def __bool__(self):
        # Return self != 0
        return bool(self._len)

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

    def __len__(self):
        return self._len

    def __contains__(self, key):
        # Return key in self.
        if self.start < key < self.stop \
                and key % self.step == 0:
            return True
        return False

    def __slice__(self, subs):
        if not isinstance(subs, slice):
            raise TypeError(' subs must be \'slice\', not str')

        # faster than lambda, single instancing
        def isnone(x):
            return x is None

        if all(map(isnone, (subs.start, subs.stop, subs.step))):
            return self

        start, stop, step = (subs.start, subs.stop, subs.step)

        # step behaviour
        step = self.step * step if step else self.step

        # start, stop behaviour (TODO)
        raise NotImplementedError('slicing not fully implemented')
        # this is wierd...

        # according documentation:
        # "The slice of s from i to j with step k is defined as the sequence
        #  of items with index x = i + n*k such that 0 <= n < (j-i)/k.
        #  In other words, the indices are i, i+k, i+2*k, i+3*k and so on,
        #  stopping when j is reached (but never including j).
        #  When k is positive, i and j are reduced to len(s) if they are greater.
        #  When k is negative, i and j are reduced to len(s) - 1 if they are greater.
        #  If i or j are omitted or None, they become “end” values
        #  (which end depends on the sign of k).
        #  Note, k cannot be zero. If k is None, it is treated like 1."
        #  That should mean that for for range(5,10,4) = [5,9],
        #  the slice [100:100] should return range(2,2,4)
        #  but instead range(13,13,4) is returned...

        return Myrange(start, stop, step)

    def __getitem__(self, key):
        # Return self[key].
        if isinstance(key, slice):
            return self.__slice__(key)

        if not isinstance(key, int):
            raise TypeError(
                f' range indices must be integers or slices,'
                f' not \'{type(key)}\'')

        if not self.__contains__(key):
            raise IndexError('range object index out of range')

        # negative index
        if key < 0:
            key = self._len + key

        return self.start + self.step * key

    # with generators
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

    def __iter__(self):
        # 2nd version
        start, stop, step = (self.start, self.stop, self.step)
        # negative shrinking distance
        if (start - stop) // step < 0:
            # allignement: next value congruent to start modulo step.
            stop += (start - stop) % step
            while start != stop:
                yield start
                start += step

    '''
    def __iter__(self):
        # 3rd and final
        return Rangeiter(self)
    '''

    def __reversed__(self):
        # Return a reverse iterator.
        # delegates the problem to slicing
        # so wouldn't work currently
        return iter(self[:-1])

    def __reversed__(self):
        # 2nd version (using sign)
        sign = self.step / abs(self._step)
        start = self.start + ((self._len - 1) * self.step)
        stop = self.start - sign  # depends on sign
        step = -1 * self.step  # changes with direction
        return Rangeiter(Myrange(start, stop, step))

    def __reversed__(self):
        # 3rd  and final
        start, step = self.start, self.step
        # stop = self.stop + congruence
        stop = self.stop + (start - self.stop) % step
        return Rangeiter(Myrange(stop - step, start - step, -step))

    def __repr__(self):
        # Return repr(self).
        stop = ', ' + str(self.stop) if self.stop != DEF_STOP else ''
        step = ', ' + str(self.step) if self.step != DEF_STEP else ''
        return f'Myrange({self.start}{stop}{step})'

    def count(self, key):
        # Rangeobject.count(value) -> integer
        # Return number of occurrences of value.
        # a number should appear at most once...
        return 1 if key in self else 0

    def index(self, key):
        # rangeobject.index(value) -> integer
        # return index of value.
        if not self.__contains__(key):
            raise ValueError(f'{key} is not in range')
        return (key - self.start) // self.step
