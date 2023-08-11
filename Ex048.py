soma = 0
cont = 0
n = int(input("Digite um número para extrair e somar os números impares multiplos de 3: "))
for c in range(1, n+1, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
print(f"A soma dos {cont} valores solicitados são {soma}")
