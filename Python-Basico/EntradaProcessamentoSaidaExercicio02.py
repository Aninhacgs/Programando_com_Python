#2)Uma P.G. (progressão geométrica) fica determinada pela sua razão (q) e pelo primeiro termo (a1). Escreva um algoritmo em PORTUGOL que seja capaz de determinar
#qualquer termo de uma P.G., dado a razão e o primeiro termo.

#Entrada de dados

a1 = int(input("Digite o valor do primeiro termo: "))

q = int(input("Digite o valor da razão: "))

n = int(input("Digite o valor de n: "))

#processamento dos dados

an = a1 * q ** (n-1)

#impressão do processamento dos dados

print("O valor da P.G. é: ",an)
