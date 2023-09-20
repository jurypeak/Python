import csv

def create_array():
    entryID = [""] * 30
    location = [""] * 30
    forename = [""] * 30
    surname = [""] * 30
    jumps = [0] * 30

    file = open('athletes.csv', 'r')

    x = 0
    for row in csv.reader(file):
      entryID[x] = row[0]
      location[x] = row[1]
      forename[x] = row[2]
      surname[x] = row[3]
      jumps[x] = row[4]
      x = x + 1

    return entryID, location, forename, surname, jumps

def bibValuefile(entryID, location, forename, surname, jumps):
  file = open('bibValues.csv', 'wt', newline='')
  bibValue = [] * 30
  firstintials = []
  firstasciis = []
  for x in range(30):
    firstintial = [char for char in forename[x]][0]
    firstintials.append(firstintial)
    firstascii = [char for char in location[x]][0]
    firstasciis.append(ord(firstascii[0]))
    bibValue.append(str(firstintials[x])+str(surname[x])+str(firstasciis[x]))
    writer = csv.writer(file, delimiter=',')
    writer.writerow([entryID[x], bibValue[x]])
    
  file.close

  return entryID, location, forename, surname, jumps

def max_jumps(jumps):
  maxjumps = int(jumps[0])
  for x in range(1, 30):
    if int(jumps[x]) > maxjumps:
      maxjumps = int(jumps[x])

  return maxjumps, entryID, location, forename, surname, jumps

def searching(maxjumps, entryID, location, forename, surname, jumps):
  for x in range(30):
    if int(jumps[x]) == maxjumps:
      print(forename[x], surname[x])

def finalists(location):
  Motherwell = 0
  Inverness = 0
  Kirkcaldy = 0
  Coatbridge = 0
  for x in range(0, len(location)):
    if location[x] == "Motherwell":
      Motherwell = Motherwell + 1
    elif location[x] == "Inverness":
      Inverness = Inverness + 1
    elif location[x] == "Kirkcaldy":
      Kirkcaldy = Kirkcaldy + 1
    elif location[x] == "Coatbridge":
      Coatbridge = Coatbridge + 1
  print('\n'+"Motherwell", Motherwell, '\n'+"Inverness", Inverness, '\n'+"Kirkcaldy", Kirkcaldy, '\n'+"Coatbridge", Coatbridge)
    
entryID, location, forename, surname, jumps = create_array()
entryID, location, forename, surname, jumps = bibValuefile(entryID, location, forename, surname, jumps)
maxjumps, entryID, location, forename, surname, jumps = max_jumps(jumps)
searching(maxjumps, entryID, location, forename, surname, jumps)
finalists(location)