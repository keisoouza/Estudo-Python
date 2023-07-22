d = float(input("Qual a distância da viagem: "))
vc = d * 0.50
vl = d * 0.45
if d <= 200:
    print(f"Você vai pagar R${vc}")
else:
    print(f"Você vai pagar R${vl}")