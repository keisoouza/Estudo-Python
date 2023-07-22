print("Este é um ano bissexto?")
ano = int(input("Ano: "))
bs = ano % 4
if bs == 0:
    print("É um ano bissexto.")
else:
    print("Não é um ano bissexto.")