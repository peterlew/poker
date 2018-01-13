
import sys
import os

cardSym = "\xE2\x96\x88"

def displayGameState(game):
    os.system('clear')
    for i in xrange(0, 3):
        print
    print "\t\t\t" + str(game.pot)
    print
    print
    for i in xrange(0, game.phase):
        sys.stdout.write("\t" + str(game.community[i]))
    for i in xrange(game.phase, 5):
        sys.stdout.write("\t" + cardSym)
    print 
    print
    print
    for player in game.players:
        stackStr = str(player.stack)
        if player.isActing:
            stackStr = '\x1b[1;30;47m' + stackStr + '\x1b[0m'
        if player.justWon:
            stackStr = '\x1b[1;30;42m' + stackStr + '\x1b[0m'
        print "  " + stackStr + "\t" + str(player.hand) + "  " + str(player.playerBet) +  "\t\t\t\t" + "ODDS"
        print
    print
    print
