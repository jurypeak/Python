from dataclasses import dataclass

def create_array():
  
  @dataclass
  class ingredient:
    Weight: int = 0
    Name: str = ""
    Percents: int = 0
    
  val = False
  length = int()
  while val == False:
    length = input("How many ingredients will you be entering? \n")
    try:
      length = int(length)
    except ValueError:
        print("No letters, characters, symbols and words please. \n")
    if length < 1:
      print("Must be greater than one. \n")
    else:
      val = True
    
  ingredients = [ingredient() for x in range(length)]
    
  return ingredients, length

def inputted_grams(ingredients, length):
  
  x = 0
  v = 0
  while x < length:
      ingredients[x].Name = input("Name of ingredient"+ " "+str(x+1)+":"+"\n")
      ingredients[x].Weight = input("How many grams for " + ingredients[x].Name + "? \n")
      try:
        ingredients[x].Weight = float(ingredients[x].Weight)
      except ValueError:
          print("Insert numbers only, please re-enter name of ingredient"+" "+str(x+1)+":" "\n")
      if ingredients[x].Weight < 1:
        v=v+1
      if v == length:
        x = 0
        print("There must be at least one ingredient with a higher number than zero, please re-enter all ingredients. \n")
      else:
        x=x+1
        
  return ingredients, length
        
def calculation(ingredients, length):
  
  v = []
  for x in range(length):
    v.append(ingredients[x].Weight)
  total = sum(v)
  for x in range(length):
    ingredients[x].Percents = ingredients[x].Weight / total * 100
    ingredients[x].Percents = round(ingredients[x].Percents, 0)
    print(str(ingredients[x].Name)+ ", "+ str(ingredients[x].Weight) + "g, " + str(ingredients[x].Percents) + "%")
    
  return ingredients, length

def write_to_file(ingredients, length):

  val = False
  while val == False:
    newfile = input("Would you like to create a new file or add to a existing file, enter yes to create a new file or no to add to a existing file. \n")
    if newfile == "Yes" or newfile == "yes":
      filename = input("What would you like this file to be called? \n")
      file = open(filename+'.csv', 'w+', newline='')
      break
    if newfile == "No" or newfile == "no":
      filename = input("What is the existing file called you'd like to enter the percentage's to. \n")
      file = open(filename+'.csv', 'a', newline='')
      break
    elif newfile != "Yes" or newfile != "yes" or newfile != "No" or newfile != "no":
      val = False
      print("Please enter yes or no. \n")
  
  import csv, operator
  
  writer = csv.writer(file, delimiter=',')
  writer.writerow(["Name", "Weight", "Percentage"])
  for x in range(0, length):
    writer.writerow([ingredients[x].Name, str(ingredients[x].Weight) + "g", str(ingredients[x].Percents) + "%"])
    
  data = csv.reader(open(filename+".csv"),delimiter=',')
  data = sorted(data, key=operator.itemgetter(2))    
  
ingredients, length =  create_array()
ingredients, length = inputted_grams(ingredients, length)
ingredients, length = calculation(ingredients, length)
write_to_file(ingredients, length)
  
    
    
  
