'''cont = 0
while True:
    cont += 1
    print(f'{cont}',end=' -> ')
print('Acabou')'''

n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma dos números digitados foi {s}')
