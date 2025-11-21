valores = list()
while True:
    valor = int(input('Digite um valor: '))

#Para verificar se o valor ja foi adicionado a lista
    if valor not in valores:
        valores.append(valor)
        print('\033[32mValor adicionado com sucesso!\033[m')
    else:
        print('\033[31mValor duplicado, Tente outro\033[m')

# Para digitar sim ou não
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
    if resp == 'N':
         break

 #Para colocar em ordem crescente
print(f'A lista em ordem crescente ficou assim: ', end='')
valores.sort()
print(f'\033[33;1m{valores}\033[m')
