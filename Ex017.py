import math

co = float(input("Digite o valor do cateto oposto:"))
ca = float(input("Digite o valor do cateto adjacente:"))
ppot = co ** 2
spot = ca ** 2
soma = ppot + spot
hip = math.sqrt(soma)
print(f"O comprimento da hipotenusa é {hip:.2f}!")