from datetime import date

print("Digite sua data de nascimento.")
dia = int(input("Dia: "))
mes = int(input("Mês: "))
ano = int(input("Ano: "))
dataNas = date(ano, mes, dia)
print(f"Você nasceu em: {dataNas}")

hoje = date.today()

delta = hoje - dataNas
deltaDias = delta.days
deltaAnos = deltaDias // 365

if deltaAnos <= 9:
    print("Categoria: Mirim")
elif deltaAnos >= 10 and deltaAnos <= 14:
    print("Categoria: Infatil")
elif deltaAnos >= 15 and deltaAnos <= 19:
    print("Categoria: Junior")
elif deltaAnos == 20:
    print("Categoria: Sênior")
else:
    print("Categoria: Master")