#Antes de o racionamento de energia ser decretado, quase ninguém falava em quilowatts; mas, agora, todos incorporaram essa palavra em seu vocabulário. Sabendose
#que 100 quilowatts de energia custa um sétimo do salário mínimo, fazer um algoritmo em PYTHON que receba o valor do salário mínimo e a quantidade de quilowatts gasta por uma residência e calcule (imprima).
#- o valor em reais de cada quilowatt;
#- o valor em reais a ser pago;
#- o novo valor a ser pago por essa residência com um desconto de 10%.

#Entrada de dados

salarioMinimo = float(input("Digite o valor referente ao salário minimo: "))

while(salarioMinimo <= 0):
    print("Digite um valor válido para salario minímo!")
    salarioMinimo = float(input("Digite o valor referente ao salário minimo: "))

quantidadeQW = float(input("Digite o valor da quantidade de quilowatt gasto na residência: "))

while(quantidadeQW <= 0):
    print("Digite um valor válido para salario minímo!")
    quantidadeQW = float(input("Digite o valor da quantidade de quilowatt gasto na residência: "))

#Processamento dos dados

valorQW = (salarioMinimo / 7) / 100

valorPago = quantidadeQW * valorQW

desconto = valorPago * (10 / 100)

novoValor = valorPago - desconto

#Limitação de 2 casas decimais para os valores

conversaoValorQW = round (valorQW,2)

conversaoPG = round (valorPago,2)

conversaoNV = round (novoValor,2)

#Impressão do processamento

print("Valor em reais de cada quilowatt R$:",conversaoValorQW)

print("Valor em reais a ser pago R$:",conversaoPG)

print("Valor a ser pago com desconto de 10% R$:",conversaoNV)
