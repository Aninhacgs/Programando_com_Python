#Crie um algoritmo em PORTUGOL que leia a idade de uma pessoa e informe a sua
#classe eleitoral:
#- não eleitor (abaixo de 16 anos);
#- eleitor obrigatório (entre a faixa de 18 e menor de 65 anos);
#- eleitor facultativo (de 16 até 18 anos e maior de 65 anos, inclusive).

#Entrada de dados

idade = int(input("Digite a idade: "))

while(idade == 0 or idade < 0):
    print("Digite uma idade válida!")
    idade = int(input("Digite a idade: "))     

#Processamento e impressão

if(idade < 16):
    print("Não eleitor")

elif(idade > 18 and idade < 65):
    print("Eleitor obrigatorio")

elif(idade == 16 or idade <= 18 or idade > 65):
    print("Eleitor facultativo")

