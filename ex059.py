from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
escolha = 0
resultado = 0
while escolha != 5:
    print('''Escolha uma das opções do menu:
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa''')
    escolha = int(input('Qual opção? '))
    if escolha == 1:
        resultado = n1 + n2
        print(f'O resultado é {resultado}')
    elif escolha == 2:
        resultado = n1 * n2
        print(f'O resultado é {resultado}')
    elif escolha == 3:
        if n1 > n2:
         resultado = n1
        else:
            resultado = n2
        print(f'O maior é {resultado}')
    elif escolha == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif escolha == 5:
        print('Saindo...')
        sleep(3)
        print('Até logo!')

   


