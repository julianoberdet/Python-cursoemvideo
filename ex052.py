#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n = int(input('Digite um número: '))
if n % 2 == 0 or n % 1 == 0:
    print(f'{n} é um número primo')