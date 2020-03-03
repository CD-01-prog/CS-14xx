import sys
#creates the index to be used this case it is a empty index
def createIndex():
    index = {}
    return index

#/// repl tested
#recives the main index and the book the user wants to add and puts it in the index returning the updated index
def recordBook(index, isbn, title):
    index[str(isbn)] = title
    return index
    
#/// repl tested
#checks the index to see if the isbn is in it and returns the book that is found if a book is there
def findBook(index, isbn):
    answer = index.get(str(isbn), "")
    return answer
    
#///repl tested
#makes a numbered list of the contents of the current index
def listBooks(index):
    i = 1
    spacer = ":"
    for key,val in index.items():
        print( i, key, spacer, val)
        i += 1
    return index
    
#does not receive any parameters. It must return a list of strings that contains the lines of the menu.
def formatMenu():
    menu = [ 'What would you like to do?', '[r] Record a Book', '[f] Find a Book', '[l] List all Books', '[q] Quit' ]
    for i in menu:
        print(i)

#is the code to get the useres input
def formatMenuPrompt():
    action = input('Enter an option: ')
    return action
    
#///seemed to work unsure how it is supposed to work
#cleans up the users answer and makes sure they didnt enter a empty string and askes the user to give a answer if they do
def getUserChoice(user):
    out = 0
    while out == 0:
        user.strip()
        if len(user) > 0:
            out = 1
            return user
        else:
            user = input("please pick")
            
#///seems to work
#askes for the isbn the user is going to use and returns it cleaned up
def getISBN():
    isbn = input("Enter an ISBN: ")
    isbn = getUserChoice(isbn)
    return isbn
    
#/// is the same as get isbn so seems to work
#asks for the title the user is going to usse and returns it cleaned up
def getTitle():
    title = input("Enter a title: ")
    title = getUserChoice(title)
    return title
    
#gets the book info from user and adds it to the main index returning the updated index
def recordBookAction(index):
    isbn = getISBN()
    title = getTitle()
    index = recordBook(index, isbn, title)
    print("Book saved!")
    return index
    
#returns the book the user is looking for by isbn if there other wise lets user know it is not there
def findBookAction(index):
    isbn = getISBN()
    book = findBook(index, isbn)
    if book != "":
        print("Book found:" + book)
        return index
    else:
        print("sorry that book is not in our database")
        return index
    
#returns all the books in the index and lets the user know if there isnt any
def listBooksAction(index):
    if len(index) == 0:
        print("sorry but we seem to be missing the database right now sorry")
        return index
    else:
        listBooks(index)
        return index
    
#this quits out the entire program
def quitAction(index):
    print("have a good day")
    sys.exit(0)
    
    
#based on what the user wants it activates the corrasponding program then returns to the main loop
def applyAction(index, choice):
    choice.strip()
    if choice == 'r':
        index = recordBookAction(index)
        return index
    elif choice == 'f':
        findBookAction(index)
        return index
    elif choice == 'l':
        listBooksAction(index)
        return index
    elif choice == 'q':
        quitAction(index)
    else:
        print("non-approved command retry or raise your command level")
        return index
#This function ties everything together. Creating an index,repeatedly asking the user their choice, taking action.
def main():
    index = createIndex()
    run = True
    while run == True:
        formatMenu()
        choice = formatMenuPrompt()
        index = applyAction(index, choice)
        print("\n")
main()
