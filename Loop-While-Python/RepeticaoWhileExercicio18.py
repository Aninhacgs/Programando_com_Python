#Criar um algoritmo em PYTHON que imprima todos os números de 1 até 100, inclusive, e a média de todos eles.

#Inicialiação de variável
n = 1
soma = 0


#Processamento e impressão
print("----------VALORES DO INTERVALO 1 A 100----------")
while(n <= 100):
    print(n)
    soma = soma + n
    n = n + 1


media = float (soma / 100)

print("----------A MÉDIA DOS VALORES DO INTERVALO DE 1 A 100---------- = ",media)
