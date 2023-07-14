a = float(input("Qual é a altura da parede?:"))
l = float(input("E qual é a largura?:"))
m = a * l
t = m / 2
print("Para uma parede de {}x{} metros, sua área é de {}".format(a, l, m))
print("Serão necessários {:.2f} litros de tinta".format(t))