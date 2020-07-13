#Certo dia o professor de Johann Friederich Carl Gauss (aos 10 anos de idade) mandou que os alunos somassem os números de 1 a 100.
#Imediatamente Gauss achou a resposta – 5050 – aparentemente sem cálculos.
#Supõe-se que já aí, Gauss, houvesse descoberto a fórmula de uma soma de uma progressão aritmética. Sn = (a1 + an) * n / 2
#Agora você, com o auxílio dos conceitos de algoritmos e da linguagem PYTHON, construa um algoritmo para realizar a soma de uma P.A.
#de N termos, com o primeiro a1 e o último an.


#Entrada de dados

a1 = int(input("Digite o valor do primeiro termo: "))

an = int(input("Digite o valor do último termo: "))

n = int(input("Digite a quantidade de termos: "))

#Processamento dos dados

Sn = (a1 + an) * n / 2

#Impressão do processamento

print("O resultado da soma da P.A para quantidade ",n," termos é: ",Sn)
