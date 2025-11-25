valores = list()
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'A lista ficou assim {valores}')
print(f'Foram digitados {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {valores}')
if 5 in valores:
    print(f'\033[32mO número 5 está na lista \033[m')
else:
    print('\033[31mO número 5 não está na lista\033[m')