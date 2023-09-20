from dataclasses import dataclass

@dataclass
class Person:
  forename : str = ""
  surname : str = ""
  age : int = 0
  height : float = 0
  license : bool = False

myPerson = [Person() for x in range (2)]
  
for x in range (len(myPerson)):
  myPerson[x].forename = str(input("Enter forename. "))
  myPerson[x].surname = str(input("Enter surname. "))
  myPerson[x].age = int(input("Enter age. "))
  myPerson[x].height = float(input("Enter height. "))
  myPerson[x].license = bool(input("Enter True if you have a license, if not press enter. "))

Max = myPerson[0].age
Firstname = myPerson[0].forename
Lastname = myPerson[0].surname
for x in range(0, len(myPerson)):
  if myPerson[x].age > Max:
    Max = myPerson[x].age
    Firstname = myPerson[x].forename
    Lastname = myPerson[x].surname
  else:
    x = x+1

ifTrue = myPerson[0].license
counter = 0
for x in range(0, len(myPerson)):
  if myPerson[x].license == True:
    counter = counter + 1

found = False
namechosen = input("What surname would you like to search for? ")
for x in range(0, len(myPerson)):
  if myPerson[x].surname == namechosen:
    found = True
    position = x
if found == False:
  print("Can't find the surname entered") 
else:
  print("Name found", myPerson[position])

print("Oldest person,", Firstname, Lastname, Max)
print("Students with licenses:", counter)


with open("Person.csv","w") as writefile:
  for x in range(len(myPerson)):
    writefile.write(str(myPerson[x].forename) + "," + str(myPerson[x].surname) + "," + str(myPerson[x].age) + "," + str(myPerson[x].height) + "," + str(myPerson[x].license) + "\n")