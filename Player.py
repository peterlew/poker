
class Player:
    def __init__(self, stack):
        self.stack = stack
        self.playerBet = 0
        self.isActing = False
        self.justWon = False
        self.type = "Bot"

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
        self.type = "User"

    def playerAction(self, game):
        activeBet = game.activeBet
        bet = raw_input("Bet? ")
        if bet == "f":
            self.fold(game)
            return
        if bet == "":
            bet = activeBet
        bet = int(bet)
        while bet < activeBet:
            bet = raw_input("Current bet is " + str(activeBet) + ". Bet? ")
            if bet == "":
                bet = activeBet
            bet = int(bet)
        self.makeBet(game, bet)

class Caller(Player):
    def playerAction(self, game):
        self.makeBet(game, game.activeBet)

class Raiser(Player):
    def playerAction(self, game):
        desiredBet = game.activeBet + 1
        if desiredBet > self.stack:
            self.fold(game)
        else:
            self.makeBet(game, desiredBet)

class Folder(Player):

    def playerAction(self, game):
        if game.activeBet > 0:
            self.fold(game)
            return -1

class Wimp(Player):

    def playerAction(self, game):
        if game.activeBet > self.stack / 2:
            self.fold(game)
            return -1
        else:
            self.makeBet(game, game.activeBet)
            return 1

class Statistician(Player):

    def playerAction(self, game):
        odds = self.handPerc / 100.0
        desiredBet = max(int((game.pot * odds) / (1 - odds)) - 1, 0)
        req = game.activeBet - self.playerBet
        if req > desiredBet:
            self.fold(game)
            return
        else:
            self.makeBet(game, self.playerBet + min(self.stack, desiredBet))




