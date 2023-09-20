def create_class():
  from dataclasses import dataclass
  
  @dataclass
  class book:
    ID: int = 0
    Forname: str = ""
    Surname: str = ""
    Company: str = ""
    Quantity: int = 0
    
  books = [book() for x in range(15)]

  import csv
  
  file = open('books_orders.csv', 'r')
  x = 0
  for row in csv.reader(file):
        books[x].ID = row[0]
        books[x].Forname = row[1]
        books[x].Surname = row[2]
        books[x].Company = row[3]
        books[x].Quantity = row[4]
        x = x + 1
  return books

def main_program(books):
  import csv
  file = open('DATA.csv', 'wt', newline="")
  writer = csv.writer(file, delimiter=',')
  writer.writerow(["ID", "Company","Forname","Surname", "Quantity", "Total", "DiscountTotal", "Percentage"])
  Total = []
  Discount = []
  Percentage = []
  CompanyX = books[1].Company
  QuantityX = int(books[1].Quantity)
  for x in range(15):
    QuantityX = int(books[x].Quantity)
    total = round(QuantityX * 15.99, 2)
    CompanyX = books[x].Company
    if QuantityX >= 100:
      percentage = 15
      discount = round(total / 100 * 15, 2)
      discount = round(total - discount, 2)
    elif QuantityX < 100:
      percentage = 0
      discount = total
    print("The total without discounts for", CompanyX, "is", "£"+str(total), '\n' "A discount of", str(percentage)+"%"" for", CompanyX+",","the new total is:", "£"+str(discount)+",", "they bought", books[x].Quantity, "books", '\n')
    Total.append(total)
    Discount.append(discount)
    Percentage.append(percentage)

  import csv
  file = open('DATA.csv', 'a', newline='')
  writer = csv.writer(file, delimiter=',', quotechar='"',quoting=csv.QUOTE_ALL)
  for x in range(15):
    writer.writerow([books[x].ID, books[x].Company, books[x].Forname, books[x].Surname, books[x].Quantity, "£"+str(Total[x]), "£"+str(Discount[x]), str(Percentage[x])+"%"])
    
    
books = create_class()
main_program(books)