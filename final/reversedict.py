"""
Exercise 1 – Dictionary reversals
The candidate is required to implement the function reverse_dict which receives as input a dictio-
nary D1 and returns a dictionary D2, whose content will have as keys the values of D1 and as values

those keys of D1 the values are assigned to.
Example:

 D1 = {
 ”MIO”: 102,
 ”ADS”: 105,
 ”DGI”: 107,
 ”VBE”: 105,
 ”FFI”: 102
 }

 D2 = reverse_dict(D1)

 # D2 will have the following content

 D2 = {
 102: [”FFI”, ”MIO”],
 105: [”ADS”, ”VBE”],
 107: [”DGI”]
 }

"""


def reverse(dictionary):
    return {v: k for k, v in dictionary.items()}


if __name__ == '__main__':

    a = {'a': 1, 'b': 2}
    print(reverse(a))
