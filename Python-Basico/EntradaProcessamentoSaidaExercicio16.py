#Seja uma seqüência A,B,C, ... determinando um Progressão Geométrica (P.G.), o termo médio (B) de uma P.G. é determinado pela média geométrica de seus termos,
#sucessor (C) e antecessor (B).Com base neste enunciado construa um algoritmo em PYTHON que calcule o termo médio (B) através de A, C. Utilize a fórmula B² = A * C

#Entrada de dados

A = int(input("Digite o valor correspondente ao antecessor: "))

C = int(input("Digite o valor correspondente ao sucessor: "))

#Processamento dos dados

B = str(A * C)

#Impressão do processamento

print("Termo Médio da P.G: ",B)
