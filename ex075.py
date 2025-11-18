num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite outro número: ')))
print(f'Você digitou os números: ',end='')
for n in num:
    print(f'{n} ',end=' ')

#Quantas vezes aparece o número 9
if 9 in num:
    print(f'\nO número 9 apareceu {num.count(9)} vezes')

#Posição do número 3
if 3 in num:
    print(f'O número 3 está {num.index(3)+1}ª posição')
else:
    print('O número 3 NÃO foi digitado')
print('Os valores pares digitados foram: ',end='')
#Ver os número pares
for n in num:
    if n % 2 == 0:
        print(f'{n} ',end='')





