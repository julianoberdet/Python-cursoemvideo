while True:
    n = int(input('Digite um número para saber sua tabuada: '))
    print('--' * 20)
    if n < 0:
         break
    for c in range(1,11):
        print(f'{n} x {c} = {n*c}')
    print('--' * 20)
print('\033[31;1mPROGRAMA DE TABUADA ENCERRADO. Volte sempre!\033[m')