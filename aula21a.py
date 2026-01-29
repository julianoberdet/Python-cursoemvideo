#Intercative help
'''help(print)
help(len)
help(input)
print(print.__doc__)'''

# DOCSTRING
'''def contador(i,f,p):
    """
    -> Faça uma contagem e mostra na tela.
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c} ',end='')
        c += p
    print('FIM!')

help(contador)'''

#Parâmetros opcionais
'''def somar(a=0,b=0,c=0):
    s = a+b+c
    print(f'A soma vale {s}')

somar(3,2,5)
somar(8,4)
somar()'''

#Escopo de variaveis
'''def teste(b):
    global a
    a = 8
    b += 4
    c = 2                                #Escopo local
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')
                                        #Escopo global
#Programa principal
a = 5
teste(a)
print(f'A fora vale {a}')'''

#Retorno de valores
'''def somar(a=0,b=0,c=0):
    s = a + b + c
    return s

r1 = somar(3,2,5)
r2 = somar(1,7)
r3 = somar(4)
print(f'Meus cálculos deram {r1}, {r2} e {r3}')'''

#Parte prática
     #Exemplo 1
'''def fatorial(num=1):
    f = 1
    for c in range(num,0,-1):
        f *= c
    return f

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}')'''
      #Exemplo 2
def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input('Digite um número: '))
if par(num):
    print('É Par')
else:
    print('Não é par')