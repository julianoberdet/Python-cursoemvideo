from random import randint
v = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar?[P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}, total de {total}' , end=' ')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você \033[32;1mVENCEU!\033[m')
            v += 1
        else:
            print('Você \033[31;1mPERDEU!\033[m')
            break
    elif tipo == 'I':
        if total % 2 != 0:
            print('Você \033[32;1mVENCEU!\033[m')
            v += 1
        else:
            print('Você \033[31;1mPERDEU!\033[m')
            break
    print('\033[33mVamos jogar novamente...\033[m')
print(f'\033[31;1mGAME OVER...\033[m Você venceu \033[32m{v}\033[m vezes')

