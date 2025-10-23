n = 0
tot = 0
soma = 0
while n != 999:
    n = int(input('Digite um valor: '))
    if n != 999:
        tot += 1
        soma += n
    else:
        print('FIM')
print(f'O usuário digitou {tot} números e a soma entre esses números foi {soma}')


