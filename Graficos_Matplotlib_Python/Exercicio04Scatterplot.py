import matplotlib.pyplot as plt
x = [1,3,5,7,9]
y = [2,3,7,1,0]

titulo = "Gráfico de Barras"
eixox = "Eixo x"
eixoy = "Eixo y"


plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.scatter(x,y, label = "Meus Pontos",color = "r", marker="*", s=100)
plt.legend()
plt.plot(x,y, color="k",linestyle = ":")
plt.show()