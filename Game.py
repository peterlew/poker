
import Deck
import Display
from time import sleep

class Player:
    def __init__(self, stack):
        self.stack = stack
        self.playerBet = 0

    def playerAction(self, game):
        activeBet = game.round.activeBet
        if activeBet > self.stack:
            self.fold(game.round)
            return -1
        else:
            self.makeBet(game, activeBet)
            return 1

    def fold(self, round):
        self.playerBet = "F"
        round.players.remove(self)
        self.active = False

    def makeBet(self, game, bet):
        game.round.activeBet = bet
        betDiff = bet - self.playerBet
        self.stack -= betDiff
        game.round.pot += betDiff
        self.playerBet = bet

class User(Player):
    def __init__(self, stack):
        Player.__init__(self, stack)

    def playerAction(self, game):
        activeBet = game.round.activeBet
        bet = raw_input("Bet? ")
        if bet == "f":
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
        desiredBet = game.round.activeBet + 1
        if desiredBet > self.stack:
            self.fold(game.round)
            return -1
        else:
            self.makeBet(game, desiredBet)
            return 1

class Folder(Player):
    def __init__(self, stack):
        Player.__init__(self, stack)

    def playerAction(self, game):
        if game.round.activeBet > 0:
            self.fold(game.round)
            return -1

class Round: 
    def __init__(self, players):
        self.deck = Deck.Deck()
        self.players = list(players)
        for player in self.players:
            player.hand = (Deck.Hand(self.deck))
            player.active = True
        self.pot = 0
        self.activeBet = 0

class Game:
    def __init__(self, players, stack):
        self.players = []
        for player in players:
            self.players.append(player(stack))
        self.round = Round(self.players)

def betAction(game):
    round = game.round
    for player in game.players:
        if not player.active:
            continue
        player.playerAction(game)
        Display.displayGameState(game)
        sleep(0.5)
    while True:
        for player in game.players:
            if not player.active:
                continue
            if all(player.playerBet == round.players[0].playerBet for player in round.players):
                return
            player.playerAction(game)
            Display.displayGameState(game)
            sleep(0.5)

def playGame(numPlayers, stack):
    game = Game(numPlayers, stack)
    Display.displayGameState(game)
    betAction(game)

playGame([User, Folder, Player, Raiser, Player], 100)


