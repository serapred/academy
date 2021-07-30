def bubble_sort(collection):

    swap = True  # determines if at any scan a swap op has taken place
    length = len(collection)

    while swap:
        swap = False
        for i in range(0, length - 1):
            if collection[i] > collection[i + 1]:
                collection[i], collection[i + 1] = collection[i + 1], collection[i]
                swap = True

        # decrementing the length on the assumption that
        # at each iteration the n-ith element will be
        # in its final position
        length -= 1

    return collection


if __name__ == '__main__':

    a = [2, 4, 12, 18, 5, 7, 9, 15, 12]
    b = bubble_sort(a)
    print(b)
