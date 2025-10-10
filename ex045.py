from random import randint
from time import sleep
itens = ('PEDRA','PAPEL','TESOURA')
computador = randint(0,2)
print('''Suas Opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual sua jogada? '))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('P0!!!')
print('-=' * 15)
print(f'O computador escolheu {itens[computador]}')
print(f'Você escolheu {itens[jogador]}')
print('-=' * 15)
if computador == 0: #Computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('VOCÊ GANHOU')
    elif jogador == 2:
        print('COMPUTADOR GANHOU')
    else:
        print('\033[34mJOGADA INVÁLIDA\033[m')
elif computador == 1: #Computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR GANHOU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('VOCÊ GANHOU')
    else:
        print('\033[34mJOGADA INVÁLIDA\033[m')
elif computador == 2: #Computador jogou TESOURA
    if jogador == 0:
        print('VOCÊ GANHOU')
    elif jogador == 1:
        print('COMPUTADOR GANHOU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('\033[34mJOGADA INVÁLIDA\033[m')
