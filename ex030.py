#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR:

n = int(input('Digite um número: '))
print('Analisando seu número...')
if n % 2 == 0:
    print(f'O número {n} é PAR')
else:
    print(f'O número {n} é IMPAR')
