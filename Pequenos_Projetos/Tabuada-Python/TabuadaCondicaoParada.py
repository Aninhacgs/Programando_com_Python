#constante para condição de parada
resposta = 0

#Processamento de impressao com condição de parada
while(resposta == 0):
    #entrada de dados
    numero = int(input("Digite um valor: "))

#Verifica se o valor inserido pode ser calculado

    while(numero == 0 or numero < 1):
        print("valor incorreto!")
        numero = int(input("Digite um valor: "))

    print("----------TABUADA DO NÚMERO ",numero,"----------") 
       
    for n in range(11):
        print(numero," X ",n," = ",numero * n)

    resposta = int(input("Digite 1 (um) para finalizar ou 0 (zero) para calcular outro valor: "))
