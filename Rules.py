
import Deck

'''
Straight flush  rank
4 of a kind     rank
full house      rank    2nd rank
flush           rank    2nd rank    3rd rank    4th rank    5th rank
straight        rank 
3s              rank    2nd rank    3rd rank
two pair        rank    2nd rank    3rd rank
pair            rank    2nd rank    3rd rank    4th rank
high cards      rank    2nd rank    3rd rank    4th rank    5th rank
'''

def dealFive(deck):
    cards = []
    for i in xrange(1, 6):
        cards.append(deck.deal())
    return cards

def dictFromRanks(ranks):
    rankDict = {}
    for rank in ranks:
        if rank in rankDict:
            rankDict[rank] += 1
        else:
            rankDict[rank] = 1
    return rankDict

def evalFive(cards):
    sortedRanks = sorted(map(lambda card: card.rank, cards))
    rankDict = dictFromRanks(sortedRanks)
    groupedRanks = [(v, k) for k, v in rankDict.iteritems()]
    sortedGroupedRanks = sorted(groupedRanks, )
    return groupedRanks
'''
    isFlush = all(card.suit == cards[0].suit) for card in cards
    isStraight = sortedRanks == range(sortedRanks[0], sortedRanks[4] + 1)
    eval = [0, 0, 0, 0, 0]
    if(isFlush and isStraight):
        eval[0] = 9
    elif()
'''
