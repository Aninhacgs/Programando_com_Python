#Criar um algoritmo em PYTHON que imprima todos os números de 1 até 100, inclusive, e a soma do quadrado desses números.

#importando a biblioteca math
import math

#Inicialiação de variável
n = 1
soma = 0


#Processamento e impressão
print("----------VALORES DO INTERVALO 1 A 100----------")
while(n <= 100):
    print(n)
    quadrado = math.pow(n,2)
    soma = soma + quadrado
    n = n + 1

print("----------A SOMA DO QUADRADO DOS VALORES DO INTERVALOR DE 1 A 100---------- = ",soma)


