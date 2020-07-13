#9) Escreva um algoritmo em PYTHON que imprima o quadrado dos números no intervalo fechado de 1 a 20.

#importando a biblioteca math

import math

#constante n

n = 1

#Processamento e impressao dos dados

while(n <= 20):
    quadrado = math.pow(n,2)
    print(quadrado)
    n = n + 1
