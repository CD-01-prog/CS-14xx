import random

class Player:

    def __init__(self, name):
        self.name = name
        self.letters = []
        for i in range(7):
            self.drawLetter()
        return

    def getName(self):
        return self.name

    def getLetters(self):
        return self.letters

    def drawLetter(self):
        block = 'aaaaaaaaabbccddddeeeeeeeeeeeeffggghhiiiiiiiiijkllllmmnnnnnnooooooooppqrrrrrrssssttttttuuuuvvwwxyyz'
        pick = random.randint(0, len(block)-1)
        self.letters.append(block[pick])
        return

    def printLetters(self):
        answer = ""
        word = self.letters
        for letter in word:
            answer = answer + letter + " "
        print(answer)
        return

    def checkWord(self, word):
        tlist = self.letters
        size = 0
        if len(word) > len(tlist):
            return False
        for i in range(len(word)):
          if word[i] in tlist:
            size += 1
        if len(word) == size:
            for bletter in word:
                tlist.remove(bletter)
            return True
        return False
