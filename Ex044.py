preco = float(input("Qual o valor do produto: "))
pgmt = str(input("Qual a forma de pagamento: "))
dinheiro = preco * 0.90
cartao = preco * 0.95
c3x = preco * 1.20

if pgmt == "cartao" or pgmt == "Cartao":
    qtdParcelas = input("Quantidade de parcelas: ")
    if qtdParcelas == "1":
        print(f"Você ganhou um desconto de 5%, o valor do produto passou a ser R${cartao}")
    elif qtdParcelas == "2":
        print(f"Para pagamentos em até 2x no cartão não há juros e nem descontos, o valor continua sendo R${preco}")
    elif qtdParcelas == "3":
        print(f"Esta forma de pagamento incluem 20% de juros, o valor do total do produto passou a ser R${c3x}")
else:
    print(f"O valor a ser pago é {dinheiro}")
