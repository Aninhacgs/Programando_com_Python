#Criar um algoritmo em PYTHON que leia um número (NUM), e depois leia NUM números inteiros e imprima o menor deles.

#Entrada de valores

valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))

#Processamento

while(valor2 < valor1):
    print("O segundo valor deve ser maior que o primeiro valor!")
    valor2 = int(input("Digite o segundo valor: "))


auxiliar = valor2

while(auxiliar > valor1):

    if(auxiliar > valor1):
        menor = auxiliar

    auxiliar = auxiliar - 1


#Impressão do maior valor
    
print("O menor valor do intervalo de ",valor1," e ",valor2," = ",menor)
