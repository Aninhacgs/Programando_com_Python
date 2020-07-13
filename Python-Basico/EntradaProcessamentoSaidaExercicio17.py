#O produto de uma série de termos de uma Progressão Geométrica (P.G.) pode ser calculado pela fórmula: P = a1 ** n * q ** (n * (n - 1) / 2. Agora, escreva um algoritmo
#em PYTHON para determinar o produto dos n primeiros termos de uma P.G.

#Entrada de dados

a1 = int(input("Digite o valor correspondente ao primeiro termo: "))

q = int(input("Digite o valor correspondente a razão: "))

n = int(input("Digite o valor correspondente a quantidade de termos: "))

#Processamento dos dados

P = a1 ** n * q ** (n * (n - 1) / 2)

#Impressão do processamento

print("Produto da P.G: ", P)
