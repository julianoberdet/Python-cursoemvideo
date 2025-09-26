#Escreva um programa que faça o computador "pensar" em um número de 0 a 5 e peça para o usuário
#tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela
#se o usuário venceu ou perdeu


from random import randint
from time import sleep
computador = randint(0,5)
print('-=-' *20)
print('Vou pensar em número de 0 a 5.Tente advinhar..')
print('-=-' *20)
numero = int(input('em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
print('E O RESULTADO É...')
sleep(3)
print(computador)
if computador == numero:
    print('PARABÉNS, você me ganhou 😃')
else:
    print(f'GANHEI! Eu pensei no número {computador} e não no {numero} 😞')
print('Muito obrigado, até a próxima!')
