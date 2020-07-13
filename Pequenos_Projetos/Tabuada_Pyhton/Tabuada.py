
j = range(0, 11)
opcao = 0


while(opcao!=5):
    print("========== TABUADA ==========")
    print("1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n5 - Sair")
    opcao=int(input("\n\nSelecione uma opção: "))
    if(opcao == 1):
        n = int(input("Digite o valor para gerar a tabuada: "))
        for i in j:
            print("\t",i," + ",n," = ",i+n)

    elif(opcao == 2):
        n = int(input("Digite o valor para gerar a tabuada: "))
        for i in j:
            print("\t",i," - ",n," = ",i-n)

    elif(opcao == 3):
        n = int(input("Digite o valor para gerar a tabuada: "))
        for i in j:
            print("\t",i," * ",n," = ",i*n)

    elif(opcao == 4):
        n = int(input("Digite o valor para gerar a tabuada: "))
        for i in j:
            div = i / n
            aux = round(div,2)
            print("\t",i," / ",n," = ",aux)



