#Faça Um programa em que fernando insira uma data de chegada e diga se Vitória está em alta temporada ou não.
#De 01/01 até 20/01 existe Alta temporada 

# De 01/07 até 30/07 existe Alta temporada

# De 21/12 até 31/12 existe Alta temporada



data = input("Digite a data da chegada: ")
dia, mes, ano = data.split("/")
dia = int(dia)
if mes == "01" and (dia >= 1 and dia <= 20):
    print("Vitória está em alta temporada.")
elif mes == "07" and (dia >= 1 and dia <= 30):
    print("Vitória está em alta temporada.")
elif mes == "12" and (dia >= 21 and dia <= 31):
    print("Vitória está em alta temporada.")
else:
    print("Vitória não está em alta temporada.")