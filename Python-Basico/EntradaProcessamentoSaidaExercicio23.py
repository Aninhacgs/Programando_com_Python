#Criar um algoritmo em PYthon que leia um valor de hora (hora:minutos) e informe (calcule) o total de minutos se passaram desde o início do dia (0:00h).

#Entrada de dados

hora = int(input("Digite o valor da hora: "))

minutos = int(input("Digite o valor referente aos minutos: "))

#Processamento dos dados

totalMinutos = hora * 60 + minutos

#Impressão do processamento

print("A quantidade de minutos decorridos é: ",totalMinutos)
