#12) Escreva um algoritmo em PYTHON que receba quinze números do usuário e imprima a raiz quadrada de cada número.

import math

#constante n

n = 1

#Processamento e impressao dos dados

while(n <= 15):
    valor =  int(input("Digite um valor: "))
    raiz = math.sqrt(valor)
    print("A raiz quadrada do valor ",valor," = ",raiz)
    n = n + 1

