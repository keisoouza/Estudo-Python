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

atraso = deltaAnos - 18
falta = 18 - deltaAnos

if deltaAnos > 18:
    print(f"Seu alistamento está com um atraso de {atraso} anos.")
elif deltaAnos == 18:
    print("Você já está na idade de se alistar.")
else:
    print(f"Você é muito novo, falta {falta} anos para se alistar.")