import json
import string


with open('../files/morsedict.json') as jsonf:
    MORSE = json.load(jsonf)


UPPER = {k: v for k, v in zip(string.ascii_lowercase, string.ascii_uppercase)}
