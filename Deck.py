
from random import choice

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        if self.rank > 9:
            rankPrint = ['T', 'J', 'Q', 'K', 'A'][self.rank - 10]
        else:
            rankPrint = str(self.rank)
        rankPrint = '\x1b[0;37;44m' + rankPrint + '\x1b[0m'
        suitSymbols = {'s' : '\x1b[0;30;44m\xE2\x99\xA0\x1b[0m',
                       'c' : '\x1b[0;30;44m\xE2\x99\xA3\x1b[0m',
                       'h' : '\x1b[0;31;44m\xE2\x99\xA5\x1b[0m',
                       'd' : '\x1b[0;31;44m\xE2\x99\xA6\x1b[0m'}  
        return rankPrint + suitSymbols[self.suit]

    def __repr__(self):
        return self.__str__()

class Deck:

    def __init__(self):
        self.deck = []
        for suit in ['s', 'h', 'd', 'c']:
            for rank in xrange(2, 15):
                self.deck.append(Card(rank, suit))

    def deal(self, numCards):
        cards = []
        for i in xrange(0, numCards):
            pick = choice(self.deck)
            self.deck.remove(pick)
            cards.append(pick)
        return cards

class Hand:

    def __init__(self, deck):
        self.cards = deck.deal(2)

    def __str__(self):
        return str(self.cards[0]) + " " + str(self.cards[1])

    def __repr__(self):
        return self.__str__()








