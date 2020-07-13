#entrada de dados
numero = int(input("Digite um valor: "))

#Verifica se o valor inserido pode ser calculado

while(numero == 0 or numero < 1):
    print("valor incorreto!")
    numero = int(input("Digite um valor: "))


#Processamento de impressao
for n in range(11):
    print(numero," X ",n," = ",numero * n)
