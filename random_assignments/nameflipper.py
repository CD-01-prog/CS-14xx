#main function for a name flipper takes a string name and returns a string of the name fliped
def nameFlipper(name):
    #stores the first and last name
    first = ''
    last = ''
    #uses the space to decide where the first and last name are
    for i in range(len(name)):
        if name[i] == " ":
            first = name[0:i]
            last = name[i+1:]
    #now first and last found can be flipped and returned to user
    
    return str(last + ", " + first)

#testing the three test cases
def main():
    if nameFlipper("Bill Salter") == "Salter, Bill":
        print("Bill Salter Passed")
    else:
        print(nameFlipper("Bill Salter"))
        print("Bill Salter Failed")
        
    if nameFlipper("Michael Green") == "Green, Michael":
        print("Michael Green Passed")
    else:
        print(nameFlipper("Michael Green"))
        print("Michael Green Failed")
        
    if nameFlipper("J Graff") == "Graff, J":
        print("J Graff Passed")
    else:
        print(nameFlipper("J Graff"))
        print("J Graff Failed")
