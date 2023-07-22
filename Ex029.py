print("O limite desta estrada é de 80Km/h.")
km = float(input("Há quantos Km/h o carro estava: "))
multa = (km - 80) * 7
if km >= 80:
    print(f"Você foi multado em R${multa}")
else:
    print("Você não foi multado.")