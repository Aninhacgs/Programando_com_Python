#Criar um algoritmo em PYTHON que leia dois números e imprimir o quadrado do menor número e raiz quadrada do maior número, se for possível.

#importando a biblioteca math
import math

#Entrada de dados

valor1 = int(input("Digite o primeiro valor: "))

valor2 = int(input("Digite o segundo valor: "))

#Processamento dos dados

if(valor1 < valor2):
    quadrado = valor1 ** 2
    print("O quadrado do numero, ",valor1," é: ",quadrado)

    if(valor2 >= 0):
        raiz = math.sqrt(valor2)
        print("A raiz quadrada do numero, ", valor2," é: ",raiz)

    else:
        print("Não foi possível calcular a raiz quadrada do valor, ",valor2)

elif(valor2 < valor1):
    quadrado = valor2 ** 2
    print("O quadrado do numero, ",valor2," é: ",quadrado)

    if(valor1 >= 0):
        raiz = math.sqrt(valor1)
        print("A raiz quadrada do numero, ", valor1," é: ",raiz)

    else:
        print("Não foi possível calcular a raiz quadrada do valor, ",valor1)
    
