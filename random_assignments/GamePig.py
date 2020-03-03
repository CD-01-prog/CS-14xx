import random
def main():
  #starting point of both players
    player1 = 0
    player2 = 0
    temp_score = 0
    i = 1
    intro()
    score_disply(player1, player2)
    while player1 < 100 or player2 < 100:
        if i % 2 == 0:
          player2 = turn(i, player1, player2, temp_score)
          
        else:
          player1 = turn(i, player1, player2, temp_score)
        score_disply(player1, player2)
        i = i + 1
    print("The game is over.\n")
    score_disply(player1, player2)
    if player1 > player2:
        print("Player 1 wins.")
    else:
        print("Player 2 wins.")

def turn(i, player1, player2, temp_score):
#sets up the variables to keep track of for only this turn
    turn_roll = 0
    turn_points = 0
    player_turn = 1
    #determines whos turn it is
    if i % 2 == 0:
      player_turn = 2
    else:
      player_turn = 1
    #start player turn and determines the points 
    proceed = input("Player " + str(player_turn) + " press enter to begin your turn.\n")
    turn_roll = roll()
    print("You rolled a " + str(turn_roll))
    #check to see if rolled a 1 to quit or contniue
    if turn_roll == 1:
      turn_points = 0
      temp_score = 0
      return 0
    else:
      turn_points = turn_points + turn_roll
      print("Your turn points are now " + str(turn_points) + ".")
      proceed = input("continue rolling(1 for yes 0 for no)?")
      #check to see if player wants to keep rolling
      proceed = proceed.strip()
      if str(proceed) == str(1):
        if player_turn == 1:
          temp_score = temp_score + turn_points
          turn(i, player1, player2, temp_score)
        else:
          temp_score = temp_score + turn_points
          turn(i, player1, player2, temp_score)
      #if not returns the scores the player got 
      else:
        if player_turn == 1:
          player1 = player1 + turn_points + temp_score
          print(player1)
          return player1
        else:
          player2 = player2 + turn_points + temp_score
          return player2
    

#display score of both players
def score_disply(player1, player2):
    print("Player 1 has " + str(player1) + " points.\n")
    print("Player 2 has " + str(player2) + " points.\n")
    print("==================================================================\n")
    return

#is the dice
def roll():
    D6dice = random.randrange(1,7)
    return D6dice

#is the starting text to explain the game
def intro():
    print("""Welcome to the Game of Pig. To win, be the player with the most points at the end of the game. The game ends at the end of a round where at least one player has 100 or more points.\n""")
    print("""On each turn, you may roll the die as many times as you like to obtain more points.  However, if you roll a 1, your turn is over, and you do not obtain any points that turn.\n""")
    return

main()
