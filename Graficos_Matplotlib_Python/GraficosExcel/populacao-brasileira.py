import matplotlib.pyplot as plt

dados = open("populacao-brasileira.csv").readlines()

x = []
y = []

for i in range(len(dados)):
    if i !=0:
        linha = dados[i].split(";")
        x.append(int(linha[0]))
        y.append(int(linha[1]))
        
plt.bar(x,y, color='c')
plt.plot(x,y, color='k', linestyle="--")
plt.title("Crescimento da População Brasileira")
plt.xlabel("Ano")
plt.ylabel("População X 100.000")
plt.show()
'''Salvando uma imagem
plt.savefig("PopulacaoBrasileira.png", dpi=300)'''