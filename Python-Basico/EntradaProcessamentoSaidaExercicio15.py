#Seja uma seqüência A,B,C, ... determinando um Progressão Aritmética (P.A.), o termo médio (B) de uma P.A. é determinado pela média aritmética de seus termos, sucessor (C) e antecessor (A).
#Com base neste enunciado construa um algoritmo em PYTHON que calcule o termo médio (B) através de A, C. Utilize a fórmula B = (A + C) / 2

#Entrada de dados

A = int(input("Digite o valor correspondente ao antecessor: "))

C = int(input("Digite o valor correspondente ao sucessor: "))

#Processamento dos dados

B = (A + C) / 2

#Impressão do processamento

print("Termo Médio: ",B)
