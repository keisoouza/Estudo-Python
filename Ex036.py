print("Para avaliarmos o seu empréstimo imobiliário, preencha as informações abaixo.")
casa = float(input("Qual o valor da casa: "))
anos = int(input("Em quantos anos planeja pagar: "))
salario = float(input("Qual o valor do seu salário: "))
pcl = anos * 12
pres = casa / pcl
pct = salario * 0.30
print(f"O valor da casa é {casa:.3f}, o valor da prestação é {pres:.3f} e será parcelado em {pcl}x.")
print("Analisando...")
if pres > pct:
    print("O empréstimo foi negado!")
else:
    print("O empréstimo foi aprovado!")