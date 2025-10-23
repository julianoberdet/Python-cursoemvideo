from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
escolha = 0
while escolha != 5:
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa''')
    escolha = int(input('>>>>>> Qual opção? '))
    if escolha == 1:
        resultado = n1 + n2
        print(f'A soma entre {n1} + {n2} = \033[1;32m{resultado}\033[m')
    elif escolha == 2:
        resultado = n1 * n2
        print(f'A multiplicação entre {n1} x {n2} = \033[1;32m{resultado}\033[m')
    elif escolha == 3:
        if n1 > n2:
         resultado = n1
        else:
            resultado = n2
        print(f'O maior entre {n1} e {n2} é \033[1;32m{resultado}\033[m')
    elif escolha == 4:
        print('Informe os números novamente..')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif escolha == 5:
        print('Saindo...')
        sleep(3)
    else:
        print('\033[1;31mOpção inválida. Tente novamente\033[m')
    print('-==' * 10)
print('Até logo!')

   


