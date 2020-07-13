#Desenvolvedora: Ana Gomes
#Data: 18/12/2018

#importanto a bibilioteca Math
import math

#Definindo a constante

resposta = 0

#Calculadora

print("--------------------CALCULADORA--------------------\n")
print("Escolha uma opção para selecionar a operação matemática\n")
print("Opção - 01 - Soma")
print("Opção - 02 - Subtração")
print("Opção - 03 - Multiplicação")
print("Opção - 04 - Divisão")
print("Opção - 05 - Raiz Quadrada")
print("Opção - 06 - Fatorial")
print("Opção - 07 - coseno")
print("Opção - 08 - seno")
print("Opção - 09 - Potenciação")
print("Opção - 10 - Hipotenusa")
print("Opção - 11 - Teto")
print("Opção - 12 - X com sinal de Y")
print("Opção - 13 - Valor absoluto")
print("Opção - 14 - Piso")
print("Opção - 15 - Verificar se o valor de x é positivo ou negativo infinito")
print("Opção - 16 - Verificar se o valor de x é um NAN segundo o IEEE 754")
print("Opção - 17 - Calcular x * (2 ** i)")
print("Opção - 18 - Verificar a parte inteira e a parte fracionária de x")
print("Opção - 19 - Verificar o valor truncado de x")
print("Opção - 20 - calcular a potenciação do valor de euler elevado ao valor de x")
print("Opção - 21 - calcular a potenciação do valor de euler elevado ao valor de x - 1")
print("Opção - 22 - calcular o logaritmo de log(x) / log(base)")
print("Opção - 23 - calcular o logaritmo de natural 1 + x (base e)")
print("Opção - 24 - calcular o logaritmo na base 10")
print("Opção - 25 - calcular o logaritmo na base 2")
print("Opção - 26 - calcular o arco seno de x")
print("Opção - 27 - calcular a tangente de x")
print("Opção - 28 - calcular o arco tangente de x")
print("Opção - 29 - calcular o arco coseno de x")
print("Opção - 30 - calcular atan(y / x)")
print("Opção - 31 - consultar o valor de pi")
print("Opção - 32 - consultar o valor de euler")
print("Opção - 33 - converter o ângulo em graus")
print("Opção - 34 - converter o ângulo em radianos")
print("Opção - 35 - Calcular o seno hiperbólico inverso de x")
print("Opção - 36 - Calcular o cosseno hiperbólico inverso de x")
print("Opção - 37 - Calcular a tangente hiperbólica inversa de x")
print("Opção - 38 - Calcular o seno hiperbólico de x")
print("Opção - 39 - Calcular o cosseno hiperbólico de x")
print("Opção - 40 - Calcular a tangente hiperbólica de x")
print("Opção - 41 - Calcular a função de erro de x")
print("Opção - 42 - Calcular a função de erro complementar em x")
print("Opção - 43 - Calcular a função gamma de x")
print("Opção - 44 - Logaritmo natural do valor absoluto da função Gamma em x")
print("Opção - 45 - Calcular a mantissa e o expoente de x")
print("Opção - 46 - Calcular o mod da divisão de dois números")
print("Opção - 47 - Calcular o maior divisor comum de dois números")
print("Opção - 48 - Calcular a aproximidade dos valores x e y")
print("Opção - 49 - Verificar se o valor de x não é infinito ou NaN")
print("Opção - 50 - consultar o valor da constante")
print("Opção - 51 - Somar os valores de um vetor")

while(resposta == 0):
    opcao = int(input("Digite a opção: "))

    if(opcao == 1):
        valor1 = int(input("Digite o primeiro valor: "))
        valor2 = int(input("Digite o segundo valor: "))
        soma = valor1 + valor2
        print("A soma dos valores ",valor1," e ",valor2," = ",soma,"\n")
        

    elif(opcao == 2):
        valor1 = int(input("Digite o primeiro valor: "))
        valor2 = int(input("Digite o segundo valor: "))
        subtracao = valor1 - valor2
        print("A subtração dos valores ",valor1," e ",valor2," = ",subtracao,"\n")


    elif(opcao == 3):
        valor1 = int(input("Digite o primeiro valor: "))
        valor2 = int(input("Digite o segundo valor: "))
        multiplicacao = valor1 * valor2
        print("A multiplicação dos valores ",valor1," e ",valor2," = ",multiplicacao,"\n")

    elif(opcao == 4):
        valor1 = float(input("Digite o primeiro valor: "))
        valor2 = float(input("Digite o segundo valor: "))
        divisao = valor1 / valor2
        casas = round(divisao,2)
        print("A divisao dos valores ",valor1," e ",valor2," = ",casas,"\n")


    elif(opcao == 5):
        valor = float(input("Digite o valor: "))
        raiz = math.sqrt(valor)
        print("A raiz quadrada do valor ",valor," = ",raiz,"\n")



    elif(opcao == 6):
        valor = float(input("Digite o valor: "))
        fatorial = math.factorial(valor)
        print("O fatorial do valor ",valor," = ",fatorial,"\n")

    elif(opcao == 7):
        valor = float(input("Digite o valor do ângulo: "))
        coseno = math.cos(valor)
        print("O coseno do ângulo ",valor," = ",coseno,"\n")


    elif(opcao == 8):
        valor = int(input("Digite o valor do ângulo: "))
        seno = math.sin(valor)
        print("O seno do ângulo ",valor," = ",seno,"\n")


    elif(opcao == 9):
        valor1 = int(input("Digite o valor da base: "))
        valor2 = int(input("Digite o valor do expoente: "))
        potenciacao = math.pow(valor1,valor2)
        print("A potenciação dos valores ",valor1," e ",valor2," = ",potenciacao,"\n")

    elif(opcao == 10):
        valor1 = int(input("Digite o valor do cateto x: "))
        valor2 = int(input("Digite o valor do cateto y: "))
        hipotenusa = math.hypot(valor1, valor2)
        casas = round(hipotenusa,2)
        print("A hipotenusa dos catetos ",valor1," e ",valor2," = ",casas,"\n")


    elif(opcao == 11):
         valor = float(input("Digite o valor: "))
         teto = math.ceil(valor)
         print("O teto do valor ",valor," = ",teto,"\n")

    elif(opcao == 12):
        valor1 = int(input("Digite o valor de x: "))
        valor2 = int(input("Digite o valor de y: "))
        inversao = math.copysign(valor1,valor2)
        print("A inversão de sinal ",valor1," e ",valor2," = ",inversao,"\n")


    elif(opcao == 13):
        valor = float(input("Digite o valor: "))
        absoluto = math.fabs(valor)
        print("O valor absoluto do valor ",valor," = ",absoluto,"\n")

    
    elif(opcao == 14):
        valor = float(input("Digite o valor: "))
        piso = math.floor(valor)
        print("O piso do valor ",valor," = ",piso,"\n")


    elif(opcao == 15):
        valor = float(input("Digite o valor: "))
        verifica = math.isinf(valor)
        print("o valor ",valor," = ",verifica,"\n")


    elif(opcao == 16):
        valor = float(input("Digite o valor: "))
        verifica = math.isnan(valor)
        print("o valor ",valor," = ",verifica,"Segundo o IEEE 754\n")


    elif(opcao == 17):
        x = float(input("Digite o valor de x : "))
        i = int(input("Digite o valor de i: "))
        calcula = math.ldexp(x,i)
        print("o resultado a operação x * (2 ** i) dos valores ",x," e ",i," = ",calcula,"\n")


    elif(opcao == 18):
        valor = float(input("Digite o valor: "))
        verifica = math.modf(valor)
        print("A parte fracionária e parte inteira de ",valor," = ",verifica,"\n")


    elif(opcao == 19):
        valor = float(input("Digite o valor: "))
        verifica = math.trunc(valor)
        print("O valor truncado de ",valor," = ",verifica,"\n")
        
    
    elif(opcao == 20):
        x = float(input("Digite o valor: "))
        verifica = math.exp(x)
        print("O resultado de (e ** x) de ",x," = ",verifica,"\n")


    elif(opcao == 21):
        x = float(input("Digite o valor: "))
        verifica = math.expm1(x)
        print("O resultado de e ** x - 1 de ",x," = ",verifica,"\n")


    elif(opcao == 22):
        x = int(input("Digite o valor de x: "))
        base = int(input("Digite o valor da base: "))
        log = math.log(x,base)
        print("O valor do log de log(x) ",x," / log(base) ",base," = ",log,"\n")


    elif(opcao == 23):
        x = float(input("Digite o valor: "))
        verifica = math.log1p(x)
        print("O logaritmo de 1 + x (base e) do valor ",x," = ",verifica,"\n")


    elif(opcao == 24):
        x = float(input("Digite o valor: "))
        verifica = math.log10(x)
        print("O logaritmo na base 10 do valor ",x," = ",verifica,"\n")


    elif(opcao == 25):
        x = float(input("Digite o valor: "))
        verifica = math.log2(x)
        print("O logaritmo na base 2 do valor ",x," = ",verifica,"\n")

    elif(opcao == 26):
        x = float(input("Digite o valor do ângulo: "))
        verifica = math.asin(x)
        print("O arco seno do ângulo ",x," = ",verifica,"\n")


    elif(opcao == 27):
        x = int(input("Digite o valor do ângulo: "))
        verifica = math.atan(x)
        print("A tangente do ângulo ",x," = ",verifica,"\n")


    elif(opcao == 28):
        x = int(input("Digite o valor do ângulo: "))
        verifica = math.atan(x)
        print("O arco tangente do ângulo ",x," = ",verifica,"\n")


    elif(opcao == 29):
        x = float(input("Digite o valor do ângulo: "))
        verifica = math.acos(x)
        print("O arco coseno do ângulo ",x," = ",verifica,"\n")


    elif(opcao == 30):
        x = int(input("Digite o primeiro valor de x: "))
        y = int(input("Digite o segundo valor de y: "))
        calcula = math.atan2(y,x)
        print("O resultado de atan(y / x) do valor de x ",x," e do valor de y ",y," = ",calcula,"\n")


    elif(opcao == 31):
        pi = math.pi
        print("O valor de pi =  ",pi,"\n")


    elif(opcao == 32):
        euler = math.e
        print("O valor de euler =  ",euler,"\n")


    elif(opcao == 33):
        angulo = int(input("Digite o valor do ângulo: "))
        graus = math.degrees(angulo)
        print("O valor do ângulo ",angulo," em graus =  ",graus,"\n")

    elif(opcao == 34):
        angulo = int(input("Digite o valor do ângulo: "))
        radianos = math.radians(angulo)
        print("O valor do ângulo ",angulo," em radianos =  ",radianos,"\n")


    elif(opcao == 35):
        angulo = int(input("Digite o valor do ângulo: "))
        seno = math.asinh(angulo)
        print("O seno hiperbólico do ângulo ",angulo," =  ",seno,"\n")


    elif(opcao == 36):
        angulo = int(input("Digite o valor do ângulo: "))
        cosseno = math.acosh(angulo)
        print("O cosseno hiperbólico do ângulo ",angulo," =  ",cosseno,"\n")


    elif(opcao == 37):
        angulo = float(input("Digite o valor do ângulo: "))
        tangente = math.atanh(angulo)
        print("A tangente hiperbólica do ângulo ",angulo," =  ",tangente,"\n")


    elif(opcao == 38):
        angulo = int(input("Digite o valor do ângulo: "))
        senoh = math.sinh(angulo)
        print("O seno hiperbólico do ângulo ",angulo," =  ",senoh,"\n")


    elif(opcao == 39):
        angulo = int(input("Digite o valor do ângulo: "))
        cossenoh = math.cosh(angulo)
        print("O cosseno hiperbólico do ângulo ",angulo," =  ",cossenoh,"\n")

    elif(opcao == 40):
        angulo = int(input("Digite o valor do ângulo: "))
        tangenteh = math.tanh(angulo)
        print("A tangente hiperbólica do ângulo ",angulo," =  ",tangenteh,"\n")


    elif(opcao == 41):
        x = int(input("Digite o valor de x: "))
        funcao = math.erf(x)
        print("A função de erro de ",x," =  ",funcao,"\n")


    elif(opcao == 42):
        x = int(input("Digite o valor de x: "))
        funcao = math.erfc(x)
        print("A função de erro complementar ",x," =  ",funcao,"\n")


    elif(opcao == 43):
        x = int(input("Digite o valor de x: "))
        funcao = math.gamma(x)
        print("A função gamma de ",x," =  ",funcao,"\n")


    elif(opcao == 44):
        x = int(input("Digite o valor de x: "))
        funcao = math.lgamma(x)
        print("O logaritmo do valor absoluto da função gamma de ",x," =  ",funcao,"\n")


    elif(opcao == 45):
        x = float(input("Digite o valor de x: "))
        funcao = math.frexp(x)
        print("A mantissa e o expoente de ",x," =  ",funcao,"\n")


    elif(opcao == 46):
        valor1 = float(input("Digite o primeiro valor: "))
        valor2 = float(input("Digite o segundo valor: "))
        mod = math.fmod(valor1, valor2)
        print("O resto da divisão dos valores ",valor1," e ",valor2," = ",mod,"\n")


    elif(opcao == 47):
        x = int(input("Digite o primeiro valor: "))
        y = int(input("Digite o segundo valor: "))
        calcula = math.gcd(x,y)
        print("O maior divisor comum dos valores ",x," e ",y," = ",calcula,"\n")


    elif(opcao == 48):
        x = float(input("Digite o primeiro valor: "))
        y = float(input("Digite o segundo valor: "))
        calcula = math.isclose(x,y)
        print("Os valores ",x," e ",y," estão proximos? ",calcula,"\n")


    elif(opcao == 49):
        x = float(input("Digite o valor de x: "))
        funcao = math.isfinite(x)
        print("O valor ",x," não é infinito ou NaN? ",funcao,"\n")


    elif(opcao == 50):
        x = math.tau
        print("O valor da constante tau ",x,"\n")


    elif(opcao == 51):
        i = 0
        vet = []
        n = int(input("Digite a quantidade de números para o vetor: "))
        while(i <n):
            valor = float(input("Digite o valor: "))
            vet.append(valor)
            i = i + 1

        soma = math.fsum(vet)        
        
        print("A soma dos valores do vetor ",vet," = ",soma,"\n")


    else:
        print("Opção inválida!")


    resposta = int(input("Para realizar uma nova operação digite 0 e para finalizar digite 1: "))



