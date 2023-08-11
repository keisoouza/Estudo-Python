total = 0
print("Identificador de números primos.")
n = int(input("Digite um número: "))
for c in range(1, n+1):
    if n % c == 0:
        print(end=" ")
        total += 1
    else:
        print(end=" ")
print(f"O número {n} foi divisível {total} vezes.")
if total == 2:
    print("Isso significa que ele é um número primo.")
else:
    print("Isso significa que ele não é um número primo.")
