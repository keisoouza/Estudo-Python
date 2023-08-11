import random

print("=" * 20)
print("VAMOS JOGAR JOKENPO!")
print("=" * 20)

lista = ['pedra', 'papel', 'tesoura']
pc = random.choice(lista)
player = str(input("Você escolhe PEDRA, PAPEL ou TESOURA? ")).strip().lower()

while player != 'pedra' and player != 'papel' and player != 'tesoura':
    player = str(input("Não entendi essa opção! Escolha PEDRA, PAPEL ou TESOURA: ")).strip().lower()

if player == 'papel' and pc == 'pedra' or player == 'pedra' and pc == 'tesoura' or player == 'tesoura' and pc == 'papel':
    print(f"GANHOU! Poxa, você escolheu {player} e eu escolhi {pc}.")
elif player == pc:
    print(f"Ih, empatamos! Nós dois escolhemos {pc}.")
else:
    print(f"HÁ! Ganhei de você! Você escolheu {player} e eu escolhi {pc}!")