#Escreva um algoritmo em PYTHON que leia uma temperatura em gruas centígrados e apresente a temperatura convertida em graus Fahrenheit.
#A fórmula de conversão é: F = (9 * C + 160) / 5
#Onde F é a temperatura em Fahrenheit e C é a temperatura em centígrados

#Entrada de dados

C = float(input("Digite a temperatura em graus centigrados: "))

#Processamento dos dados

F = (9 * C + 160) / 5

#Impressão dos dados

print("Temperatura em Fahrenheit: ",F)
