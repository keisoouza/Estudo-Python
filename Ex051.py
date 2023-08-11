p = int(input("Digite o primeiro número da PA: "))
r = int(input("Digite a razão da PA: "))
d = p + (10 - 1) * r
print("Os dez primeiros números da sua PA são:")
for c in range(p, d + r, r):
    print(c)