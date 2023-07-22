n = int(input("Digite um número inteiro: "))
print("""Escolha uma dessas opções: 
 [ 1 ] PARA BINÁRIO
 [ 2 ] PARA OCTAL
 [ 3 ] PARA HEXADECIMAL""")

opção = int(input("Sua opção: "))

if opção == 1:
        print(f"O valor de {n} em Binário é {bin(n)[2:]}")
elif opção == 2:
        print(f"O valor de {n} em Octal é {oct(n)[2:]}")
elif opção == 3:
        print(f"O valor de {n} em Hexadecimal é {hex(n)[2:]}")
else:
        print(f"Opção Invalida ! Tente novamente !")