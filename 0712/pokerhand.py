"""
Poker hand ranking

In this challenge, you have to establish which kind of Poker combination is present in a deck of five
cards. Every card is a string containing the card value (with the upper-case initial for face-cards) and the lower-case initial for suits, as in the examples below:

"Ah" Ace of hearts
"Ks" King of spades
"3d" Three of diamonds
"Qc" Queen of clubs

There are 10 different combinations. Here's the list, in decreasing order of importance:
Name Description

- Royal Flush -> A, K, Q, J, 10, all with the same suit.               # sequence
- Straight Flush -> Five cards in sequence, all with the same suit.    # sequence + color
- Four of a Kind -> Four cards of the same rank.                       # rank
- Full House -> Three of a Kind with a Pair.                           # rank+
- Flush -> Any five cards of the same suit, not in sequence.           # color
- Straight -> Five cards in a sequence, but not of the same suit.      # sequence
- Three of a Kind -> Three cards of the same rank.                     # rank
- Two Pair -> Two different Pair.                                      # rank+
- Pair -> Two cards of the same rank.                                  # rank
- High Card -> No other valid combination.                             # rank- (base)

Given a list hand containing five strings being the cards, implement a function that returns a string
with the name of the highest combination obtained, accordingly to the table above.

Ex:
poker_hand_ranking(["10h", "Jh", "Qh", "Ah", "Kh"]) "Royal Flush"
poker_hand_ranking(["3h", "5h", "Qs", "9h", "Ad"]) "High Card"
poker_hand_ranking(["10s", "10c", "8d", "10d", "10h"]) "Four of a Kind"

"""

from collections import OrderedDict

SUITS = {'s': 'spades', 'h': 'hearts', 'c': 'clubs', 'd': 'diamonds'}
VALUES = {'2': (2, 'two'), '3': (3, 'three'), '4': (4, 'four'),
          '5': (5, 'five'), '6': (6, 'six'), '7': (7, 'seven'),
          '8': (8, 'eight'), '9': (9, 'nine'), '10': (10, 'ten'),
          'J': (11, 'Jack'), 'Q': (12, 'Queen'), 'K': (13, 'King'),
          'A': (14, 'Ace')}

# range 2 - 14


class Card(object):
    """docstring for Card"""

    def __init__(self, value, suit):
        super(Card, self).__init__()

        if suit not in SUITS:
            raise ValueError(f'{suit} not among {self.suits}')

        if value not in VALUES:
            raise ValueError(f'{value} not among {self.values.keys()}')

        self.value = value
        self.suit = suit
        self.point = VALUES[value][0]
        self.vname = VALUES[value][1]
        self.sname = SUITS[suit]

    def __str__(self):
        return f'{self.vname} of {self.sname}'

    def __repr__(self):
        return f'Card({self.value},{self.suit})'


# assume sorted hand
def is_sequence(hand):
    return hand[-1].point - hand[0].point == 5


def is_color(hand):
    return len({c.suit for c in hand}) == 1


# point functions


def ranks(hand):

    values = {c.point for c in hand}

    return tuple([c.value for c in hand].count(c) for c in values)


class Evaluator(object):
    """docstring for Ranker"""

    @classmethod
    def eval(cls, hand):

        if len(hand) != 5:
            raise ValueError('hands must consist of exactly 5 cards')
        points = [c.points for c in hand]
        ranks = ranks(points)
        spoints = sorted(points)

        if not is_sequence(points):
            pass
        return max(ran)


if __name__ == '__main__':

    c1 = Card('A', 's')
    c2 = Card('8', 'h')
    c3 = Card('10', 'h')
    c4 = Card('2', 's')
    c5 = Card('Q', 'c')
    print(c1)
    h = [c1, c2, c3, c4, c5]
    e = Evaluator
    print(e.eval(h))
