print("Seu nome tem Silva?")
nome = str(input("Seu nome completo: "))
nm = nome.split()
if nm[1] =="Silva":
    print("Tem.")
else:
    print("Não tem.")