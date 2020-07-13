#Escreva um algoritmo em PYTON para determinar se um dado número N (recebido através do teclado) é POSITIVO, NEGATIVO ou NULO

#Entrada de dados

N = int(input("Digite um valor: "))

#Processamento dos dados

if(N == 0):
    print("O numero ", N," é nulo!")

elif(N > 0):
    print("O número ",N," é positivo!")

elif(N < 0):
    print("O número ",N,"é negativo!")
