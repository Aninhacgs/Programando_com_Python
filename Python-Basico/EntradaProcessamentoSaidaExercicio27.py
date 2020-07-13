#Criar um algoritmo em PORTUGOL que efetue o cálculo da quantidade de litros de combustível gastos em uma viagem, sabendo-se que o carro faz 12 km com um litro.
#Deverão ser fornecidos o tempo gasto na viagem e a velocidade média. O algoritmo deverá apresentar os valores da Distância percorrida e a quantidade de
#Litros utilizados na viagem. Distância = Tempo x Velocidade  Litros = Distancia / 12

#Entrada de dados
velocidade = float(input("Digite o valor da velocidade: "))

unidadeVelocidade = input("Digite o valor da unidade da velocidade se é m/s ou km/h: ")

while(unidadeVelocidade != "m/s" and unidadeVelocidade != "km/h"):
    print("Digite um valor valido para unidade da velocidade!")
    unidadeVelocidade = input("Digite o valor da unidade da velocidade se é m/s ou km/h: ")

hora = int(input("Digite o valor referene a hora: "))

minuto = int(input("Digite o valor referente ao minuto: "))

conversaoMinuto = float(minuto / 60)

segundo = int(input("Digite o valor referente ao segundo: "))

conversaoSegundo = float(segundo / 3600)

tempoTotal = hora + conversaoMinuto + conversaoSegundo

#Processamento dos dados

if(unidadeVelocidade == "m/s"):
    conversaoVelocidade = float (velocidade / 3.6)
    distancia = conversaoVelocidade * tempoTotal

elif (unidadeVelocidade == "km/h"):
    distancia = velocidade * tempoTotal


litros = distancia / 12

conversaoDistancia = round(distancia,2)

conversaoLitros = round(litros,2)

#Impressão dos dados

print("Distancia percorrida: ",conversaoDistancia,"km")
print("Quantidade de litros: ",conversaoLitros,"litros")
