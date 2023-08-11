n = 0
ida = 0
id = 0
for c in range(1, 5):
    print(f"{c}ª pessoa.")
    nome = str(input("Nome: ")).strip().lower().title()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo (M/F): ")).strip().upper()
    sx = sexo[0]
    ida += idade
    if sx == 'M' and idade > id:
        id = idade
        nmv = nome
    elif sx == 'F' and idade < 20:
        n += 1
print(f"A média de idade é {ida/4}")
print(f"O nome do homem mais velho é {nmv} e ele tem {id}")
print(f"O total de mulher(es) com menos de 20 anos é {n}")