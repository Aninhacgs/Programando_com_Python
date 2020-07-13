#Construir um algoritmo em PYTHON para calcular as raízes de uma equação do 2ºgrau, sendo que os valores dos coeficientes A, B, e C devem ser fornecidos pelo
#usuário através do teclado.

#Importação da biblioteca math
import math

#Entrada de dados
A = float(input("Digite o valor de A: "))

B = float(input("Digite o valor de B: "))

C = float(input("Digite o valor de C: "))

#Processamento / impressão dos dados

delta = math.pow(B,2) - 4 *A * C

if(delta > 0):
    x1 = (- B + math.sqrt(delta)) / (2 * A)
    converte1 = round(x1,2)
    print("Valor de x1 ",converte1)
    x2 = (- B - math.sqrt(delta)) / (2 * A)
    converte2 = round(x2,2)
    print("Valor de x1 ",converte2)

elif (delta == 0):
    x1 = - B / (2 * A)
    converte1 = round(x1,2)
    print("Valor de x1 ",converte1)
    x2 = x1
    converte1 = round(x1,2)
    print("Valor de x1 ",converte2)
else:
    print("Não existem raízes reais!")
