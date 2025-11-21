valores = list()
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar?[S/N] ')).upper().strip()
    if resp == 'N':
        break
print(f'A lista ficou assim {valores}')
print(f'Foram digitados {len(valores)} números na lista')
valores.sort(reverse=True)
print(f'A lista ordenada de trás pra frete ficou assim: {valores}')
if 5 in valores:
    print(f'\033[32mO número 5 foi sim digitado\033[m')
else:
    print('\033[31mO número 5 não está na lista\033[m')