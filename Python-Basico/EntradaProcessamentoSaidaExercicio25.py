#Todo restaurante, embora por lei não possa obrigar o cliente a pagar, cobra 10% de comissão para o garçom. Crie um algoritmo em PYTHON que leia o valor gasto
#com despesas realizadas em um restaurante e imprima o valor da gorjeta e o valor total com a gorjeta.

#Entrada dos dados

valor = float(input("Digite o valor gasto: "))

#Processamento dos dados

gorjeta = valor * 10 / 100
valorTotal = valor + gorjeta

#Impressão dos dados

print("Valor da gorjeta: ",gorjeta)
print("Total a ser pago: ",valorTotal)
