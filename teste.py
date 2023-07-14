from datetime import date, datetime

d1 = int(input("Data inicial: "))
d2 = int(input("Data final: "))

diff = d2 - d1

dias = diff.days
anos, days = dias // 365, dias % 365
mes, days = days // 30, dias % 30

print("Se passaram {} dias, {} mes e {} anos.".format(dias, mes, anos))
