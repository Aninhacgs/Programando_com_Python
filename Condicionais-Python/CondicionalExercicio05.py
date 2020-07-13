#A prefeitura de Contagem abriu uma linha de crédito para os funcionários estatutários.O valor máximo da prestação não poderá ultrapassar 30% do salário bruto. Fazer um
#algoritmo que permita entrar com o salário bruto e o valor da prestação, e informar se o empréstimo pode ou não ser concedido.

#Entrada de dados

salario = float(input("Digite o valor referente ao salário: "))

while(salario == 0 or salario < 0):
    print ("Digite um valor válido para salário!")
    salario = float(input("Digite o valor referente ao salário: "))

prestacao = float(input("Digite o valor referente a prestação: "))

while(prestacao == 0 or prestacao < 0):
    print ("Digite um valor válido para prestação!")
    prestacao = float(input("Digite o valor referente a prestação: "))

#Processamento / impressão dos dados

percentual = salario * (30 / 100)

if(prestacao <= percentual):
    print("O empréstimo pode ser concedido!")

else:
    print("O empréstimo não pode ser concedido!")
