#13) Escreva um algoritmo em PYTHON que receba dez números do usuário e imprima a metade de cada número.

#constante n

n = 1

#Processamento e impressao dos dados

while(n <= 10):
    valor =  float(input("Digite um valor: "))
    metade = valor / 2
    conversao = round (metade,2)
    print("A metade do valor ",valor," = ",conversao)
    n = n + 1
