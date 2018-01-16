
import Deck
import Display
import Scoring
import Prediction
from Player import User, Caller, Statistician
from time import sleep
from random import choice

import pdb

waitTime = 0.5

class Game: 

    def __init__(self, players, stack, godMode):
        self.godMode = godMode
        self.players = []
        for i in xrange(len(players)):
            newP = players[i](stack)
            newP.position = i
            self.players.append(newP)

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
        self.community = []
        self.roundOver = False
        Prediction.predictRound(self)
        Display.displayGameState(self)

    def flop(self):
        self.phase = 3
        self.community += self.deck.deal(3)
        Prediction.predictRound(self)
        Display.displayGameState(self)

    def turn(self):
        self.phase = 4
        self.community += self.deck.deal(1)
        Prediction.predictRound(self)
        Display.displayGameState(self)

    def river(self):
        self.phase = 5
        self.community += self.deck.deal(1)
        Prediction.predictRound(self)
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
        self.ante()
        self.betAction()
        self.flop()
        self.betAction()
        self.turn()
        self.betAction()
        self.river()
        self.betAction()
        self.roundOver = True
        winners = Scoring.scoreRound(self)
        self.awardPot(winners)
        self.elmination()

    def awardPot(self, winners):
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

    def elmination(self):
        for player in self.players:
            if player.stack == 0:
                self.players.remove(player)
        if len(self.players) == 1:
            self.players[0].justWon = True
            Display.displayGameState(self)
            raw_input("Play again?")
            self.__init__(*newGameParams)

    def ante(self):
        for player in self.players:
            player.stack -= 1
            self.pot += 1

newGameParams = [[User, Statistician], 100, False]
g = Game(*newGameParams)
while True:
    g.playRound()


