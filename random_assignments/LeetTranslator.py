key = {'4':'A', '8':'B', 'C':'C', 'D':'D',  'F':'F', 'G':'G', 'H':'H', 'I':'I', 'J':'J', 'K':'K',  'M':'M', 'N':'N', 'P':'P', 'Q':'Q', 'R':'R', 'U':'U', 'V':'V', 'W':'W', 'X':'X', 'Y':'Y', 'Z':'Z', '@':'a', 'b':'b', 'c':'c', 'd':'d', '3':'e', 'f':'f', 'g':'g', 'h':'h', 'i':'i', 'j':'j', 'k':'k', '1':'l', 'm':'m', 'n':'n', '0':'o', 'p':'p', 'q':'q', 'r':'r', '5':'s', '7':'t', 'u':'u', 'v':'v', 'w':'w', 'x':'x', 'y':'y', 'z':'z', ' ':' ', ',':',', '-':'-', ':':':', "\n":"\n", "'":"'", '.':'.','?':'?', '!':'!'}
#puts the translation into the english file by writing the translation onto it
def put_into(E_file, translation_holder):
    file = open(E_file, 'w')
    file.write(translation_holder)
    file.close()
    return file
#translates the leet file by comparing every indivual charcter to its key and returing what english it is
def Translate_L(L_file):
    file = open(L_file, 'r')
    translation_holder = ""
    for char in file:
        translation_holder = translation_holder + key[char]
    file.close()
    return translation_holder
#into text so not to clog up the main function
def intro():
    print("""Welcome to the Leet Speak Translator \nIf you have a file that is written in leet speak, we can translate it back to normal English for you. \nJust give me the name of the file you want to have translated, and the name you want for the translated file.""")

def leetTranslator():
#boring into text
    intro()
    #get file to use
    L_file = input("name of leet file?\n")
    #translate the file
    translation_holder = []
    Translate_L(L_file)
    #put translation into file of user choice
    E_file = input("name of english file?\n")
    put_into(E_file, translation_holder)
    #give the user back the file
    return file
