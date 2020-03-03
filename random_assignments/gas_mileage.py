import sys

def milesPerGallon(miles, gallons):
    if gallons == 0.0:
        return 0.0
    answer = miles/gallons
    return float(answer)

def createNotebook():
    return []

def recordTrip(notebook, date, miles, gallons):
    dictionary = {}
    dictionary['date'] = date
    dictionary['miles'] = miles
    dictionary['gallons'] = gallons
    notebook.append(dictionary)
    return

def listTrips(notebook):
    for trip in notebook:
        print("On " + str(trip['date']) + ": " + str(trip['miles']) + " miles traveled using " + str(trip['gallons']) + " gallons. Gas mileage: " + str(milesPerGallon(trip['miles'],trip['gallons'])) + " MPG,")
    return

def calculateMPG(notebook):
    TGallons = 0.0
    Tmiles = 0.0
    for trip in notebook:
        TGallons += trip['gallons']
        Tmiles += trip['miles']
    MPG = milesPerGallon(Tmiles, TGallons)
    return MPG

def formatMenu():
    menu = ['What would you like to do?', '[r] Record Gas Consumption', '[l] List Mileage History', '[c] Calculate Gas Mileage', '[q] Quit']
    return menu

def formatMenuPrompt():
    answer = input("Enter an option: ")
    return answer

def getUserString(question):
    userAnswer = ''
    while len(userAnswer) == 0:
        userAnswer = input(question)
    userAnswer.strip()
    return userAnswer

def getUserFloat(question):
    userAnswer = 0.0
    while float(userAnswer) <= 0.0:
        userAnswer = input(question)
        while True:
            try:
                float(userAnswer)
            except(ValueError):
                userAnswer = input(question + " please be reasonable")
            else:
                break
    return float(userAnswer)

def getDate():
    userAnswer = getUserString("date please.")
    return userAnswer

def getMiles():
    miles = getUserFloat("miles please.")
    return miles

def getGallons():
    gallons = getUserFloat("gallons please.")
    return gallons

def recordTripAction(notebook):
    date = getDate()
    miles = getMiles()
    gallons = getGallons()
    recordTrip(notebook, date, miles, gallons)
    print("adventure recorded")
    return

def listTripsAction(notebook):
    if len(notebook) == 0:
        print("you still need to go on a trip")
    listTrips(notebook)
    return

def calculateMPGAction(notebook):
    if len(notebook) == 0:
        print("you still need to go on a trip")
        return
    answer = calculateMPG(notebook)
    print("On average you do " + str(answer) + " MPG a trip")
    return

def quitAction(notebook):
    print("come back soon")
    sys.exit(0)

def applyAction(notebook, choice):
    choice.strip()
    if choice == 'r':
        index = recordTripAction(notebook)
        return notebook
    elif choice == 'l':
        listTripsAction(notebook)
        return notebook
    elif choice == 'c':
        calculateMPGAction(notebook)
        return notebook
    elif choice == 'q':
        quitAction(notebook)
    elif choice == 'x':
        print("so what are you looking for funny person")
        return notebook
    else:
        print("non-approved command retry or raise your command level")
        return notebook

def main():
    notebook = createNotebook()
    run = True
    while run == True:
        for line in formatMenu():
          print(line)
        choice = formatMenuPrompt()
        notebook = applyAction(notebook, choice)
        print("\n")

if __name__ == '__main__':
    main()
main()
