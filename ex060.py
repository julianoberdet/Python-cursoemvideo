n = int(input('Digite um número para saber o seu fatorial: '))
c = n
f = 1
print(f'Calculando {n}! = ', end=' ')
while c > 0:
    print(f'{c}', end=' ')
    print(' x ' if c > 1 else ' = ', end=' ')
    f *= c
    c -= 1
print(f'\033[34m{f}\033[m')


#Usando for
'''n = int(input('Digite um número para saber o seu fatorial: '))
c = n
f = 1
for c in range(1 , c+1):
    f = f * c
print(f'O fatorial de {c} é {f}')'''

#Usando módulo
'''from math import factorial
n = int(input('Digite um valor para saber o seu fatorial: '))
f = factorial(n)
print(f'O fatorial de {n} é {f}')'''