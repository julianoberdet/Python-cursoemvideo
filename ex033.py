#Faça um programa que leia três números e mostre qual é o maior e qual é o menor:

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
print('Analisando os números..')
if n1 > n2 and n3 :
    print(f'O maior número é {n1}')
if n2 > n1 and n3:
    print(f'O maior número é {n2}')
if n3 > n1 and n3:
    print(f'O Maior número é {n3}')
else:

