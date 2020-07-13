#Escreva um algoritmo em PYTHON que leia um número e informe se ele é ou não divisível por 5.

#Entrada de dados

N = int(input("Digite um valor: "))

#Processamento dos dados

if(N % 5 == 0):
    print("Numero ,N," é divisível por 5!")

else:
    print("Numero ",N," não é divisível por 5!")
