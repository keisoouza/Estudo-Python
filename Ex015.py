d = int(input("Quantos dias o carro foi alugado:"))
km = float(input("Quantos KM foram rodados:"))
cd = d * 60
ckm = km * 0.15
print(f"O carro foi alugado por {d} dias e rodou por {km}Km, o aluguel custou R${cd} e a taxa por Km custou R${ckm}")
print("O custo total do carro foi R${}".format(cd + ckm))