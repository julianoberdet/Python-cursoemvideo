from random import randint
computador = randint(0,10)
acertou = False
palpite = 0
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('--------Tente acertar o numero que eu pensei-------')
while not acertou:
    jogador = int(input('Digite um palpite: '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if computador > jogador:
            print('Mais... Tente novamente')
        else:
            print('Menos... Tente novamente')
print(f'O computador pensou no número {computador}')
print(f'Você acertou com {palpite} tentativas. PARABÉNS!')