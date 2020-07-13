#11) Escreva um algoritmo em PYTHON que receba dez números do usuário e imprima o cubo de cada número.

#importando a biblioteca math

import math

#constante n

n = 1

#Processamento e impressao dos dados

while(n <= 10):
    valor =  int(input("Digite um valor: "))
    cubo = math.pow(valor,3)
    print("O cubo do valor ",valor," = ",cubo)
    n = n + 1

