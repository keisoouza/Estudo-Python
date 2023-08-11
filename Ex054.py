from datetime import date
a = date.today().year
maior = 0
menor = 0
print("Digite o ano de nascimento de 7 pessoas e veja quantas delas são maiores de idade.")
for p in range(1, 8):
    cont = 0
    n = int(input(f"Pessoa {p}: "))
    i = a - n
    if i >= 18:
        maior += 1
    else:
        menor += 1
print(f"Pessoas maiores de idade: {maior}")
print(f"Pessoas menores de idade: {menor}")