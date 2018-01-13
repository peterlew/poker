
import Deck
import Display
import Scoring
from time import sleep
from random import choice

import pdb

waitTime = 0.1

class Player:
    def __init__(self, stack):
        self.stack = stack
        self.playerBet = 0
        self.isActing = False
        self.justWon = False

    def playerAction(self, game):
        activeBet = game.activeBet
        if activeBet > self.stack + self.playerBet:
            self.fold(game)
            return -1
        else:
            self.makeBet(game, activeBet)
            return 1

    def fold(self, game):
        self.playerBet = "F"
        game.activePlayers.remove(self)
        self.active = False

    def makeBet(self, game, bet):
        game.activeBet = bet
        betDiff = bet - self.playerBet
        self.stack -= betDiff
        game.pot += betDiff
        self.playerBet = bet

class User(Player):
    def __init__(self, stack):
        Player.__init__(self, stack)

    def playerAction(self, game):
        activeBet = game.activeBet
        bet = raw_input("Bet? ")
        if bet == "f":
            self.fold(game)
            return -1
        if bet == "":
            bet = activeBet
        bet = int(bet)
        while bet < activeBet:
            bet = raw_input("Current bet is " + str(activeBet) + ". Bet? ")
            if bet == "":
                bet = activeBet
            bet = int(bet)
        self.makeBet(game, bet)
        return 1

class Raiser(Player):
    def __init__(self, stack):
        Player.__init__(self, stack)

    def playerAction(self, game):
        desiredBet = game.activeBet + 1
        if desiredBet > self.stack:
            self.fold(game)
            return -1
        else:
            self.makeBet(game, desiredBet)
            return 1

class Folder(Player):
    def __init__(self, stack):
        Player.__init__(self, stack)

    def playerAction(self, game):
        if game.activeBet > 0:
            self.fold(game)
            return -1

class Game: 

    def __init__(self, players, stack):
        self.players = []
        for player in players:
            self.players.append(player(stack))

    def newRound(self):
        self.deck = Deck.Deck()
        self.activePlayers = list(self.players)
        for player in self.activePlayers:
            player.hand = Deck.Hand(self.deck)
            player.active = True
            player.playerBet = 0
        self.pot = 0
        self.activeBet = 0
        self.phase = 0
        Display.displayGameState(self)

    def flop(self):
        self.phase = 3
        self.community = self.deck.deal(3)
        Display.displayGameState(self)

    def turn(self):
        self.phase = 4
        self.community += self.deck.deal(1)
        Display.displayGameState(self)

    def river(self):
        self.phase = 5
        self.community += self.deck.deal(1)
        Display.displayGameState(self)

    def betAction(self):
        for player in self.players:
            if not player.active:
                continue
            player.isActing = True
            Display.displayGameState(self)
            player.playerAction(self)
            sleep(waitTime)
            player.isActing = False
        while True:
            for player in self.players:
                if not player.active:
                    continue
                if all(player.playerBet == self.activePlayers[0].playerBet for player in self.activePlayers):
                    Display.displayGameState(self)
                    sleep(waitTime)   
                    self.activeBet = 0
                    for player in self.players:
                        if player.playerBet != "F":
                            player.playerBet = 0
                        player.isActing = False
                    return
                player.isActing = True
                Display.displayGameState(self)
                player.playerAction(self)
                sleep(waitTime)
                player.isActing = False

    def playRound(self):
        self.newRound()
        self.betAction()
        self.flop()
        self.betAction()
        self.turn()
        self.betAction()
        self.river()
        self.betAction()
        bestScore = [0, 0, 0, 0, 0, 0]
        winners = []
        for player in self.activePlayers:
            score = Scoring.evalCards(self.community + player.hand.cards)
            if score >= bestScore:
                if score == bestScore:
                    winners.append(player)
                else:
                    winners = [player]
                bestScore = score
        potSplit = self.pot / len(winners)
        potExtra = self.pot % len(winners)
        for winner in winners:
            winner.justWon = True
        Display.displayGameState(self)
        raw_input("Press ENTER to continue")
        for winner in winners:
            winner.justWon = False
            winner.stack += potSplit
        choice(winners).stack += potExtra

g = Game([User, Folder, Player, Raiser, Player], 100)
while True:
    g.playRound()


