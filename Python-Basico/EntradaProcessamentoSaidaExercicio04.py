#4)Dada a razão de uma P.G. (progressão geométrica) e um termo qualquer, k (ak).Escreva um algoritmo em PYTHON para calcular qualquer outro termo, n, (an).
#an = ak * q **(n - k)

#Entrada de dados
ak = int(input("Digite o valor do primeiro termo: "))

q = int(input("Digite o valor da razão: "))

n = int(input("Digite o valor de n: "))

k = int(input("Digite o valor do termo que deseja calcular: "))

#Processamento dos dados

an = ak * q ** (n - k)

#Impressão do processamento

print("O valor da P.G para o termo ",k,"é: ",an)
