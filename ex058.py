from random import randint
from time import sleep
computador = 0
numero = -1
totvezes = 0
while computador != numero:
    print('Tente acertar o numero que eu pensei')
    computador = randint(0, 10)
    numero = int(input('Digite um numero: '))
    print('Processando...')
    sleep (3)
    print(f'O computador pensou no número {computador}')
    if numero == computador:
        print('Você venceu')
        totvezes += 1
    else:
        print('Computador venceu')
        totvezes +=1
print(f'O jogador precisou de {totvezes} vezes para advinhar')