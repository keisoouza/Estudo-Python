n = input("Digite um número com 3 dígitos: ")
n1 = n.split()[0][0]
n2 = n.split()[0][1]
n3 = n.split()[0][2]

maiorValor = 0

if n1 > n2:
    maiorValor = n1
else:
    maiorValor = n2
if maiorValor > n3:
    maiorValor = maiorValor
else:
    maiorValor = n3

menorValor = 0

if n1 < n2:
    menorValor = n1
else:
    menorValor = n2
if menorValor < n3:
    menorValor = menorValor
else:
    menorValor = n3 

print(f"O maior valor é {maiorValor}")
print(f"o menor valor é {menorValor}")
