qtdDiasContados = 0
data = str(input("Insira a data de hoje: "))
dia,mes,ano = data.split("/")

dia = int(dia)
mes = int(mes)
ano = int(ano)

listQtdDiasMes = [0,31,29,31,30,31,30,31,31,30,31,30,31]
for i in range(mes):
    qtdDiasContados = qtdDiasContados + listQtdDiasMes[i]

if ano % 4 != 0 and qtdDiasContados != 0:
    qtdDiasContados = qtdDiasContados -1

if qtdDiasContados == 0 : 
    print("Não se passou nenhum dia do ano de {} do inicio até a data de {}".format(ano, data))
else:
    print("Se passaram {} dias do ano de {}, do inicio até a data de {}".format(qtdDiasContados, ano, data))