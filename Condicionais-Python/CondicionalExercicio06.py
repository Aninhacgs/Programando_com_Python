#Construa um algoritmo em PYTHON, que receba três valores, A, B e C, e armazene-os em três variáveis com os seguintes nomes:
#MAIOR, INTER e MENOR (os nomes correspondem aos valores ordenados).

#Entrada de dados

A = float (input("Digite o valor referrente a A: "))

B = float(input("Digite o valor referente a B: "))

C = float(input("Digite o valor referente a C: "))

#Processamento e impressão

if(A < B and A < C):
    MENOR = A
    print("Menor valor ",MENOR)
    if(B < C):
        INTER = B
        print("Valor intermediário ",INTER)
        MAIOR = C
        print("Maior valor ",MAIOR)
    else:
        INTER = C
        MAIOR = B

if(B < A and B < C):
    MENOR = B
    print("Menor valor ",MENOR)
    if(A < C):
        INTER = A
        print("Valor intermediário ",INTER)
        MAIOR = C
        print("Maior valor ",MAIOR)
    else:
        INTER = C
        print("Valor intermediário ",INTER)
        MAIOR = A
        print("Maior valor ",MAIOR)

if(C < B and C < A):
    MENOR = C
    print("Menor valor ",MENOR)
    if(B < A):
        INTER = B
        print("Valor intermediário ",INTER)
        MAIOR = A
        print("Maior valor ",MAIOR)
    else:
        INTER = A
        print("Valor intermediário ",INTER)
        MAIOR = B
        print("Maior valor ",MAIOR)
