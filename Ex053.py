print("identificando um palíndromo.")
f = str(input("Digite um frase e veja se ela é um palíndromo: "))
nf = f.strip().lower().replace(' ','')
n = len(nf)
f = n - 1
i = 0
p = 0

for c in range(0, n):
    if nf[i] == nf[f]:
        p = p + 1
        i = i + 1
        f = f - 1
if p == n:
    print("A frase é um palíndromo.")
else:
    print("A frase não é um palíndromo.")
