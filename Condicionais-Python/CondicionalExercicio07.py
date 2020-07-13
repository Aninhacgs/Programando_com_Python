#Criar um algoritmo em PYTHON que leia o valor da compra e imprima o valor da venda.

#Entrada de dados
compra = float(input("Digite o valor da compra: "))

while(compra == 0 or compra < 0):
    print("Digite  um valor válido para compra: ")
    compra = float(input("Digite o valor da compra: "))

#processamento e impressão
if(compra < 10):
    venda = compra + compra *(70 / 100)
    conversao = round(venda,2)
    print("Valor da venda R$:",conversao)

elif(compra < 30):
    venda = compra + compra * (50 / 100)
    conversao = round(venda,2)
    print("Valor da venda R$:",conversao)

elif(compra < 50):
    venda = compra + compra * (40 / 100)
    conversao = round(venda,2)
    print("Valor da compra R$:",conversao)

else:
    venda = compra + compra * (30 / 100)
    conversao = round(venda,2)
    print("Valor da compra R$:",conversao)
