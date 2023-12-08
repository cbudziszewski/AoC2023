from enum import Enum

class HandType(Enum):
    HIGHCARD = 0
    ONEPAIR = 1
    TWOPAIR = 2
    THREEOFAKIND = 3
    FULLHOUSE = 4
    FOUROFAKIND = 5
    FIVEOFAKIND = 6

class Hand:
    def __init__(self, cards, bid = 0, joker = False):
        self._CARD_VALUE=['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
        if joker:
            self._CARD_VALUE=['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
        self._CARD_VALUE.reverse()
        self.cards = cards
        self.bid = bid
        self.joker = joker

    def handtype(self):
        cardcount = sorted([self.cards.count(v) for v in set(self.cards)])
        if self.joker and self.cards.count('J') < 5:
            cardcount = sorted([self.cards.count(v) for v in set(self.cards.replace('J',''))])
            cardcount[-1] += self.cards.count('J') 

        mapping = dict()
        mapping['11111'] = HandType.HIGHCARD
        mapping['1112']  = HandType.ONEPAIR
        mapping['122']   = HandType.TWOPAIR
        mapping['113']   = HandType.THREEOFAKIND
        mapping['23']    = HandType.FULLHOUSE
        mapping['14']    = HandType.FOUROFAKIND
        mapping['5']     = HandType.FIVEOFAKIND
        return mapping[''.join(map(str,cardcount))]

    def as_number(self):
        return "" + f"{self.handtype().value}" + ''.join([ f"{self._CARD_VALUE.index(x):02d}" for x in self.cards])

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
            if self._CARD_VALUE.index(c1) < other._CARD_VALUE.index(c2):
                return 1
            if self._CARD_VALUE.index(c1) > other._CARD_VALUE.index(c2):
                return -1
        return 0
