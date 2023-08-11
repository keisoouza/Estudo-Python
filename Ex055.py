print("Digite o peso de 5 pessoas para ver qual o maior e o menor.")
maior = 0
menor = 0

for p in range(1, 6):
    peso = float(input(f"Pessoa {p}: "))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print(f"O maior peso lido foi: {maior:.2f}Kg")
print(f"O menor peso lido foi: {menor:.2f}Kg")