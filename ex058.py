from random import randint
computador = randint(0,10)
jogador = 0
totvezes = 0
print('--------Tente acertar o numero que eu pensei-------')
while jogador != computador:
    jogador = int(input('Digite um numero: '))
    if jogador == computador:
        print('Você venceu')
        totvezes += 1
    else:
        print('Computador venceu')
        totvezes += 1
print(f'O computador pensou no número {computador}')
print(f'O jogador precisou de {totvezes} vezes para advinhar')