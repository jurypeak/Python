from dataclasses import dataclass

@dataclass
class Temp:
      Dayofweek : str = ""
      Dayofmonth : int = 0
      Month : int = 0
      TempCelsius : int = 0
      TempFahrenheit : int = 0

def create_Array(Temp):
    Temperatures =[Temp() for x in range(7)]
    return Temperatures

def userinput(Temperatures):
  Temperatures[x].Dayofweek=str(input("What is the day of this week "))
  Temperatures[x].Dayofmonth=int(input("What is the day of this month "))
  Temperatures[x].Month=int(input("What month is it "))
  Temperatures[x].TempCelsius=int(input("What is temperature in celsius today "))
    
  return Temperatures

def calculation(Temperatures):
  Temperatures[x].TempFahrenheit = int(round(Temperatures[x].TempCelsius * 1.8 + 32))

def display_Data(Temperatures):
    print("\n",Temperatures[x].Dayofweek, "|", Temperatures[x].Dayofmonth, "|", Temperatures[x].Month, "|", Temperatures[x].TempCelsius, "°C", "|", Temperatures[x].TempFahrenheit, "°F\n")

def displayavg(Temperatures):
      totalC = 0
      totalF = 0
      for x in range(0, 7):
        totalC = totalC + Temperatures[x].TempCelsius
        totalF = totalF + Temperatures[x].TempFahrenheit
      totalC = round(totalC / 7, 1)
      totalF = round(totalF / 7, 1)
      print("The average temperature across the 7 days was", int(totalC), "°C and", int(totalF), "°F\n")


Temperatures = create_Array(Temp)
for x in range(0, 7):
  Temperatures = userinput(Temperatures)
  calculation(Temperatures)
  display_Data(Temperatures)
displayavg(Temperatures)
