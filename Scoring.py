
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
    groupedRanks = [[v, k] for k, v in rankDict.iteritems()]
    sortedGroupedRanks = sorted(groupedRanks)
    handPattern = [g for [g, r] in sortedGroupedRanks]
    handRanks = [r for [g, r] in sortedGroupedRanks]
    isFlush = all(card.suit == cards[0].suit for card in cards)
    isStraight = sortedRanks == range(sortedRanks[0], sortedRanks[4] + 1)
    eval = [0, 0, 0, 0, 0, 0]
    if(isFlush and isStraight):
        eval[0] = 9
        eval[1] = sortedRanks[4]
    elif(handPattern == [1, 4]):
        eval[0] = 8
        eval[1] = handRanks[1]
        eval[2] = handRanks[0]
    elif(handPattern == [2, 3]):
        eval[0] = 7
        eval[1] = handRanks[1]
        eval[2] = handRanks[0]
    elif(isFlush):
        eval[0] = 6
        for i in xrange(1, 6):
            eval[i] = sortedRanks[5 - i]
    elif(isStraight):
        eval[0] = 5
        eval[1] = sortedRanks[4]
    elif(handPattern == [1, 1, 3]):
        eval[0] = 4
        eval[1] = handRanks[2]
        eval[2] = handRanks[1]
        eval[3] = handRanks[0]
    elif(handPattern == [1, 2, 2]):
        eval[0] = 3
        eval[1] = handRanks[2]
        eval[2] = handRanks[1]
        eval[3] = handRanks[0]
    elif(handPattern == [1, 1, 1, 2]):
        eval[0] = 2
        eval[1] = handRanks[3]
        eval[2] = handRanks[2]
        eval[3] = handRanks[1]
        eval[4] = handRanks[0]
    elif(handPattern == [1, 1, 1, 1, 1]):
        eval[0] = 1
        for i in xrange (1, 6):
            eval[i] = handRanks[5 - i]
    return eval

def allCombos(ls):
    if len(ls) == 1:
        return [ls]
    else:
        map(lambda lst: lst.append(ls[0]), allCombos(ls))
        


