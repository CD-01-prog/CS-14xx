def main():
  course = {}
  intro()
  out = 0
  while out == 0:
      Request_Class(course)
      out = Display_Course(course)
  return print("Have a great semester!")

#contains the intro info for the user
def intro():
    print("Welcom to the class schedule planner.\n")
    print("This application will help you schedule the times for your classes next semester. Enter the class name and time slot for your desired classes.\n")
    print("The resulting list of courses will be displayed.\n")
    print("At Dixie State, there are 13 normal class start times.\nWe will number them as follows:\n1- 8:00am MWF\n2- 9:00am MWF\n3- 10:00am MWF\n4- 11:00am MWF\n5- 12:00pm MWF\n6- 1:00pm MWF\n7- 2:00pm MWF\n8- 3:00pm MWF\n9- 7:30am TR\n10- 9:00am TR\n11- 10:30am TR\n12- 1:00pm TR\n13- 2:30pm TR\n\n")

#will get the class person wants and add it to their class list
def Request_Class(course):
    print("add a class:\n")
    key = input("Time slot?\n")
    name = input("Course Name?\n")
    course[key] = name
    return course

#will display their current list and ask if they want to add more
def Display_Course(course):
    print("Your current course list is:\n")
    for key,name in course.items():
      print(str(key) + ' ' + name + "\n")
    proceed = input("Add another course? (1 to continue or 0 to stop)")
    proceed = proceed.strip()
    if str(proceed) == str("0"):
      out = 1
      return out
    

main()
