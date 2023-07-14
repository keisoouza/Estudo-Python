from math import sin,cos,tan,pi

n = float(input("Digite o ângulo em graus:"))
print(f"Estes são os valores para o ângulo {n}°:")
print(sin((n*pi)/180))
print(cos((n*pi)/180))
print(tan((n*pi)/180))