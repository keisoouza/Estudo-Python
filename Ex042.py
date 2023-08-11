s1 = float(input("Digite o primeiro segmento: "))
s2 = float(input("Digite o segundo segmento: "))
s3 = float(input("Digite o terceiro segmento: "))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print("Os segmentos podem formam um triângulo.")
    if s1 == s2 or s2 == s3:
        print("Formam um triângulo equilátero.")
    elif s1 != s2 and s1 != s3:
        print("Formam um triângulo escaleno.")
    else:
        print("Formam um triângulo isósceles.")
else:
    print("Não podem formam um triângulo.")
