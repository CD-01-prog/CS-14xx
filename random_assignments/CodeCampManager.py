def loop_question(TFile):
    #this will append names to the file provided right before
    TFile.open(TFile, "a")
    out = 0
    TvM = 10
    #first while loop asks for team name to add and askes if they want to add more teams after the team member while loop
    while out == 0:
        TFile.append("Team " + input("Team name?"))
        #second while loop loops through asking for team members and appends them to file quits if enter is hit or 4 names are entered
        while TvM < 14:
            TvM = TvM + 1
            name = input("Team member?")
            if name == "":
                TvM = 15
            else:
                TFile.append("Member " + name)
        proceed = input("Another team?(y for yes and n for no)\n")
        if proceed == 'n':
            out = 1
        else:
            TvM = 10
    TFile.close()
    return TFile

def intro():
    #is the intro text
    print("""Welcom to Code Camp Team Manager\n\nThis program will add teams to
the team database file. You can run the program again to add more
teams to the file.\n\nUse the other program to display a list of teams.\n\n""")

def Write_Team_Member():
    intro()
    TFile = input("Team file name?")
    loop_question(TFile)
    return TFile
