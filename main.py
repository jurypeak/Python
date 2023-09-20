def create_array():
    RacerID = [0] * 20
    Forename = [""] * 20
    Surname = [""] * 20
    Nationality = [""] * 20
    RaceTeam = [""] * 20
    Time1 = [0] * 20
    Time2 = [0] * 20
    Time3 = [0] * 20

    import csv

    file = open('Racing.csv', 'r')

    x = 0
    for row in csv.reader(file):
      RacerID[x] = row[0]
      Forename[x] = row[1]
      Surname[x] = row[2]
      Nationality[x] = row[3]
      RaceTeam[x] = row[4]
      Time1[x] = row[5]
      Time2[x] = row[6]
      Time3[x] = row[7]
      x = x + 1

    return RacerID, Forename, Surname, Nationality, RaceTeam, Time1, Time2, Time3

def main_program(RacerID,Forename,Surname,Nationality,RaceTeam,Time1,Time2,Time3):
  
  import csv
  location = input("Enter the file location. ")
  file = open(location, 'wt', newline='')
  writer = csv.writer(file, delimiter=',')
  writer.writerow(["RacerID","Forename","Surname","RaceTeam","Fastest Time","Average Time"])

  QuickestTime = Time1[1]
  FirstnameofRacer = Forename[1]
  LastnameofRacer = Surname[1]
  RacerTeam = RaceTeam[1]
  for x in range(20):
    QuickestTime = min(Time1[x], Time2[x], Time3[x])
    FirstnameofRacer = Forename[x]
    LastnameofRacer = Surname[x]
    RacerTeam = RaceTeam[x]
    AvgTime = Time1[1]
    AvgTime = round((int(Time1[x])+int(Time2[x])+int(Time3[x])))
    AvgTime = round(AvgTime/3, 2)

    print('\n', FirstnameofRacer, LastnameofRacer, "of", RacerTeam , "achevied a time of", str(QuickestTime)+"s", "their quickest time. They also achevied an average time of", str(AvgTime)+"s")
    
    file = open(location, 'a', newline='')
    writer = csv.writer(file, delimiter=',')
    writer.writerow([RacerID[x],Forename[x],Surname[x],RaceTeam[x],QuickestTime,AvgTime])

RacerID,Forename,Surname,Nationality,RaceTeam,Time1,Time2,Time3 = create_array()
main_program(RacerID,Forename,Surname,Nationality,RaceTeam,Time1,Time2,Time3)
