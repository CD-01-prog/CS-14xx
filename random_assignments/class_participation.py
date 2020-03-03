import random
#this program should take a file and randomly choose a name from that list until told to quit
def main():
    #get the varibles i am useing set
    choose = 0
    name = ""
    #intro the user
    print("Welcom to Participation Manager!\n I'll read your roll file and randomly pick students for you.\n")
    filename = input("What is the name of the roll file?")
    file = open(filename, 'r')
    #is the program takes a name from the file
    while choose == 0:
        print(name + "\n")
        answer = input("q to quit")
        if answer == "q":
            choose += 1
        else:
            name = random.sample(file)
    file.close()
