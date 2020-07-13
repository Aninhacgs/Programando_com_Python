#Dados três valores A, B e C, construa um algoritmo em PYTHON para verificar se estes valores podem ser valores dos lados de um triângulo, e se for um triângulo
#retângulo, determinar (imprimir) os seus ângulos internos.

#Importando a biblioteca
import math

#Entrada de dados

A = float(input("Digite o valor do ângulo A: "))

while(A == 0 or A < 0):
    print("Digite um valor válido para o ângulo!")
    A = float(input("Digite o valor do ângulo A: "))

B = float(input("Digite o valor do ângulo B: "))

while(B == 0 or B < 0):
    print("Digite um valor válido para o ângulo!")
    B = float(input("Digite o valor do ângulo B: "))

C = float(input("Digite o valor do ângulo C: "))

while(C == 0 or C < 0):
    print("Digite um valor válido para o ângulo!")
    C = float(input("Digite o valor do ângulo C: "))

#Processamento / impressão
if(A < B + C and B < A + C):
    print("É um triângulo!")
    ANG3 = 0

elif(A > B and A > C):
    print("É um triângulo retângulo!")
    ANG1 = math.asin(B / A)
    print("Arco-seno: ",ANG1)
    ANG2 = math.acos(C / A)
    print("Arco-cosseno: ",ANG2)

elif(B > A and B > C):
    print("É um triângulo retângulo!")
    ANG1 = math.asin(A / B)
    print("Arco-seno: ",ANG1)
    ANG2 = math.acos(C / B)
    print("Arco-cosseno: ",ANG2)

elif(C > A and C > B):
    print("É um triângulo retângulo!")
    ANG1 = math.asin(A / C)
    print("Arco-seno: ",ANG1)
    ANG2 = math.acos(B / C)
    print("Arco-cosseno: ",ANG2)

else:
    print("Os valores digitados não podem ser lados de um triângulo!")
