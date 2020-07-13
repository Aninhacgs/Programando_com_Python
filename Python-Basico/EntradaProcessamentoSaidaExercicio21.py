#Criar um algoritmo em PYTHON que leia dois valores para as variáveis A e B, que efetue a troca dos valores de forma que a variável A passe a ter o valor da variável B e
#que a variável B passe a ter o valor da variável A. Apresente os valores trocados.

#Entrada dos dados

valor1 = int(input("Digite o primeiro valor: "))

valor2 = int(input("Digite o segundo valor: "))

#Processamento dos dados

auxiliar = valor2

valor2 = valor1

valor1 = auxiliar

#Impressão dos dados

print("Inversao dos valores: Primeiro valor ",valor1, " Segundo valor ",valor2)
