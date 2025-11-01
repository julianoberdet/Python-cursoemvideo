from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0,10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar?[P/I] ')).strip().upper()[0]
    print(f'O jogador escolheu {jogador} e o computador escolheu {computador} o total foi {total}',end=': ')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    print(f'Você escolheu {tipo}',end=' ')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você \033[32;1mVENCEU!\033[m')
            v += 1
        else:
            print('Você \033[31;1mPERDEU!\033[m')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você \033[32;1mVENCEU!\033[m')
            v += 1
        else:
            print('Você \033[31;1mPERDEU!\033[m')
            break
    print('Vamos jogar novamente...')
print(f'\033[31;1mGAME OVER...\033[m Você venceu \033[36;1m{v}\033[m vezes')

