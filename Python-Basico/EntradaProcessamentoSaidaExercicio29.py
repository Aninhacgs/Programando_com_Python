#Criar um algoritmo em PYTHON que efetue o cálculo do salário líquido de um professor. Os dados fornecidos serão: valor da hora aula, número de aulas dadas no
#mês e percentual de desconto do INSS.

#Entrada de dados
valorHora = float(input("Digite o valor da hora aula: "))

#implementação de segurança garantindo que o valor informado será válido
while(valorHora <= 0):
    print("Digite um valor válido para valor da hora aula!")
    valorHora = float(input("Digite o valor da hora aula: "))

numeroAulas = int(input("Digite a quantidade de aulas dadas: "))

#implementação de segurança garantindo que o valor informado será válido
while(numeroAulas <= 0):
    print("Digite um valor válido para número de aulas!")
    numeroAulas = int(input("Digite a quantidade de aulas dadas: "))

taxaINSS = float(input("Digite o valor referene a taxa do INSS: "))

#implementação de segurança garantindo que o valor informado será válido
while(taxaINSS <= 0):
    print("Digite um valor válido para taxa INSS!")
    taxaINSS = float(input("Digite o valor referene a taxa do INSS: "))

#Processamento dos dados

salarioBruto = valorHora * numeroAulas

conversaoSB = round(salarioBruto,2)

desconto = salarioBruto * taxaINSS / 100

conversaoDesconto = round(desconto,2)

salarioLiquido = salarioBruto - desconto

conversaoSL = round(salarioLiquido,2)

#Impressão dos dados

print("Valor do salário bruto R$:",conversaoSB)
print("Valor do desconto do INSS R$:",conversaoDesconto)
print("Valor do salário liquido R$:",conversaoSL)
