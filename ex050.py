#Desenvolva um programa que eia seis números inteiros e mostre a soma apenas daqueles que forem pares

s = 0
for c in range(0 , 6 , 1):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
     s += n
print(f'A soma dos números pares digitados é {s}')


