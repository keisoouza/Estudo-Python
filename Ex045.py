import random

print("Vamos brincar de pedra, papel ou tesoura.")
vc = str(input("Sua mão: "))
jkp = ["pedra", "papel", "tesoura"]

print(f"Minha mão: {random.choices(jkp)}")