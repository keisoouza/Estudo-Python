print("Calculando o seu IMC.")
peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))
imc = peso / (altura * altura)
print(f"Seu IMC é {imc:.2f}")
print("O status do seu IMC de acordo com a tabela de Índice de Massa Corporal.")

if imc <= 18.5:
    print("Abaixo do peso.")
elif imc >= 18.5 and imc <= 25:
    print("Peso ideal.")
elif imc >= 25 and imc <= 30:
    print("Sobrepeso.")
elif imc >= 30 and imc <= 40:
    print("Obesidade.")
else:
    print("Obesidade mórbida.")