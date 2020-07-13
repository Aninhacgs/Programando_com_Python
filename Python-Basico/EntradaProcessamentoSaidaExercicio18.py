#Em épocas de pouco dinheiro, os comerciantes estão procurando aumentar suas vendas oferecendo desconto. Faça um algoritmo em PYTHON que possa entrar com o valor
#de um produto e imprima o novo valor tendo em vista que o desconto foi de 9%. Além disso, imprima o valor do desconto.

#Entrada de dados

valor = float(input("Digite o valor do produto RS: "))

#Processamento dos dados

Desconto = ((valor * 9) / 100) * 100

#Impressão dos dados

print("Valor com 9% de desconto R$:",Desconto)

