frase = str(input("Escreva uma frase: "))
a = frase.lower().count('a')
print('A letra A aparece {} vezes'.format(a))

pri = (frase.find('a'))+1
print('A letra A aparece a primeira vez na casa {}'.format(pri))

frase = frase[::-1]
ult = len(frase)-frase.lower().find('a')
print('A letra A aparece a última vez na casa {}'.format(ult))