from datetime import date
 
def numOfDays(date1, date2):
    return (date2-date1).days

d1 = input("Data inicial: ")
d2 = input("Data final: ")

date1 = date() 
date2 = date()
print(numOfDays(date1, date2), "days")