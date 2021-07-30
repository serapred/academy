from maps import MORSE


class Codec(object):
    """Codec Class

    This class allows to encode/decode string from/to
    the morse code.
    A generalization could be made by isolating the
    separators of encoder/decoder

    """
    encoder = MORSE
    decoder = {v: k for k, v in encoder.items()}
    alpha = {s for s in ''.join(decoder.keys())}

    @classmethod
    def _encode_char(cls, char):
        return cls.encoder[char]

    @classmethod
    def _encode_word(cls, word):
        # technically, in morse code, letters are
        # separated by 1 space, while words by 3
        # for readability 1, and 2  spaces will be used

        mword = map(cls._encode_char, list(word))
        return ' '.join(mword)

    @classmethod
    def _encode_line(cls, line):

        mline = map(cls._encode_word, line.split(' '))
        return '  '.join(mline)

    @classmethod
    def encode(cls, text):
        mtext = map(cls._encode_line, text.split('\n'))
        return '\n'.join(mtext)

    @classmethod
    def _decode_char(cls, char):
        return cls.decoder[char]

    @classmethod
    def _decode_word(cls, word):
        mword = map(cls._decode_char, word.split(' '))
        return ''.join(mword)

    @classmethod
    def _decode_line(cls, line):
        mline = map(cls._decode_word, line.split('  '))
        return ' '.join(mline)

    @classmethod
    def decode(cls, text):
        mtext = map(cls._decode_line, text.split('\n'))
        return '\n'.join(mtext)

    @classmethod
    def is_encoded(cls, text):
        return set(text).issubset(cls.alpha.union(' \n'))


class ConversionHandler(object):
    """ Conversion Handler

    operates with two types of streams of
    characters converting to/from a specified alphabet
    via a minimalistic codec interface.
    Each stream  parameter left to None,
    opens the correspondent system standard.

    :param codec: Codec class
    :type codec: Codec
    """
    codec = Codec
    newline = '\n'

    @classmethod
    def convert_stream(cls, src, dst):
        try:
            for line in src:
                line = line.rstrip(cls.newline)
                if cls.codec.is_encoded(line):
                    dst.write(cls.codec.decode(line) + cls.newline)
                else:
                    dst.write(cls.codec.encode(line) + cls.newline)
        except KeyboardInterrupt:
            pass  # something more useful?


if __name__ == '__main__':
    c = Codec
    h = ConversionHandler

    with open(0, 'r') as stdin, open(1, 'w') as stdout:
        h.convert_stream(stdin, stdout)
