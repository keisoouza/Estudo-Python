soma = 0
print("Somente números pares serão somados, os números impares serão ignorados!")
for c in range(0, 6):
    n = int(input("Digite um número: "))
    if n % 2 == 0:
        soma = soma + n
print(f"O valor da soma dos pares é {soma}.")