from random import randint
from time import sleep
lista = []
jogos = []
print('-' * 50)
print('                    MEGA SENA        ')
print('-' * 50)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot +=1
print('-=' * 5 , f'Sorteando {quant} jogos...', '-=' * 5)
for i, l in enumerate(jogos):
    print(f'\033[0;30mJogo {i+1}\033[m - \033[0;32m{l}\033[m')
    sleep(1)
print('-=' * 5,'\033[1;36m< BOA SORTE >\033[m','-=' * 5)


