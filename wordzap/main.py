import player

#contains the intro text
def intro():
	intro = "Welcom! Time to play! Try to use all of your letters. \n The first player that uses all of their letters wins!\n"
	return intro

#will be used when asking num of players get user int to make sure it is legal and no whitespace
def GetUserInt(question):
  userAnswer = 0
  while int(userAnswer) <= 0:
    userAnswer = input(question)
    while True:
      try:
        int(userAnswer)
      except(ValueError):
        userAnswer = input(question + " please be reasonable")
      else:
        break
  return int(userAnswer)

#get user string remove whitespace for easy handling
def GetUserString(question):
  userAnswer = ''
  userAnswer = input(question)
  userAnswer.strip()
  return userAnswer

#converts the user input into lower case so everything fits
def converToLower(word):
	word.lower()
	return word

#uses getuserint to get number of players specificaly may be able to remove and have just getuserint
def GetNumPlayers():
	TestedAnswer = GetUserInt("How many players will be playing?")
	return TestedAnswer

#from the int of how many users creates that many players return dictionary 1:player1 etc
def SetUpPlayers(usernumber):
  playerslist = []
  for i in range(int(usernumber)):
    item = player.Player(GetUserString("Enter name for player " + str(i + 1)))
    playerslist.append(item)
  return playerslist

#will get dictionary of players and what turn it is in order to run a turn
def gameTurn(players, turn):
  round = True
  while round:
    name = players[turn].getName()
    print(name +  ", it is your turn!")
    print("Your letters are: ")
    players[turn].printLetters()
    userAnswer = converToLower(GetUserString("Enter a word to play(or press enter to pass"))
    if userAnswer == "":
      players[turn].drawLetter()
      letters = players[turn].getLetters()
      print("You get another letter, " + letters[-1] + "\n")
      round = False
      return players
    elif players[turn].checkWord(userAnswer):
      print("Great job!\n")
      round = False
      return players
    print("the right letters were not found")
    print('\n')


#is the game
def main():
  print(intro())
  usernumber = GetNumPlayers()
  players = SetUpPlayers(usernumber)
  print("Great! Now we can play!\n")
  run = True
  turn = 0
  while run == True:
    if turn == usernumber:
      turn = 0
      print('Okay! Next round!\n')
    players = gameTurn(players, turn)
    if len(players[turn].getLetters()) == 0:
      name = players[turn].getName()
      print(name + " wins!!")
      run = False
    turn += 1

main()
