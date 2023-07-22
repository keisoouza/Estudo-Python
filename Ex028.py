from random import randint
print("Vamos brincar!")
print("Tente adivinhar qual número eu escolhi entre 0 e 5.")
cpu = randint(0, 5)
rsp = int(input("Escolha um número: "))
if rsp == cpu:
    print("Parabéns, você acertou!")
else:
    print("Que pena, não foi dessa vez.")