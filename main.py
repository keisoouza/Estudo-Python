from datetime import date, datetime

di1 = int(input("Dia inicial: "))
mes1 = int(input("Mês inicial: "))
ano1 = int(input("Ano inicial: "))

di2 = int(input("Data final: "))
mes2 = int(input("Mês final: "))
ano2 = int(input("Ano final: "))

d1 = datetime.date(ano1, mes1, di1)
d2 = datetime.date(ano2, mes2, di2)

diff = (d2 - d1)

dias = diff.days
anos, days = dias // 365, dias % 365
mes, days = days // 30, dias % 30

print(dias, mes,  anos)