#Para vários tributos, a base de cálculo é o salário mínimo. Fazer um algoritmo em PYTHON que leia o valor do salário mínimo e o valor do salário de uma pessoa.
#Calcular e imprimir quantos salários mínimos essa pessoa ganha.

#Entrada de dados
salarioMinimo = float(input("Digite o valor do salário minímo: "))

while(salarioMinimo <=0):
    print("Digite um valor válido para salario minímo!")
    salarioMinimo = float(input("Digite o valor do salário minímo: "))

    
salarioBruto = float(input("Digite o valor do salário bruto: "))

while(salarioBruto <=0):
    print("Digite um valor válido para salario bruto!")
    salarioBruto = float(input("Digite o valor do salário minímo: "))

#Processamento dos dados

quantidade = float(salarioBruto / salarioMinimo)

arredondamento = round(quantidade,2)

#Impressão dos dados

print("Quantidade de salario minímos: ",arredondamento)


