#3)Dada a razão de uma P.A. (progressão aritmética) e um termo qualquer, k (ak). Escreva um algoritmo em PORTUGOL para calcular qualquer outro termo, n, (an).
# an = ak + (n - k) * r

#Entrada de dados
ak = int(input("Digite o valor para o primeiro termo: "))

n = int(input("Digite o valor de n: "))

k = int(input("Digite o valor para o termo que deseja calcular: "))

r = int(input("Digite o valor da razão: "))

#Processamento de dados

an = ak + (n - k) * r

#Impressão do processamento

print("O valor da P.A referente ao termo ",k,"é: ",an)
