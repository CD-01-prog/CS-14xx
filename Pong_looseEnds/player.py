import random

class Player:

    def __init__(self, name):
        self.name = name
        self.letters = []
        for i in range(7)
            drawLetter()
        return

    def getName(self):
        return self.name

    def getLetters(self):
        return self.letters

    def drawLetter(self):
        block = 'aaaaaaaaabbccddddeeeeeeeeeeeeffggghhiiiiiiiiijkllllmmnnnnnnooooooooppqrrrrrrssssttttttuuuuvvwwxyyz'
        pick = random.randint(0, len(block))
        self.letters.append(block[pick])
        return

    def printLetters(self):
        answer = ""
        word = self.letters
        for letter in word:
            answer += letter + " "
        print(answer)
        return

    def checkWord(word):
        tempword = word
        size = 0
        tempList = self.letters
        badLetters = []
        if len(word) > len(tempList):
            return False
        for letter in tempList:
          for wordletter in tempword:
            if wordletter == letter:
              tempword = tempword.replace(wordletter, "")
              badLetters.append(letter)
              tempList.remove(letter)
              size += 1
        if size == len(word):
            for letter in masterList:
                for bletter in BadLetters:
                  if letter == bletter:
                    self.letters.remove(letter)
                    BadLetters.remove(bletter)
            return True
        return False
