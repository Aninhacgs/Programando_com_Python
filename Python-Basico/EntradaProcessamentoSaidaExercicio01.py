#1) Uma P.A. (progressão aritmética) fica determinada pela sua razão (r) e pelo primeiro termo(a1). Escreva um algoritmo em PYTHON que seja capaz de determinar
#qualquer termo de uma P.A., dado a razão e o primeiro termo. an = a1+(n-1)*r

#Entrada de dados
a1 = float(input("Digite um valor para o primeiro termo: "))

while(a1 < 0.0 or a1 == 0.0):
    print("Digite um valor válido para o primeiro termo!")
    a1 = float(input("Digite um valor para o primeiro termo: "))

n = int(input("Digite a quantidade de termos que deseja calcular: "))

while(n == 0 or n < 0):
    print("Digite um valor válido para quantidade!")
    n = int(input("Digite a quantidade de termos que deseja calcular: "))

r = float(input("Digite um valor para a razão: "))

while(r == 0.0 or r < 0.0):
    print("Digite um valor válido para razão!")
    r = float(input("Digite um valor para a razão: "))

#Processamento dos dados

an = float(a1 + (n -1) * r)

#Conversão para duas casas decimais
conversao = round(an,2)

#Impressão dos dados

print("O valor da progressão aritmética é: ",conversao)
