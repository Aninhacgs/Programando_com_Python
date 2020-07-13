#10) Escreva um algoritmo em PYTHON que receba dez números do usuário e imprima o quadrado de cada número.

#importando a biblioteca math

import math

#constante n

n = 1

#Processamento e impressao dos dados

while(n <= 10):
    valor =  int(input("Digite um valor: "))
    quadrado = math.pow(valor,2)
    print("O quadrado do valor ",valor," = ",quadrado)
    n = n + 1
