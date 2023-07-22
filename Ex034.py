s = float(input("Qual o seu salário: "))
ss = s * 1.10
si = s * 1.15
if s >= 1.250:
    print(f"Você ganhou um aumento de 10% e vai ganhar R${ss:.3f}")
else:
    print(f"Você ganhou um aumento de 15% e vai ganhae R${si:.3f}")