from player import *
import sys
#contains the intro text
def intro():
    intro = "Welcom! Time to play! Try to use all of your letters. \n The first player that uses all of their letters wins!\n")
    return intro

#will be used when asking num of players get user int to make sure it is legal and no whitespace
def GetUserInt(userint):
    if userint > 0:
        return int(userint)
    GetNumPlayers()

#get user string remove whitespace for easy handling
def GetUserString(userstring):

#converts the user input into lower case so everything fits
def converToLower(word):
    word.lower()
    return word
#uses getuserint to get number of players specificaly may be able to remove and have just getuserint
def GetNumPlayers():
    answer = input('How many players will be playing? ')
    TestedAnswer = GetUserInt(answer)
    return TestedAnswer

#from the int of how many users creates that many players return dictionary 1:player1 etc
def SetUpPlayers(usernumber):

#tells whos turn it is to make sure everyone gets a turn
def determineTurn(turn):

#will get dictionary of players and what turn it is in order to run a turn
def gameTurn(players, turn):

#is the game
def main():
    print(intro())
    usernumber = GetNumPlayers()
    players = SetUpPlayers(usernumber)
    print("Great! Now we can play!")
    run = True
    turn = 1
    while run == True
        determineTurn(turn)
        players = gameTurn(players, turn)
