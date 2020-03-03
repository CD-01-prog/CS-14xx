import os.path
#recives a file strips it then returns the differnet lines as a list /// tested in repl worked
def fileToList(filename):
    exist = os.path.isfile(filename)
    Flist = []
    if exist == True:
        file = open(filename,'r')
        for line in file:
            Flist.append(line.strip())
        file.close()
    return Flist

#recives a list of strings and returns the first string in the list /// tested in repl worked    
def returnFirstString(strings):
    if len(strings) > 0:
        return strings[0]
    else:
        return ""

#recives 2 strings will return true if the strings contain characters false if they dont /// tested in repl worked    
def strandsAreNotEmpty(strand1, strand2):
    if len(strand1) > 0 and len(strand2) > 0:
        return True
    else:
        return False

#recives 2 strings will return true if same length false if they are differnet /// tested in repl worked    
def strandsAreEqualLengths(strand1, strand2):
    if len(strand1) == len(strand2):
        return True
    else:
        return False

#recives 3 values 2 strings 1 is the target string another is a canidate string and a integer it tests to
#see if the target and canidate have the same characters for the length of the integer /// tested in repl worked
def candidateOverlapsTarget(target, candidate, overlap):
    if target[len(target) - overlap:] == candidate[0:overlap]:
        return True
    else:
        return False

#recives 2 strings 1 target string and 1 canadite string it returns the value of how much overlap there is and
#returns -1 if the strings are differnt sizes or 1 is empty /// passed tests on description in repl
def findLargestOverlap(target, candidate):
    count = 0
    overlap = 1
    if strandsAreNotEmpty(target, candidate) == False or strandsAreEqualLengths(target, candidate) == False:
        return -1
    else:
        while len(target) > overlap:
            if candidateOverlapsTarget(target, candidate, overlap) == True:
                count = overlap
                overlap += 1
            else:
              overlap += 1
        return count

#recives 2 values 1 target string and a list of caditnt strings it checks to see which one is the best then returns
#a tuple with the best string and the number of overlap it has if there is no overlap for any of them it should
#return a empty tuple with a empty string and 0 /// passed tests on description in repl
def findBestCandidate(target, candidates):
    best = ()
    word = ""
    number = 0
    for line in candidates:
        if findLargestOverlap(target, line) > number:
            word = line
            number = findLargestOverlap(target, line)
    best = (word, number)
    return best

#recives 3 paramerters 1 target string and a candiate string and the overlap integer it joins the two strings at
# the overlap point /// passed tests on description in repl
def joinTwoStrands(target, candidate, overlap):
    if overlap == 0:
      return target
    word = target[0:overlap - 1] + candidate
    return word

#ask the user for the files to use and prints the combined string
def main():
    target = fileToList(input("Target strand filename: "))
    candidate = fileToList(input("Candidate strands filename: "))
    best = findBestCandidate(target, candidate)
    answer = joinTwoStrands(target, best[0], best[1])
    print(answer)

#for testing purposes
if __name__ == '__main__':
    main()
