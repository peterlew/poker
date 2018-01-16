
import Scoring
import Deck
import copy

def simulateRound(game):
    if game.phase == 5:
        return Scoring.scoreRound(game)
    cardsNeeded = 5 - game.phase
    game.community += game.deck.deal(cardsNeeded)
    winners = Scoring.scoreRound(game)
    game.deck.deck += game.community[-cardsNeeded:]
    game.community = game.community[:-cardsNeeded]
    return winners

def predictHand(game, staticPlayers):
    retainHands = {}
    origDeck = copy.copy(game.deck)
    alterPlayers = copy.copy(game.players)
    for player in staticPlayers:
        alterPlayers.remove(player)
    for player in alterPlayers:
        retainHands[player] = copy.deepcopy(player.hand)
    for player in staticPlayers:
        player.handPerc = 0
    for i in xrange(100):
        for player in alterPlayers:
            game.deck.deck += player.hand.cards
        for player in alterPlayers:
            player.hand = Deck.Hand(game.deck)
        result = simulateRound(game)
        for player in staticPlayers:
            if player in result:
                player.handPerc += 1
    for player in alterPlayers:
        player.hand = retainHands[player]
    game.deck = origDeck

def predictRound(game):
    for player in game.players:
        player.winPerc = 0
    for i in xrange(100):
        for winner in simulateRound(game):
            winner.winPerc += 1
    for player in game.players:
        predictHand(game, [player])
