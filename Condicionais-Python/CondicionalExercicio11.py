#Criar um algoritmo em PYTHON que leia o destino do passageiro, se a viagem inclui retorno (ida e volta) e informar o preço da passagem conforme a tabela a seguir:
#1-Região Norte, 2-Região Nordeste, 3-Região Centro-Oeste, 4-Região Sul

#Entrada de dados
print("Digite um dos valores abaixo para selecionar a região\n")
print("1 - Região Norte \n")
print("2 - Região Nordeste \n")
print("3 - Região Centro-Oeste \n")
print("4 - Região Sul \n")

regiao = int(input("Digite o código referrente a região: "))

while(regiao != 1 and regiao != 2 and regiao != 3 and regiao !=4):
             print("Digite uma região válida!")
             regiao = int(input("Digite o código referente a região"))
             

passagem =input("Caso deseje uma passagem apenas para ida escreva sim, caso contrário escreva não: ")

while(passagem != "sim" and passagem != "SIM" and passagem != "Sim" and passagem != "NÃO"
      and passagem != "não" and passagem != "Não"):
    print("Digite um valor válido para passagem apenas de ida!")
    passagem =input("Caso deseje uma passagem apenas para ida escreva sim, caso contrário escreva não")

#Processamento / impressão dos dados
if(passagem == "sim" or passagem == "SIM" or passagem == "Sim"):
    if(regiao == 1):
        print("Valor da passagem de ida para região norte R$:500,00")
    elif(regiao == 2):
        print("Valor da passagem de ida para região nordeste R$:350,00")
    elif(regiao == 3):
        print("Valor da passagem de ida para região centro-oeste R$:350,00")
    elif(regiao == 4):
        print("Valor da passagem de ida para região sul R$:300,00")

elif(passagem == "não" or passagem == "NÃO" or passagem == "NÃO"):
    if(regiao == 1):
        print("Valor da passagem de ida e volta para região norte R$:900,00")
    elif(regiao == 2):
        print("Valor da passagem de ida e volta para região nordeste R$:650,00")
    elif(regiao == 3):
        print("Valor da passagem de ida e volta para região centro-oeste R$:600,00")
    elif(regiao == 4):
        print("Valor da passagem de ida e volta para região sul R$:550,00")



    
