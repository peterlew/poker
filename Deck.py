
from random import choice

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        if self.rank > 10:
            rankPrint = ['J', 'Q', 'K', 'A'][self.rank - 11]
        else:
            rankPrint = str(self.rank)
        suitSymbols = {'s' : '\xE2\x99\xA0',
                       'c' : '\xE2\x99\xA3',
                       'h' : '\xE2\x99\xA5',
                       'd' : '\xE2\x99\xA6'}  
        return rankPrint + suitSymbols[self.suit]

    def __repr__(self):
        return self.__str__()

class Deck:

    def __init__(self):
        self.deck = []
        for suit in ['s', 'h', 'd', 'c']:
            for rank in xrange(2, 15):
                self.deck.append(Card(rank, suit))

    def deal(self):
        pick = choice(self.deck)
        self.deck.remove(pick)
        return pick

class Hand:

    def __init__(self, deck):
        self.card1 = deck.deal()
        self.card2 = deck.deal()

    def __str__(self):
        return str(self.card1) + " | " + str(self.card2)

    def __repr__(self):
        return self.__str__()








