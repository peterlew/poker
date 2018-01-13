
import sys
import os

cardSym = "\xE2\x96\x88"

def displayGameState(game):
    os.system('clear')
    for i in xrange(0, 3):
        print
    print "\t\t\t" + str(game.round.pot)
    print
    print
    for i in xrange(0, 5):
        sys.stdout.write("\t" + cardSym)
    print 
    print
    print
    for player in game.players:
        print "  " + str(player.stack) + "\t" + str(player.hand) + "  " + str(player.playerBet) +  "\t\t\t\t" + "ODDS"
        print
    print
    print
