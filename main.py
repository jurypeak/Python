import csv
import random

def create_array():
    ID = [""] * 20
    Forename = [""] * 20
    Surname = [""] * 20
    Username = [""] * 20
    Password = [""] * 20

    file = open('members.csv', 'r')

    x = 0
    for row in csv.reader(file):
      ID[x] = row[0]
      Forename[x] = row[1]
      Surname[x] = row[2]
      Username[x] = row[3]
      Password[x] = row[4]
      x = x + 1

    return ID, Forename, Surname, Username, Password

def username_password():
  NewID = input("CustomerID please ")
  Newforename = input("Forename please ")
  Newsurname = input("Surname please ")

  first_intial = [char for char in Newforename][0]
  Newusername = str(first_intial).upper()[0]+str(Newsurname)+str(NewID)
  print(Newusername)

  number = []
  randuppercase = []
  randlowercase = []

  for x in range(0,7):
    number.append(random.randint(0,9))
    randuppercase.append(chr(random.randint(ord('A'), ord('Z'))))
    randlowercase.append(chr(random.randint(ord('a'), ord('z'))))
  
  spchr = random.randint(0,2)

  specialchr = ["!", "$", "*"]
  
  Newpassword =str(randuppercase[1])+str(randlowercase[1])+str(number[1])+str(randuppercase[x])+str(randlowercase[x])+ str(number[x])+str(specialchr[spchr])
  Newpassword = [char for char in str(Newpassword)]
  pos1 = 2
  pos2 = random.randint(1,5)

  Newpassword[pos1], Newpassword[pos2] = Newpassword[pos2], Newpassword[pos1]

  print("".join(Newpassword))

  return NewID, Newforename, Newsurname, Newpassword, Newusername

def writing(ID, Forename, Surname, Username, Password, NewID, Newforename, Newsurname, Newpassword, Newusername):
  
  file = open('DATA.csv', 'wt', newline='')
  writer = csv.writer(file, delimiter=',')
  writer.writerow(["ID","Forename","Surname","Username","Password"])

  ID.append(NewID)
  Forename.append(Newforename)
  Surname.append(Newsurname)
  Username.append(Newusername)
  Password.append(Newpassword)
  
  for x in range(1, len(ID)):
    file = open('DATA.csv', 'a', newline='')
    writer = csv.writer(file, delimiter=',')
    writer.writerow([ID[x], Forename[x], Surname[x], Username[x], Password[x]])

ID, Forename, Surname, Username, Password = create_array()
NewID, Newforename, Newsurname, Newpassword, Newusername = username_password()
writing(ID, Forename, Surname, Username, Password, NewID, Newforename, Newsurname, Newpassword, Newusername)