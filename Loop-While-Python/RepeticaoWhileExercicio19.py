#Criar um algoritmo em PYTHON que leia um número (NUM), e depois leia NUM números inteiros e imprima o maior deles. Suponha que todos os números lidos serão positivos.


#Entrada de valores

valor1 = int(input("Digite o primeiro valor: "))

while(valor1 < 0):
    print("O valor deve ser maior do que zero!")
    valor1 = int(input("Digite o primeiro valor: "))

    
valor2 = int(input("Digite o segundo valor: "))

while(valor2 < 0):
    print("O valor deve ser maior do que zero!")
    valor2 = int(input("Digite o primeiro valor: "))


#Processamento

while(valor2 < valor1):
    print("O segundo valor deve ser maior que o primeiro valor!")
    valor2 = int(input("Digite o segundo valor: "))


auxiliar = valor1

while(auxiliar < valor2):

    if(auxiliar > valor1 and auxiliar != valor2):
        maior = auxiliar

    auxiliar = auxiliar + 1

#Impressão do maior valor
    
print("O maior valor inteiro positivo do intervalo de ",valor1," e ",valor2," = ",maior)
