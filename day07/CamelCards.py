from enum import Enum

class HandType(Enum):
    HIGHCARD = 0
    ONEPAIR = 1
    TWOPAIR = 2
    THREEOFAKIND = 3
    FULLHOUSE = 4
    FOUROFAKIND = 5
    FIVEOFAKIND = 6

CARD_VALUE=['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
CARD_VALUE.reverse()

class Hand:
    def __init__(self, cards, bid = 0):
        self.cards = cards
        self.bid = bid

    def handtype(self):
        mapping = dict()
        mapping['11111'] = HandType.HIGHCARD
        mapping['1112']  = HandType.ONEPAIR
        mapping['122']   = HandType.TWOPAIR
        mapping['113']   = HandType.THREEOFAKIND
        mapping['23']    = HandType.FULLHOUSE
        mapping['14']    = HandType.FOUROFAKIND
        mapping['5']     = HandType.FIVEOFAKIND
        return mapping[''.join(sorted([str(self.cards.count(v)) for v in set(self.cards)]))]

    def as_number(self):
        return "" + f"{self.handtype().value}" + ''.join([ f"{CARD_VALUE.index(x):02d}" for x in self.cards])

    def __str__(self):
        return f"Hand({self.cards}, {self.bid})"

    def __repr__(self):
        return f"Hand({self.cards}, {self.bid})"

    def compare (self, other):
        if self.handtype().value < other.handtype().value:
            return 1
        if self.handtype().value > other.handtype().value:
            return -1
        for c1, c2 in zip(self.cards, other.cards):
            if CARD_VALUE.index(c1) < CARD_VALUE.index(c2):
                return 1
            if CARD_VALUE.index(c1) > CARD_VALUE.index(c2):
                return -1
        return 0


