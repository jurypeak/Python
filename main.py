def Create_Array():
  Beaches = [""] * 974
  Rating = [0.0] * 974
  
  import csv
  
  file = open('beachData.csv', 'r')
  
  x = 0
  for row in csv.reader(file):
    Beaches[x] = row[0]
    Rating[x] = row[1]
    x = x + 1

  return Beaches, Rating, file

def Average(Beaches, Rating): 
  
  total = 0
  for x in range(1, len(Rating)):
    total = total + float(Rating[x])
    average=total/973
  
  print('Average rating is:', round(average, 2))

  return average, total

def Appending(file):
  import csv 
  print("Please enter the beach, (if not, enter 'None'):")
  beachinput=input()
  print("Please enter the rating, (if not, enter 'None'):")
  ratinginput=input()
  with open('Data.csv', 'a') as fd:
    writer = csv.writer(fd)
    writer.writerow([beachinput, ratinginput])
    print("Appended succesfully")
    file.close()

Beaches, Rating, file = Create_Array()
Average(Beaches, Rating)
Appending(file)


