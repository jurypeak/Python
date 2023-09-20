def readfile():
  id=[]
  place=[]
  forename=[]
  surname=[]
  jumps=[]
  file=open("athletes.txt","r")  
  x=0
  for row in file:
    data=row.split(",")
    id.append(data[0])
    place.append(data[1])
    forename.append(data[2])
    surname.append(data[3])
    jumps.append(data[4])
    x=x+1

  file.close()

  return id,place,forename,surname,jumps

def display(id,place,forename,surname,jumps):
  for x in range(0,len(id)):
    print (id[x],place[x],forename[x],surname[x],jumps[x])

id,place,forename,surname,jumps=readfile()
display(id,place,forename,surname,jumps)