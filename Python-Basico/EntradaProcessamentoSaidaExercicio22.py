#Criar um algoritmo em PYTHON que leia o numerador e o denominador de uma fração e transforme esses valores em um número racional.

#Entrada de dados

numerador = float(input("Digite o valor do numerador: "))

denominador = float(input("Digite o valor do denominador: "))


#Verificação dos valores do numerador e denominador para impedir divisã por zero

while(numerador == 0):
    print("Digite um valor válido para o numerador!")
    numerador = float(input("Digite o valor do numerador: "))

while(denominador == 0):
    print("Digite um valor válido para o denominador!")
    denominador = float(input("Digite o valor do denominador: "))


#Processamento dos dados

numeroReal = float (numerador / denominador)


#Impressão do processamento

print("O número real gerado pela divisão do numerador ",numerador, "e do denominador ", denominador, "é: ",numeroReal)


