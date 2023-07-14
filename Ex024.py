print("Sua cidade tem Santo no nome?")
cid = input("Qual o nome da sua cidade: ")
san = cid.split()
if san[0] == "Santo":
    print("Começa!")
else:
    print("Não começa.")