def criarArquivo():
    arquivo = open("dados.txt","w")
    arquivo.close()

def escreveArquivo():
    nome = input("Por favor digite seu nome: ")

    arquivo = open("dados.txt","a")
    arquivo.write(nome)
    arquivo.write("\n(00)0000-0000\n")
    arquivo.close()

def lerArquivo():
    arquivo = open("dados.txt","r")
    line = arquivo.readline()

    while line != "":
        print(line)
        line = arquivo.readline()
    arquivo.close()

criarArquivo()
escreveArquivo()
lerArquivo()
