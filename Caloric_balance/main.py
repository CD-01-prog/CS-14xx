from caloric_balance import *
import sys

def formatMenu():
    menu = ['What would you like to do?', '[f] Record Food Consumption', '[a] Record Physical Activity', '[q] Quit']
    return menu

def formatMenuPrompt():
    answer = input("Enter an option: ")
    return answer

def formatActivityMenu():
    options = ['Choose an activity to record', '[j] Jump rope', '[r] Running', '[s] Sitting', '[w] Walking']
    return options

def getUserString(question):
    userAnswer = question
    if len(userAnswer) == 0:
        userAnswer = input(question)
    userAnswer.strip()
    return userAnswer

def getUswerFloat(question):
    userAnswer = 0.0
    if userAnswer <= 0.0 and isinstance(userAnswer, float):
        userAnswer = input(question)
    return float(userAnswer)

def createCaloricBalance():
    gender = input("your gender(f or m): ")
    age = input("your age: ")
    height = input("your height(in inches): ")
    weight = input("your weight(in pounds): ")
    Caloric_Balance = CaloricBalance(gender, age, height, weight)
    return Caloric_Balance

def recordActivityAction(CaloricBalance):
    menu = formatActivityMenu()
    powerpoints = {}
    for item in menu:
        print(item)
        powerpoints[item[1]] = 0
    powerpoints['j'] = .03
    powerpoints['r'] = .05
    powerpoints['s'] = .01
    powerpoints['w'] = .02
    userAnswer = input("which activity did you do?: ")
    for key in powerpoints:
        if key == userAnswer:
            userTime = input("how long did you do it?: ")
            try:
              int(userAnswer)
            except(ValueError):
              print("please enter a number")
              return
            if int(userAnswer) <= 0:
              print("please pick a number greater then 0")
              return
            CaloricBalance.recordActivity(powerpoints[key], userTime)
            print("your balance has been updated")
            return
    print("that is not a known activity sorry")
    return

def eatFoodAction(CaloricBalance):
    userAnswer = input("how many calories did you eat?: ")
    try:
      int(userAnswer)
    except(ValueError):
      print("please enter a number")
      return
    if int(userAnswer) <= 0:
      print("please pick a number greater then 0")
      return
    else:
      CaloricBalance.eatFood(userAnswer)
    print("record updated thank you")
    return

def quitAction(CaloricBalance):
    print("program over have a good day")
    sys.exit(0)

def applyAction(CaloricBalance, choice):
    choice.strip()
    if choice == 'f':
        eatFoodAction(CaloricBalance)
        return CaloricBalance
    elif choice == 'a':
        recordActivityAction(CaloricBalance)
        return CaloricBalance
    elif choice == 'q':
        quitAction(CaloricBalance)
        return
    else:
        print("that command is not athurized raise your command level to try that command")
        return CaloricBalance

def main():
    run = True
    print("Hi! This program will calculate your caloric balance for the day! Before we can start, I need some information about you. Be honest!\n")
    CaloricBalance = createCaloricBalance()
    menu = formatMenu()
    print("\nThanks! Now, throughout the day, tell me each time you eat or move.Your caloric balance is starting at " + str(CaloricBalance.getBalance())  + "(you need to eat something)\n")
    while run:
        for line in menu:
          print(line)
        choice = getUserString(formatMenuPrompt())
        CaloricBalance = applyAction(CaloricBalance, choice)
        print('\n')

if __name__ == '__main__':
    main()
