City = [""] * 15
Country = [""] * 15
Population = [""] * 15
Sea_Level = [""] * 15
  
import csv
  
file = open('Cities.csv', 'r')

x = 0
for row in csv.reader(file):
  City[x] = row[0]
  Country[x] = row[1]
  Population[x] = row[2]
  Sea_Level[x] = row[3]
  x = x + 1

file = open('Data.csv', 'wt', newline='')

writer=csv.writer(file, delimiter=',')

for x in range(15):
  writer.writerow([City[x], Country[x], Population[x], Sea_Level[x]])

file.close()