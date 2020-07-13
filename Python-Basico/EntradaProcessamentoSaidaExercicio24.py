#Criar um algoritmo em PORTUGOL que leia o valor de um depósito e o valor da taxa de juros. Calcular e imprimir o valor do rendimento e o valor total depois do rendimento.

#Entrada dos dados

deposito = float(input("Digite o valor do depósito: "))

taxaJuros = float(input("Digite o valor da taxa de juros: "))

#processamento dos dados

rendimento = deposito * taxaJuros / 100

valorTotal = deposito + rendimento

#Impressão dos dados

print("Valor do rendimento: ",rendimento," Valor total: ",valorTotal)
