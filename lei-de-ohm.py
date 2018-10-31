
import math
valid = False


while valid == False:
    calc = input('O que você deseja calcular? Para resistência use "R", para votagem use "V" e para corrente use "A":').lower()
    if calc =='a' or calc == 'v' or calc == 'r':
        valid = True
    else:
        print('Digite apenas as letras "V", "R" e "A" para calculcar a Voltagem, Resistencia e Corrente, respectivamente.')


if calc =='a' or calc == 'v' or calc == 'r':
    if calc == 'a':
        r= float(input('Insira o valor da resistência. Use apenas valores separados por ponto:'))
        v= float(input('Insira o valor da voltagem. Use apenas valores separados por ponto:'))
        valor = round(r/v,3)
        print ('O valor da corrente é:', valor ,'A')

    elif calc == 'v':
        r= float(input('Insira o valor da resistência. Use apenas valores separados por ponto:'))
        i= float(input('Insira o valor da corrente:'))
        valor = round(i * r, 3)
        print ('O valor da voltagem é:', valor ,'V')

    elif calc == 'r':
        v= float(input('Insira o valor da voltagem. Use apenas valores separados por ponto:'))
        i= float(input('Insira o valor da corrente. Use apenas valores separados por ponto:'))
        valor = round(v / i,3)
        print ('O valor da resistencia é:', valor ,'Ω')
