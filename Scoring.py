
import Deck

'''
9. Straight flush  rank
8. 4 of a kind     rank
7. full house      rank    2nd rank
6. flush           rank    2nd rank    3rd rank    4th rank    5th rank
5. straight        rank 
4. 3s              rank    2nd rank    3rd rank
3. two pair        rank    2nd rank    3rd rank
2. pair            rank    2nd rank    3rd rank    4th rank
1. high cards      rank    2nd rank    3rd rank    4th rank    5th rank
'''

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

def evalCards(cards):
    numCards = len(cards)
    if numCards == 5:
        return evalFive(cards)
    bestHand = [0, 0, 0, 0, 0, 0]
    for i in xrange(0, numCards):
        evalHand = evalCards(cards[0:i] + cards[i+1:numCards])
        if evalHand > bestHand:
            bestHand = evalHand
    return bestHand




        


